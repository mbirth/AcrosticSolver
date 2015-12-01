#!/usr/bin/env python3
# (c)2015 Markus Birth <markus@birth-online.de>
# -*- coding: utf-8 -*-

import math

WORDLIST="web2.txt"

#SQUARE="NRONACNELEGOOESLEIEECIDEAIRBBTBODETS"
#SQUARE="DUAEAYURIZESAEIRLPESPESRSSESSAPPSEED"
#SQUARE="ERRSERYTORLTERYRERSLEEOSE"
#SQUARE="NNREDCTEMAROACRAMEEIAIMTONCTETERESEC"
#SQUARE="NEREILGEDENALRLELRIGNAATREONALETUGTE"
#SQUARE="FNADIHALNARTANUUGIANFALNSCGNTATRICTS"
SQUARE="RRCOLALAALETSTEIIRSATSTRRECCAEOSEHRE"
word_len = math.sqrt(len(SQUARE))

print("Word length: %i" % word_len)


def count_letters(pool):
    letters = {}

    for i in range(len(pool)):
        letter = pool[i]
        if not letter in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1

    return letters

letters = count_letters(SQUARE)
print(repr(letters))

for l in letters:
    if letters[l]%2 == 1:
        print("Diag candidate: %s" % l)

candidates = []

f = open("web2.txt", "r")
for line in f:
    line = line.strip().upper()
    # check word length
    if len(line) != word_len:
        continue
    # check word letters
    cand_letters = count_letters(line)
    for l in cand_letters:
        if not l in letters:
            break
        # If a letter occurs twice in a word, we need at least 3 to build it across and down. (1=>1, 2=>3, 3=>5, etc.)
        if cand_letters[l]*2-1 > letters[l]:
            break
    else:
        candidates.append(line)

f.close()

#for c in candidates:
#    print(c)

print("%i candidates." % len(candidates))
#print(candidates)

def check_valid(word, letters):
    for i in range(len(word)):
        l = word[i]
        if not l in letters:
            return False
        if letters[l]>1:
            letters[l] -= 1
        else:
            del letters[l]
        if i == 0:
            continue
        if not l in letters:
            return False
        if letters[l]>1:
            letters[l] -= 1
        else:
            del letters[l]
    return letters

def try_solve(letters, words = [], max_level = 99):
    level = len(words)
    if level == max_level:
        return ["---ABORTED---"]
    start_letters = ""
    for i in range(len(words)):
        start_letters += words[i][level]
#    if level == max_level -1:
#        print("Prefix: %s, letters: %s" % (start_letters, repr(letters)))
    next_matches = []
    for w in candidates:
        if w[:level] != start_letters:
            continue
        rem_letters = check_valid(w[level:], letters.copy())
        if type(rem_letters) is dict:
#            next_matches.append(w)
            if len(rem_letters)>0:
                more = try_solve(rem_letters.copy(), words + [w], max_level)
                if more:
                    next_matches.append((w, more))
            else:
                next_matches.append(w)
    return next_matches

#rem_first = check_valid("BEACON", letters.copy())
#rem_second = check_valid("NROBE", rem_first.copy())
#print(rem_second)
#result = try_solve(rem_second.copy(), ["BEACON", "ENROBE"])

result = try_solve(letters.copy(), max_level=5)
print(result)