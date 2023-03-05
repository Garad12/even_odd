list1=(1,2,3,4,5,6,7,8,9)
number_odd = 0
number_even = 0
for number in list1:
    if(number%2==0):
        number_even = number_even+1
    else:
        number_odd =number_odd+1
print('Number of odd numbers=',number_odd)
print('Number of even numbers=',number_even)