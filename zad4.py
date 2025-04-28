def read(path: str) -> list[(int, int)]:
    data = []
    with open(path, 'r') as file:
        for line in file:
            line_tab = line.strip().split(" ")
            data.append((int(line_tab[0]), int(line_tab[1])))

    return data

def zad1(numbers: list[(int), (int)]) -> (int, int):
    squares = []
    for square in numbers:
        squares.append(square[0] * square[1])
    return min(squares), max(squares)

data = read("prostokaty.txt")
print(zad1(data))