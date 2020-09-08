list = [1, 2, 4, 5, 3, 9, 5]
dubbedElement = []

for i in range(len(list)):
    count = 0
    if list[i] in dubbedElement:
        continue
    for k in range(len(list)):
        if list[i] == list[k]:
            count = count + 1
        if k == len(list) - 1:
            if count > 1:
                print("Elemento " + str(list[i]) + " pasikartojimu skaicius: " + str(count - 1))
                dubbedElement.append(list[i])