#!/usr/bin/python
"""
gridGen
by Lars Otten <lotten@uci.edu>, 2016.

Python script that generates grid-shaped graphical models in UAI file format.

Usage:
$ gridGen.py N [det]
where N is grid size (N x N) and det (optionally) is the level of forced determinism.
"""

import sys
import os
import random

DOMAIN_SIZE = 2
NETWORK_TYPE = 'MARKOV'
FLOAT_FORMAT = '%.3f'

def main(size, deteterminism):
  print NETWORK_TYPE
  # Domain info
  no_var = size ** 2
  print no_var
  for i in range(no_var):
    print DOMAIN_SIZE,
  print

  # Number of functions
  no_fun = 2 * size * (size-1)
  print no_fun

  # Function scope info, horizontal edges first
  for row in range(size):
    for col in range(size-1):
      print '2', col + row * size, col + 1 + row * size
  for col in range(size):
    for row in range(size-1):
      print '2', col + row * size, col + size + row * size  

  # Randomly generated function tables
  table_size = DOMAIN_SIZE ** 2
  for i in range(no_fun):
    print
    print table_size
    for j in range(DOMAIN_SIZE):
      for k in range(DOMAIN_SIZE):
        if random.random() < deteterminism:
          print FLOAT_FORMAT % 0,
        else:
          print FLOAT_FORMAT % (1-random.random()),
      print

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print 'Need to specify grid size and (optionally) level of determinism.'
  else:
    size = int(sys.argv[1])
    determinism = float(sys.argv[2]) if len(sys.argv) > 2 else .5
    if determinism < 0 or determinism > 1:
      print 'Invalid determinism value %f, required within [0,1].' % determinism
    else:
      random.seed()
      main(size, determinism)
