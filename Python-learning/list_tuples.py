vardai = ['Tadas', 'Simas', 'Agne', 'Linas', 'Vita']

print(vardai)
print(vardai[0:3])
print(vardai[-1])

vardai[2] = 'Kernius'

print(vardai)

skaiciai = [1, 3, 5, 7, 2]
# max = max(vardai)
# print(max)
max = skaiciai[0]

for x in skaiciai:
    if x > max:
        max = x

print(max)