import sys

# p=11    #prime 1
# q=3     #prime 2
# N=p*q   #prime product
# e=3     #prime which doesn't share a factor with PHI  
# M=4     #message 

p = int(input('Enter first prime: '))
q = int(input('Enter second prime: '))

print('N = ',str(p*q)) 
print('PHI = ',str((p-1)*(q-1)))

N = p*q

e = int(input('Enter prime which is a not a factor of PHI: '))

M = int(input('Enter message: '))

# if (len(sys.argv)>1):
#     p = int(sys.argv[1])
# if (len(sys.argv)>2):
#     q = int(sys.argv[2])
# if (len(sys.argv)>3):
#     e = int(sys.argv[3]) 
# if (len(sys.argv)>4):
#     M = int(sys.argv[4])

PHI=(p-1)*(q-1) 

for d in range(1,100): 
    if ((e*d % PHI)==1): 
        break 

print e,N 
print d,N 

cipher = M**e % N 
print cipher 

message = cipher**d % N 
print message