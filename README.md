Magic Word Square (aka. CrossDoku) Solver
=========================================

Get a dictionary file (text file with one word per line) from [here](http://www.puzzlers.org/dokuwiki/doku.php?id=solving:wordlists:about:start)
and change the `WORDLIST` variable accordingly.


`SQUARE` holds the raw square - without spaces or anything else. Just all letters one after another.


At the bottom, the `letters` variable holds all available letters from the `SQUARE` and their amounts.

To start a search, run:

```
result = try_solve(letters.copy())
print(result)
```

If it doesn't find anything, try a different wordlist or specify a limit to which you want to search to:

```
result = try_solve(letters.copy(), max_level=4)
print(result)
```

If you already have the first and second words, use this:

```
rem_first = check_valid("BEACON", letters.copy())    # get remaining letters after first word
rem_second = check_valid("NROBE", rem_first.copy())  # get remaining letters after second word (NOTE: Since the letter "E" is used up already, we specify NROBE.)
result = try_solve(rem_second.copy(), ["BEACON", "ENROBE"])   # solve remaining
print(result)
```


Example
-------

For a given magic word square puzzle, i.e. letters and number of letters are given, e.g.:

```
AAACCC
CEEEEE
EEEIIL
LMRRRR
RRSSSS
TTTTUU
```

You should write it into the `SQUARE` variable like this:

```
SQUARE="AAACCCCEEEEEEEEIILLMRRRRRRSSSSTTTTUU"
```

If you run the script, the output should look like this after a few seconds:

```
Word length: 6
{'C': 4, 'L': 2, 'R': 6, 'S': 4, 'I': 2, 'A': 3, 'E': 8, 'U': 2, 'M': 1, 'T': 4}
Diag candidate: A
Diag candidate: M
1248 candidates.
.------.
|CIRCLE|
|ICARUS|
|RAREST|
|CREATE|
|LUSTRE|
|ESTEEM|
'------'
```

First, it determines the length per word from the `SQUARE` string.

Then it lists all letters and their amount.

"Diag candidate" means, that letter has an odd amount and is on the diagonal.

"1248 candidates." means it found 1248 words in the dictionary which could fit into our square.

After a few seconds, if a solution was found, it is displayed as the solved square.
