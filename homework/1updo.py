import random


def updown_game():
    secret_number = random.randint(1, 100)
    count = 0
    print("겜 고고")

    while True:
        try:
            user = int(input())
            count += 1
            if user < secret_number:
                print("업!")
            elif user > secret_number:
                print("다운!")
            else:
                print("정답!")
                print(f"몇번했어? {count}")
                break
        except ValueError:
            print("오류")


updown_game()
