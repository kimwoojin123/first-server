import http.server
import socketserver

class CustomHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
PORT = 8080

handler = CustomHttpRequestHandler
server=socketserver.TCPServer(("", PORT), handler)
server.serve_forever()