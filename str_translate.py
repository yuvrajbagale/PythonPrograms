translation_table = str.maketrans("aeiou","12345")
my_string = "this is a string!"
translated = my_string.translate(translation_table)
print(translated)
