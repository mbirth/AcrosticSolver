Acrostic Solver
===============

Get a dictionary file (text file with one word per line) from [here](http://www.puzzlers.org/dokuwiki/doku.php?id=solving:wordlists:about:start)
and change the `WORDLIST` variable accordingly.


`SQUARE` holds the square - without spaces or anything else. Just all letters one after another.


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
