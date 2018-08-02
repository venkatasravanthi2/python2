n,k=input().split()
n,k=int(n),int(k)
sum=0
arr=[int(x) for x in input().split()]
for i in range(0,k):
    sum=sum+arr[i]
print(sum)
