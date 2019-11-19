import random

#dice_input = input('Please input a die config in DND style (e.g. 2d6)')

while input:
    dice_input = input('Please input a die config in DND style (e.g. 2d6): ')

    sep_input = dice_input.split('d')

    sep_input[0] = int(sep_input[0])
    sep_input[1] = int(sep_input[1])

    die_results = []
    for x in range(0, sep_input[0]):
        die_results.append(random.randrange(1, (sep_input[1] + 1)))

    print(f"{die_results} >>> {sum(die_results)}")