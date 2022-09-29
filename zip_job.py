#!/usr/bin/python3

from zipfile import *
import os


array = ['a', 'b', 'c', 'd']
VERSION = os.environ['VERSION']


for arr in array:
    open('{}.txt'.format(arr), 'w')

for arr in array:
     open('{}.txt'.format(arr), 'r')

for arr in array:
    with ZipFile('{}_{}.zip'.format(arr, VERSION), 'w') as zipf:
        zipf.write('{}.txt'.format(arr))

for arr in array:
     open('{}_{}.zip'.format(arr, VERSION), 'r')
