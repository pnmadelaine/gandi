#!/usr/bin/env python3

from gandi import Domain

gandi_ip_v4 = "92.243.26.156"
gandi_ip_v6 = "2001:4b98:dc0:43:f816:3eff:fe36:b573"

typhon = Domain("typhon-ci.org")

typhon.a("@", gandi_ip_v4)
typhon.a("www", gandi_ip_v4)
typhon.aaaa("@", gandi_ip_v6)
typhon.aaaa("www", gandi_ip_v6)

print(typhon.push())
