from domains.test_oop import test_oop
import curses

screen = curses.initscr()
t = test_oop()
t.start()