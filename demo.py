#given an array of numbers find any two numbers , whose sum equal to given number
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
    