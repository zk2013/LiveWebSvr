#!/usr/bin/env python

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import json

# import svr cfg
import livecfg
from livecfg import dbcfg
from dbproxy import *
 
from  login import LoginHandler # handle login

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

# handle welcome ad
class AdHandler(tornado.web.RequestHandler):
    def post(self):
        self.write(json.dumps(livecfg.ad))

def main():
	# connect mysql database
	g_db_proxy = LiveDbProxy(dbcfg['dbuser'],dbcfg['dbpasswd'],dbcfg['dbhost'],dbcfg['database'])
	LiveDbProxyholder.set_dbproxy(g_db_proxy)
	if g_db_proxy.openDb() == False:
		print('open db fail')
		return
	else:
		print('open db ok')
	
	tornado.options.parse_command_line()
	application = tornado.web.Application([
		(r"/", MainHandler),
		(r"/ad/open", AdHandler),
		(r"/login/mResponse",LoginHandler),
	])
	
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.current().start()
	g_db_proxy.close()

if __name__ == "__main__":
    main()
