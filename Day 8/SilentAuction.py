def find_highest_bidder(bidders):
    highest_bid = 0
    highest_bidder = ''
    for key in bidders:
        if bidders[key] > highest_bid:
            highest_bidder = key
            highest_bid = bidders[key]
    
    print(f'The winner is {highest_bidder} with a bid of ${highest_bid}')
    return highest_bid

def main():
    bidders = {}
    other_bidders = 'yes'
    while other_bidders == 'yes':
        name = input('Enter the bidder\'s name: ')
        bid = int(input('How much would you like to bid? $'))
        bidders[name] = bid

        other_bidders = input('Are there any other bidders? Type \'yes\' or \'no\' ').lower()
        if other_bidders == 'no':
            find_highest_bidder(bidders)
            break

main()
