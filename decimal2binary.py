while True:
    inp = input('Enter a decimal number to convert it to a binary number: ')
    if inp == 'q':
        break

    output = []

    def d2b(n):
        if (n - 128) >= 0:
            n -= 128
            output.append(1)
        else:
            output.append(0)

        if (n - 64) >= 0:
            n -= 64
            output.append(1)
        else:
            output.append(0)

        if (n - 32) >= 0:
            n -= 32
            output.append(1)
        else:
            output.append(0)

        if (n - 16) >= 0:
            n -= 16
            output.append(1)
        else:
            output.append(0)

        if (n - 8) >= 0:
            n -= 8
            output.append(1)
        else:
            output.append(0)

        if (n - 4) >= 0:
            n -= 4
            output.append(1)
        else:
            output.append(0)

        if (n - 2) >= 0:
            n -= 2
            output.append(1)
        else:
            output.append(0)

        if (n - 1) >= 0:
            n -= 1
            output.append(1)
        else:
            output.append(0)


        print(' '.join(str(i) for i in output) + '\n')


    d2b(int(inp))