def count_occurrences(word, text):
    count = 0
    words = text.split()
    for w in words:
        if w.strip(".,!?") == word:
            count += 1
    return count

def replace_word(word, replacement, text):
    words = text.split()
    replaced_words = []
    count = 0
    for w in words:
        if w.strip(".,!?") == word:
            count += 1
            replacement_word = replacement if count % 2 == 0 else word
            replaced_words.append(replacement_word)
        else:
            replaced_words.append(w)
    return ' '.join(replaced_words)

with open('file_to_read.txt', 'r') as file:
    text = file.read()

# Calculate the total number of occurrences of 'terrible' words
word_to_count = "terrible"
occurrences = count_occurrences(word_to_count, text)
print(f'“{word_to_count}”Total number of words：{occurrences}')

# Replace words
replacement_even = "pathetic"
replacement_odd = "marvellous"
replaced_text = replace_word(word_to_count, replacement_even, text)

# Write after modifying the file
with open('result.txt', 'w') as file:
    file.write(replaced_text)

print('Replacement completed. The modified text has been written to the ''result. txt'' file.')
