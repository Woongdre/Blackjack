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


report_score = 'Your score is {}'.format(5)
print(report_score)


#function to draw a random card from cards dictionary
def get_card():
    rand_draw = random.choice(list(cards))
    value = cards[rand_draw]
    #print('Random draw of a card is',rand_draw,'-',value)
    return value

print(get_card())

def declare_winner():
    p1_score = get_card() + get_card()
    print('Youre current scoure is {}'.format(p1_score)
    if p1_score < 22:
        more = input('Do you want another card? (y/n): ')
        if more == 'y':
            p1_score = p1_score + get_card()
            print(p1_score)
        else:
            print(p1_score)
    else:
          print('You are busted with {}'.format(p1_score))

declare_winner()
