import random

#p1 = input('Type Player1 name')
#p2 = input('Type Player2 name')

#creating a dictionary for cards
cards = {'ace':1, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5,
          'six':6, 'seven':7, 'eight':8, 'nine':9, 'jack':10,
          'queen':10, 'king':10}

#testing if dictionary work or not
#print(cards.keys())
#print(cards.values())


#report_score = 'Your score is {}'.format()
#print(report_score)


#function to draw a random card from cards dictionary
def get_card():
    rand_draw = random.choice(list(cards))
    value = cards[rand_draw]
    #print('Random draw of a card is',rand_draw,'-',value)
    return value

print(get_card())

def declare_winner():
    p1_card = []
    p2_card = []
    
    while len(p1_card) != 2:
        p1_card.append(get_card())
        if len(p1_card) == 2:
            print('Player1 has', p1_card)
    
    while len(p2_card) != 2:
        p2_card.append(get_card())
        if len(p2_card) == 2:
            print('Player2 has', p2_card)

declare_winner()

