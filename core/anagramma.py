import argparse
import random

parser = argparse.ArgumentParser(description='Create anagrams for the given word.')
parser.add_argument('word',help="the word you want to anagram")
parser.add_argument('-c','--count',help="limits the number of anagrams",type=int,default=5)
args = parser.parse_args()

word = args.word
count = args.count
anagram_list=[]
i=0
while True:
    if i > 100:
        print 'Too many iterations, stopping.'
        break
    charlst = list(word)        # convert the string into a list of characters
    random.shuffle(charlst)     # shuffle the list of characters randomly
    anagram = ''.join(charlst)
    i+=1
    if len(anagram_list) >= count:
        print 'Done.'
        break
    if (anagram in anagram_list) or (word == anagram):
        continue
    print 'Adding {}.'.format(anagram)
    anagram_list.append(anagram)
print 'Anagrams found: {}.'.format(anagram_list)