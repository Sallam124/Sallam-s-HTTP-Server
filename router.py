# router.py
# Handles URL routing logic for the HTTP server
from response import build_response  # Placeholder for response builder
from static_handler import serve_static_file  # Placeholder for static file serving

# Main routing function
def handle_request(request_data):
    """
    Parses the HTTP request, determines the route, and returns an HTTP response (bytes).
    """
    # Parse HTTP method and path from request_data
    try:
        request_line = request_data.splitlines()[0]
        method, path, _ = request_line.split()
    except Exception:
        return build_response(400, b'<h1>400 Bad Request</h1>', {'Content-Type': 'text/html'})

    # Route to appropriate handler
    if path == '/':
        return build_response(200, b'<h1>Home</h1>', {'Content-Type': 'text/html'})
    elif path == '/about':
        return build_response(200, b'<h1>About</h1>', {'Content-Type': 'text/html'})
    else:
        return serve_static_file(path) 