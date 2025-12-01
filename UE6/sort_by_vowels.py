def sort_by_vowels(words):
    vowels = "aeiouAEIOU"
    return sorted(words, key=lambda w: sum(c in vowels for c in w))

words = ["apple", "sky", "orange", "myth", "echo"]
print(sort_by_vowels(words))