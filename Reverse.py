def reverse_string_with_slicing(str):
    return str[::-1]


def reverse(str):
	index = len(str)
	backwards = []
	while index:
		index -= 1
		backwards.append(str[index])

	return ''.join(backwards)

print reverse("Ben")