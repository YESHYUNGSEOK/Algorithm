from itertools import combinations

L, C = map(int, input().split())
Alphabets = sorted(list(map(str, input().split())))
combs = sorted(list(combinations(Alphabets, L)))
aeiou = 'aeiou'
for comb in combs:
    word, a, b = '', 0, 0
    for alphabet in comb:
        word += alphabet
        if alphabet in aeiou:
            a += 1
        else:
            b += 1
    if a and b >= 2:
        print(word)
