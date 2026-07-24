/**
 * Shared types for feedback submissions.
 * Wire these up when implementing persistence and API handlers.
 */

export type FeedbackStatus = "new" | "reviewed" | "archived";

export interface FeedbackSubmission {
  id: string;
  name: string;
  email: string;
  message: string;
  status: FeedbackStatus;
  createdAt: string;
  updatedAt: string;
}

export interface CreateFeedbackInput {
  name: string;
  email: string;
  message: string;
}
