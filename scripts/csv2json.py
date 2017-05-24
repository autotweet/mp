#!/usr/bin/env python

import json
import sys

with open(sys.argv[1]) as f:
    # Skip header
    f.readline()
    d = {}
    for line in f:
        idx, name, surname, twitter, _ = line.strip().split('\t', 4)
        name    = name.strip("-'\" ")
        surname = surname.strip("-'\" ")
        twitter = twitter.strip("-'\" ")
        if twitter.startswith('@'):
            twitter = twitter.split()[0]
            d['%s %s' % (name, surname)] = twitter

    print(str(d).replace(',', ',\n'))
