x = input()
word = list(x)

con =  'bcdfghjklmnpqrstvwxyz'
new_word = ''

for i in range(len(x)):
  if word[i] in 'aeiou':
    new_word = new_word + word[i]
    
  elif word[i] == 'z':
        new_word = new_word + 'zuz'

  elif word[i] in con:
    index = con.find(word[i])
    first_letter = word[i]
    third_letter = con[index+1]
    
    if word[i] in 'bc':
      second_letter = 'a'
    if word[i] in 'dfg':
      second_letter = 'e'
    if word[i] in 'hjkl':
      second_letter = 'i'
    if word[i] in 'mnpqr':
      second_letter = 'o'
    if word[i] in 'stvwxyz':
      second_letter = 'u'
    
    new_word = new_word + first_letter + second_letter + third_letter
print(new_word)
