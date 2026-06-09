#!/usr/bin/env python3
"""
Convert eCFR XML files to clean, readable plain text.
Preserves hierarchical structure: PART > SUBPART > SECTION > APPENDIX.
"""

import defusedxml.ElementTree as ET  # hardened drop-in for xml.etree (prevents XXE/entity-expansion)
import os
import re

DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "regulations")

FILES = [
    ("hipaa_45cfr_part160_general_admin.xml", "hipaa_45cfr_part160_general_admin.txt"),
    ("hipaa_45cfr_part162_admin_requirements.xml", "hipaa_45cfr_part162_admin_requirements.txt"),
    ("hipaa_45cfr_part164_security_privacy.xml", "hipaa_45cfr_part164_security_privacy.txt"),
    ("hipaa_45cfr_part160_2020.xml", "hipaa_45cfr_part160_2020.txt"),
    ("hipaa_45cfr_part162_2020.xml", "hipaa_45cfr_part162_2020.txt"),
    ("hipaa_45cfr_part164_2017.xml", "hipaa_45cfr_part164_2017.txt"),
    ("hipaa_45cfr_part164_2020.xml", "hipaa_45cfr_part164_2020.txt"),
    ("hipaa_45cfr_part164_2024.xml", "hipaa_45cfr_part164_2024.txt"),
]


def get_text(elem):
    """Recursively extract all text from an element, including tail text of children."""
    parts = []
    if elem.text:
        parts.append(elem.text)
    for child in elem:
        parts.append(get_text(child))
        if child.tail:
            parts.append(child.tail)
    return "".join(parts)


def clean_text(text):
    """Normalize whitespace in extracted text."""
    # Collapse internal whitespace runs (including newlines) to single space
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def format_table(table_elem):
    """Convert an HTML-style table element to a plain-text representation."""
    rows = []
    for tr in table_elem.iter("TR"):
        cells = []
        for cell in tr:
            if cell.tag in ("TH", "TD"):
                colspan = int(cell.get("colspan", "1"))
                cell_text = clean_text(get_text(cell))
                cells.append((cell_text, colspan))
        rows.append(cells)

    if not rows:
        return ""

    # Determine the actual number of columns
    max_cols = max(sum(c[1] for c in row) for row in rows)

    # Expand cells with colspan into the grid
    expanded = []
    for row in rows:
        exp_row = []
        for text, colspan in row:
            exp_row.append(text)
            for _ in range(colspan - 1):
                exp_row.append("")
        # Pad if needed
        while len(exp_row) < max_cols:
            exp_row.append("")
        expanded.append(exp_row)

    # Calculate column widths (cap at 50 to keep readable)
    col_widths = [0] * max_cols
    for row in expanded:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(cell))
    col_widths = [min(w, 50) for w in col_widths]

    lines = []
    sep = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"
    lines.append(sep)
    for row in expanded:
        parts = []
        for i, cell in enumerate(row):
            parts.append(" " + cell.ljust(col_widths[i]) + " ")
        lines.append("|" + "|".join(parts) + "|")
        # Put separator after header row (first row) and after each row
        lines.append(sep)

    return "\n".join(lines)


def process_element(elem, indent=0, lines=None):
    """Recursively process XML elements and build output lines."""
    if lines is None:
        lines = []

    tag = elem.tag
    prefix = "  " * indent

    # --- Structural containers ---

    if tag == "DIV5" and elem.get("TYPE") == "PART":
        # Part-level heading
        head = elem.find("HEAD")
        if head is not None:
            heading_text = clean_text(get_text(head))
            lines.append("=" * 80)
            lines.append(heading_text)
            lines.append("=" * 80)
            lines.append("")

        # Authority and Source at part level
        auth = elem.find("AUTH")
        if auth is not None:
            lines.append("Authority: " + clean_text(get_text(auth)).replace("Authority:", "").strip())
            lines.append("")
        source = elem.find("SOURCE")
        if source is not None:
            lines.append("Source: " + clean_text(get_text(source)).replace("Source:", "").strip())
            lines.append("")

        # Process children (subparts, sections, etc.)
        for child in elem:
            if child.tag in ("HEAD", "AUTH", "SOURCE"):
                continue
            process_element(child, indent, lines)

    elif tag == "DIV6" and elem.get("TYPE") == "SUBPART":
        # Subpart heading
        head = elem.find("HEAD")
        if head is not None:
            heading_text = clean_text(get_text(head))
            lines.append("")
            lines.append("-" * 80)
            lines.append(heading_text)
            lines.append("-" * 80)
            lines.append("")

        # Authority and Source at subpart level
        auth = elem.find("AUTH")
        if auth is not None:
            lines.append("  Authority: " + clean_text(get_text(auth)).replace("Authority:", "").strip())
            lines.append("")
        source = elem.find("SOURCE")
        if source is not None:
            lines.append("  Source: " + clean_text(get_text(source)).replace("Source:", "").strip())
            lines.append("")

        for child in elem:
            if child.tag in ("HEAD", "AUTH", "SOURCE"):
                continue
            process_element(child, indent + 1, lines)

    elif tag == "DIV8" and elem.get("TYPE") == "SECTION":
        # Section
        head = elem.find("HEAD")
        section_num = elem.get("N", "")
        if head is not None:
            heading_text = clean_text(get_text(head))
            lines.append("")
            lines.append(prefix + heading_text)
            lines.append(prefix + "-" * len(heading_text))
        elif section_num:
            lines.append("")
            lines.append(prefix + f"Section {section_num}")
            lines.append(prefix + "-" * (len(section_num) + 8))
        lines.append("")

        for child in elem:
            if child.tag == "HEAD":
                continue
            process_element(child, indent + 1, lines)

    elif tag == "DIV9":
        # Appendix or sub-section division
        head = elem.find("HEAD")
        if head is not None:
            heading_text = clean_text(get_text(head))
            lines.append("")
            lines.append(prefix + heading_text)
            lines.append(prefix + "~" * len(heading_text))
            lines.append("")

        for child in elem:
            if child.tag == "HEAD":
                continue
            process_element(child, indent + 1, lines)

    # --- Content elements ---

    elif tag == "P":
        text = clean_text(get_text(elem))
        if text:
            lines.append(prefix + text)
            lines.append("")

    elif tag == "EXTRACT":
        # Indented block quote
        for child in elem:
            process_element(child, indent + 1, lines)

    elif tag == "TABLE":
        table_text = format_table(elem)
        if table_text:
            # Indent the whole table
            for tl in table_text.split("\n"):
                lines.append(prefix + tl)
            lines.append("")

    elif tag == "CITA":
        text = clean_text(get_text(elem))
        if text:
            lines.append(prefix + "[" + text + "]")
            lines.append("")

    elif tag == "DIV":
        # Generic wrapper (used around tables)
        for child in elem:
            process_element(child, indent, lines)

    elif tag in ("AUTH", "SOURCE"):
        # Already handled at structural levels; skip if encountered elsewhere
        pass

    elif tag in ("HEAD", "HED", "PSPACE", "I", "E", "XREF"):
        # Inline elements handled by get_text(); skip standalone processing
        pass

    elif tag in ("THEAD", "TBODY", "TR", "TH", "TD"):
        # Table internals handled by format_table
        pass

    else:
        # Fallback: extract text from any unrecognized element
        text = clean_text(get_text(elem))
        if text:
            lines.append(prefix + text)
            lines.append("")

    return lines


def convert_file(xml_path, txt_path):
    """Parse one XML file and write the plain text output."""
    print(f"Converting: {os.path.basename(xml_path)}")
    tree = ET.parse(xml_path)
    root = tree.getroot()

    lines = process_element(root)

    # Clean up excessive blank lines (max 2 consecutive)
    output = "\n".join(lines)
    output = re.sub(r"\n{4,}", "\n\n\n", output)
    output = output.strip() + "\n"

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(output)

    line_count = output.count("\n")
    print(f"  -> {os.path.basename(txt_path)} ({line_count} lines)")


def main():
    for xml_name, txt_name in FILES:
        xml_path = os.path.join(DIR, xml_name)
        txt_path = os.path.join(DIR, txt_name)
        if not os.path.exists(xml_path):
            print(f"WARNING: {xml_name} not found, skipping.")
            continue
        convert_file(xml_path, txt_path)
    print("Done.")


if __name__ == "__main__":
    main()
