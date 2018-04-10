#!/usr/bin/env python3

f = open('botocore_import.txt')

list = []
line = "start"
while line:
    line = f.readline()
    l = line.split()
    if len(l) == 2:
        list.append(l[1])

res = set(list)
print(res)

f.close()
