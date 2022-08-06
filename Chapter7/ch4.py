#write a program with an infinite loop
#the loop should have the option to quit
#each time through the loop the user will be asked to guess if the number is in the list
number_list = [ '1', '2', '3', '4', '5', '6', '7', '8' ]

while True:
    guess = input('Guess what number is in my list or type q to quit ')
    if guess == 'q':
        break
    else:
        for i in number_list:
            if guess == i:
                print("your number is in my list!")
                break
            elif guess != i:
                print("your number is not in my list!")
                break
