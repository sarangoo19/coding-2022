>>> def score_letter(letter,position,true_word):
...     if(true_word[position]==letter):
...             return '*'
...     if(letter in true_word):
...             return 'o'
...     else:
...             return '-'
