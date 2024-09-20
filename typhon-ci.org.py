#!/usr/bin/env python3

from gandi import Domain

root = Domain("typhon-ci.org")

# mailo
root.txt("@", "mailo=dsOW4yoKVf0lN0MYilawU29gKuufMJsN")
root.mx("@", "mx.mailo.com.")
root.spf("@", "v=spf1 a include:mailo.com -all")
root.txt("mailo._domainKey", "v=DKIM1; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCdwAJaRCIWEd088s1Ybf0fa/jm4Mfoxj4+2SwqDretnglKBDdUKFilOKsm98PPyzLKmOzcIbDl7/T2A9XF615l6bKEZIlQVmkEQ3ssiU92R9Fq44w8Ru6gMO1danULThxdGJ/HrJ2BXpGBzCNCF9b4liDi1eZxNIH8dtv9QHujiwIDAQAB;")
root.txt("_dmarc", "v=DMARC1; p=quarantine;")

# github
root.txt("_github-pages-challenge-typhon-ci", "c610846f2a7dcf5730ad0344a3d058")
root.txt("_gh-typhon-ci", "928a457aa7")
for x in ["08","09","10","11"]:
    y = "185.199.1"+x+".153"
    root.a("@", y)
for x in ["0","1","2","3"]:
    y = "2606:50c0:800"+x+"::153"
    root.aaaa("@", y)
root.cname("www", "typhon-ci.github.io.")
root.cname("doc", "typhon-ci.github.io.")

# etna
root.a("etna", "49.12.195.166")
root.aaaa("etna", "2a01:4f8:1c1c:180d::1")

print(root.push())
