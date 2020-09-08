def spam():
    global eggs
    eggs = 'spam' # this is a global

def bacon():
    eggs = 'bacon' # this is a local

def ham():
    print(eggs) # this is a global

eggs = 42 # this is a global
spam()
print(eggs)