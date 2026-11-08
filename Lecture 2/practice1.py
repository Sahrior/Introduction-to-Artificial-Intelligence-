# show the count of each letter

sentence = "I study in UIU";

cnt = {}

for i in sentence:
    if i != " ":
        i = i.lower()
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1

print(cnt)