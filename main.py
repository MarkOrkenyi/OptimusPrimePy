import time


def read_primes():
    primes = []
    with open("primes1000.txt") as f:
        data = f.readlines()
    for number in data:
        primes.append(int(number))
    return primes


def find_primes(limit):
    result = []
    numbers = list(range(1, limit + 1, 2))
    numbers.pop(0)
    numbers.insert(0, 2)
    divider = 3
    while divider * divider < limit:
        for (i, number) in enumerate(numbers):
            if number % divider == 0 and number != divider:
                numbers[i] = False
        divider += 2

    for number in numbers:
        if number is not False:
            result.append(number)

    return result


def main():
    calculated = find_primes(7920)
    stored = read_primes()
    print(calculated == stored)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
