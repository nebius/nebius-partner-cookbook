import { Github } from "lucide-react";
import { GITHUB_REPO_URL } from "@/lib/site";

export function GitHubCorner() {
  return (
    <a
      href={GITHUB_REPO_URL}
      target="_blank"
      rel="noreferrer"
      aria-label="Open the Agent Blueprint Recipes repository on GitHub"
      title="Open on GitHub"
      className="group fixed right-0 top-0 z-50 block size-20 overflow-hidden text-paper transition focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent focus-visible:ring-offset-2 focus-visible:ring-offset-paper sm:size-24"
    >
      <span
        aria-hidden
        className="absolute right-0 top-0 block size-0 border-t-[80px] border-l-[80px] border-t-accent border-l-transparent transition group-hover:border-t-accent-strong sm:border-t-[96px] sm:border-l-[96px]"
      />
      <Github
        aria-hidden
        className="absolute right-3 top-3 size-7 rotate-45 transition group-hover:scale-110 sm:right-4 sm:top-4 sm:size-8"
        strokeWidth={2.4}
      />
    </a>
  );
}
