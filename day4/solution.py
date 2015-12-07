#!/usr/bin/env python

import md5

start = 0
found = False
secret_key = "yzbqklnj"

while not found:
    md5_hash = md5.new(secret_key + str(start))
    key = md5_hash.hexdigest()
    found = key[0:5] == "00000"
    start += 1

print(start - 1, key)

