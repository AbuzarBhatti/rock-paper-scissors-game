import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

computer_choice = random.choice(choices)
user_choice = input("What's your choice? R for rock, P for paper, S for scissors : ")
result = 'TIE'

#Assigning ASCII art to the user-choice based on what he chose

if user_choice.lower() == 'r':
    user_choice = choices[0]
elif user_choice.lower() == 'p':
    user_choice = choices[1]
elif user_choice.lower() == 's':
    user_choice = choices[2]
else:
    print('Invalid selection...')

# Comparing choices to get results

if computer_choice == choices[1] and user_choice == choices[0]:
    result = 'COMPUTER WINS'
elif computer_choice == choices[0] and user_choice == choices[1]:
    result = 'YOU WON'
elif computer_choice == choices[0] and user_choice == choices[2]:
    result = 'COMPUTER WINS'
elif computer_choice == choices[2] and user_choice == choices[0]:
    result = 'YOU WON'
elif computer_choice == choices[1] and user_choice == choices[2]:
    result = 'YOU WON'
elif computer_choice == choices[2] and user_choice == choices[1]:
    result = 'COMPUTER WINS'

print(f'User chose : \n {user_choice}\n')
print(f'Computer chose : \n {computer_choice}\n')
print(f'Result : {result}')

