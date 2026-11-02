""" nums=[10,3,4,5,6]

largest = float('-inf')
second = float('-inf')



for i in nums:

    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i



print(second) """

# i=10 larg=-inf sec=-inf check i > larg  larg=i => sec=-inf larg=10
#        |--------|    

# i=3 larg=10 sec=-inf check i >larg fle => check i > sec larg=10 sec=i => larg=10 sec=3

# i=4 larg=10 sec=3 check i>larg fle => check i > sec larg=10 sec=i => larg=10 sec=4

# i=5 larg=10 sec=4 check i>larg fle => check i > sec larg=10 sec=i => larg=10 sec=5

# i=6 larg=10 sec=5 check i>larg fle => check i >sec larg =10 sec=i => larg=10 sec=6


# o/p 6


n = 123456
product = 0

while n > 0:
    dig = n % 10   #  123456 => 6  5
    product = product * 10 + dig # =>65
    n = n // 10 # 12345

print(product)


""" 
         1 2 3 4 5 6       6 5 4 3 2 1
         1 0 0 0 0 0       6 0 0 0 0 0
           2 0 0 0 0         5 0 0 0 0
             3 0 0 0           4 0 0 0
               4 0 0             3 0 0
                 5 0               2 0
                   6                 1






 """