ciphertext = str(input(' Cipher text: '))
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def LetterFrequency():
    LetterFrequency = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 
                       'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0 }
    for letter in ciphertext.upper():
        if letter in letters:
            LetterFrequency[letter]+=1
    return LetterFrequency

print('Analysis:', LetterFrequency())

r1 = str(input('please enter replace rule: '))
r2 = str(input('replace with: '))

for text in ciphertext:
    if text in letters:
        newstring = ciphertext.replace(r1, r2)
print('Plaintext: ', newstring)

