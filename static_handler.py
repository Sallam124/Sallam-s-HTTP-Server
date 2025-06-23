# static_handler.py
# Serves static files from the public/ directory
from response import build_response  # Placeholder for response builder
from utils import get_content_type  # Placeholder for content type detection
import os

PUBLIC_DIR = 'public'

def serve_static_file(path):
    """
    Attempts to serve a static file from the public/ directory.
    Returns an HTTP response (bytes).
    """
    # Normalize the path to prevent directory traversal
    safe_path = os.path.normpath(path).lstrip("/\\")
    file_path = os.path.join(PUBLIC_DIR, safe_path)

    # If the path is a directory, try to serve index.html
    if os.path.isdir(file_path):
        file_path = os.path.join(file_path, "index.html")

    if not os.path.isfile(file_path):
        # File not found, return 404
        body = b'<h1>404 Not Found</h1>'
        headers = {'Content-Type': 'text/html', 'Content-Length': str(len(body))}
        return build_response(404, body, headers)

    # Read the file
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
    except Exception:
        body = b'<h1>500 Internal Server Error</h1>'
        headers = {'Content-Type': 'text/html', 'Content-Length': str(len(body))}
        return build_response(500, body, headers)

    # Detect content type
    content_type = get_content_type(file_path)
    headers = {'Content-Type': content_type, 'Content-Length': str(len(content))}
    return build_response(200, content, headers) 