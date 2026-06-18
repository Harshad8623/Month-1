def is_palindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    return "Not Palindrome"
s = input("Enter String : ").lower()
print(is_palindrome(s))
