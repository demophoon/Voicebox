#!/usr/bin/env python
# encoding: utf-8

import urllib
import urllib2
import json


ROOM_ID = "ROOM"
ORG_ID = "ORD_ID"
SESSION_ID = "SESSION_ID"


def popup(text=None):
    if not text:
        return
    data = urllib.urlencode({
        'organization': ORG_ID,
        'room_code': ROOM_ID,
        'session': SESSION_ID,
        'text': text,
    })
    return urllib2.urlopen("http://vbsongs.com/api/v1/popups", data=data)


def get_queue():
    data = urllib.urlencode({
        'organization': ORG_ID,
        'room_code': ROOM_ID,
        'session': SESSION_ID,
    })
    request = urllib2.Request("http://vbsongs.com/api/v1/queue?{}".format(data))
    request.add_header('Accept', 'application/json')
    payload = urllib2.urlopen(request)
    return json.loads(payload.read())


def move_in_queue(_from, to):
    data = urllib.urlencode({
        'organization': ORG_ID,
        'room_code': ROOM_ID,
        'session': SESSION_ID,
        'from': _from,
        'to': to,
    })
    request = urllib2.Request("http://vbsongs.com/api/v1/queue/reorder")
    request.add_header('Accept', 'application/json')
    payload = urllib2.urlopen(request, data=data)
    return json.loads(payload.read())
