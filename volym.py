#!/usr/bin/env python

# Systemvolymen justeras om musen förs ut till vänster sida och man rullar på musen rulle.

import os
from Xlib import X, display
from Xlib.ext import record
from Xlib.protocol import rq

a = display.Display()

b = a.record_create_context(0, [record.AllClients], 
        [{'core_requests': (0, 0),
          'core_replies': (0, 0),
          'ext_requests': (0, 0, 0, 0),
          'ext_replies': (0, 0, 0, 0),
          'delivered_events': (0, 0),
          'device_events': (X.KeyPress, X.MotionNotify),
          'errors': (0, 0),
          'client_started': False,
          'client_died': False}])

def notera_svar(svar):
    data = svar.data
    while len(data):
        handelse, data = rq.EventField(None).parse_binary_value(data, a.display, None, None)        
        if handelse.type == X.ButtonPress:
            if handelse.root_x < 20:
                if handelse.detail is 4 : os.system("amixer -D pulse sset Master 2%+ & pid=$!") 
                if handelse.detail is 5 : os.system("amixer -D pulse sset Master 5%- & pid=$!") 
             
a.record_enable_context(b, notera_svar)
