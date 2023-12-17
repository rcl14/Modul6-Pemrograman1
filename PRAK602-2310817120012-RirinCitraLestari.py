def calculate_zetsu_rooms(n, zetsu):
    result = [zetsu[i] * (i + 1) for i in range(n)]
    print(*result)

def main():
    n = int(input())
    zetsu = list(map(int, input().split()))

    calculate_zetsu_rooms(n, zetsu)

if __name__ == "__main__":
    main()
