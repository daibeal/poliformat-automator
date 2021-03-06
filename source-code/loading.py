import time, sys


def print_bar():
    time.sleep(2)
    toolbar_width = 70
    # setup toolbar
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width + 1))  # return to start of line, after '['

    for i in range(toolbar_width):
        time.sleep(0.1)
        # update the bar
        sys.stdout.write("-")
        sys.stdout.flush()

    sys.stdout.write("] - 100%\n")  # this ends the progress bar
