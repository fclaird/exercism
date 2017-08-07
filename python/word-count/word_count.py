def word_count(sentence):
	import string
	punctuation = str().join([char for char in sentence if char in string.punctuation])
	for char in punctuation: sentence = sentence.replace(char, ' ')
	words = sentence.casefold().split()
	word_map = {words.pop(0): 1}
	for word in words:
		if word in word_map.keys(): word_map[word] = word_map[word] + 1
		else: word_map[word] = 1
	return word_map
