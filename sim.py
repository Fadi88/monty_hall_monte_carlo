from random import choice


def sim():
    num_doors = 100

    rounds = 100000

    doors = list(range(num_doors))

    n_keep = 0
    n_switch = 0

    for _ in range(rounds):
        prize = choice(doors)
        guess = choice(doors)

        if prize == guess:
            n_keep += 1
        else:
            n_switch += 1

    print(f"keep choice win chance {n_keep / rounds *100}%")
    print(f"switch choice win chance {n_switch / rounds *100}%")


if __name__ == "__main__":
    sim()
