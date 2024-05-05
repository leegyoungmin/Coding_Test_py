def check_all(items):
    for item in items:
        if item != 0:
            return False
    return True

def solution(want, number, discount):
    start_idx = 0
    answer = 0

    while start_idx != len(discount):
        want_dictionary = dict(zip(want, number))

        items = discount[start_idx:start_idx + 10]

        for item in items:
            if want_dictionary.get(item) != None:
                want_dictionary[item] -= 1

        start_idx += 1
        if check_all(want_dictionary.values()):
            answer += 1
        
    return answer

if __name__ == '__main__':
    want = ["apple"]
    number = [10]
    discount = ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]

    r = solution(want, number, discount)
    print(r)