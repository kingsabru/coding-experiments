from collections import namedtuple

def main():
  Card = namedtuple('Card', 'rank suit')
  card1 = Card('7', 'spades')

  print(card1)
  print(f'card1.rank = {card1.rank}, card1.suit = {card1.suit}')
  print('Unpacking namedtuple: {} {}'.format(*card1))

  MasterCard = namedtuple('MasterCard', Card._fields + ('cvv',))
  mastercard1 = MasterCard('7', 'spades', '123')

  print(mastercard1)

  mastercard1 = mastercard1._replace(cvv='233')
  print(mastercard1._asdict())

  mastercard2 = MasterCard._make(['7', 'hearts', '245'])
  print(mastercard2)

if __name__ == '__main__':
  main()

# Resources
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://dbader.org/blog/writing-clean-python-with-namedtuples