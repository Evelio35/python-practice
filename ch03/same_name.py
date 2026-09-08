def spam():
    eggs = 'spam local'
    print(eggs)  # This will print 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs)  # This will print 'bacon local'
    spam()
    print(eggs)  #This will print 'bacon local'

eggs = 'global'
bacon()
print(eggs) #This will print 'global'