def multiply(a, b, c, cnt: int = 0):
    if cnt >= b:
        return int(a % c)

    multiply((a * a) % c, b, c, cnt + 1)


if __name__ == '__main__':
    a,b,c = input().split(" ")
    multiply(int(a),int(b),int(c))