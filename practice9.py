
word = 'Архангельск'
print(word[-1])

new_word = word.lower()
count = 0
for i in new_word:
    if i == 'а':
        count += 1
print(count)


word = "Архангельск"
vocab = ["а", "е", "и", "о", "у", "э", "ю", "я", "ы"]
count = 0
for i in word.lower():
    for j in vocab:
        if i == j:
            count += 1
print(count)


sentence = 'Мы приехали в гости'
print(len(sentence.split()))

for i in sentence.split():
    print(i[0])


new_sentence = sentence.replace(' ','')
print(int(len(new_sentence)/len(sentence.split())))
