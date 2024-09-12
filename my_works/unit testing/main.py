def adder():
    n = int(input())
    for _ in range(n):
        x, y = map(int, input().split())
        print(x + y)


if __name__ == "__main__":
    adder()