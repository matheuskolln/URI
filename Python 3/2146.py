while True:
    try:
        print('{}'.format(int(input()) - 1))
    except EOFError:
        break