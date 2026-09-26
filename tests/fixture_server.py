from __future__ import annotations

import re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlsplit


class Handler(BaseHTTPRequestHandler):
    def log_message(self, format: str, *args: object) -> None:
        return

    def _respond(self) -> None:
        parsed = urlsplit(self.path)
        query = parse_qs(parsed.query)
        crlf_value = query.get("pa_crlf", [""])[0]
        crlf_match = re.search(r"X-PA-Injected:\s*(pa-scan-[a-f0-9]+)", crlf_value)

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        if parsed.path.startswith("/finding"):
            origin = self.headers.get("Origin")
            if origin:
                self.send_header("Access-Control-Allow-Origin", origin)
                self.send_header("Access-Control-Allow-Credentials", "true")
            if crlf_match:
                self.send_header("X-PA-Injected", crlf_match.group(1))
        self.end_headers()
        self.wfile.write(b"headerproof-action-fixture")

    do_GET = _respond
    do_OPTIONS = _respond


if __name__ == "__main__":
    ThreadingHTTPServer(("127.0.0.1", 18080), Handler).serve_forever()
