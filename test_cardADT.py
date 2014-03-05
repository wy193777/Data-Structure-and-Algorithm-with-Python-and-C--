# test_cardADT.py
import cardADT


def printAll():
    for suit in 'cdhs':
        for rank in range(1, 14):
            myCard = cardADT.create(rank, suit)
            print(cardADT.toString(myCard))

if __name__ == '__main__':
    printAll()
