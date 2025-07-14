#!/usr/bin/python3
"""Module for setting up a basic HTTP server using http.server"""
import http.server
import json


class HTTPHandler(http.server.BaseHTTPRequestHandler):
    """Custom HTTP request handler to serve text and JSON responses"""

    def do_GET(self):
        """Handle GET requests for various endpoints"""

        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode('utf-8'))

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("OK".encode('utf-8'))

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Endpoint not found".encode('utf-8'))


if __name__ == '__main__':
    """Start the HTTP server on port 8000"""
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, HTTPHandler)
    print("Starting server at http://localhost:8000")
    httpd.serve_forever()
