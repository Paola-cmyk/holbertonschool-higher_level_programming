from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_data.encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            json_info = json.dumps(info)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_info.encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_msg = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error_msg).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
