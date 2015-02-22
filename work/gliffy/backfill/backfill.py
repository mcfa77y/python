#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, os, re
import json
import argparse

from s3 import S3
from db import DB
        
def initGlobals(config):
  global PREFIX, SUFFIX, IMAGE_PATTERN, IMAGE_THUMB_PATTERN, IMAGE_DIR, QUERY_WINDOW, QUERY_MAX_ROWS, s3, IS_DIAGRAM
  PREFIX = config["PREFIX"]
  SUFFIX = config["SUFFIX"]

  IMAGE_PATTERN = re.compile(config["IMAGE_PATTERN"], re.IGNORECASE)
  IMAGE_THUMB_PATTERN = re.compile(config["IMAGE_THUMB_PATTERN"], re.IGNORECASE)

  IMAGE_DIR = config["IMAGE_DIR"]
  QUERY_WINDOW = config["QUERY_WINDOW"]
  QUERY_MAX_ROWS = config["QUERY_MAX_ROWS"]

  IS_DIAGRAM = config["IS_DIAGRAM"]

  s3 = S3(config["BUCKET_NAME"], config["AWS_ACCESS_KEY_ID"], config["AWS_SECRET_ACCESS_KEY"])

def main():
  # get arguments
  parser = argparse.ArgumentParser(description='backfill images from db to aws')
  parser.add_argument('config', nargs=1, type=argparse.FileType('r'), default=sys.stdin, help="json config file")
  # print vars(parser.parse_args())['config']
  
  # load config file as json
  config = json.load(vars(parser.parse_args())['config'][0])

  initGlobals(config)

  

  db = DB(config["DB_URL"], config["DB_NAME"], config["USER"], config["PASSWORD"], 
          config["QUERY"], config["QUERY_WINDOW"], config["TABLE_NAME"])
  
  i = 0
  while i * QUERY_WINDOW < QUERY_MAX_ROWS:
    paths = db.getImagePaths(i)
    i += 1
    for idNumber, path in paths.iteritems():
      if putFile(IMAGE_DIR + path, idNumber):
        db.markSuccess(idNumber)
      else:
        db.markFail(idNumber)
    
  sys.exit()

# take given path and walk the directory looking for files
# and put them into s3
def putFile(path, idNumber):
  for root, dirs, files in os.walk(path):
    print root, "consumes"
    for name in files:
      filenamePath = root+"/"+name
      with open(filenamePath,'r') as phile:
        if 'swf' in name:
          continue
        idNumber = root.split("/")[-1]
        key = ""
        name = name.encode("ascii")
        info = "\n\tid: " + idNumber + " name: " + name
        print info
        # for diagrams skip if file name doesn't match id
        if idNumber not in name and IS_DIAGRAM:
          print "\tSKIPPING: " + idNumber + " not in " + name
          continue
        # found image
        if IMAGE_PATTERN.match(name) != None and len(IMAGE_PATTERN.match(name).group()) > 0:
          key = getKey(idNumber)
          print "\tput Image"
        # found image thumbnail
        elif IMAGE_THUMB_PATTERN.match(name) != None and len(IMAGE_THUMB_PATTERN.match(name).group()) > 0:
          key = getThumbKey(idNumber)
          print "\tput Image thumbnail"
        elif key == "":
          print "ERROR: cannot add - " + name
          return False
          continue
        print("\tKEY: " + key)
        # write to s3
        if s3.put(key, phile) == False:
          return False
  return True

def getKey(idNumber):
  return PREFIX + str(idNumber)

def getThumbKey(idNumber):
  return getKey(idNumber) + SUFFIX

main()
