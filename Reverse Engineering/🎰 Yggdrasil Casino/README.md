# Yggdrasil Casino [500 pts]

**Category:** Reverse Engineering

**Solves:** 1

## Description
Welcome to Casino Royale!
No matter whats your guess, I hope you dont bet much because this binary is cheating on you!
Find a way to redirect the program to `win_game` function! That function will immediately print you a flag!
Flag is in format: `LKSPJKT{.*}`
Notes: If you find strings `LKSPJKT{this.... blbalbalbla` , thats NOT the flag :3, flag can only be retrieved if you successfully redirect the program to win the game by calling `win_game` function.

Author: `Felix`

**Hint**
* Solving this challenge using your decompiler is painful, its **easier** to use a dynamic analysis approach instead ~ but theres a `catch` ...

## Solution

### Flag

LKSPJKT{r34L_c4$1n0_g4mbler}
