# Impossible Challenge [500 pts]

**Category:** Cryptography

**Solves:** 0

## Description
I made a random quiz because I know youre such a random guy. But I bet no such things that can brute force a 30 - 50 bytes in a loop for a day in this competition! 

Flag is in format: `LKSPJKT{.*}`

Author: `Felix`

**Hint**
* How would you find a seed when you know the random value retrieved? This will blow your mind but the final state of randomness can be `reverse-engineered` :) .....
Yeah this is Cryptography + Reverse Engineering challenge which may require a lot of scripting.
Python RNG is based from `https://github.com/python/cpython/blob/main/Modules/_randommodule.c ` (yeah analyze that :u), and as you can see that the state can be tampered (?)
How would one could satisfy the state if there are enough *n* integers?

## Solution

### Flag

