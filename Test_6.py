#Problem 2

### The order of these steps is as follows:

###  A -> C -> B -> D

###  Open -> Read file -> Write file -> Close file

#Problem 3

### Questions 4 and 6 are not correct.

### In Python, "t" and "tb" modes do not exist.


#Problem 1

### Functions of input :     input(), read() , readline(), readlines()

### Functions of output :    print(), write(), writeline()


#Problem 4

inFp = open("data1.txt","r")

inStr = inFp.readline(3)
print(inStr, end = "")

inFp.close()

# Q6
inFp = open("data1.txt","r")
outFp = open("data3.txt", "w")

inList = inFp.read()
for inStr in inList:
    outFp.write(inStr)

inFp.close()
outFp.close()