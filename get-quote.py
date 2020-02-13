import random


def primary():
    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    last = 16

    rnd = random.randint(0, last)
    print(quotes[rnd].replace('\n', ""))

    rnd = random.randint(0, last)
    print(quotes[rnd].replace("\n", ""))


def add_quote(quote):
    f = open("quotes.txt", "a")
    f.write(quote)
    f.close()


if __name__ == "__main__":
    primary()
    add_quote("My new line is added")
