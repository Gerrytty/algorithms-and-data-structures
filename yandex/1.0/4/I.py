num_words_in_vocab = int(input())

d = {}

for i in range(num_words_in_vocab):
	word = input()
	lower_word = word.lower()

	if lower_word not in d:
		d[lower_word] = [word]
	else:
		d[lower_word].append(word)

input_text = input().split()

count_mistakes = 0
for word in input_text:
	lower_word = word.lower()

	if lower_word not in d:
		count_not_low = 0
		for letter in word:
			if not letter.islower():
				count_not_low += 1

		if count_not_low != 1:
			count_mistakes += 1
	else:
		ok = False
		for correct_word in d[lower_word]:
			if correct_word == word:
				ok = True
				break
		if not ok:
			count_mistakes += 1

print(count_mistakes)