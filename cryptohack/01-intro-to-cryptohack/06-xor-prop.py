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

key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key2 = "911404e13f94884eabbec925851240a52fa381ddb79700dd6d0d"
key3 = "504053b757eafd3d709d6339b140e03d98b9fe62b84add0332cc"
flag = ""
