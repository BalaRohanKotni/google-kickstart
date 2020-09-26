t = int(input())
tc = 0

while t>0:
  n,b = map(int, input().split())
  a = list(map(int, input().split()))
  count = 0
  a.sort()

  for i in a:
    if i<=b:
      b -= i
      count += 1

  tc += 1

  print("Case #" + str(tc) + ": " + str(count))

  t -=1
