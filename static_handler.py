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
    # TODO: Map URL path to file path
    # TODO: Check if file exists, read file, detect content type
    # TODO: Return 404 if not found
    return build_response(501, b'Not Implemented') 