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
    # Map status_code to reason phrase
    reasons = {
        200: 'OK',
        400: 'Bad Request',
        404: 'Not Found',
        500: 'Internal Server Error',
        501: 'Not Implemented',
    }
    reason = reasons.get(status_code, 'Unknown')

    # Build headers
    if headers is None:
        headers = {}
    if 'Content-Length' not in headers:
        headers['Content-Length'] = str(len(body))
    if 'Content-Type' not in headers:
        headers['Content-Type'] = 'text/html'

    header_lines = ''.join(f'{k}: {v}\r\n' for k, v in headers.items())
    response = f'HTTP/1.1 {status_code} {reason}\r\n{header_lines}\r\n'.encode('utf-8') + body
    return response 