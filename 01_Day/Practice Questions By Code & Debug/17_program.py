start = 1
end = 100
i = start
sum = 0
while i <= end:
    if i % 2 ==0 and i % 7 == 0:
        sum += i
    i += 1
print(f"Sum of numbers from {start} to {end} which are divisible by both 2 and 7 is: {sum}")