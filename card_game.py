#importing random module
import random


#dictionary for card values
values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":11,"Queen":12,"King":13,"Ace":14}
#tuples for suits 
suits = ("Hearts","Spade","Diamonds","Clubs")
#tuples for ranks
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")


# Card Class

class Card:

    '''For creating card objects'''

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank +" of " + self.suit


class Deck:
    
    def __init__(self):

        '''To create a deck of 52 different cards'''
        self.all_cards = []

        for suit in suits:
            for rank in ranks:

                created_object = Card(suit,rank)
                self.all_cards.append(created_object)

    # for shuffling of card deck
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    # picking one card from shuffled deck
    def deal_one(self):
        return self.all_cards.pop()

# Player Class
class Player:
    
    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def add_card(self,card_objects):
        if type(card_objects) == type([]):
            self.all_cards.extend(card_objects)
        else:
            self.all_cards.append(card_objects)

    def remove_card(self):
        return self.all_cards.pop()
        
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards"


game_on = True

#game logic

player_one = Player("One")
player_two = Player("Two")

my_deck = Deck()
my_deck.shuffle()

for i in range(26):
    player_one.add_card(my_deck.deal_one())
    player_two.add_card(my_deck.deal_one())


# Start game
rounds = 0

while game_on:

    rounds += 1
    print(f"Round : {rounds}")

    # Player One loss
    if len(player_one.all_cards) == 0:
        print(f"Player One out of Cards!\nPlayer Two wins.")
        break

    # Player Two loss
    if len(player_two.all_cards) == 0:
        print(f"Player Two out of Cards!\nPlayer One wins.")
        break


    # Starting game
    player_one_cards = []
    player_one_cards.append(player_one.remove_card())

    player_two_cards = []
    player_two_cards.append(player_two.remove_card())
    
    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_card(player_one_cards)
            player_one.add_card(player_two_cards)
            at_war = False

        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player_two.add_card(player_one_cards)
            player_two.add_card(player_two_cards)
            at_war = False

        else:

            print("WAR!")

            if len(player_one.all_cards) < 5:
                print("Player One fails to raise war!")
                print("PLAYER TWO WINS!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player Two fails to raise war!")
                print("PLAYER ONE WINS!")
                game_on = False
                break

            else:
                
                for i in range(5):
                    player_one_cards.append(player_one.remove_card())
                    player_two_cards.append(player_two.remove_card())
