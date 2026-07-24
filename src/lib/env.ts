/**
 * Central place for environment variables.
 * Add validation (e.g. Zod) when secrets and DB URLs are introduced.
 */

export const env = {
  nodeEnv: process.env.NODE_ENV,
  // Example placeholders — set in Vercel project settings / .env.local
  // databaseUrl: process.env.DATABASE_URL,
  // adminSecret: process.env.ADMIN_SECRET,
} as const;
