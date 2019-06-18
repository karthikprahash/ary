N,k=map(int,input().split())

E=list(map(int,input().split()))[:N]

sum=0

for x in range(k):

    sum=sum+E[x]

print(sum)
