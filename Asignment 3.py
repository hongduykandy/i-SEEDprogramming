
################################## QUESTION_04
score = int(input("enter your score : "))
 
if score >=90:
    print("scholarship student", end='')
elif score >=60:
    print("pass", end='')
else:
    print("Failed", end='')


################################### QUESTION_05
num = 5
if num%2==0:
    res = 'even number'
else:
    res = 'old number'
    
res1 = 'even number'if num%2==0 else 'old number'

print(res1)

################################# QUESTION_06
nn = [100, 200, 300, 400, 500]
nn[1]=777
print(nn)

# QUESTION_055

nn = [100, 200, 300, 400, 500]

nn[4]
nn[-1]
nn[-2]
nn[1:4]
nn[0:1]
nn[2:-1]
nn[0::2]
nn[::-1]
nn[::-2]


# QUESTION_08    
hap = 0

n=1234
while n in range(1234, 4568):
    if n%444 ==0:
       hap +=n
    n +=1
    
print(hap)


# QUESTION_09

A = 0
for i in range(3333, 9999):
    
    if i%1234 == 0:
       A +=i
    if A<100000:
        continue
    else:
        break
print(A)

#######  QUESTION_14

myData = [[n*m for n in range(1,3)] for m in range(2,4)]
print(myData)





     
     