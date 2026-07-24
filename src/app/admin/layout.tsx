import type { Metadata } from "next";
import { AdminNav } from "@/components/layout/admin-nav";

export const metadata: Metadata = {
  title: "Admin",
};

export default function AdminLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <div className="flex flex-col gap-6">
      <div className="flex flex-col gap-1">
        <h1 className="text-2xl font-semibold tracking-tight">Admin</h1>
        <p className="text-sm text-neutral-600 dark:text-neutral-400">
          Review and manage feedback submissions.
        </p>
      </div>
      <AdminNav />
      {children}
    </div>
  );
}
