from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class ImmutableCard:
  rank:str
  suit:str
  
@dataclass(frozen=True)
class ImmutableDeck:
  cards:List[ImmutableCard]
  
def main():
    queen_of_hearts = ImmutableCard('Q', '♡')
    ace_of_spades = ImmutableCard('A', '♠')
    deck = ImmutableDeck([queen_of_hearts, ace_of_spades])
    print(deck)
    deck.cards[0] = ImmutableCard('7', '♢')
    print(deck)

if __name__ == '__main__':
  main()