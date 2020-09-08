def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    if number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

while True:
    try:
        num = int(input('Enter number: '))
        while num != 1:
            num = collatz(num)
        break
    except ValueError:
        print("You must type a number!")