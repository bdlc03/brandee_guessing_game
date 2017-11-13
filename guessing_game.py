import random
import time

play = True
guess1 = 0
guess2 = 0
guess1_2 = 0
guess2_2 = 0
guess1_3 = 0
guess2_3 = 0
while play == True:

    e = random.randrange(1, 11)
    e2 = random.randrange(1, 11)
    m = random.randrange(1, 21)
    m2 = random.randrange(1, 21)
    h = random.randrange(1, 101)
    h2 = random.randrange(1, 101)

    e_2 = random.randrange(1, 11)
    e2_2 = random.randrange(1, 11)
    m_2 = random.randrange(1, 21)
    m2_2 = random.randrange(1, 21)
    h_2 = random.randrange(1, 101)
    h2_2 = random.randrange(1, 101)

    def p2():
        global guess2
        print("Player 2")
        time.sleep(1.5)
        if l == 1:
            print("You only get 10 tries!")
            for i in range(10):
                print("Enter a number (1-10):")
                p = input()
                guess2 = guess2 + 1
                while p != e2:
                    if p > e2:
                        print("Lower:")
                        p = input()
                        guess2 = guess2 + 1
                    else:
                        print("Higher:")
                        p = input()
                        guess2 = guess2 + 1
                    if p == e2:
                        p1_2()
                        break
        elif l == 2:
            for i in range(15):
                print("Enter a number (1-20):")
                p = input()
                guess2 = guess2 + 1
                while p != m2:
                    if p > m2:
                        print("Lower:")
                        p = input()
                        guess2 = guess2 + 1
                    else:
                        print("Higher:")
                        p = input()
                        guess2 = guess2 + 1
                    if p == m2:
                        p1_2()
                        break
        else:
            for i in range(30):
                print("Enter a number (1-100):")
                p = input()
                guess2 = guess2 + 1
                while p != h2:
                    if p > h2:
                        print("Lower:")
                        p = input()
                        guess2 = guess2 + 1
                    else:
                        print("Higher:")
                        p = input()
                        guess2 = guess2 + 1
                    if p == h2:
                        p1_2()
                        break


    def p1():
        global guess1
        print("Round 1")
        time.sleep(1)
        print("Player 1")
        time.sleep(1)
        if l == 1:
            print("You only get 10 tries!")
            for i in range(10):
                print("Enter a number (1-10):")
                p = input()
                guess1 = guess1 + 1
                while p != e:
                    if p > e:
                        print("Lower:")
                        p = input()
                        guess1 = guess1 + 1
                    else:
                        print("Higher:")
                        p = input()
                        guess1 = guess1 + 1
                    if p == e:
                        p2()
                        break
        elif l == 2:
            print("You only get 15 tries!")
            for i in range(15):
                print("Enter a number (1-20):")
                p = input()
                while p != m:
                    if p > m:
                        print("Lower:")
                        p = input()
                    else:
                        print("Higher:")
                        p = input()
                if p == m:
                    p2()
                    break
        else:
            print("You only get 30 tries!")
            for i in range(30):
                print("Enter a number (1-100):")
                p = input()
                while p != h:
                    if p > h:
                        print("Lower:")
                        p = input()
                    else:
                        print("Higher:")
                        p = input()
                if p == h:
                    p2()
                    break


    def p1_2():
        global guess1_2
        print("Round 2")
        time.sleep(1)
        print("Player 1")
        time.sleep(1)
        if l == 1:
            print("You only get 10 tries!")
            for i in range(10):
                print("Enter a number (1-10):")
                p = input()
                guess1_2 = guess1_2 + 1
                while p != e_2:
                    if p > e_2:
                        print("Lower:")
                        p = input()
                        guess1_2 = guess1_2 + 1
                    else:
                        print("Higher:")
                        p = input()
                        guess1_2 = guess1_2 + 1
                if p == e_2:
                    p2_2()
                    break
        elif l == 2:
            print("You only get 15 tries!")
            for i in range(15):
                print("Enter a number (1-20):")
                p = input()
                guess1_2 = guess1_2 + 1
                while p != m_2:
                    if p > m_2:
                        print("Lower:")
                        p = input()
                        guess1_2 = guess1_2 + 1
                    else:
                        print("Higher:")
                        p = input()
                        guess1_2 = guess1_2 + 1
                if p == m_2:
                    p2_2()
        else:
            print("You only get 30 tries!")
            for i in range(30):
                print("Enter a number (1-100):")
                p = input()
                guess1_2 = guess1_2 + 1
                while p != h_2:
                    if p > h_2:
                        print("Lower:")
                        p = input()
                        guess1_2 = guess1_2 + 1
                    else:
                        print("Higher:")
                        p = input()
                        guess1_2 = guess1_2 + 1
                if p == h_2:
                    p2_2()
                    break


    def p2_2():
        global guess2_2
        print("Player 2")
        time.sleep(1)
        if l == 1:
            print("You only get 10 tries!")
            for i in range(10):
                print("Enter a number (1-10):")
                p = input()
                guess2_2 = guess2_2 + 1
                while p != e2_2:
                    if p > e2_2:
                        print("Lower:")
                        p = input()
                        guess2_2 = guess2_2 + 1
                    else:
                        print("Higher:")
                        p = input()
                        guess2_2 = guess2_2 + 1
                    if p == e2_2:
                        p1_3()
                        break
        elif l == 2:
            print("You only get 15 tries!")
            for i in range(15):
                print("Enter a number (1-20):")
                p = input()
                guess2_2 = guess2_2 + 1
                while p != m2_2:
                    if p > m2_2:
                        print("Lower:")
                        p = input()
                        guess2_2 = guess2_2 + 1
                    else:
                        print("Higher:")
                        p = input()
                        guess2_2 = guess2_2 + 1
                    if p == m2_2:
                        p1_3()
                        break
        else:
            print("You only get 30 tries!")
            for i in range(30):
                print("Enter a number (1-100):")
                p = input()
                guess2_2 = guess2_2 + 1
                while p != h2_2:
                    if p > h2_2:
                        print("Lower:")
                        p = input()
                        guess2_2 = guess2_2 + 1
                    else:
                        print("Higher:")
                        p = input()
                        guess2_2 = guess2_2 + 1
                    if p == h2_2:
                        p1_3()
                        break


    def p1_3():
        global guess1_3
        print("Round 3")
        time.sleep(1)
        print("\nFinal Round.")
        time.sleep(1)
        print("Player 1")
        time.sleep(1)
        if l == 1:
            print("You only get 10 tries!")
            for i in range(10):
                print("Enter a number (1-10):")
                p = input()
                guess1_3 = guess1_3 + 1
                while p != e:
                    if p > e:
                        print("Lower:")
                        p = input()
                        guess1_3 = guess1_3 + 1
                    else:
                        print("Higher:")
                        p = input()
                        guess1_3 = guess1_3 + 1
                if p == e:
                    p2_3()
                    break
        elif l == 2:
            print("You only get 15 tries!")
            for i in range(15):
                print("Enter a number (1-20):")
                p = input()
                guess1_3 = guess1_3 + 1
                while p != m:
                    if p > m:
                        print("Lower:")
                        p = input()
                        guess1_3 = guess1_3 + 1
                    else:
                        print("Higher:")
                        p = input()
                        guess1_3 = guess1_3 + 1
                if p == m:
                    p2_3()
                    break
        else:
            print("You only get 30 tries!")
            for i in range(30):
                print("Enter a number (1-100):")
                p = input()
                guess1_3 = guess1_3 + 1
                while p != h:
                    if p > h:
                        print("Lower:")
                        p = input()
                        guess1_3 = guess1_3 + 1
                    else:
                        print("Higher:")
                        p = input()
                        guess1_3 = guess1_3 + 1
                if p == h:
                    p2_3()
                    break


    def p2_3():
        global guess2_3
        global play
        print("Player 2")
        time.sleep(1)
        if l == 1:
            print("Remember, you only get 10 tries!")
            for i in range(10):
                print("Enter a number (1-10):")
                p = input()
                guess2_3 = guess2_3 + 1
                while p != e:
                    if p > e:
                        print("Lower:")
                        p = input()
                        guess2_3 = guess2_3 + 1
                    else:
                        print("Higher:")
                        p = input()
                        guess2_3 = guess2_3 + 1
                    if p == e:
                        print("You got it!")
                        win()
                        break
        elif l == 2:
            print("Remember, you only get 15 tries!")
            for i in range(15):
                print("Enter a number (1-20):")
                p = input()
                guess2_3 = guess2_3 + 1
                while p != m:
                    if p > m:
                        print("Lower:")
                        p = input()
                        guess2_3 = guess2_3 + 1
                    else:
                        print("Higher:")
                        p = input()
                    if p == m:
                        print("You got it!")
                        win()
                        break
        else:
            print("Remember, you only get 30 tries!")
            for i in range(30):
                print("Enter a number (1-100):")
                p = input()
                guess2_3 = guess2_3 + 1
                while p != h:
                    if p > h:
                        print("Lower:")
                        p = input()
                        guess2_3 = guess2_3 + 1
                    else:
                        print("Higher:")
                        p = input()
                        guess2_3 = guess2_3 + 1
                    if p == h:
                        print("You got it!")
                        win()
                        break


    def win():
        if guess1 + guess1_2 + guess1_3 > guess2 + guess2_2 + guess2_3:
            print("Player 2 wins!")
            end()
        else:
            print("Player 1 wins!")
            end()


    def end():
        print("Play again? (Y/N)")
        y = 1
        n = 2
        Y = 1
        N = 2
        play = int(input("Enter a choice:"))
        if play == 1:
            play = True
            main()
        else:
            play = False


    def main():
        guess1 = 0
        guess2 = 0
        guess1_2 = 0
        guess2_2 = 0
        guess1_3 = 0
        guess2_3 = 0
        print("Welcome to the Guessing Game.")
        print("Mode: Human vs. Human (Player 1 vs. Player 2")
        l = input("Play 1-Easy(10) 2-Medium(20) 3-Hard(100):")
        global l
        p1()

    main()