import curses
import time

N_CNT = 12
M_CNT = 24

MIN_NUM = 1
MAX_NUM = 26 
 
stdscr = curses.initscr()
 
def main(stdscr):

    n = N_CNT
    m = M_CNT

    for i in range(MIN_NUM, MAX_NUM):

        for i in range(MIN_NUM, MAX_NUM):

            m =  m + 1

            stdscr.clear()
            stdscr.addstr(n, m, 'X')
            stdscr.refresh()

            time.sleep(0.1)

        #stdscr.getkey()
 
        for i in range(MIN_NUM, MAX_NUM):

            m =  m - 1

            stdscr.clear()
            stdscr.addstr(n, m, 'X')
            stdscr.refresh()

            time.sleep(0.1)

if __name__ == '__main__':
    curses.wrapper(main)
