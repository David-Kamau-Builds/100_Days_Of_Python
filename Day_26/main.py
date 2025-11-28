import pandas
phonetic_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:row.code for (index, row) in phonetic_data_frame.iterrows()}

word = input("What word do you want to convert?: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)