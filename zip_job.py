#!/usr/bin/python3

from zipfile import *
import os


array = ['a', 'b', 'c', 'd']
VERSION = os.environ['VERSION']


for arr in array:
    open('{}.txt'.format(arr), 'w')
    open('{}.txt'.format(arr), 'r')
    with ZipFile('{}_{}.zip'.format(arr, VERSION), 'w') as zipf:
        zipf.write('{}.txt'.format(arr))
    open('{}_{}.zip'.format(arr, VERSION), 'r')
