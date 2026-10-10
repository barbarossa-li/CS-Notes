"""猜数字：在 1 到 100 之间猜一个随机整数。

运行：python3 guess_number.py
"""

import random


def read_guess() -> int | None:
    """读取一次猜测。返回 None 表示玩家选择退出。"""
    while True:
        raw = input("请输入 1 到 100 的整数（输入 q 退出）：").strip()
        if raw.lower() == "q":
            return None
        try:
            guess = int(raw)
        except ValueError:
            print("这不是整数，请重新输入。")
            continue
        if 1 <= guess <= 100:
            return guess
        print("数字要在 1 到 100 之间。")


def play() -> None:
    answer = random.randint(1, 100)
    attempts = 0
    print("我想好了一个 1 到 100 之间的整数。")

    while True:
        guess = read_guess()
        if guess is None:
            print(f"已退出，答案是 {answer}。")
            return

        attempts += 1
        if guess < answer:
            print("太小了。")
        elif guess > answer:
            print("太大了。")
        else:
            print(f"猜对了！你一共猜了 {attempts} 次。")
            return


if __name__ == "__main__":
    play()
