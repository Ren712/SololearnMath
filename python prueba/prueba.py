
'''
Find which math expression matches the answer that you are given, if you have an integer answer, and a list of math expressions.
Task: 
Test each math expression to find the first one that matches the answer that you are given.

Input Format: 
Two inputs: an integer and a space separated string of math expressions. The following operations need to be supported: addition +, subtraction -, multiplication *, division /. 
An expression can include multiple operations.

Output Format: 
A string that tells the index of the first math expression that matches. If there are no matches, output 'none'.

Sample Input: 
15
(2+100) (5*3) (14+1)

Sample Output: 
index 1
'''
def scaneq(eq):
  num = [0,0,0,0]
  char = ['','','']
  cantn = 0
  cantc = -1
  mult = 1
  for y in eq:
    if y=='(':
      continue
    elif y==')':
      return num,cantc,char
    elif (y=='*') or (y=='+') or (y=='/') or (y=='-'):
      cantc += 1
      cantn += 1
      char[cantc] = y
      mult = 1
    elif (y>='0') and (y <='9'):
      if mult != 1:
        num[cantn] *= 10
      mult = 0 
      num[cantn] += int(y)
      
def calc(num,cantc,char,res):
  for i in range(cantc+1):
    if char[i] == '*':
      num[0]=num[i+1]*num[0] 
    elif char[i] == '/':
      num[0]=num[i+1]/num[0] 
    elif char[i] == '+':
      num[0]=num[i+1]+num[0]
    elif char[i] == '-':
      num[0]=num[i+1]-num[0]
  if int(num[0]) == int(res):
    return 1
  else: 
    return 0 


result = input()
int(result)
raweqs = input()
sepeqs = raweqs.split(" ")

#print(result)
ind = 0
for x in sepeqs:
  fnum,fcantc,fchar = scaneq(x)
  if calc(fnum,fcantc,fchar,result)==1:
    print("index", end=' ')
    print(ind)
    exit()
  ind += 1
print("none")

