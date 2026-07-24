import type { Metadata } from "next";
import { ResponsesList } from "@/components/admin/responses-list";

export const metadata: Metadata = {
  title: "Responses",
};

export default function AdminResponsesPage() {
  return (
    <section className="flex flex-col gap-4">
      <h2 className="text-lg font-medium">Responses</h2>
      <ResponsesList />
    </section>
  );
}
