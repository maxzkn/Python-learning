name = ''
while not name:
    print('Enter your name:')
    name = input()
print('How many guests?')
numOfGuests = int(input())
if numOfGuests:
    print('Be sure to have enough space for your guests')
print('Done')