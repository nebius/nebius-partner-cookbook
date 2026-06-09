const JERSEY_CSS_URL = "https://fonts.googleapis.com/css2?family=Jersey+15&display=swap";

let cachedJersey: ArrayBuffer | null | undefined;

export async function getJerseyFont(): Promise<ArrayBuffer | null> {
  if (cachedJersey !== undefined) return cachedJersey;

  try {
    const css = await fetch(JERSEY_CSS_URL).then((response) => response.text());
    const match = css.match(/url\((https:\/\/fonts\.gstatic\.com\/[^)]+)\)/);
    if (!match?.[1]) {
      cachedJersey = null;
      return cachedJersey;
    }
    const font = await fetch(match[1]).then((response) => response.arrayBuffer());
    cachedJersey = font;
    return cachedJersey;
  } catch {
    cachedJersey = null;
    return cachedJersey;
  }
}
