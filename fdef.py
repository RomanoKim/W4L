# Curses functions
# print with attributes
def cpa(win, row, col, st, attr=[]):
    # enable attributes
    for x in attr:
        win.attron(x)
    win.addstr(row, col, st)
    # turn off attributes
    for x in attr:
        win.attroff(x)

# print centered, at vertical offset with attributes
def cpac(win, off, st, attr=[]):
    max_y, max_x = win.getmaxyx()
    cpa(win, max_y//2+off, max_x//2 - len(st)//2, st, attr)


# print at bottom 20% of screen with divider
def cpabox(win, strs=[]):
    max_y, max_x = win.getmaxyx()
    row = (max_y * 4)//5
    cpa(win, row-1, 0, "="*max_x)
    for x in strs:
        cpa(win, row, 0 , x)
        row += 1
