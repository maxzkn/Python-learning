def spam():
    print(eggs) # ERROR!
    eggs = 'spam local'
    eggs = 'global'

eggs = 'global'
spam()