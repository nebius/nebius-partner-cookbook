import { cn } from "./cn";

interface NebiusLogoProps {
  /** Pixel height — width is derived from the SVG aspect ratio (~3.64:1). */
  height?: number;
  className?: string;
}

/**
 * The official Nebius wordmark lockup. The SVG carries its own lime-yellow
 * background, so it reads as a brand chip on dark surfaces with no wrapper.
 */
export function NebiusLogo({ height = 24, className }: NebiusLogoProps) {
  const width = Math.round(height * (1133.9 / 311.8));
  return (
    /* eslint-disable-next-line @next/next/no-img-element */
    <img
      src="/NEBIUS-color.svg"
      alt="Nebius"
      width={width}
      height={height}
      className={cn("inline-block select-none", className)}
      draggable={false}
    />
  );
}
