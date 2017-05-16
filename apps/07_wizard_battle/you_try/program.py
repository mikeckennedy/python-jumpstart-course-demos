import random

import time
from actors import Wizard, Creature, SmallAnimal, Predator, Dragon


def main():
    print_header()
    game_loop()


def print_header():
    print('----------------------')
    print('----- Wizard Battle -------')
    print('----------------------')


def game_loop():
    creatures = [
        SmallAnimal('Toad', 2),
        Predator('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 20, True),
        Wizard('Evil Wizard', 100)

    ]

    hero = Wizard('You', 75)

    while True:

        active_creature = random.choice(creatures)
        print("A {} of level {} has appeared from a dark and dreary forest"
              .format(active_creature.name, active_creature.level))
        print("")

        cmd = input('Do you [A]ttack, [R]un away, or [L]ook around?')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("You must rest and regain your strength")
                time.sleep(3)
                print("You're ready to try again")

        elif cmd == 'r':
            print("You lose your nerve and run away!")
        elif cmd == 'l':
            print("The wizard {} looks around and takes in the surroundings:".format(hero.name))
            for c in creatures:
                print(' * A {} of level {} '.format(c.name, c.level))

        else:
            print('Thanks for playing...exiting the game')
            break

        if not creatures:
            print("You've defeated all the dreary creatures")
            exit()


if __name__ == '__main__':
    main()
