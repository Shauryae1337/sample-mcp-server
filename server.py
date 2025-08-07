import socket
import json
import os

CONFIG_FOLDER = 'config'

def load_config():
    config = {}
    for file in os.listdir(CONFIG_FOLDER):
        if file.endswith(".json"):
            with open(os.path.join(CONFIG_FOLDER, file), 'r') as f:
                data = json.load(f)
                config.update(data)
    return config

HOST = '127.0.0.1'
PORT = 5000

config_data = load_config()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            key = data.decode().strip()
            print(f"Received request: {key}")
            response = config_data.get(key, "Key not found")
            conn.sendall(str(response).encode())
