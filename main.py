# 24. CAESAR SHIFRI (faqat shifrlash)
text = input()
k = int(input())

res = ""
for c in text:
    res += chr(ord(c) + k)

print(res)
