from hero import Hero
from monster import Monster

def action_choose():
    action = input(
        "Enter the required action:\n1- Attack \n2- Defend \n3- Heal \n4- LevelUp \n")
    return action


def main():
    hero_name = input("Enter hero's name: ")
    hero = Hero(hero_name)
    monster = Monster('monster', hero)

    print(f"{hero_name}'s hp: {hero.hp}, {hero_name}'s level: {hero.level} \n ~~~~~~~~   ~~~~~~~~~")
    print(f"Monster's hp: {monster.hp}, Monster's level {monster.level}\n ~~~~~~~~   ~~~~~~~~~")

    while hero.hp > 0:
        action = action_choose()
        hero.increase_coins(1)

        if action == '1':
            hero.attack(monster)
            if monster.hp <= 0:
                monster = Monster('monster', hero)
            monster.attack(hero)
            print("Monster attacked you!")
        elif action == '2':
            hero.defend(monster)
            print("Monster attacked you, you defended 80 percent damage")
        elif action == '3':
            hero.heal()
        elif action == '4':
            hero.level_up()

        print(
            f"{hero_name}'s hp: {hero.hp}, level: {hero.level}, coins: {hero.coin} \n ~~~~~~~~   ~~~~~~~~~")
        print(f"Monster's hp: {monster.hp}, level {monster.level} \n ~~~~~~~~   ~~~~~~~~~")

    if hero.hp <= 0:
        print("\n Game Over. You're dead!")


if __name__ == "__main__":
    main()
