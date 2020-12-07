import csv

with open("C:\Max\Code\PycharmProjects\Python\csv_reader", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open("C:\Max\Code\PycharmProjects\Python\csv_reader", 'w', newline='') as new_csv_file:
        fieldnames = ['City', 'Unit price']
        csv_writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames, extrasaction='ignore')

        csv_writer.writeheader()

        # sukuriau nauja faila tik su city ir unit prices laukais
        for line in csv_reader:
            csv_writer.writerow(line)