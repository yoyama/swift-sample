#!/usr/bin/env python
# -*- coding: utf-8 -*-

from swiftclient import *

auth_url = "http://localhost:8080/auth/v1.0"
user = "test:tester"
key = "testing"

conn = Connection(auth_url, user, key)

(resp_headers, containers) = conn.get_account()

print "<response headers>"
for (k, v) in resp_headers.items():
    print "%s : %s" % (k, v)

print "\n<containers>"
for c in containers:
    print "%s" % c
