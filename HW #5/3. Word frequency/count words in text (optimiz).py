# Задача: Візьміть файл, в якому є багато англійських слів у рядках.
# Порахуйте частоту зустрічі кожного слова та видрукуйте відсортовано.

r = open('text.txt', 'r', encoding='utf-8')

chars = '.,!-"—?():%1234567890'
del_chars = (r.read().translate(str.maketrans('', '', chars)))

conv_to_list = del_chars.split()


def count_words(text):
    counts = dict()
    for word in text:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
    
result = dict(count_words(conv_to_list))

r.close()

sort_result = sorted(result.items(), key=lambda item: item[1], reverse=True)

# Принт на 2-ві колонки
max_columns1 = [14]
max_columns2 = [2]

for key, val in sort_result:
    print(f'The word: {key:{max(max_columns1)+1}}occurs:{val:{max(max_columns2)+1}} times in the text')


