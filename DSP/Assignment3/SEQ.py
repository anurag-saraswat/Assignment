# https://www.spoj.com/problems/SEQ/

'''
Approach used : 
Recursively find out the value of smaller terms and store it in the dictionary for later terms.
STEPS :
1. Check if "i <= k" then output the "b[i]" value
2. else check if "i" is present in dictionary keys then return its value
3. else recursively find out a[i] and store it as {"i" : value of "a[i]"} in the dictionary for later use
Sample Input :
3 
5 8 2 
32 54 6 
2 
3 
1 2 3 
4 5 6 
6

Sample Output :
8 
7

'''


import sys
sys.setrecursionlimit(10**9)

# Dictionary to store previously calculated values
Dict = {}

# Function to calculate the a(n) recursively
def seq(n, k, b, c):			
  if(n <= k):
    return b[n-1];
  else:
    res = 0
    for i in range(k):
      if(n-(i+1) in Dict.keys()):
        res = res + c[i]*Dict[n-(i+1)]
      else:
        res = res + c[i]*seq(n-(i+1), k, b, c)
    Dict[n] = res  
    return res % (10**9)  

T = int(input()) #no. of test cases
for i in range(T):
  # taking input
  k = int(input());
  b = [int(x) for x in input().split()]
  c = [int(x) for x in input().split()]
  n = int(input())

  # printing the result	
  print(seq(n, k, b ,c), end= "")

  
