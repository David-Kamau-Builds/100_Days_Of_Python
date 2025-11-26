PLACEHOLDER = "[name]"
INVITED_NAMES_FILE = "./Day_24/Input/Names/invited_names.txt"
STARTING_LETTER_FILE = "./Day_24/Input/Letters/starting_letter.txt"

with open(INVITED_NAMES_FILE, mode="r") as names_file:
   names = names_file.readlines()

with open(STARTING_LETTER_FILE) as letter_file:
    letter_contents = letter_file.read()

    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        output_file_path = f"./Day_24/Output/ReadyToSend/letter_to_{stripped_name}.txt"
        
        with open(output_file_path, mode="w") as ready_letter:
            ready_letter.write(new_letter)