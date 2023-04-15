def statistical(options):
    n = len(options)
    letter_count = [[0] * 26 for _ in range(n)]
    for (ind, text) in enumerate(options):
        for c in text:
            if c.isalpha():
                if ord('a') <= ord(c) <= ord('z'):
                    letter_count[ind][ord(c) - ord('a')] += 1
                elif ord('A') <= ord(c) <= ord('Z'):
                    letter_count[ind][ord(c) - ord('A')] += 1
    inv = [0] * n
    random_order = 'etaoinshrdlcumwfgypbvkxjqz'
    for i in range(n):
        cnt = [(letter_count[i][j], chr(ord('a') + j)) for j in range(26)]
        cnt.sort()
        for j in range(26):
            for k in range(j + 1, 26):
                if cnt[j][0] != cnt[k][0] and random_order.index(cnt[j][1]) < random_order.index(cnt[k][1]):
                    inv[i] += 1
    pos = 0
    for i in range(n):
        if inv[i] < inv[pos]:
            pos = i
    return options[pos]


def dictionary(options):
    pass
        
