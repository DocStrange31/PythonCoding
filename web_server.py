from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi

hostname="localhost"
port=8080
form=cgi.FieldStorage()

class web_server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/':
            self.path='test.html'
        try:
            myfile=open(self.path).read()
            self.send_response(200)
        except:
            myfile="File not Found"
            self.send_response(404)

        self.end_headers()
        self.wfile.write(bytes(myfile, 'utf-8'))


webserver= HTTPServer((hostname,port),web_server)
print("Server started http://%s:%s" % (hostname,port))

webserver.serve_forever()z1
a=form.getvalue('input1')
print(a)

webserver.server_close()
print('Server stopped')
