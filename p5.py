n=int(input('enter a number'))
i=1
fact=1
sum=0
while i<=n:
	fact=fact*i
	sum=sum+(i/fact)
	i=i+1
print(sum)
 