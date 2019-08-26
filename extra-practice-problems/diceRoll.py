# chunk of work done by recursive case
def diceCount(target, list):
    if dice==0:
        # do something
        print(i)
    else:
        for i in range(1, 7):
            # chose
            list.add(i)
            diceCount()
            list.remove(list.size()-1)
            # un chose
