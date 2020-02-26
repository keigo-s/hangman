import random
word_list = ["apple", "banana", "lemonade"]
def hangman(word):
    wrong = 0
    stages = ["",
              "_______        ",
              "|              ",
              "|      |       ",
              "|      o       ",
              "|     /|\      ",
              "|     / \      ",
              "|              "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to hangman!")
#ここでlenに-1するのは、stagesの要素は0から数え始めるから
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね:"
        char = input(msg)
        if char == "exit":
            break
        if char in rletters:
            number = rletters.index(char)
            board[number] = char
            rletters[number] = "$"
        else:
            wrong += 1
        print(" ".join(board))
#ここでeに+1するのは、[0,e]がe-1までしか繰り返されないから
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("あなたの負け！正解は{}".format(word))

hangman(random.choice(word_list))
