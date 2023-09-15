from math import sqrt, floor

def tour(friends, friend_towns, home_to_town_distances):
    distance = 0
    n = [home_to_town_distances[t[1]] for f in friends for t in friend_towns if f == t[0]]
    index = 0
    for i in n:
        if index < len(n) - 1:
            distance += sqrt(round(abs(pow(i,2) - pow(n[index + 1],2))))
            index += 1
    return floor(distance + n[0] + n[-1])