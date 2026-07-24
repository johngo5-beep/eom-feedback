import { FeedbackForm } from "@/components/feedback/feedback-form";

export default function HomePage() {
  return (
    <section className="flex flex-col gap-6">
      <div className="flex flex-col gap-2">
        <h1 className="text-2xl font-semibold tracking-tight">Share your feedback</h1>
        <p className="max-w-prose text-neutral-600 dark:text-neutral-400">
          Tell us what you think. Submissions will appear in the admin area once
          the backend is connected.
        </p>
      </div>
      <FeedbackForm />
    </section>
  );
}
