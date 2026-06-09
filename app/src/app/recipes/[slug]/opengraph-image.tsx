import { ImageResponse } from "next/og";
import { notFound } from "next/navigation";
import { getJerseyFont } from "@/lib/og-fonts";
import { getRecipe } from "@/lib/recipes";

export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

export default async function Image({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const recipe = getRecipe(slug);
  if (!recipe) notFound();

  const stack = [...recipe.stack.primary, ...recipe.stack.secondary].slice(0, 4);
  const jersey = await getJerseyFont();
  const displayFont = jersey ? "Jersey 15" : "Arial";

  return new ImageResponse(
    (
      <div
        style={{
          width: "100%",
          height: "100%",
          display: "flex",
          flexDirection: "column",
          background: "#06263a",
          color: "#e7eef6",
          position: "relative",
          overflow: "hidden",
          fontFamily: "Arial, sans-serif",
        }}
      >
        <div
          style={{
            position: "absolute",
            inset: 0,
            background:
              "radial-gradient(ellipse 70% 50% at 50% -10%, rgba(221,255,70,0.16), transparent 62%), radial-gradient(ellipse 55% 40% at 100% 100%, rgba(221,255,70,0.10), transparent 64%)",
          }}
        />
        <div
          style={{
            position: "absolute",
            inset: 0,
            opacity: 0.28,
            backgroundImage: "radial-gradient(circle at 1px 1px, #ddff46 1px, transparent 0)",
            backgroundSize: "32px 32px",
          }}
        />
        <div
          style={{
            position: "absolute",
            left: 48,
            top: 48,
            right: 48,
            bottom: 48,
            border: "1px solid #14384f",
          }}
        />
        <div
          style={{
            position: "absolute",
            left: 48,
            top: 134,
            right: 48,
            height: 1,
            background: "#14384f",
          }}
        />
        <div
          style={{
            position: "absolute",
            right: 86,
            top: 124,
            display: "flex",
            fontSize: 310,
            lineHeight: 1,
            fontFamily: displayFont,
            fontWeight: 400,
            letterSpacing: -12,
            color: "rgba(36,80,107,0.52)",
          }}
        >
          {String(recipe.order).padStart(2, "0")}
        </div>
        <div style={{ position: "relative", display: "flex", flexDirection: "column", padding: 96 }}>
          <div
            style={{
              display: "flex",
              alignItems: "center",
              gap: 18,
              fontFamily: "monospace",
              fontSize: 21,
              letterSpacing: 5,
              color: "#93a8be",
              textTransform: "uppercase",
            }}
          >
            <span>Recipe · {String(recipe.order).padStart(2, "0")}</span>
            <span style={{ color: "#ddff46" }}>{recipe.eyebrow}</span>
            <span>{recipe.difficulty}</span>
          </div>
          <div
            style={{
              marginTop: 50,
              maxWidth: 820,
              display: "flex",
              flexDirection: "column",
              fontSize: recipe.title.length > 34 ? 82 : 96,
              lineHeight: 0.9,
              fontFamily: displayFont,
              fontWeight: 400,
              letterSpacing: -3,
              color: "#e7eef6",
            }}
          >
            {wrap(recipe.title, 22).slice(0, 3).map((line, index) => (
              <span key={line} style={{ color: index === 1 ? "#ddff46" : "#e7eef6" }}>
                {line}
              </span>
            ))}
          </div>
          <div
            style={{
              marginTop: 34,
              maxWidth: 810,
              display: "flex",
              fontSize: 28,
              lineHeight: 1.24,
              fontStyle: "italic",
              color: "#93a8be",
            }}
          >
            {recipe.tagline}
          </div>
          <div style={{ marginTop: 46, display: "flex", gap: 14 }}>
            {stack.map((chip) => (
              <div
                key={chip}
                style={{
                  border: "1px solid #24506b",
                  background: "#103a51",
                  display: "flex",
                  padding: "12px 18px",
                  fontFamily: "monospace",
                  fontSize: 17,
                  letterSpacing: 3,
                  color: "#93a8be",
                  textTransform: "uppercase",
                }}
              >
                {chip}
              </div>
            ))}
          </div>
          <div
            style={{
              position: "absolute",
              left: 96,
              bottom: 52,
              display: "flex",
              fontFamily: "monospace",
              fontSize: 18,
              letterSpacing: 4,
              color: "#5a7390",
              textTransform: "uppercase",
            }}
          >
            {recipe.estimatedReadingTime} read · Agent Blueprint Recipes
          </div>
        </div>
      </div>
    ),
    {
      ...size,
      fonts: jersey
        ? [{ name: "Jersey 15", data: jersey, style: "normal", weight: 400 }]
        : undefined,
    },
  );
}

function wrap(text: string, maxChars: number): string[] {
  const words = text.split(/\s+/).filter(Boolean);
  const lines: string[] = [];
  let current = "";
  for (const word of words) {
    const next = current ? `${current} ${word}` : word;
    if (next.length > maxChars && current) {
      lines.push(current);
      current = word;
    } else {
      current = next;
    }
  }
  if (current) lines.push(current);
  return lines;
}
