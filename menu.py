__author__ = 'KoicsD'

from os import system
from msvcrt import getch


header = ""


class Index:
    def __init__(self, limit: int):
        self.limit = limit
        self.value = 0

    def increase(self):
        if self.value < self.limit - 1:
            self.value += 1

    def decrease(self):
        if self.value > 0:
            self.value -= 1


class MenuItem:
    pass


class Menu(MenuItem):
    enum_keys = {"up": 0, "down": 1, "right": 2, "left": 3, "enter": 4, "backspace": 5, "escape": 6}

    def __init__(self, title: str, message=""):
        self.title = title
        self.message = message
        self.items = []

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def load(self):
        index = Index(len(self.items))
        while True:
            system("cls")
            print(header)
            self.list_items(index.value)
            usr_ans = Menu.q_input()

            if usr_ans == Menu.enum_keys["up"] or usr_ans == Menu.enum_keys["left"]:
                index.decrease()
            elif usr_ans == Menu.enum_keys["down"] or usr_ans == Menu.enum_keys["right"]:
                index.increase()
            elif usr_ans == Menu.enum_keys["enter"]:
                if index.value in range(len(self.items)):
                    if not self.items[index.value].load():
                        break
            elif usr_ans == Menu.enum_keys["backspace"]:
                return True  # means: caller must keep loop going on
            elif usr_ans == Menu.enum_keys["escape"]:
                return False  # means: caller must return

    def list_items(self, selected):
        print(self.title)
        print()
        print(self.message)
        print()
        for i in range(len(self.items)):
            if i == selected:
                print("\t*\t" + self.items[i].title)
            else:
                print("\t\t" + self.items[i].title)

    @staticmethod
    def q_input():
        key = ord(getch())
        if key == 224:
            key = ord(getch())
            if key == 72:
                return Menu.enum_keys["up"]
            elif key == 80:
                return Menu.enum_keys["down"]
            elif key == 77:
                return Menu.enum_keys["right"]
            elif key == 75:
                return Menu.enum_keys["left"]
            else:
                return None
        elif key == 13:
            return Menu.enum_keys["enter"]
        elif key == 8:
            return Menu.enum_keys["backspace"]
        elif key == 27:
            return Menu.enum_keys["escape"]
        else:
            return None


class MenuPoint(MenuItem):
    def __init__(self, title: str, function):
        self.title = title
        self.function = function

    def load(self):
        system("cls")
        self.function()
        return False  # caller must always return


def print_bruhaha():
    print("bruhaha")


def print_nyihaha():
    print("nyihaha")


def print_nuqu():
    print("I don't give a f*ck about it.")


def demo():
    main_menu = Menu("Main menu", "This is the absolutely main menu.")

    submenu_1 = Menu("Submenu 1", "This is the 1st submenu.")
    submenu_2 = Menu("Submenu 2", "This is the 2nd submenu.")
    main_menu.add_item(submenu_1)
    main_menu.add_item(submenu_2)

    submenu_1_1 = Menu("Submenu 1.1", "This is the 1st submenu of the 1st submenu.")
    submenu_1.add_item(submenu_1_1)

    menupoint_3 = MenuPoint("printing 'bruhaha'", print_bruhaha)
    main_menu.add_item(menupoint_3)

    menupoint_1_2 = MenuPoint("printing 'nyihaha'", print_nyihaha)
    submenu_1.add_item(menupoint_1_2)

    menupoint_1_1_1 = MenuPoint("printing 'bruhaha'", print_bruhaha)
    menupoint_1_1_2 = MenuPoint("printing 'nyihaha'", print_nyihaha)
    menupoint_1_1_3 = MenuPoint("just try to choose me", print_nuqu)
    submenu_1_1.add_item(menupoint_1_1_1)
    submenu_1_1.add_item(menupoint_1_1_2)
    submenu_1_1.add_item(menupoint_1_1_3)

    main_menu.load()
    system("cls")


if __name__ == '__main__':
    demo()
