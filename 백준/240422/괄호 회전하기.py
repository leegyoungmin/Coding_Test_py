# https://school.programmers.co.kr/learn/courses/30/lessons/76502?language=python3
def lotation(s, cnt):
    if cnt == 0:
        return s

    new_santance = s[cnt:] + s[0:cnt]
    return new_santance
def solution(s):
    prefixs = ["[", "{", "("]
    answer = 0

    for i in range(0, len(s)):
        santance = lotation(s, i)
        values = []

        for char in santance:
            if len(values) == 0:
                values.append(char)
            else:
                last = values[-1]
                if last in prefixs:
                    if (last == "[" and char == "]") or (last == "{" and char == "}") or (last == "(" and char == ")"):
                        del values[-1]
                    else:
                        values.append(char)
                else:
                    values.append(char)
        if len(values) == 0:
            answer += 1
    return answer

if __name__ == '__main__':
    input = input()
    a = solution(input)
    print(a)