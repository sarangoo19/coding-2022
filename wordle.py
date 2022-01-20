from random import choice

USER_PROMPT = 'Guess the word:'

def score_letter(letter,position,true_word):
	#for example, score_letter('A',1,'ABBA') should be correct position
    # >>> score_letter('A', 0, 'ABBA')
    # '*'
    # >>> score_letter('B', 0, 'ABBA')
    # 'o'
    # >>> score_letter('C', 0, 'ABBA')
    # '-'
	if(true_word[position]==letter):
		return '*' #for correct position
	if(letter in true_word):
		return 'o' #for correct letter, incorrect position
	else:
		return '-'

def score_word(guess,true_word):
	#>>>score_word('APPL', 'ABBA')
	# '*---'
	if len(guess) != len(true_word):
		return 'TWO WORDS ARE NOT OF SAME LENTGH.'
	score = ''
	N = len(true_word)
	for position in range(N):
		score=score+score_letter(guess[position],position,true_word)
	return score

def get_and_score_guess(true_word):
	guess = input(USER_PROMPT)
	score = score_word(guess, true_word)
	print(len(USER_PROMPT) * ' ' + score)
	return score
		
def loop_until_success(true_word):
	correct_guess = False
	while not correct_guess:
		score = get_and_score_guess(true_word)
		if score == 6 * '*':
			correct_guess = True

def get_random_word(filename):
	word_file = open(filename, 'r')
	words = word_file.readlines()
	return choice(words)

word = get_random_word('data/words.txt')[0:6]
loop_until_success(word)


