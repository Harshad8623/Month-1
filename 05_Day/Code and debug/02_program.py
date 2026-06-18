def fun():
    n = int(input("Enter a Number : "))
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            print(i, end=' ')
            if i != n//i:
                print(n//i, end=' ')
fun()