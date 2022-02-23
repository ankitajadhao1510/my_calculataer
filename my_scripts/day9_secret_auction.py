# from os import cle
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
# from replit import clear
# from art import logo
print(logo)
bids = {}
bidding_finished = False

def find_highiest_bidder(bidding_record):
  highest_bid = 0
  winner = ''
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"the winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input('What is your name? ')
  price = int(input('what is your bid? $'))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == 'no'.upper():
    bidding_finished = True
    find_highiest_bidder(bids)
  elif should_continue == 'yes'.upper():
    continue

