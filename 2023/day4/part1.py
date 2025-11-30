with open("input.txt") as file:
    text = file.read()
    cards = text.split('\n')

    res = 0

    for card in cards:
        if card == '':
            continue
        
        current_points = 0
        winning_nbrs = set()

        card_split = card.split('|')
        winning_side = card_split[0]
        your_side = card_split[1]

        winnings = winning_side.split(' ')
        winnings = [x for x in winnings if x != '']
        for winning in winnings:
            winning_nbrs.add(int(winning))


        your_nbrs = your_side.split(' ')
        your_nbrs = [int(x) for x in your_nbrs if x != '']

        for your_nbr in your_nbrs:

            print(your_nbr)
            if your_nbr in winning_nbrs:
                print("hre", your_nbr)
                if current_points == 0:
                    current_points = 1
                else:
                    current_points *= 2
        
        print(current_points)
        res += current_points

print(res)