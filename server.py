import socket
import threading
import os
import mimetypes
from router import handle_request  # Placeholder for routing logic
from log import log_request, log_error  # Placeholder for logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Define host and port
HOST = '127.0.0.1'   # localhost
PORT = 8080          # Common alternative to port 80

# Main server loop: accepts connections and spawns a thread for each client
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Serving HTTP on {HOST}:{PORT} ...")

    while True:
        client_conn, client_addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(client_conn, client_addr))
        thread.start()

# Handles a single client connection
def handle_client(client_conn, client_addr):
    try:
        request_data = client_conn.recv(1024).decode('utf-8')
        # Log the request (placeholder)
        log_request(client_addr, request_data)
        # Route the request and get a response (placeholder)
        response = handle_request(request_data)
        client_conn.sendall(response)
    except Exception as e:
        # Log the error (placeholder)
        log_error(client_addr, str(e))
    finally:
        client_conn.close()

if __name__ == '__main__':
    start_server()
