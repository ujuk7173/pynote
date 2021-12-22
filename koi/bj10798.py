# 세로읽기
s = [input() for i in range(5)]
max_length = len(max(s,key=len))

for i in range(max_length):
    for j in range(len(s)):
        if i >= len(s[j]):
            continue
        else:
            print(s[j][i], end='')
 
# using index
# for i in range(max_length):
#     for word in s:
#         if i >= len(word):
#             continue
#         else:
#             print(word[i], end='')