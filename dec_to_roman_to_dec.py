#!/usr/bin/env python
import os, sys, getopt

class RomanDecimalChart:
	'''
		RomanDecimalChart allow user to convert decimal number to roman character or viceversa.
		x = RomanDecimalChart()
		print x.dec_to_roman(6)
		print x.roman_to_dec("VI")
	'''

	def __init__(self):
		self.chart = [['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]

	def dec_to_roman (self, integer):
		returnstring=''
		for n in self.chart:
			while integer-n[1]>=0:

				integer-=n[1]
				returnstring+=n[0]

		return returnstring

	def roman_to_dec (self, string):

		returnint=0
		for n in self.chart:
			cont_yes=True

			while cont_yes:
				if len(string)>=len(n[0]):

					if string[0:len(n[0])]==n[0]:
						returnint+=n[1]
						string=string[len(n[0]):]

					else: cont_yes=False
				else: cont_yes=False
		return returnint


def main(argv):
	try:
	  opts, args = getopt.getopt(argv,"hvn:r:",["n=","range=","version="])
	except getopt.GetoptError:
	  print 'dec_to_roman_to_dec.py -n <number> -r <range> -v <version>'
	  sys.exit(2)
	x = RomanDecimalChart()
	print ""
	try: 
		for opt, arg in opts:
			if opt == '-h':
				print 'dec_to_roman_to_dec.py -n <number> -r <range> -v <version>'
				sys.exit()
			elif opt in ('-v'):
				print "|" + "-" * 50
				print "|  Copyright by 	: Anuj Patel"
				print '|  version 		: v1.0'
				print "|" + "-" * 50
				sys.exit()
			elif opt in ("-n", "--number"):
				roman = x.dec_to_roman(int(arg))
				roman_dec = x.roman_to_dec(str(roman))
				
				#print int(arg) + " => " + str(roman)+ " => " + int(d)
				print "Decimaal => Roman Character => Decimal"
				print arg + " => " +  roman + " =>  "  + str(roman_dec) 
				sys.exit()
			elif opt in ("-r", "--range"):
				rng = arg.split('-')
				print "Decimaal => Roman Character => Decimal"
				for y in range(int(rng[0]), int(rng[1])):
					roman = x.dec_to_roman(y)
					roman_dec = x.roman_to_dec(str(roman))
					print arg + " => " +  roman + " =>  "  + str(roman_dec) 

				
				sys.exit()
			else:
				print 'dec_to_roman_to_dec.py -n <number> -r <range> -v <version>'
				sys.exit()
	except Exception as e:
		print e

	
if __name__ == "__main__":
	main(sys.argv[1:])






