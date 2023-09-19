N = int(input().strip())

words = []


for _ in range(0, N):
    word = input()
    words.append(word)

    for word in words:
        s1 = ''
        s2 = ''

    for i in range(0, len(word)):
        if i%2 == 0:
            s1 += word[i]
        else:
            s2 += word[i]
    print('{} {}'.format(s1, s2))