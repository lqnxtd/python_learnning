#!/usr/bin/env python

'makeTextFile.py -- create text file'

import os

ls = os.linesep
#fname = 't.txt'
fname = ''

while True:
    if os.path.exists(fname):
        print("error: '%s' already exists" % fname)
    else:
        break
        
all = []

print("\nEnter lines ('.' by itself to quit).\n")

while True:
    entry = input('>')
    if entry == '.':
        break
    else:
        all.append(entry)
        
fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()

print('DONE!')