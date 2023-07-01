# Shubhangi Language
# vowels -> g
# ----------

# dog -> dgg
# cat ->  cgt

def Translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":  # letter.lower() in "aeiou"
            if letter.isupper():
                translation = translation+"G"
            else:
                translation = translation+"g"
        else:
             translation = translation+letter
    return translation

print(Translate(input("Enter a Phrase: ")))