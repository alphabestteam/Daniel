from costumer import costumer
from register import register


def main():

    user1 = costumer("Ari")
    user2 = costumer("Chen")
    user3 = costumer("Daniel")

    user1.add_product("Pasta", 2, 3)
    user1.add_product("Pasta", 2, 3)
    user1.add_product("Pasta", 2, 3)
    user1.add_product("Pasta", 2, 3)

    user2.add_product("XL", 5, 4)
    user2.add_product("Pasta", 7, 3)
    user3.add_product("Coke", 6, 4)

    user1.remove_product("Pasta", 1)
    user2.remove_product("XL", 4)
    user3.remove_product("Coke", 1)

    register1 = register()
    register2 = register()

    register1.check_out_customer(user1)
    register1.check_out_customer(user2)
    register2.check_out_customer(user3)

    register1.print_summary()
    register2.print_summary()


if __name__ == '__main__':
    main()
