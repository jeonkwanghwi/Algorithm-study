import sys

def sol(words):
    # 1) 단어 맨뒤에서부터 확인하면서 감소하는 부분 찾기
    # 2) 다시 단어 맨뒤에서부터 확인하면서 감소하는 부분보다 큰 부분 찾기
    # 3) 둘 위치 바꿔주기
    # 4) 1)의 위치 뒷 부분 정렬

    k = -1 # 오름차순인지 체크하는 변수

    # 단어가 오름차순인지 확인하기
    for i in range(len(words) - 1):
        # 가장 마지막에 오름차순인 인덱스를 k에 저장
        if words[i] < words[i + 1]:
            k = i

    # 만약 문자가 내림차순이면 위 for문에서 if로 안들어가서 k는 그대로 -1일테고
    # 바꿀 수 없으므로 false를 return 하고 주어진 단어를 그대로 출력
    if k == -1:
        return False

    # k는 가장 마지막 오름차순의 인덱스 번호.
    # 맨 뒤에서부터 앞으로 가며 words[k]보다 큰 words[i]를 찾는다.
    # 즉, k로부터 가장 가까운 내림차순인 곳을 찾는다.
    # words[k] < words[i]를 만족하는 i를 발견했으면 tmp에 i를 넣어주고 바로 break
    for i in range(len(words) - 1, -1, -1):
        if words[k] < words[i]:
            tmp = i
            break

    # s[k]와 s[tmp]의 위치를 바꿔준다.
    words[k], words[tmp] = words[tmp], words[k]
    # 그리고 new_word에 s[0 : k+1]까지 넣어준다.
    new_word = words[:k + 1] # 여긴 순서가 더렵혀지지 않은 깨끗한 부분

    # 그리고 뒤에 부분을 정렬해서 new_word에 붙여준다.
    new_word.extend(list(reversed(words[k + 1:])))


    return new_word


t = int(sys.stdin.readline())
for _ in range(t):
    word = input().rstrip()
    answer = sol(list(word))

    if answer:
        print(''.join(answer))
    else:
        print(word)