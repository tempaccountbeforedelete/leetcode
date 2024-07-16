def last_word_len(s):
    return len(s.strip().split(" ")[-1])


if __name__ == "__main__":
    numbers: list = [
        "Hello World",
        "   fly me   to   the moon  ",
        "luffy is still joyboy",
    ]

    for s in numbers:
        print(last_word_len(s))
