#!/usr/bin/env python3

from gandi import Domain

gandi_ip_v4 = "92.243.26.156"
gandi_ip_v6 = "2001:4b98:dc0:43:f816:3eff:fe36:b573"
ovh_ip_v4 = "51.178.183.169"
ovh_ip_v6 = "2001:41d0:404:200::38e2"

typhon = Domain("typhon-ci.org")

typhon.a("@", gandi_ip_v4)
typhon.a("www", gandi_ip_v4)
typhon.aaaa("@", gandi_ip_v6)
typhon.aaaa("www", gandi_ip_v6)

typhon.a("etna", ovh_ip_v4)
typhon.aaaa("etna", ovh_ip_v6)

print(typhon.push())
