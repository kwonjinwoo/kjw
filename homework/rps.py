import random

jw_list = ['묵', '찌', '빠']
decide_outcome = {0: '쉽네!', 1: '지지~', 2: '무승부ㅠ'}


def determineWinner(my, ai):

    if not my in jw_list:
        return '다시 적어'

    if my == ai:
        return '무승부'
    elif (my == '묵' and ai == '찌') or \
        (my == '찌' and ai == '빠') or \
            (my == '빠' and ai == '묵'):
        return 'my 승!'
    else:
        return 'ai 승!'


def rock_paper_scissors():
    while True:
        print("겜 고고")
        user_choice = input("찌, 묵, 빠 중에서 선택하세요 ('종료': ")

        if user_choice == '종료':

            print("종료")
            break

        if user_choice not in jw_list:
            print('찌, 묵, 빠 입력')
            continue

        computer_choice = random.choice(jw_list)
        print(f"나: {user_choice}, 컴터: {computer_choice}")

        result = determineWinner(user_choice, computer_choice)
        print(f"결과: {result}")


if __name__ == "__main__":
    rock_paper_scissors()
