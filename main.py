import time
import curses
from curses import wrapper
import sys

# App purpose:
# add a task
# track time spent on task
#
# Instead of keybinds
# Use numbers

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
    tasks.append(task_name.decode())

    stdscr.refresh()

    wrapper(showKeybinds)


def showTasks(stdscr):
    stdscr.addstr("\n")

    task_list = ""
    i = 0

    while i < len(tasks):
        task_list += str(i) + ". " + tasks[i] + " "
        i += 1

    stdscr.addstr(task_list)
    stdscr.addstr("\n")

    stdscr.refresh()

    stdscr.getkey()
    wrapper(showKeybinds)


def showKeybinds(stdscr):
    # Keybinds
    stdscr.addstr("\n")
    stdscr.addstr("1. Add task ")
    stdscr.addstr("2. Tasks ")
    stdscr.addstr("q. Quit")
    stdscr.addstr("\n")

    # Prompt
    stdscr.addstr("Home => ", curses.A_BOLD)
    stdscr.refresh()

    # Add task
    key = stdscr.getkey()
    if key == "1":
        # Go to add tasks
        wrapper(addTask)
    # Show tasks
    elif key == "2":
        # Go to show tasks
        wrapper(showTasks)
    # Quit
    elif key == "q":
        sys.exit


def main(stdscr):
    curses.echo()
    stdscr.clear()

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

    # Show dashboard
    wrapper(showKeybinds)


if __name__ == "__main__":
    wrapper(main)
