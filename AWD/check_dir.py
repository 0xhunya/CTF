# -*- coding:utf-8 -*-
#昏鸦

import os
import time

def gettime():
	return time.strftime('[%Y-%m-%d/%H:%M:%S]',time.localtime(time.time()))

def getdirlist():
	dirlist = []
	for root, dirs, files in os.walk(r".", topdown=False):
		for name in files:
			dirlist.append(os.path.join(root, name))
	return dirlist

def main():
	while 1:
		dirs = getdirlist()
		time.sleep(1)
		new_dirs = getdirlist()
		if new_dirs == dirs:
			pass
		else:
			if len(list(set(new_dirs).difference(set(dirs))))==0:
				s = "- {}".format(','.join(list(set(dirs).difference(set(new_dirs)))))
			else:
				s = "+ {}".format(','.join(list(set(new_dirs).difference(set(dirs)))))
			print "{} {}".format(gettime(),s)

if __name__ == '__main__':
	main()
