#!/usr/bin/python3

from zipfile import *

array = ['a', 'b', 'c', 'd']
VERSION = '1.2.0'


for arr in array:
    open('{}.txt'.format(arr), 'w')

for arr in array:
    try:
       open('{}.txt'.format(arr), 'r')
    except IndexError:
                     print("ERROR: something went wrong")

for arr in array:
    with ZipFile('{}_{}.zip'.format(arr, VERSION), 'w') as zipf:
        zipf.write('{}.txt'.format(arr))

for arr in array:
    try:
       open('{}_{}.zip'.format(arr, VERSION), 'r')
    except IndexError:
                     print("ERROR: something went wrong")
