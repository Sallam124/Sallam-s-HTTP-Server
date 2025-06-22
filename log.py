# log.py
# Logging functions for the HTTP server

def log_request(client_addr, request_data):
    """
    Logs an incoming HTTP request.
    """
    # TODO: Implement structured logging (to file or stdout)
    print(f"Request from {client_addr}:\n{request_data}")

def log_error(client_addr, error_msg):
    """
    Logs an error that occurred while handling a request.
    """
    # TODO: Implement error logging (to file or stdout)
    print(f"Error for {client_addr}: {error_msg}") 