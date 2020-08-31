text = input("Введите текст: ")
i = 1
textlist = []
for e in range(text.count(" ") + 1):
    textlist = text.split()
    if len(textlist[e]) <= 10:
        print(f"{i} {textlist[e]}")
        i += 1
    else:
        print(f"{i} {textlist[e] [0:10]}")
        i += 1