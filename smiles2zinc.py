#!/usr/bin/env python

#script reads smiles from a file or command line
#output smiles with ZINC codes added. 
#http://zinc.docking.org
#Ryan G. Coleman
#https://github.com/ryancoleman/zinc-web

import sys
import urllib2
import urllib

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

if __name__ == '__main__':
  print smiles2zinc('COc1ccc(cc1C2OCC(CO2)(CO)[N+](=O)[O-])[N+](=O)[O-]')
