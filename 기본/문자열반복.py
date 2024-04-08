def main():
    T = int(input())
    alphas = set("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:")

    while T != 0:
        inputs = input().split(' ')
        R = int(inputs[0]); S = inputs[1]

        str = ''

        for char in S:
            str += (char * R)
        print(str)
        T -= 1


if __name__ == '__main__':
    main()