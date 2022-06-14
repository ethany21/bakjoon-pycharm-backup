length = int(input())

switch = list(map(int, input().split()))
num = int(input())

lst = []

for _ in range(num):
    a, b = input().split()
    lst.append([int(a), int(b)])

if __name__ == '__main__':

    for i in range(num):
        if lst[i][0] == 1:
            for j in range(lst[i][1] - 1, length, lst[i][1]):
                if switch[j] == 1:
                    switch[j] = 0
                elif switch[j] == 0:
                    switch[j] = 1

        elif lst[i][0] == 2:
            stop = False
            distance = 0
            start = lst[i][1] - 1
            while not stop:
                if switch[start - distance] == switch[start + distance]:
                    if switch[start - distance] == 0:
                        switch[start - distance] = 1
                        switch[start + distance] = 1
                    elif switch[start - distance] == 1:
                        switch[start - distance] = 0
                        switch[start + distance] = 0
                    distance += 1
                    if start - distance <= 0 or start + distance > length - 1:
                        break
                else:
                    stop = True

    print(*switch)