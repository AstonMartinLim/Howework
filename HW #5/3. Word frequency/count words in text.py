# Задача: Візьміть файл, в якому є багато англійських слів у рядках.
# Порахуйте частоту зустрічі кожного слова та видрукуйте відсортовано.

r = open('text.txt', 'r', encoding='utf-8')
t = r.read() 


def count_words(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
    
result = dict(count_words(t))

r.close()

sort_res = sorted(result.items(), key=lambda item: item[1], reverse=True)

for key, val in sort_res:
    print(f'The word: "{key}" occurs: {val} times in the text')
