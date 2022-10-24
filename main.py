import requests


def start():
    guessed = "арбуз".lower()
    rnd = 0
    all_words = []
    no_format_words = []
    print("Введите свое первое слово:")
    while rnd != 5:
        for _ in all_words:
            print(f"- {_}")
        user_word = get_word(no_format_words)
        for _ in range(5 - len(all_words)-1):
            print(f"- _____")
        if user_word:
            no_format_words.append(user_word)
            anl_word = analyze_word(user_word, guessed)
            if user_word == guessed:
                print(f"\033[1m\033[32mВы победили, это было слово {user_word.capitalize()}\033[0m")
                break
            else:
                all_words.append(anl_word)
            rnd += 1
        print("="*20)
        print("Напишите следующее слово:")
    if rnd == 5:
        print("Попытки закончились, вы проиграли.")


def get_word(last_words):
    word = input("- ").strip().lower()
    if word in last_words:
        print_red("Это слово уже было!")
        return False
    if len(word) != 5:
        print_red("Неверная длинна.")
        return False
    elif any(not x.isalpha() for x in word):
        print_red("Не все символы слова - буквы.")
        return False
    elif not check_dict(word):
        print_red("Слова нет в базе.")
        return False
    return word


def print_red(text):
    print(f"\033[1m\033[31mError: {text}\033[0m")


def analyze_word(word: str, guess_word: str):
    liters = list(word)
    guessed_litters = list(guess_word)
    for i in range(len(liters)):
        lit = liters[i]
        if lit == guessed_litters[i]:
            liters[i] = f"\033[33m{lit}\033[0m"
        elif lit in guessed_litters:
            liters[i] = f"\033[34m{lit}\033[0m"
        else:
            liters[i] = f"\033[37m{lit}\033[0m"
    return "".join(liters)


def check_dict(word: str):
    if "По вашему запросу ничего не найдено" in requests.get(f"https://vfrsute.ru/{word}/").text:
        return False
    return True


if __name__ == '__main__':
    start()
