
__author__='''

######################################################
                By Nexsct                          
######################################################

    Bill Munene
    Admin
    Nexsct sys
    bill.munene@outlook.com

######################################################
'''
print (__author__)
import os
def main():
	try:
		try:
			import Tkinter
		except:
			import tkinter
		import pyglet
		os.system("cd Tools && python Gui.py")
	except Exception as e:
		print(e)
		input("")
if __name__=='__main__':
	main()
