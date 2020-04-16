import random

def main():
    dice_rolls = int(input('How many rolls bro?'))
    dice_size = int(input('How many sides broo?'))
    dice_sum = 0
    for i in range(0, dice_rolls):
        roll = random.randint(1, dice_size)
        dice_sum += roll
        if roll == 1:
         print(f'You rolled a {roll}! Critical Failure!!')
        elif roll == 6:
         print(f'You rolled a {roll}! Critical Sucess!')
        else:
         print(f'Whoaaa you just rolled a {roll}!')

    print(f'You have a total of {dice_sum}')

if __name__== "__main__":
  main()
