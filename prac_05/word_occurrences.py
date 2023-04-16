words_counted = {}
user_input = input("Text: ")

words_list = user_input.split()

for word in words_list:
    if word in words_counted:
        words_counted[word] += 1
    else:
        words_counted[word] = 1

words = list(words_counted.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    count = words_counted[word]
    print(f"{word:{max_length}} : {count}")



