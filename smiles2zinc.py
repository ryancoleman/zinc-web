#!/usr/bin/env python

#script reads smiles from a file or command line
#output smiles with ZINC codes added. 
#http://zinc.docking.org
#Ryan G. Coleman
#https://github.com/ryancoleman/zinc-web

import sys #always, pretty much
import string #string handling
import urllib2 #url handling
import urllib #url encoding
import argparse

def smiles2zinc(smilesString):
  '''function that takes single smiles, returns ZINC code.'''
  dataDict = {'structure.similarity':'identity', \
      'structure.smiles':smilesString, \
      'page.format':'smiles'}
  smilesEncode = urllib.urlencode(dataDict)
  request = urllib2.Request(url='http://zinc.docking.org/results/structure', \
      data=smilesEncode)
  result = urllib2.urlopen(request)
  dataOut = result.read()
  return dataOut

def parse_arguments():
  '''defines the arguments, returns the parsed arguments (or nothing) if help
  / usage shown instead'''
  parser = argparse.ArgumentParser( \
      description='gets a ZINC code for any smiles')
  parser.add_argument('infile', nargs='?', default=sys.stdin, \
      help='infile filenames, default is standard input')
  arguments = parser.parse_args()
  return arguments

def run_lots(arguments):
  '''takes input, reads smiles, passes to the smilez2zinc function'''
  if arguments.infile == sys.stdin:
    openfile = arguments.infile
  else:
    openfile = open(arguments.infile, 'r')
  for line in openfile:
    smilesZinc = smiles2zinc(string.strip(line))
    print string.strip(smilesZinc)
  

if __name__ == '__main__':
  #print smiles2zinc('COc1ccc(cc1C2OCC(CO2)(CO)[N+](=O)[O-])[N+](=O)[O-]')
  arguments = parse_arguments()
  run_lots(arguments)
