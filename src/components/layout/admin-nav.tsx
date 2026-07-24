import Link from "next/link";
import { ROUTES } from "@/lib/constants";

const links = [
  { href: ROUTES.admin, label: "Overview" },
  { href: ROUTES.adminResponses, label: "Responses" },
] as const;

export function AdminNav() {
  return (
    <nav className="flex gap-4 border-b border-neutral-200 pb-3 text-sm dark:border-neutral-800">
      {links.map((link) => (
        <Link
          key={link.href}
          href={link.href}
          className="text-neutral-600 hover:text-neutral-900 dark:text-neutral-400 dark:hover:text-neutral-100"
        >
          {link.label}
        </Link>
      ))}
    </nav>
  );
}
