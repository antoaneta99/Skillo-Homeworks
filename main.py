#PROBLEM 2
# Write a Python script that creates 5 string variables of 5 bulgarian
# PINs ( ЕГН ) and 5 names in tuples.
# Finally insert only the pairs whose name begins with a vowel
# in a dictionary and print it.

egn_1 = "9907234323"
egn_2 = "9907233323"
egn_3 = "9907232323"
egn_4 = "9907231323"
egn_5 = "9907230323"

name_1 = ("Radoslav", "Bachurov")
name_2 = ("Ivan", "Ivanov")
name_3 = ("Daniel", "Petkov")
name_4 = ("Mariya", "Petkova")
name_5 = ("Gabriela", "Staneva")

dict_vowels = {
    egn_3: name_3
}

#PROBLEM 3
# fill the following truth table.

# |  x   |  y  | x and y | x or y | not x | not y |
# |------|-----|---------|--------|-------|-------|
# |TRUE  |TRUE |  TRUE   |  TRUE  | FALSE | FALSE |
# |TRUE  |FALSE|  FALSE  |  TRUE  | FALSE | TRUE  |
# |FALSE |TRUE |  FALSE  |  TRUE  | TRUE  | FALSE |
# |FALSE |FALSE|  FALSE  |  FALSE | TRUE  | TRUE  |