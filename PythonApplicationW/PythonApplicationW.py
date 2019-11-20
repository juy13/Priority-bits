import io
import binascii

def bin_format(integer, length):
    return f'{integer:0>{length}b}'

def bit_ord(str_came):
	i = 0
	str_out = ''
	while (i < len(str_came)):
		str_in = str_came[i] + str_came[i + 1]
		bin_out = bin_format(int(str_in, 16), len(str_in))
		one_amount = 0
		for j in bin_out:
			if j is '1':
				one_amount += 1
		if (one_amount % 2) == 0:
			if bin_out[len(bin_out) - 1] == '0':
				bin_out = bin_out[:len(bin_out) - 1]
				bin_out += '1'
			if bin_out[len(bin_out) - 1] == '1':
				bin_out = bin_out[:len(bin_out) - 1]
				bin_out += '0'
		a = hex(int(bin_out, 2))
		str_out += a[2:]
		i += 2
	return str_out




str = "a3c7"
bit_ord(str)
print(bin_format(int(str, 16), len(str)))
