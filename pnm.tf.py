#!/usr/bin/env python3

from gandi import Domain

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

# github
root.txt("_github-pages-challenge-pnmadelaine", "299d6a2706fcb22d5aa713aaa4472c")
for x in ["08","09","10","11"]:
    y = "185.199.1"+x+".153"
    root.a("@", y)
for x in ["0","1","2","3"]:
    y = "2606:50c0:800"+x+"::153"
    root.aaaa("@", y)
root.cname("www", "pnmadelaine.github.io.")

print(root.push())
