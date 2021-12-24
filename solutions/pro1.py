# 완주하지 못한선수 -hash
# sol1 -dictionary
def solution(participant,completion):
    d={}
    for x in participant:
        d[x]=d.get(x,0)+1
    for x in completion:
        d[x]-=1
    dnf=[k for k, v in d.items() if v >0]
    answer=dnf[0]
    return answer



# sol2 -sort
def solution2(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]


print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],
["josipa", "filipa", "marina", "nikola"]))