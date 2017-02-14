#!/usr/bin/env python3
import sys
import re
import os
import codecs

input_filename = sys.argv[1]
output_filename = sys.argv[2]

file_size = round(os.path.getsize(input_filename) / (1024 ** 3))
print('input size is %.1f GB' % file_size)

with codecs.open(input_filename, encoding='utf-8') as input_file, codecs.open(output_filename, 'w', 'utf-8') as output_file:
    read_bytes = 0
    print_chunk = 1024 ** 3
    next_print = 0.1

    line = input_file.readline()
    while not line.startswith('INSERT'):
        line = input_file.readline()

    while line:
        if re.search(r'\(.+\)[,;]', line):
            row = line \
                .replace('(', '')

            row = re.sub(r'\)[,;]', '', row)
            output_file.write(row)
        if input_file.tell() > print_chunk * next_print:
            print('converted %.1f GB out of %.1f' % (next_print, file_size))
            next_print += 0.1
        line = input_file.readline()