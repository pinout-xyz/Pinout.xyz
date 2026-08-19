#!/usr/bin/env python3

import sys

from pinoutxyz.build import build
from pinoutxyz.site import Site

build(Site('.', sys.argv[1] if len(sys.argv) > 1 else 'en'))
