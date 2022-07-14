#given an array of numbers find any two numbers , whose sum equal to given number
# AVINASH

def pairs(a, s, n):
    for i in range (0,s-1):
        for j in range(i+1, s):
            if(a[i]+a[j]==n):
                print(f" pair is : ({a[i],a[j]}) ")

                return 1
    return 0
if __name__ == "__main__":
    a=[1,2,3,4,5]
    n=7
    s=len(a)
    
#ravitejacode
a=[1,2,3,4,5]
n=7
tlist =[]
for i in range(len(a)):
    for j in range(len(a)-1):
        if (i!=j) and ((a[i]+a[j+1]) == n):
            if(i,j+1) not in tlist and (j+1,i) not in tlist:
                tlist.append((i,j+1))
                print("index ->" ,",i," "",j+1)
                print("sum=", i+j+1)
