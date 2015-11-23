#!/usr/bin/python
from gevent import http
import resource
import subprocess
import os
import pwd
import sys
from sys import platform as _platform

port = 9999
redirectlocation = "http://www.google.com"

def callback(request):
    body = ''
    request.add_output_header('Location', redirectlocation)
    request.add_output_header('Content-Length', str(len(body)))
    request.add_output_header('Content-Type', 'text/html')
    request.send_reply(301, "Moved Permanently", body)

if len(sys.argv) == 3:
    port = int(sys.argv[1])
    redirectlocation = sys.argv[2]
    if _platform == "linux" or _platform == "linux2":
        # linux
        resource.setrlimit(resource.RLIMIT_NOFILE, (131072, 131072))
    print resource.getrlimit(resource.RLIMIT_NOFILE)
    http.HTTPServer(('0.0.0.0', port), callback).serve_forever()
else:
    print("\nNot enough arguments!\nExample ./redirectbot.py 9999 http://www.google.com")
