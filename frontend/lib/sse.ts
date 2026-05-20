export async function streamQuery(
  role: string,
  query: string,
  onEvent: (event: any) => void,
  onDone: () => void,
  onError: (err: any) => void
): Promise<void> {
  try {
    const backendUrl = process.env.NEXT_PUBLIC_BACKEND_URL ?? "http://localhost:10000";
    const response = await fetch(`${backendUrl}/query`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ role, query }),
    });

    if (!response.ok || !response.body) {
      throw new Error(`HTTP ${response.status}`);
    }

    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    let buffer = "";

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      buffer += decoder.decode(value, { stream: true });

      // SSE frames are separated by "\n\n"
      const parts = buffer.split("\n\n");
      buffer = parts.pop() ?? "";

      for (const frame of parts) {
        for (const line of frame.split("\n")) {
          if (line.startsWith("data: ")) {
            try {
              onEvent(JSON.parse(line.slice(6)));
            } catch {
              // skip malformed line
            }
          }
        }
      }
    }

    // flush any remaining buffered content
    for (const line of buffer.split("\n")) {
      if (line.startsWith("data: ")) {
        try {
          onEvent(JSON.parse(line.slice(6)));
        } catch {}
      }
    }

    onDone();
  } catch (err) {
    onError(err);
  }
}
