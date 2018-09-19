# Example: Given a smaller string s and a bigger string b, design an algorithm to find all permutations
# of the shorter string within the longer one. Print the location of each permutation. 

def inner_permutations(s, b):
    s = sorted(s)
    lenS, lenB = len(s), len(b)
    for i in range(lenB-lenS+1):
        if b[i] in s:
            if s == sorted(b[i:i+lenS]):
                print(i, b[i:i+lenS])

s = 'abbc'
b = 'cbabadcbbabbcbabaabccbabc'

inner_permutations(s, b)
