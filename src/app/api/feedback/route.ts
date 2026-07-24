import { NextResponse } from "next/server";

/**
 * Feedback API stubs.
 * Implement create/list handlers when storage is ready.
 */

export async function GET() {
  return NextResponse.json(
    {
      data: [],
      message: "Feedback list endpoint is not implemented yet.",
    },
    { status: 501 },
  );
}

export async function POST() {
  return NextResponse.json(
    {
      message: "Feedback create endpoint is not implemented yet.",
    },
    { status: 501 },
  );
}
