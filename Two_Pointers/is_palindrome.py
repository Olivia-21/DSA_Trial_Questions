# Is palindrome using Two pointers
# Efficient Approach
def is_pal(s):
    left, right = 0, len(s)- 1
    if s[left] != s[right]:
        return f"{s} is not a palindrome"
    left += 1
    right -= 1
    return f"{s} is a palindrome"

print(is_pal("car"))
print()

# OR

# Not so efficient, always handle the false first 
def is_palindrome(word):
    lef, rig = 0, len(word) - 1
    if word[lef] == word[rig]:
        lef += 1
        rig -= 1
    else:
        return f"{word} is not a palindrome"
    return f"{word} is a palindrome"

print(is_palindrome("madam"))