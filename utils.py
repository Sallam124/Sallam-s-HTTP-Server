# utils.py
# Helper functions for the HTTP server

def get_content_type(file_path):
    """
    Returns the MIME type for a given file path.
    """
    import mimetypes
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type or 'application/octet-stream' 