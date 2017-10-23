def cpa(win, row, col, st, attr=[]):
    # enable attributes
    for x in attr:
        win.attron(x)
    win.addstr(row, col, st)
    # turn off attributes
    for x in attr:
        win.attroff(x)

def cpac(win, off, st, attr=[]):
    max_y, max_x = win.getmaxyx()
    cpa(win, max_y//2+off, max_x//2 - len(st)//2, st, attr)

def cpabox(win, line, st):
    max_y, max_x = win.getmaxyx()
    row = (max_y * 4)//5
    cpa(win, row-1, 0, "="*max_x)
    cpa(win, row+line, 0 , st)
