#!/usr/bin/env python
# -*- coding: utf8 -*-
import json
import sys

import requests
import six

goo_gl = 'https://www.googleapis.com/urlshortener/v1/url'

__doc__ = 'https://developers.google.com/url-shortener/'


def shorten(url):
    data = dict(longUrl=url)
    headers = {'content-type': 'application/json'}
    res = requests.post(goo_gl, data=json.dumps(data), headers=headers)
    if res.ok:
        return res.json()
    else:
        res.raise_for_status(res.content)


def expand(shortUrl):
    # https://www.googleapis.com/urlshortener/v1/url?shortUrl=http://goo.gl/fbsS
    params = {'shortUrl': shortUrl}
    return _get(params)


def stat(shortUrl):
    params = {'shortUrl': shortUrl, 'projection': 'FULL'}
    return _get(params)


def _get(params):
    res = requests.get(goo_gl, params=params)
    if res.ok:
        return res.json()
    else:
        res.raise_for_status(res.content)


def history(shortUrl):
    raise NotImplementedError()


if __name__ == '__main__':
    if(len(sys.argv) > 1):
        url = sys.argv[1]
        if 'goo.gl' in url:
            six.print_(expand(url)['longUrl'])
        else:
            six.print_(shorten(url)['id'])

# vim: et sw=4 ts=4
