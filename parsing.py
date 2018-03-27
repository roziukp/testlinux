import argparse
import sys


def createParser():
	parser=argparse.ArgumentParser()
	subparser=parser.add_subparsers (dest='command')

	hello_parser=subparser.add_parser('hello')
	hello_parser.add_argument('--name','-n', nargs='+', default=['world'])


	goodbay_parser=subparser.add_parser('goodbay')
	goodbay_parser.add_argument('-c',type=int, default=1)

	return parser


def run_hello(namespace):

	for names in namespace.name:
		print('Hello,{}'.format(names))


def run_goodbay(namespace):
	for _ in range(namespace.c):
		print("Goodbay")



def main():
	parser=createParser()
	namespace=parser.parse_args(sys.argv[1:])


	if namespace.command == 'hello':
		run_hello(namespace)
	elif namespace.command == 'goodbay':
		run_goodbay(namespace)

	else:
		print('Wrong input values!')

if __name__=='__main__':
	main()