#!/usr/bin/env python3
import socket
import json


def start_server(host="127.0.0.1", port=65432):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(1)

        conn, addr = server_socket.accept()
        data = conn.recv(4096).decode("utf-8")

        received_dict = json.loads(data)
        print("Received dictionary from client:")
        print(received_dict)

        conn.close()
        server_socket.close()

    except Exception:
        return None


def start_client(data, host="127.0.0.1", port=65432):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        serialized_data = json.dumps(data)
        client_socket.sendall(serialized_data.encode("utf-8"))

        client_socket.close()

    except Exception:
        return None
