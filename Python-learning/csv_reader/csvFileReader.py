import csv
new_list = []

with open("C:\Max\Code\supermarket_sales.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    # ------------- mano budas (su listais, sukuria lista su visom eilutem) --------------

    for row in csv_reader:
        new_list.append(row)
    # arba trumpiau:
    # new_list = [row for row in csv_reader]

    print(new_list[0])
    print(new_list[5])

    # ------------ kitas budas (su listais, sukuria lista tik su dviem eilutem) -------------

    # for idx, row in enumerate(csv_reader):
    #     if idx in (0, 5):
    #         new_list.append(row)
    # print(new_list[0])
    # print(new_list[1])
    # arba trumpiau:
    # rows = [row for idx, row in enumerate(csv_reader) if idx in (0, 5)]
    # print(type(rows))
    # print(rows[0])
    # print(rows[1])

    # ------------ kitas budas (su generators (geriau kai didziulis failas), sukuria tik su dviem eilutem) -------------
    # def rows(num1, num2):
    #     for idx, row in enumerate(csv_reader):
    #         if idx in (num1, num2):
    #             yield row
    # my_rows = rows(0, 5)
    # print(my_rows)
    # for line in my_rows:
    #     print(line)
    # arba trumpiau (generators):
    # rows = (row for idx, row in enumerate(csv_reader) if idx in (0, 5))
    # print(type(rows))
    # for line in rows:
    #     print(line)