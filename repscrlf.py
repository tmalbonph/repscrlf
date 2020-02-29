#!/usr/bin/env python3
"""The Space, CR+LF Stripper, version 1.0.1
"""
# BSD 3-Clause License

# Copyright (c) 2020, Teddy Albon Sr.
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.

# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.

# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
from __future__ import print_function
import os
import sys


def print_stderr(*args, **kwargs):
    """Write string to stderr"""
    print(*args, file=sys.stderr, **kwargs)


def usage(err_msg, is_quite):
    """How to use"""
    if not is_quite:
        print_stderr('')
        print_stderr('repscrlf, version 1.0.1, (c) 2019-2020 albonteddy at gmail dot com')
        print_stderr('Replace space and/or CR+LF from a text file.')
        print_stderr('')
        print_stderr('usage: {} source_filename [-quite, -q]'.format(sys.argv[0]))
        print_stderr('')
    if err_msg:
        print_stderr('ERROR: {}'.format(err_msg))
        print_stderr('')
    # Return the conversion as EMPTY string
    print('')
    return True


def main():
    """
    repscrlf - The Space, CR+LF Stripper, version 1.0.1\n
    \n
    purpose  - this is mainly use to convert a JSON file\n
               and use the converted text as parameter\n
               to another software, like aws cli, etc.\n
    \n
    input    - a JSON file or text file
    \n
    output   - a text file without CR+LF or SPACE written into stdout.\n
    \n
    notes    - on error, the messages is written into stderr so that\n
               the error will not interfer with the result on stdout.\n
    \n
    """
    is_quite = False
    s_unknown = None
    if len(sys.argv) > 2:
        if sys.argv[2] in ['-quite', '-q']:
            is_quite = True
        else:
            s_unknown = sys.argv[2]
    if len(sys.argv) < 2:
        return usage('Missing source_filename', is_quite)
    file_name = sys.argv[1]
    if not os.path.isfile(file_name):
        return usage("Missing file '{}'".format(file_name), is_quite)
    if s_unknown:
        return usage("Unknown option {}".format(s_unknown), True)
    input_f = open(file_name, mode='r')
    s_lines = input_f.readlines()
    input_f.close()
    n_lines = len(s_lines)
    s_file = ''
    for n_i in range(n_lines):
        row = s_lines[n_i]
        text = row.replace(' ', '')
        row = text.replace('\n', '')
        s_file += row
    # Return the conversion as string without spaces and/or CR+LF.
    print("{}".format(s_file))
    return True

main()
