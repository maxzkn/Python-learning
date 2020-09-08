while True:
    print('Who are u?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is a pass?')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')