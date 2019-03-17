#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import uuid
import logging
import BaseHTTPServer

class MyRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler, object):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.send_header('Set-Cookie', 'JSESSIONID=' + str(uuid.uuid4()));
        self.end_headers()
        hostname = os.environ.get('HOSTNAME')
        cookie = self.headers.get('Cookie')
        self.wfile.write("HOSTNAME=" + hostname + "\n")
        self.wfile.write("COOKIE=" + cookie + "\n")
        logging.info([cookie, hostname])


def run_server():
    logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)
    logging.info('Starting httpd...')
    server_address = ('', 80)
    httpd = BaseHTTPServer.HTTPServer(server_address, MyRequestHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
