import webbrowser
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import time
import os

class AuthHandler(BaseHTTPRequestHandler):
    def _load_template(self, filename):
        template_path = os.path.join(os.path.dirname(__file__), 'templates', filename)
        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            if 'success' in filename:
                return "<html><body><h1>Success!</h1><p>Authorization successful. You can close this window.</p><script>setTimeout(() => window.close(), 3000);</script></body></html>"
            else:
                return "<html><body><h1>Error</h1><p>Authorization failed. Please try again.</p></body></html>"
    def do_GET(self):
        if self.path.startswith('/callback'):
            parsed_url = urlparse(self.path)
            query_params = parse_qs(parsed_url.query)
            
            if 'code' in query_params:
                self.server.auth_code = query_params['code'][0]
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                success_html = self._load_template('success.html')
                self.wfile.write(success_html.encode())
            else:
                self.send_response(400)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                error_html = self._load_template('error.html')
                self.wfile.write(error_html.encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def log_message(self, format, *args):
        pass

def get_auth_code_automatically(auth_url, port=8080):
    server = HTTPServer(('localhost', port), AuthHandler)
    server.auth_code = None
    server.timeout = 1
    
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    
    print(f"\n🌐 Opening Spotify login in your browser...")
    print(f"📱 If it doesn't open automatically, copy this URL:")
    print(f"   {auth_url}")
    print(f"\n⏳ Waiting for authorization (this may take a moment)...")
    
    try:
        webbrowser.open(auth_url)
    except:
        print("❌ Could not open browser automatically")
    
    timeout = 300
    start_time = time.time()
    
    while server.auth_code is None:
        if time.time() - start_time > timeout:
            server.shutdown()
            raise TimeoutError("Authorization timed out after 5 minutes")
        
        time.sleep(1)
    
    auth_code = server.auth_code
    server.shutdown()
    server_thread.join(timeout=1)
    
    return auth_code