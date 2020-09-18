def int_func(clearword):
    return clearword.title()


word = input("Введите предложение: ")
wordlist = list(word)
n = 0
for i in range(len(wordlist)):
    if 97 <= ord(wordlist[n]) <= 122 or ord(wordlist[n]) == 32:
        n += 1
    else:
        wordlist.pop(n)
clearword = "".join(wordlist)

print(int_func(clearword))
