# 1. k-mer counting

Remember Exercise 2 (Analyse a repeat structure) from yesterday's assignment?

We are going to make a repeating DNA sequence and extract some subsequences
from it.
- Make a short tandem repeat that consists of three "ACGT" units and five
  "TTATT" units.
- Print all suffixes of the repeat structure.
  - **Note**: A suffix is an ending. For example, the word "spam" has five
  suffixes: "spam", "pam", "am", "m" and "".
- Print all substrings of length 3.
- Print all unique substrings of length 3.

**Hint**: All elements in a set are unique.

## (1/2)

Perform the following:
- Make a function from your implementation.
- Have *k* as an argument to the function.
- Test the function on several input strings.

## (2/2)

Modify your function to use a dictionary with substring counts.
- Use the substrings as dictionary keys.
- Use the counts as dictionary values.
- Have the function return the dictionary.
- Add a docstring to the function.
- Use the function to print k-mer counts for some strings.
