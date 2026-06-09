import { ImageResponse } from "next/og";
import { getJerseyFont } from "@/lib/og-fonts";
import { getRecipes } from "@/lib/recipes";

export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

export default async function Image() {
  const recipes = getRecipes();
  const jersey = await getJerseyFont();
  const displayFont = jersey ? "Jersey 15" : "Arial";
  const subtitle =
    "Runnable, observable, deployable recipes for building AI agents on Nebius Token Factory + Partners.";

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
            right: 110,
            top: 172,
            display: "flex",
            fontSize: 250,
            lineHeight: 1,
            fontFamily: displayFont,
            fontWeight: 400,
            letterSpacing: -10,
            color: "rgba(36,80,107,0.52)",
          }}
        >
          {String(recipes.length).padStart(2, "0")}
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
            <span>[ Session Ready ]</span>
            <span style={{ color: "#ddff46" }}>/ Agent Blueprint Recipes · live</span>
          </div>
          <div
            style={{
              marginTop: 58,
              display: "flex",
              flexDirection: "column",
              fontSize: 108,
              lineHeight: 0.86,
              fontFamily: displayFont,
              fontWeight: 400,
              letterSpacing: -3,
            }}
          >
            <span>Production agents,</span>
            <span style={{ color: "#ddff46" }}>unforked.</span>
          </div>
          <div
            style={{
              marginTop: 44,
              maxWidth: 780,
              display: "flex",
              fontSize: 30,
              lineHeight: 1.24,
              fontStyle: "italic",
              color: "#93a8be",
            }}
          >
            {subtitle}
          </div>
          <div style={{ marginTop: 58, display: "flex", gap: 14 }}>
            {['fastapi', 'python 3.12', 'nebius', 'partners'].map((chip) => (
              <div
                key={chip}
                style={{
                  border: "1px solid #24506b",
                  background: "#103a51",
                  display: "flex",
                  padding: "12px 18px",
                  fontFamily: "monospace",
                  fontSize: 18,
                  letterSpacing: 3,
                  color: "#93a8be",
                  textTransform: "uppercase",
                }}
              >
                {chip}
              </div>
            ))}
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
