card_count = [0] * 220

with open("input.txt") as file:
    text = file.read()
    cards = text.split('\n')
    

    for card_idx, card in enumerate(cards):

        card_count[card_idx] += 1

        nbr_winnings = 0
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
            if your_nbr in winning_nbrs:
                nbr_winnings += 1

        for win_idx in range(1, nbr_winnings+1):
            card_count[card_idx+win_idx] += card_count[card_idx]
    
res = 0
for amount in card_count:
    res += amount

print(res)


