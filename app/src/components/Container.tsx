import { cn } from "./cn";

interface ContainerProps {
  children: React.ReactNode;
  size?: "sm" | "md" | "lg" | "full";
  className?: string;
}

const SIZE: Record<NonNullable<ContainerProps["size"]>, string> = {
  sm: "max-w-2xl",
  md: "max-w-3xl",
  lg: "max-w-5xl",
  full: "max-w-7xl",
};

export function Container({ children, size = "md", className }: ContainerProps) {
  return <div className={cn("mx-auto w-full px-6", SIZE[size], className)}>{children}</div>;
}
