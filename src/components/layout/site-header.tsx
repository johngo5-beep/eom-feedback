import Link from "next/link";
import { APP_NAME, ROUTES } from "@/lib/constants";

export function SiteHeader() {
  return (
    <header className="border-b border-neutral-200 dark:border-neutral-800">
      <div className="mx-auto flex h-14 max-w-5xl items-center justify-between px-4">
        <Link href={ROUTES.home} className="text-sm font-semibold tracking-tight">
          {APP_NAME}
        </Link>
        <nav className="flex items-center gap-4 text-sm text-neutral-600 dark:text-neutral-400">
          <Link href={ROUTES.home} className="hover:text-neutral-900 dark:hover:text-neutral-100">
            Feedback
          </Link>
          <Link
            href={ROUTES.admin}
            className="hover:text-neutral-900 dark:hover:text-neutral-100"
          >
            Admin
          </Link>
        </nav>
      </div>
    </header>
  );
}
