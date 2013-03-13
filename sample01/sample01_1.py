#!/usr/bin/env python
# -*- coding: utf-8 -*-

from swiftclient import *

auth_url = "http://localhost:8080/auth/v1.0"
user = "test:tester"
key = "testing"

(url, token) = get_auth(auth_url, user, key)

print "storage url:%s" % url
print "token      :%s" % token

(resp_headers, containers) = get_account(url, token)

print "\n<response headers>"
for (k, v) in resp_headers.items():
    print "%s : %s" % (k, v)
print "\n<containers>"
for c in containers:
    print "%s" % c
