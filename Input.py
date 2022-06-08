# redefine input
# from sys import exit as Exit

def stdin(s):
    try:
        return input(s)
    except (KeyboardInterrupt, EOFError):       # ctrl + c
        # Exit()
        pass