#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import cgi
import json
from BaseHTTPServer import BaseHTTPRequestHandler


class RequestHandler(BaseHTTPRequestHandler):
    template = u"""
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8" /></head><body>
<form method="POST" action="/">
<div><textarea name="data"></textarea></div><div><input type="submit">
<div>{message}</div>
<div><pre>{data}</pre></div>
</form></body></html>"""
    outputs = {
        'data': '',
        'message': '',
    }

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(self.template.format(**self.outputs))
        return

    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                'REQUEST_METHOD': 'POST',
                'CONTENT_TYPE': self.headers['Content-Type'],
            })
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        try:
            obj = json.loads(form['data'].value)
            self.outputs['message'] = ''
            self.outputs['data'] = json.dumps(obj, sort_keys=True, indent=4, ensure_ascii=False)
        except ValueError as e:
            self.outputs['message'] = 'invalid json data: [{0}]'.format(e.message)
            self.outputs['data'] = form['data'].value

        self.outputs = dict(map(lambda (k, v): (k, cgi.escape(v)), self.outputs.iteritems()))
        self.wfile.write(self.template.format(**self.outputs).encode('utf8'))
        return


def serve(args):
    from BaseHTTPServer import HTTPServer
    server = HTTPServer((args.host, args.port), RequestHandler)
    print 'Starting server, http://{host}:{port} use <Ctrl-C> to stop'.format(host=args.host, port=args.port)
    server.serve_forever()


def get_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, default='localhost'),
    parser.add_argument('--port', type=int, default=5000),
    return parser

if __name__ == '__main__':
    parser = get_arg_parser()
    args = parser.parse_args()
    serve(args)

# vim: et sw=4 ts=4
