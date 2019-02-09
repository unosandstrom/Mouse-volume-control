#!/usr/bin/env python

import os
from Xlib import X, display
from Xlib.ext import record
from Xlib.protocol import rq

record_dpy = display.Display()

ctx = record_dpy.record_create_context(
        0,
        [record.AllClients],
        [{
                'core_requests': (0, 0),
                'core_replies': (0, 0),
                'ext_requests': (0, 0, 0, 0),
                'ext_replies': (0, 0, 0, 0),
                'delivered_events': (0, 0),
                'device_events': (X.KeyPress, X.MotionNotify),
                'errors': (0, 0),
                'client_started': False,
                'client_died': False,
        }])

def record_callback(reply):
    data = reply.data
    while len(data):
        event, data = rq.EventField(None).parse_binary_value(data, record_dpy.display, None, None)        
        if event.type == X.ButtonPress:
#            print  event.detail, event.root_x, event.root_y 
            if event.root_x < 20:
                if event.detail is 4 : 
                    os.system("amixer -D pulse sset Master 2%+ & pid=$!") 
                if event.detail is 5 :
                    os.system("amixer -D pulse sset Master 5%- & pid=$!") 
             
record_dpy.record_enable_context(ctx, record_callback)
