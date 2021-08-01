# Word count

# Goal : Ask the user what is on their mind, after the user responds
# count the number of words in the sentence and print that as an output.


print('Welcome to the word count program')

# Counting the words from a user input
# user_input = input('What is on your mind today: ')
#
# word_list = user_input.split()
# print(len(word_list))
# word_count = len(word_list)
#
# print(f"Oh nice, you just told me what's on your mind in {word_count} words!")


# Counting words in a file
filename = input("Please enter the filename: ")

try:
    with open(f"{filename}.txt", "r") as file:
        word_count = 0
        document_lines = file.read().splitlines()
        for line in document_lines:
            word_list = line.split()
            word_count += len(word_list)

    print(f"The total number of words in this file is equal to : {word_count}")

except FileNotFoundError:
    print(f"The file with the name {filename}.txt was not found. Sorry ! ")



