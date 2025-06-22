# response.py
# Builds HTTP response strings for the server

def build_response(status_code, body, headers=None):
    """
    Constructs a raw HTTP/1.1 response.
    status_code: int (e.g., 200)
    body: bytes
    headers: dict or None
    Returns: bytes
    """
    # TODO: Map status_code to reason phrase
    # TODO: Build headers (Content-Type, Content-Length, etc.)
    # TODO: Combine status line, headers, and body into a response
    return b'HTTP/1.1 501 Not Implemented\r\n\r\nNot Implemented' 