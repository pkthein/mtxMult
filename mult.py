# mtxMult
# Author : Phyo Htut

i0 = [int(i) for i in input().split()]
m = i0[0]
n = i0[1]
r = i0[2]

ret = []

matA = []
vecR = []

for row in range(m):
  arr = [int(i) for i in input().split()]
  matA.append(arr)

for col in range(n):
  arr = [int(i) for i in input().split()]
  vecR.append(arr)

for dim in range(r):
  for row in range(m):
    arr = [i for i in matA[row]]
    for col in range(n):
      arr[col] = vecR[col][dim] * matA[row][col]
    ret.append(arr)

for r in range(len(ret)):
  ret[r] = sum(ret[r])

for row in range(m):
  print(str(ret[row]) + ' ' + str(ret[row + m])) 

