sentence = "this is a common interview question"
result = {}
for x in sentence:
    if x in result:
        result[x] += 1
    else:
        result[x] = 1
print('rsult ', result)

sorted_frq = sorted(result.items(), key=lambda kv: kv[1], reverse=True)

print('final ', sorted_frq[0])
