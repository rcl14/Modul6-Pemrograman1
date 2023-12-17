def create_matrix(rows, cols, values):
    matrix = [values[i * cols:(i + 1) * cols] for i in range(rows)]
    return matrix

def main():
    rows, cols = map(int, input().split())
    values = list(map(int, input().split()))
    matrix = create_matrix(rows, cols, values)

    for row in matrix:
        print(*row)

if __name__ == "__main__":
    main()
