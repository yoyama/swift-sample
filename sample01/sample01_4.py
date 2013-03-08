#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from swiftclient import *


def create_container(conn, container):
    try:
        conn.put_container(container)
    except:
        pass
    try:
        headers = conn.head_container(container)
        return headers
    except:
        raise


auth_url = "http://localhost:8080/auth/v1.0"
user = "test:tester"
key = "testing"

if(len(sys.argv) != 4):
    print "%s container object_name file_to_uploaded" % sys.argv[0]
    sys.exit(1)

container_name = sys.argv[1]
object_name = sys.argv[2]
upload_file = sys.argv[3]

try:
    conn = Connection(auth_url, user, key)
    create_container(conn, container_name)
    f = open(upload_file, 'r')
    conn.put_object(container_name, object_name, f, chunk_size=4096)
    headers = conn.head_object(container_name, object_name)
    for (k, v) in headers.items():
        print "%s : %s" % (k, v)

except:
    print "Exception occured"
    raise
