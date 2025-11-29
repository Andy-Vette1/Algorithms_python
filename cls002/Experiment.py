from typing import *
import random

def main():
    print("The Gini coefficient of a society is a decimal value between 0 and 1.")
    print("A Gini coefficient of 0 represents perfect wealth equality (everyone has the same).")
    print("A Gini coefficient of 1 represents perfect inequality (one person holds all wealth).")
    print("A lower coefficient means fairer wealth distribution; a higher one means more unequal distribution.")
    print("In 2022, the global average Gini coefficient was 0.44.")
    print("It is generally believed that when the Gini coefficient reaches 0.5,")
    print("it indicates a huge wealth gap and highly uneven distribution.")
    print("Society may face crises, such as high crime rates or social unrest.")
    print("Test started.")

    n = 100
    t = 100000

    print(f"Number of people: {n}")
    print(f"Number of rounds: {t}")

    experiment(n, t)
    print("Test ended.")

def experiment(n: int, t: int):
    wealth_list = [100 for _ in range(n)]

    for _ in range(t):
        for i in range(n):
            if wealth_list[i] > 0:
                r = random.randint(0, n - 1)
                while r == i:
                    r = random.randint(0, n - 1)
                wealth_list[r] += 1
                wealth_list[i] -= 1


    wealth_list.sort()
    print("List of individual wealth (poorest to richest):")
    for i in range(n):
        print(f"{int(wealth_list[i])} ", end="")
        if i % 10 == 9:
            print()

    print(f"The Gini coefficient of this society is: {calGini(wealth_list)}")

def calGini(wealth_list: List):
    sum_of_abs_diff = 0
    sum_of_wealth = 0
    n = len(wealth_list)
    for wealth in wealth_list:
        sum_of_wealth += wealth
        for i in range(n):
            sum_of_abs_diff += abs(wealth_list[i] - wealth)
    return sum_of_abs_diff / ( sum_of_wealth * 2 * n)


if __name__ == '__main__':
    # experiment(100, 10)
    main()