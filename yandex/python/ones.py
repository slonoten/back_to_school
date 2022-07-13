n_digits = int(input())

max_length = 0
current_length = 0

for _ in range(n_digits):
	digit = input()
	if digit == '1':
		current_length += 1
	else:
		if current_length:
			if current_length > max_length:
				max_length = current_length
			current_length = 0

print (max(max_length, current_length))