def score_letter(letter,position,true_word):
	#for example, score_letter('A',1,'ABBA') should be correct position
     if(true_word[position]==letter):
             return '*' #for correct position
     if(letter in true_word):
             return 'o' #for correct letter, incorrect position
     else:
             return '-'
def score_word(guess,true_word):
	#>>>score_word('APPL', 'ABBA')
	# '*---'
	N = len(true_word)
	for position in range(N):
		score_letter(guess[position], position, true_word)

score_word('APPL', 'ABBA')
