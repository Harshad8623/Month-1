count = 0
word = input("Enter a Word : ").lower()
for i in word:
    if i in "aeiou":
        count += 1
print(f"Vowels in the {word} are : {count}")