import { cn } from "./cn";

interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  interactive?: boolean;
}

export function Card({ interactive = false, className, ...rest }: CardProps) {
  return (
    <div
      className={cn(
        "border border-edge bg-surface/60 p-5 backdrop-blur-sm",
        interactive &&
          "group relative cursor-pointer transition hover:border-accent/60 hover:bg-surface",
        className,
      )}
      {...rest}
    />
  );
}
