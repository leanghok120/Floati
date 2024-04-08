import time
import curses
from curses import wrapper

# App purpose:
# add a task
# track time spent on task
#
# Instead of keybinds
# Use numbers

path = ""
tasks = []


def timer(stdscr):
    stdscr.clear()

    seconds = 0

    while True:
        seconds += 1
        time.sleep(1)
        stdscr.addstr(str(seconds))
        stdscr.refresh()


def addTask(stdscr):
    # Make the character visible as u type
    curses.echo()

    stdscr.addstr("\n")
    stdscr.addstr("Task name: ")

    # Input
    task_name = stdscr.getstr()
    tasks.append(task_name)

    stdscr.refresh()

    # Go back to Home
    wrapper(main)


def showTasks(stdscr):
    stdscr.clear()


def main(stdscr):
    curses.echo()
    stdscr.clear()

    # Set Path to home
    path = "Home"

    stdscr.addstr(
        r"""
                  ______ _             _   _ 
                 |  ____| |           | | (_)
                 | |__  | | ___   __ _| |_ _ 
                 |  __| | |/ _ \ / _` | __| |
                 | |    | | (_) | (_| | |_| |
                 |_|    |_|\___/ \__,_|\__|_|

                       [ @Leangphok ]


    """
    )

    # Keybinds
    stdscr.addstr("1. Add task ")
    stdscr.addstr("2. Tasks")
    stdscr.addstr("\n")

    # Prompt
    stdscr.addstr(path + " => ", curses.A_BOLD)
    stdscr.refresh()

    # Add task
    key = stdscr.getkey()
    if key == "1":
        # Go to add tasks
        wrapper(addTask)
    elif key == "2":
        # Go to show tasks
        wrapper(showTasks)


if __name__ == "__main__":
    wrapper(main)
