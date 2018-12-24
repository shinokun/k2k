import curses
import time
import signal
import sys

N_CNT = 12
M_CNT = 24

MIN_NUM = 1
MAX_NUM = 26 

def handler(signal, frame):
        print('Done');
        sys.exit(0)
signal.signal(signal.SIGINT, handler)
 
stdscr = curses.initscr()

def main(stdscr):

    n = N_CNT
    m = M_CNT

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

    while(True):

        for i in range(MIN_NUM, MAX_NUM):

            m =  m + 1

            stdscr.clear()
            stdscr.addstr(n, m, 'X',curses.color_pair(1))
            stdscr.refresh()

            time.sleep(0.1)

        #stdscr.getkey()
 
        for i in range(MIN_NUM, MAX_NUM):

            m =  m - 1

            stdscr.clear()
            stdscr.addstr(n, m, 'X',curses.color_pair(1))
            stdscr.refresh()

            time.sleep(0.1)

    pass

if __name__ == '__main__':
    curses.wrapper(main)
