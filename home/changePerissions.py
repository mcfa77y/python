#!/usr/bin/python
# Quick hack fix to recursively re-make symlinks with full permissions
#
# Author : Dan Kripac
# 
# usage:
#     fixSymLinkPermissions.py [ optional_File_Or_Dir_List ]
#
# Defaults to the current working directory if no arguments are given.
#
# Should avoid recursing to linked directories outside the directories
# that you initiate the process from (i.e outside the current working 
# directory by default)
#

import os, sys, threading, signal

symlinkMutex = threading.Lock()

def signalHandle(signum, frame):
	# wait for any symlink operations to finish so we don't leave
	# any removed symlinks unmade
	symlinkMutex.acquire()
	print('Gracefully quiting...')
	sys.exit(1)

signal.signal( signal.SIGTERM, signalHandle )
signal.signal( signal.SIGHUP,  signalHandle )
signal.signal( signal.SIGABRT, signalHandle )
signal.signal( signal.SIGINT,  signalHandle )
signal.signal( signal.SIGQUIT, signalHandle )

def fixSymLinkPermissions( fileList, recursiveLinkDomain=[] ):	
	if os.getuid() != 0:
		if __name__ == '__main__':
			print('fixSymLinkPermissions : ERROR : must be run as super user.')
			sys.exit(1)
		else:
			raise OSError('fixSymLinkPermissions : ERROR : must be run as super user.')
		
	for f in fileList:
		if os.path.exists( f ):
			if os.path.islink( f ):
				try:
					linkLoc = os.readlink( f )
					absLinkLoc = os.path.abspath( linkLoc )
					oldumask = os.umask( 0000 )
					print('Re-creating symlink %r -> %r' % (f,linkLoc) )
					symlinkMutex.acquire()
					try:
						os.remove( f )
						os.symlink( linkLoc, f )
						pass
					finally:
						symlinkMutex.release()
						
					os.umask( oldumask )
					if os.path.isdir( linkLoc ):
						outsideLinkDomain = False
						for p in recursiveLinkDomain:
							relpath = os.path.relpath(absLinkLoc,p)
							if len(relpath) and relpath[0] == '.':
								outsideLinkDomain = True
							elif len(relpath) == 0:
								outsideLinkDomain = True
								
						if not outsideLinkDomain:
							fixSymLinkPermissions( [ absLinkLoc ], recursiveLinkDomain=recursiveLinkDomain )
						else:
							print('skipping recursion to link %r' % absLinkLoc )
						
				except Exception, err:
					print('ERROR : %s creating symlink %r -> %r' % (err,f,linkLoc))
					
			elif os.path.isdir( f ):
				childFileList = []
				for c in os.listdir( f ):
					p = os.path.join( f, c )
					if os.path.exists( p ):
						childFileList.append( p )
					else:
						print('path %r doesn\'t eixist?' % c)
				
				if len(childFileList):
					fixSymLinkPermissions( childFileList, recursiveLinkDomain=recursiveLinkDomain )
		else:
			print('fixSymLinkPermissions : path %r does not exist?' % f )

if __name__ == '__main__':
	if len(sys.argv) == 1:
		fixSymLinkPermissions( [ os.getcwd() ], recursiveLinkDomain=[ os.getcwd() ] )
	else:
		fileList = []
		linkDomain = []
		for f in sys.argv[1:]:
			if not os.path.isabs( f ):
				if os.path.exists( os.path.abspath( f ) ):
					fileList.append( os.path.abspath( f ) )
			elif os.path.exists( f ):
				fileList.append( f )
			
			if os.isdir( fileList[-1] ):
				if not fileList[-1] in linkDomain:
					linkDomain.append( fileList[-1] )
			else:
				parentDir = os.path.split( fileList[-1] )[0]
				if not parentDir in linkDomain:
					linkDomain.append( parentDir )

		fixSymLinkPermissions( fileList, recursiveLinkDomain=linkDomain )
