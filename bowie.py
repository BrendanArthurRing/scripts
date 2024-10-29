#!/usr/bin/python

from sys import argv

script, file, word_count = argv

# Convert word_count argument to int.
word_count = int(word_count)

# Read the contents of 'file' given as argument.
#input_file = open(file)
#input_text = input_file.read()

input_file = open(file) 
input_text = input_file.read().decode(errors='replace')

# To get rid of UTF 8 error
# https://itsmycode.com/unicodedecodeerror-utf8-codec-cant-decode-byte-0xa5-in-position-0-invalid-start-byte/
#with open(path, 'rb') as f:
#  text = f.read().decode(errors='replace')


def succ_gen(text_in):
	b = text_in.split(' ')
	dic_out = {}
	for zz in set(b):
		dic_out[zz] = []
	for w in range(len(b) - 1):
		dic_out[b[w]].append(b[w + 1])
	return dic_out


c = succ_gen(input_text)


def generate(dictio, length):
	import random
	seed = random.choice(list(dictio.keys()))
	print(seed, end=' ')
	for d in range(length):
		if seed in dictio:
			seed = random.choice(dictio[seed])
		else:
			seed = random.choice(list(dictio.keys()))
		print(seed, end=' ')


# word_count = input('Enter Word Count >>> ')

generate(c, word_count)
