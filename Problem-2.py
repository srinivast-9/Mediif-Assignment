def is_palindrome(word):
    result = 'PALINDROME' if word.lower() == word[::-1].lower() else 'NOT PALINDROME'
    print(result)
    return result

is_palindrome('Madam')