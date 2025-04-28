def read(file: str) -> list[int]:
    with open(file) as f:
        data = f.read()
    data = data.split("\n")
    data = data[:-1]
    data_int = []
    for number in data:
        data_int.append(int(number))
    return data_int

def zad1(number: list[int]) -> (int, int):
    squaeres = [i * i for i in range(100)]
    number_of_squares = 0
    first = -1
    for number in numbers:
        if number in squaeres:
            if first == -1:
                first = number
            number_of_squares += 1

    return number_of_squares, first

def isFirst(number: int) -> bool:
    for i in range(2, number):
        if number % i == 0:
            return False
        return True


numbers = read("liczby.txt")
print(zad1(numbers))