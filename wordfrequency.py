# Simple script to make a word frequency dictionary

text_file = 'test.txt' # test.txt must be in the same folder as the script
frequency_dictionary = dict()

with open(text_file) as f: 
	for line in f:
		line = line.rstrip()
		word_list = line.split()
		for word in word_list:
			word = word.lower()
			frequency_dictionary[word] = frequency_dictionary.get(word, 0) + 1

print(frequency_dictionary)

max_key = max(frequency_dictionary, key=frequency_dictionary.get)
print(f'The most frequent word is: {max_key} ({frequency_dictionary[max_key]})')

# TODO
# export frequency_dictionary to .csv file