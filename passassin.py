#!/usr/bin/python3

#
# passassin
#
# deterministically generates site-specific passwords which conform
# to the password rules of most sites
#

import sys
import getpass
import hmac
import hashlib

SYMBOLS = '%&-_#,.?/' 
LOWER = 'abcdefghijklmnopqrstuvwxyz'
UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
DIGITS = '0123456789'
ALL = SYMBOLS + LOWER + UPPER + DIGITS
NUM_CHARS = len(ALL)

MIN_SYMBOLS = 2
MIN_LOWER = 2
MIN_UPPER = 2
MIN_DIGITS = 2
LENGTH = 16

def main():
	# get user input
	master = getpass.getpass('master passphrase: ')
	print('website: ', end='', flush=True)
	org = sys.stdin.readline().rstrip()

	# generate passwords until one is valid
	attempt = 0
	while True:
		candidate = gen_candidate(master, org, attempt)
		if is_valid(candidate):
			print(candidate)
			return
		attempt += 1

def gen_candidate(master, org, attempt):
	digest = hmac.new(bytes(master + str(attempt), 'latin-1'), bytes(org, 'latin-1'), hashlib.sha256).digest()
	candidate = ''
	num = int.from_bytes(digest, byteorder='little')
	for i in range(0, LENGTH):
		index = num % NUM_CHARS
		num = num // NUM_CHARS
		candidate += ALL[index]
	return candidate

def is_valid(candidate):
	symbols = 0
	lower = 0
	upper = 0
	digits = 0
	for i in range(0, LENGTH):
		if candidate[i] in SYMBOLS:
			symbols += 1
		elif candidate[i] in LOWER:
			lower += 1
		elif candidate[i] in UPPER:
			upper += 1
		elif candidate[i] in DIGITS:
			digits += 1
	if symbols < MIN_SYMBOLS:
		return False
	if lower < MIN_LOWER:
		return False
	if upper < MIN_UPPER:
		return False
	if digits < MIN_DIGITS:
		return False
	return True

if __name__ == '__main__':
	main()
