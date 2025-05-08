# CTF Flag Solver

def solve_ctf_flag():
    shifts = [-1, 8, -3, -6, 1, 9, 39, -8, -30, 27, -49, 32, 20, 2, -19, 17, 1, -2, -62, 47, -4, 21, -67, -1, 62, 15]
    ascii_values = [ord('L')]  # Starting with 'L'

    # Calculating the next characters based on the shifts
    for shift in shifts:
        next_char = ascii_values[-1] + shift
        ascii_values.append(next_char)

    # Converting ASCII values back to characters
    flag = ''.join(chr(value) for value in ascii_values)
    return flag

if __name__ == "__main__":
    flag = solve_ctf_flag()
    print(f"[+] The flag is: {flag}")
