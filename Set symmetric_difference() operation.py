n1=int(input())
myset=set(input().split())

n2=int(input())
myset1=set(input().split())

myset3=myset1.symmetric_difference(myset)
print(len(myset3))