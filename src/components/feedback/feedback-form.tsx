"use client";

/**
 * Public feedback form shell.
 * Form fields and submit handling will be added later.
 */
export function FeedbackForm() {
  return (
    <form
      className="flex w-full max-w-lg flex-col gap-4"
      onSubmit={(event) => {
        event.preventDefault();
      }}
      noValidate
    >
      <p className="text-sm text-neutral-500">
        Feedback form placeholder — fields and submission logic coming soon.
      </p>
      <button
        type="submit"
        disabled
        className="cursor-not-allowed rounded-md bg-neutral-900 px-4 py-2 text-sm font-medium text-white opacity-50 dark:bg-neutral-100 dark:text-neutral-900"
      >
        Submit feedback
      </button>
    </form>
  );
}
