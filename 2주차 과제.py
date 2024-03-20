
# QUESTION_01
print("100")
print(100)
print(50+50)
print("50+50")
# Results:
# 100
# 100
# 100
# 50+50

# QUESTION_02
print('%d / %d = %d' % (5, 10, 5/10))
# Results: 5 / 10 = 0

# QUESTION_03
print("%04d"%876)
print("%5s"%"CookBook")
print("%1.1f"%123.45)
# Results: 
# 0876
# CookBook
# 123.5

# QUESTION_04
print("{2:d} {0:d} {1:d}".format(111, 222, 333))
# Results: 333 111 222

# QUESTION_11
# Python program to convert decimal into other number systems

dec = int(input("Enter a Decimal Number: "))

#decimal to binary

print(bin(dec), "in Binary.")

#decimal to octal

print(oct(dec), "in Octal.")

#decimal to Hexadecimal

print(hex(dec), "in Hexadecimal.")

# QUESTION_13
int('1002', 2)
# Explain: The error message invalid literal for int() with base 2: '1002' indicates that the string '1002' cannot be converted to an integer in base 2 (binary). This is because the string contains the digit 2, which is not a valid digit in binary.
To fix the code, you need to replace the string '1002' with a valid binary string. A valid binary string can only contain the digits 0 and 1.

int('1008', 8)
# Explain: The error is caused by the int() function being unable to convert the string '1008' to an integer in base 8. This is because the string contains the digit '8', which is not a valid digit in base 8.
To fix the code, replace '1008' with '1000' or any other valid octal string.

int('AAFG', 16)
# Explain: The error message is clear: ValueError: invalid literal for int() with base 16: 'AAFG'. This means that the string 'AAFG' cannot be converted to an integer in base 16 (hexadecimal).
The reason for this is that 'AAFG' contains characters that are not valid hexadecimal digits. The valid hexadecimal digits are 0-9, a-f, and A-F.
To fix the code, you can replace 'AAFG' with a valid hexadecimal string, such as 'AF'.

# QUESTION_14
# Answer: 2, 3, 4,
