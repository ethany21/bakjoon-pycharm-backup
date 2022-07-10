from itertools import combinations

num = int(input())


def split_into_list(number: int):
    return list(map(lambda x: int(x), list(str(number))))


def separate_number_into_three(number, start, end):
    return count_odd(int(''.join(list(str(number))[0: start])) + int(''.join(list(str(number))[start: end])) + int(
        ''.join(list(str(number))[end:])))


def count_odd(number: int) -> int:
    count = 0
    for i in split_into_list(number):
        if i % 2 == 1:
            count += 1
    return count


def get_odd_num(number: int, count: int):
    if len(str(number)) == 2 or len(str(number)) == 3:
        candidate.append(count)
        return sum(split_into_list(number))

    result = count_odd(number)
    for i in list(combinations([i + 1 for i in range(len(str(number)) - 1)], 2)):
        result += separate_number_into_three(number=number, start=i[0], end=i[1])

    candidate.append(result)


if __name__ == '__main__':
    candidate = []

    get_odd_num(number=num, count=0)
    print(candidate)
