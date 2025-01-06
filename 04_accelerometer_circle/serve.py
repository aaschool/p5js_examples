import http.server
import socketserver
import ssl

PORT = 4443  # Choose a port for HTTPS

Handler = http.server.SimpleHTTPRequestHandler

# Create an SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# Load the certificate chain
context.load_cert_chain('cert.pem', 'key.pem')  

# Create an HTTPS server with the SSL context
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    print(f"Serving at https://localhost:{PORT}")
    httpd.serve_forever()
