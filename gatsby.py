#
# Determine and display the proportion of words that inclde
# each letter of the alpahabet. The letter that is used in the
# smallest proportion of words is highlighted at the end of
# program's output.

WORD_FILE = "novel.txt"

# Create a dictionary that counts the number of words containing
# each letter. Initialize the count for each letter to 0.

counts = {}
for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    counts[ch] = 0
# Open the file, process each word, and update the counts dictionary
num_words = 0
inf = open(WORD_FILE, "r")
for word in inf:
    # Convert the word to uppercase and remove the newline character
    word = word.upper().rstrip()

    # Before we can update the dictionary we need to generate a list of the unique letters in the
    # word. Otherwise we will increase the count multiple times for words that contain repeated
    # letters. We also need to ignore any non-letter characters that might be present.
    unique = []
    for ch in word:
        if ch not in unique and ch >= "A" and ch <= "Z":
            unique.append(ch)
    # Now increment the counts for all of the letters that are in the list of unique characters
    for ch in unique:
        counts[ch] = counts[ch] + 1
    # Keep track of the number of words that we have processed
    num_words = num_words + 1
# Close the file
inf.close()
# Display the result for each letter. While displaying the results we will also determine which
# character had the smallest count so that we can display it again at the end of the program.
smallest_count = min(counts.values())
for ch in sorted(counts):
    if counts[ch] == smallest_count:
        smallest_letter = ch
    percentage = counts[ch] / num_words * 100
    print(ch, "occurs in %.2f percent of words" % percentage)

# Display the letter that is easiest to avoid based on the number of words in which it appears
print()
print("The letter that is easiest to avoid is", smallest_letter)