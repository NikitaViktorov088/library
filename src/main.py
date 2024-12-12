from ui.menu import Menu
from utils.logger import setup_logger

if __name__ == "__main__":
    setup_logger()
    menu = Menu()
    menu.show()