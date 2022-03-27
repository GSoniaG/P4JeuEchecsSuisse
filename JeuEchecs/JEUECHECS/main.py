"""
main program chess game project 4
"""

from controllers.launch_controllers import LaunchChoice
from controllers.menu_controllers import HomeMenu


class Home:
    def __init__(self):
        pass

    def run(self):
        while True:
            mainmenu = HomeMenu()
            # main menu menucontrollers.py
            user_choice = mainmenu.run()

            if user_choice == 0:
                break

            choice = LaunchChoice()
            choice.run(user_choice)


def main():
    app = Home()
    app.run()


if __name__ == "__main__":
    main()
