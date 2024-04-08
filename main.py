import time
import curses
from curses import wrapper


def timer(stdscr):
    seconds = 0

    while True:
        seconds += 1
        time.sleep(1)
        stdscr.addstr(str(seconds))
        stdscr.refresh()


def main(stdscr):
    stdscr.clear()

    stdscr.addstr(
        """
                  ______ _             _   _ 
                 |  ____| |           | | (_)
                 | |__  | | ___   __ _| |_ _ 
                 |  __| | |/ _ \ / _` | __| |
                 | |    | | (_) | (_| | |_| |
                 |_|    |_|\___/ \__,_|\__|_|

    """
    )

    wrapper(timer)


if __name__ == "__main__":
    wrapper(main)
