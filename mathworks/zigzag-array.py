nums=[2,5,-1,10,4]
N=len(nums)
nums.sort()
res=[0]*N

index=0
for i in range(N):
    j=N-i-1
    if i!=j and index+1<N:
        res[index]=nums[j]
        res[index+1]=nums[i]
    index+=2

if index!=N-1:res[N-1]=nums[int(N/2)]
print(res)
    