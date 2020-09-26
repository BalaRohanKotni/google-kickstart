T=int(input())
for t in range(1, T+1):
  N=int(input())
  H=list(map(int, input().split()))
  ans=0
  for i in range(1, N-1):
    if H[i-1] < H[i] and H[i] > H[i+1]:
      ans+=1
  print("Case #"+str(t)+": "+str(ans))
