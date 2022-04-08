#!/usr/bin/env python3

from gandi import Domain

import httplib2

ovh_ip_v4 = "94.23.42.126"

root = Domain("pnm.tf")

# search engine webmaster console verifications
root.txt("@", "google-site-verification=qE-tHUdg2oCWilirbY7HeYq_kRVR1s3Pb1ujq6D0y5Q")
root.cname("b6cf11c9ba9ca8a6b661ffb0d0b99f23", "verify.bing.com.")

# DMARC for all mails
root.txt("_dmarc", "v=DMARC1; p=none; rua=mailto:root@pnm.tf")

# mailo
root.txt("@", "mailo=giJHSYjeyz3bCIAriAxVjcGHgOrxjcon")
root.mx("@", "mx.mailo.com.")
root.spf("@", "a include:mailo.com")

# servers
root.a("@", ovh_ip_v4)
root.a("www", ovh_ip_v4)

print(root.push())
