def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1
 
print('Enter a number: ')
user_input = int(input())

while True:
    print(user_input)
    if user_input == 1:
            break
    else:
        user_input = collatz(user_input)
        
    
