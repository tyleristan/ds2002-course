#!/usr/bin/env python

import os

os.environ["COLLEGE"] = input('Are you a college student? ')
os.environ["UNI"] = input('What university do you go to? ')
os.environ["SCHOOL"] = input('What school of the University of Virginia are you in? ')

print(os.getenv("COLLEGE"))
print(os.getenv("UNI"))
print(os.getenv("SCHOOL"))


