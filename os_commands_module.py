#!/usr/bin/python -tt

import sys
import os
import commands

def list_dir(dir):
	cmd = 'ls -l '+dir
	(status,output) = commands.getstatusoutput(cmd)
	filenames = os.listdir(dir)
	for filename in filenames:
		path = os.path.join(dir,filename)
		print path
		print os.path.abspath(path)
		
		
def main():

	if len(sys.argv) >= 2:
		dir = sys.argv[1]
	else:
		dir = '.'

	list_dir(dir)


if __name__ == '__main__':
  main()