import pandas

phonetic_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in phonetic_data_frame.iterrows()}

def generate_phonetic():
    word = input("What word do you want to convert?: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters A–Z are allowed. Try again.")
        return generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
