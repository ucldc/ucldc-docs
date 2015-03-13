#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os
import subprocess
from bs4 import BeautifulSoup
from pprint import pprint as pp


def main(argv=None):
    """ mirror the files """
    print(subprocess.check_call(
        'wget -mkEpnp -N -w 1 http://ucldc.github.io/ucldc-docs/'.split()
    ))

    for root, dirs, files in os.walk('ucldc.github.io'):
        for f in files:
            if (f.endswith('.html')):
                fix_links(os.path.join(root, f))


def fix_links(filename):
    """ rewrite the links """
    htmlDoc = open(filename, 'r')
    soup = BeautifulSoup(htmlDoc)
    for link in soup.find_all(['a', 'link'], { 'href': True}):
        if link['href'].endswith('index.html'):
            link['href'] = link['href'][:-10]
            print(link['href'])

    htmlDoc.close()

    html = unicode(soup).encode('utf-8')

    with open(filename, "wb") as f:
        f.write(html)


# main() idiom for importing into REPL for debugging
if __name__ == "__main__":
    sys.exit(main())


"""
Copyright © 2015, Regents of the University of California
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
- Redistributions of source code must retain the above copyright notice,
  this list of conditions and the following disclaimer.
- Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
- Neither the name of the University of California nor the names of its
  contributors may be used to endorse or promote products derived from this
  software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""
