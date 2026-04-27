num = int(input("Enter a number: "))

original = num
sum_fact = 0

while num > 0:
    digit = num % 10
    
    # find factorial of digit
    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i
    
    sum_fact += fact
    num = num // 10

if sum_fact == original:
    print("Strong Number")
else:
    print("Not a Strong Number")