def logic_gates(v,k):
	return ((v & ~k) | (~v & k))

flag = [30, 72, 213, 172, 104, 25, 21, 116, 87, 23, 33, 196, 76, 31, 196, 4, 222, 40, 206, 201, 200, 29, 194, 211, 209, 151, 75, 78, 116, 76, 209, 237, 224, 2, 15, 92, 94, 18, 208]
xp = [82, 3, 134, 252, 34, 82, 65, 15, 53, 118, 67, 189, 19, 71, 244, 86, 129, 76, 170, 188, 229, 121, 166, 166, 252, 243, 62, 99, 16, 57, 252, 137, 132, 119, 34, 56, 43, 108, 173]

check_input = input("Input the flag >> ")
for ch in range(len(check_input)):
	if logic_gates(ord(check_input[ch]),flag[ch]) != xp[ch]:
		print("Incorrect.")
		exit(-1)

print("Nice you got the flag!")