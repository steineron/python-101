import sys
import os
import commands

def list_dir(dir):
	cmd = 'ls -l '+dir
	filenames = os.path.listdir(dir)
	for filename in filenames:
		path = os.join(dir,filename)
		print path
		pring os.path.abspath(path)
		