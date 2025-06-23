# log.py
# Logging functions for the HTTP server

def log_request(client_addr, request_data):
    """
    Logs an incoming HTTP request.
    """
    print(f"[REQUEST] From {client_addr}:\n{request_data}\n{'-'*40}")

def log_error(client_addr, error_msg):
    """
    Logs an error that occurred while handling a request.
    """
    print(f"[ERROR] For {client_addr}: {error_msg}\n{'-'*40}") 