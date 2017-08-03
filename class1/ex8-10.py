#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

conf = CiscoConfParse("cisco_ipsec.txt")

cryptos = conf.find_objects(r"^crypto map CRYPTO")


# ex 8
for i in cryptos:
    print i.text
    for c in i.children:
        print c.text

#ex 9
print "\n\n############## ex 9 ################\n\n"
pfs_group2 = conf.find_objects_w_child(r"^crypto map CRYPTO", childspec=r"set pfs group2")

for i in pfs_group2:
    print i.text
    for c in i.children:
        print c.text


#ex 10
print "\n\n############## ex 10 ################\n\n"
no_aes = conf.find_objects_wo_child(r"^crypto map CRYPTO", childspec=r"set transform-set AES")

for i in no_aes:
    print i.text
    for c in i.children:
        print c.text
