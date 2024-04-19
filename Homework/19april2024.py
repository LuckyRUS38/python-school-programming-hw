from itertools import product
from itertools import permutations


def task1():
    letters = ['П', 'С', 'К', 'А', 'Л', 'Ь']
    valid_words = 0
    for word in product(letters, repeat=4):
        word_str = ''.join(word)
        if word_str[0] != 'Ь' and 'ЬЬ' not in word_str:
            valid_words += 1
    return valid_words


def task2():
    letters = ['С', 'О', 'Л', 'Н', 'Ц', 'Е']
    valid_words = 0
    for word in product(letters, repeat=6):
        word_str = ''.join(word)
        if word_str.count('О') <= 2 and word_str.count('Ц') == 1:
            valid_words += 1
    return valid_words


def task3():
    count = 0
    for num in range(1000, 10000):
        if num % 8 == 0:
            count += 1
    return count


def task4():
    name = "МАРИНА"
    vowels = "АИ"
    valid_permutations = 0
    for perm in permutations(name):
        if perm[0] not in vowels:
            valid_permutations += 1
    return valid_permutations


def task5():
    word = "АББАТИСА"
    vowels = "АИЕОУЫЭЯЮ"
    consonants = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
    word_count = 0
    for perm in permutations(word):
        valid = True
        for i in range(len(perm) - 1):
            if (perm[i] in vowels and perm[i + 1] in vowels) or (perm[i] in consonants and perm[i + 1] in consonants):
                valid = False
                break
        if valid:
            word_count += 1
    return word_count


def task6():
    word = "АММИАКАТ"
    vowels = "АИЕОУЫЭЯЮ"
    consonants = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
    word_count = 0
    for perm in permutations(word):
        valid = True
        for i in range(len(perm) - 1):
            if not ((perm[i] in vowels and perm[i + 1] in consonants) or (
                    perm[i] in consonants and perm[i + 1] in vowels)):
                valid = False
                break
        if valid:
            word_count += 1
    return word_count


print(task1())
print(task2())
print(task3())
print(task4())
print(task5())
print(task6())
