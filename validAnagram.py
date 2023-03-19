'''
- first check if both words have same lenght. 
if not impossible for them to be anagrams
- use hash table for each character we increment 1. if already existing, we keep adding 1
-
'''
from collections import Counter

def anagrams(s1, s2):

    if len(s1) != len(s2):
        return "Not an Anagram"
    return Counter(s1) == Counter(s2)
    freq1 = {}
    freq2 = {}

    for ch in s1:
        freq1[ch] += 1
    else:
        freq1[ch] = 1
    
    for ch in s2:
        freq2[ch] += 1
    else:
        freq2[ch] = 1
    
    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False
    
    return True

word1 = input("write the first word: ")
word2 = input("Write the second word: ")

anagrams(word1, word2)