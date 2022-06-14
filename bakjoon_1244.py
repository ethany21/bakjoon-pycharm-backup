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

                left = start - distance
                right = start + distance
                if left < 0 or right > length - 1:
                    break

                if switch[left] == switch[right]:
                    if switch[left] == 0:
                        switch[left] = 1
                        switch[right] = 1
                    elif switch[left] == 1:
                        switch[left] = 0
                        switch[right] = 0
                    distance += 1

                else:
                    stop = True

    for i in range(len(switch)):
        print(switch[i], end=' ')
        if (i + 1) % 20 == 0 and i != 1:
            print("")
