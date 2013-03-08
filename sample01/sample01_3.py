#!/usr/bin/env python
# -*- coding: utf-8 -*-

from swiftclient import *

auth_url = "http://localhost:8080/auth/v1.0"
user = "test:tester"
key = "testing"

conn = Connection(auth_url, user, key)

resp_headers = conn.head_account()

print "storage url:%s" % conn.url
print "token      :%s" % conn.token
