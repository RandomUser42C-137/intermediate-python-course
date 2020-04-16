import sys

sys.path.append('C:\\Program Files\\Git\\emoji')
print(sys.path)

import random
import emoji

def main():
    roll = random.randint(1, 6)
    print(f'You rolled a {roll}')
    print(emoji.emojize(':thumbs_up:'))

if __name__== "__main__":
  main()
