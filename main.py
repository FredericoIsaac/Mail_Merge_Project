PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as f:
    invited_list = [line.strip() for line in f.readlines()]


with open("./Input/Letters/starting_letter.txt") as f:
    letter = f.read()


for name in invited_list:
    named_letter = letter.replace(PLACEHOLDER, name, 1)

    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as f:
        f.write(named_letter)
