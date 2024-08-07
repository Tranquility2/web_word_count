from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus

PORT = 9000

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """ Simple HTTP request handler with CORS headers """
    # Note: The CORS headers are necessary for pyscript to work.

    def do_GET(self):
        if self.path == '/':
            self.path = '/main.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'text/html')
            self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
            self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
            self.send_header('Cross-Origin-Resource-Policy', 'cross-origin')
            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8'))
        except:
            self.send_response(HTTPStatus.NOT_FOUND)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'404 - Not Found')


if __name__ == '__main__':
    print(f"http://localhost:{PORT}/")
    httpd = HTTPServer(('', PORT), SimpleHTTPRequestHandler)
    httpd.serve_forever()