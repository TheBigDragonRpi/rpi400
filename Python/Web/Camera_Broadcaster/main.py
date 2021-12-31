import cgi
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep

PORT_NUMBER = 80	

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	def do_POST(self):
		if self.path == '/success':
		    	ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
		    	try:
		    		pdict['boundary'] = bytes(pdict['boundary']).encode('utf-8')
		    	except:
		    		print("no boundary detected...")
		    	print(pdict, ctype, self.rfile)

		    	if ctype == 'multipart/form-data':
				fields = cgi.parse_multipart(self.rfile, pdict)
				image = fields.get("file")[0]
				print(type(image))
				with open('img.jpg', 'w') as f:
	    				f.write(image)


				html = "<html><head></head><body><h1>Form data successfully recorded!!!</h1></body></html>"

				self.send_response(200, "OK")
				self.end_headers()
				self.wfile.write(bytes(html).encode('utf-8'))
		        
		        
	#Handler for the GET requests
	def do_GET(self):
		print(self.path)
		if self.path=="/":
			self.path="/index.html"
		elif self.path=="/broadcast":
			self.path="/index_broadcast.html"

		try:
			#Check the file extension required and
			#set the right mime type

			sendReply = False
			self.path = self.path.split("?")[0]
			if self.path.endswith(".html"):
				mimetype='text/html'
				sendReply = True
			if self.path.endswith(".jpg"):
				mimetype='image/jpg'
				sendReply = True
			if self.path.endswith(".gif"):
				mimetype='image/gif'
				sendReply = True
			if self.path.endswith(".js"):
				mimetype='application/javascript'
				sendReply = True
			if self.path.endswith(".css"):
				mimetype='text/css'
				sendReply = True

			if sendReply == True:
				#Open the static file requested and send it
				path = curdir + sep + self.path 
				print(path)
				f = open(path) 
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
			return


		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print ' received, shutting down the web server'
	server.socket.close()