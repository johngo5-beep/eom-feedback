import Link from "next/link";
import { ROUTES } from "@/lib/constants";

export default function AdminPage() {
  return (
    <section className="flex flex-col gap-4">
      <p className="text-neutral-600 dark:text-neutral-400">
        Admin overview placeholder. Authentication and stats will be added later.
      </p>
      <Link
        href={ROUTES.adminResponses}
        className="w-fit text-sm font-medium underline-offset-4 hover:underline"
      >
        View responses →
      </Link>
    </section>
  );
}
