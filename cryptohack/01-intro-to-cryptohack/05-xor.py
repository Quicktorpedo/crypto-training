import math

def toAscii(string):
	ascii_values, binary_values = [], []

	for letter in string:
		ascii_values.append(ord(letter))

	return ascii_values

def Xor(ascii_value, xor_by):
	return ascii_value ^ xor_by

def dec(string, xor_by):
	ascii_values, xored_results = [], []
	ascii_values = toAscii(string)

	for value in ascii_values:
		xored_results.append(Xor(value, xor_by))

	return xored_results

def asciiToString(binary_array):
	result = ""

	for value in binary_array:
		result = result + chr(value)

	return result

msg = "label"

decMsg=dec(msg, 13)

print(decMsg)

encMsg=asciiToString(decMsg)

print(encMsg)

