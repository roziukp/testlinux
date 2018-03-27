import argparse
import sys


def createParser():
	parser=argparse.ArgumentParser()
	parser.add_argument('-c',type=int,default=1)
	parser.add_argument('name')

	return parser

def main():
	parser=createParser()
	namespace=parser.parse_args(sys.argv[1:])


	for _ in range(namespace.c):
		print('Hello, {}'.format(namespace.name))


if __name__=='__main__':
	main()