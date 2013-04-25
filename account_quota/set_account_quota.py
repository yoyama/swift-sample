#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from optparse import OptionParser
from swiftclient import *


usage = "usage: %prog -a <ACCOUNT> (-s <BYTES> | -u)"
parser = OptionParser(usage=usage)
parser.add_option("-a", "--account", dest="account", default=None,
                  help="an account name which is set account quota.",
                  metavar="<ACCOUNT>")
parser.add_option("-s", "--set", dest="quota_bytes",
                  help="set account quota as the bytes", metavar="BYTES",
                  type="int")
parser.add_option("-u", "--unset", dest="remove_quota", default=False,
                  action="store_true", help="unset account quota")

(options, args) = parser.parse_args()

if not options.account:
    print "no account is specified."
    parser.print_help()
    sys.exit(1)

if options.remove_quota and options.quota_bytes or \
        not options.remove_quota and not options.quota_bytes:
    print "-s or -u should be specified exclusively."
    parser.print_help()
    sys.exit(1)

auth_url = "http://localhost:8080/auth/v1.0"
reseller_user = "admin:admin"
reseller_key = "admin"

(reseller_url, reseller_token) = get_auth(auth_url,
                                          reseller_user, reseller_key)

user_url = "http://localhost:8080/v1/AUTH_%s" % (options.account)

conn = Connection(preauthtoken=reseller_token, preauthurl=user_url)

if options.remove_quota:
    headers = {'X-Account-meta-quota-bytes': ''}
else:
    headers = {'X-Account-meta-quota-bytes': options.quota_bytes}
conn.post_account(headers)
