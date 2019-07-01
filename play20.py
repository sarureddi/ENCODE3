name=input()
n=" "
n1="0abcdefghijklmnopqrstuvwxyzabcABCDEFGHIJKLMNOPQRSTUVWXYZABC"
n1.upper()
for i in name:
  if i in n1:
    t=n1.index(i)
    t=t+3
    n=n+n1[t]
print(n)
