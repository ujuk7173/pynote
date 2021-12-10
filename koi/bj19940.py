for _ in range(int(input())):
    n = int(input())
    buttons = [0]*5
    sixties, tens, ones = n//60, (n % 60)//10, n % 10

    if ones > 5:
        tens += 1
        ones -= 10
    if tens > 3:
        sixties += 1
        tens -= 6
    if tens < 0 and ones == 5:
        tens += 1
        ones -= 10

    # buttons[0] = sixties
    # if tens >= 0: buttons[1] = abs(tens)
    # else: buttons[2] = abs(tens)
    # if ones >= 0: buttons[3] = abs(ones)
    # else: buttons[4] = abs(ones)
    # print(*buttons)

    buttons[0] = sixties
    buttons[2-(tens >= 0)] = abs(tens)
    buttons[4-(ones >= 0)] = abs(ones)
    print(*buttons)