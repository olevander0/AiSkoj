a = [i for i in range(100)]
print(a[::-1])
copies = 25
for i in range(0, len(a), copies):
    print((a[i:i + copies]))
    print(i)
