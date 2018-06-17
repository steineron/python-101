#!/usr/bin/python -tt

import sys
import os
import commands

def list_dir(dir):
	filenames = os.listdir(dir)
	for filename in filenames:
		path = os.path.join(dir,filename)
		print path
		print os.path.abspath(path)
		
def list_dir_cmd(dir):
		cmd = 'ls -l '+dir
		(status,output) = commands.getstatusoutput(cmd)
		if status:
			print 'the was an error'
		else:
			print output


def main():

	if len(sys.argv) >= 2:
		dir = sys.argv[1]
	else:
		dir = '.'

	list_dir_cmd(dir)


if __name__ == '__main__':
  main()