def solution(cards1, cards2, goal):
    c1 = cards1
    c2 = cards2
    g = goal

    result = []
    goals = []

    while len(g) != 0:
        char = g.pop(0)
        goals.append(char)

        if len(c1) != 0 and c1[0] == char:
            result.append(c1.pop(0))

        if len(c2) != 0 and c2[0] == char:
            result.append(c2.pop(0))
            
    return 'Yes' if result == goals else 'No'

if __name__ == '__main__':
    card1 = ["i", "drink", "water"]
    card2 = ["want", "to"]
    goal = ["i", "want", "to", "drink", "water"]

    r = solution(card1, card2, goal)
    print(r)