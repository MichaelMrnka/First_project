TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

users_pass = {'Bob': '123', 'Ann': 'pass123', 'Mike': 'password123', 'Liz': 'pass123'}
number_of_texts = len(TEXTS)
line = "-" * 35
text_1 = TEXTS[0]
text_2 = TEXTS[1].strip(" , . : ! ? - _ ")
text_3 = TEXTS[2].strip(" , . : ! ? - _ ")
title_text = "LEN|  OCCURENCES  |NR."

for number_of_logins in range(number_of_texts):
    user = input("Username: ")
    password = input("Password: ")
    print(line)
    if users_pass.get(user) == password:
        print(f"Welcome to the app {user},")
        break
    else:
        print("Wrong username or password. Please try it again.")
else:
    print("You've tried it many times. Please try again later.")
    quit()
print(f"We have {number_of_texts} texts to be analyzed.")
print(line)

#choice should be a number btw. 1 and 3

for choice in range(number_of_texts):
    choice = input(f"Enter a number btw. {number_of_texts - number_of_texts + 1} and {number_of_texts} to select the number of text: ")
    if choice.isnumeric() and choice <= "3":
        break
    else:
        print("This is not a number btw. 1 and 3")
else:
    print("You've tried it many times. Please try again later.")

if choice == "1":
    # number of words
    print(f"There are {sum(1 if word_1.isalnum() or word_1.istitle() or word_1.islower() else 0 for word_1 in text_1.split())} words in the selected text.")

    # number of titlecase
    print(f"There are {sum(1 if title_1.istitle() else 0 for title_1 in text_1.split())} titlecase words.")

    # number of uppercase
    print(f"There are {sum(1 if upper_1.isupper() and upper_1.isalpha() else 0 for upper_1 in text_1.split())} uppercase words.")

    # number of lowercase
    print(f"There are {sum(1 if lower_1.islower() else 0 for lower_1 in text_1.split())} lowercase words.")

    # number of numeric strings
    print(f"There are {sum(1 if num_1.isnumeric() else 0 for num_1 in text_1.split())} numeric strings.")

    #sum of all numeric
    sum_total_1 = 0
    for sum_1 in text_1.split():
        if sum_1.isnumeric():
            sum_total_1 += int(sum_1)
    print(f"The sum of all numbers {sum_total_1}.")
    print(line)

    #graph
    print("LEN|    OCCURENCES    |NR.")
    print(line)

    len_1 = {}
    for numbers_1 in text_1.split():
        if not numbers_1.strip(".,!:?").isalnum():
            continue
        elif len(numbers_1.strip(".,!:?")) not in len_1:
            len_1[len(numbers_1)] = 1
        else:
            len_1[len(numbers_1.strip(".,!:?"))] += 1
    len_1 = sorted(len_1.items())
    for numbers_11 in len_1:
        lengt_graph = "*" * (numbers_11[1])
        print(f"{numbers_11[0]:>3}|{lengt_graph:<18}|{numbers_11[1]}")




if choice == "2":
    # number of words
    print(f"There are {sum(1 if word_2.isalnum() or word_2.istitle() or word_2.islower() else 0 for word_2 in text_2.split())} words in the selected text.")

    # number of titlecase
    print(f"There are {sum(1 if title_2.istitle() else 0 for title_2 in text_2.split())} titlecase words.")

    # number of uppercase
    print(f"There are {sum(1 if upper_2.isupper() and upper_2.isalpha() else 0 for upper_2 in text_2.split())} uppercase words.")

    # number of lowercase
    print(f"There are {sum(1 if lower_2.islower() else 0 for lower_2 in text_2.split())} lowercase words.")

    # number of numeric strings
    print(f"There are {sum(1 if num_2.isnumeric() else 0 for num_2 in text_2.split())} numeric strings.")

    # sum of all numeric
    sum_total_2 = 0
    for sum_2 in text_2.split():
        if sum_2.isnumeric():
            sum_total_2 += int(sum_2)
    print(f"The sum of all numbers {sum_total_2}.")
    print(line)

    #graph
    print("LEN|    OCCURENCES    |NR.")
    print(line)

    len_2 = {}
    for numbers_2 in text_2.split():
        if not numbers_2.strip(".,!:?").isalnum():
            continue
        elif len(numbers_2.strip(".,!:?")) not in len_2:
            len_2[len(numbers_2)] = 1
        else:
            len_2[len(numbers_2.strip(".,!:?"))] += 1
    len_2 = sorted(len_2.items())
    for numbers_22 in len_2:
        lengt_graph = "*" * (numbers_22[1])
        print(f"{numbers_22[0]:>3}|{lengt_graph:<18}|{numbers_22[1]}")


if choice == "3":
    # number of words
    print(f"There are {sum(1 if word_3.isalnum() or word_3.istitle() or word_3.islower() else 0 for word_3 in text_3.split())} words in the selected text.")

    # number of titlecase
    print(f"There are {sum(1 if title_3.istitle() else 0 for title_3 in text_3.split())} titlecase words.")

    # number of uppercase
    print(f"There are {sum(1 if upper_3.isupper() and upper_3.isalpha() else 0 for upper_3 in text_3.split())} uppercase words.")

    # number of lowercase
    print(f"There are {sum(1 if lower_3.islower() else 0 for lower_3 in text_3.split())} lowercase words.")

    # number of numeric strings
    print(f"There are {sum(1 if num_3.isnumeric() else 0 for num_3 in text_3.split())} numeric strings.")

    # sum of all numerict
    sum_total_3 = 0
    for sum_3 in text_3.split():
        if sum_3.isnumeric():
            sum_total_3 += int(sum_3)
    print(f"The sum of all numbers {sum_total_3}.")
    print(line)

    # graph
    print("LEN|    OCCURENCES    |NR.")
    print(line)

    len_3 = {}
    for numbers_3 in text_3.split():
        if not numbers_3.strip(".,!:?").isalnum():
            continue
        elif len(numbers_3.strip(".,!:?")) not in len_3:
            len_3[len(numbers_3)] = 1
        else:
            len_3[len(numbers_3.strip(".,!:?"))] += 1
    len_3 = sorted(len_3.items())
    for numbers_33 in len_3:
        lengt_graph = "*" * (numbers_33[1])
        print(f"{numbers_33[0]:>3}|{lengt_graph:<18}|{numbers_33[1]}")


