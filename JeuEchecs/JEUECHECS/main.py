"""
main program chess game project 4
"""

from controllers.menu_controllers import HomeMenu

# call class HomeMenu of menucontrollers
from controllers.launch_controllers import LaunchChoice

# call class LaunchChoice of launchcontrollers


class Home:
    """
    Main part
    """

    def __init__(self):
        pass

    def run(self):

        while True:

            mainmenu = HomeMenu()  # main menu menucontrollers.py
            user_choice = mainmenu.run()

            if user_choice == 0:
                break

            choice = LaunchChoice()  # launchcontrollers.py regarding choice
            choice.run(user_choice)


def main():
    app = Home()
    app.run()


if __name__ == "__main__":
    main()
