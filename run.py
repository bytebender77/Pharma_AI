import uvicorn
import socket

def find_free_port(start_port=8000):
    """Find a free port starting from start_port."""
    port = start_port
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('localhost', port)) != 0:
                return port
            port += 1

if __name__ == "__main__":
    port = find_free_port()
    print(f"\n🚀 Starting server on http://localhost:{port}\n")
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)
