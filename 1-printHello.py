import time
alphabet = " abcdefghijklmnopqrstuvwxyz"
word = ""
cont = True

def func(word, c):
    for b in "hello world":
        for a in alphabet:
            if a != b:
                print(word, end="")
                print(a)
                time.sleep(0.02)

            else:
                word += a
                if word == "hello world":
                    print(word)
                    c = False
                    return c
                break

while func(word, cont):
    func(word, cont)