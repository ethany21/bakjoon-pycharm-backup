import math


def solution(enroll, referral, seller, amount):
    answer = {
        child: 0 for child in enroll
    }

    member = {
        child: parent for child, parent in zip(enroll, referral)
    }

    sell = dict()

    for person, cost in zip(seller, amount):
        if person not in sell:
            sell[person] = cost * 100
        else:
            sell[person] += cost * 100

    for person, cost in zip(seller, amount):

        start = person
        seed = cost * 100

        while start != "-" and seed > 0:
            answer[start] += (seed - seed // 10)
            start = member[start]
            seed //= 10

    return list(answer.values())


if __name__ == "__main__":
    enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
    referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
    seller = ["young", "john", "tod", "emily", "mary"]
    amount = [12, 4, 2, 5, 10]
    print(solution(enroll, referral, seller, amount))
