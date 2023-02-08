import sys
input = sys.stdin.readline

word = input().rstrip()
result = [''] * len(word)

def sol(arr, start):

    # 모든 문자 탐색 완료한 경우 종료
    if not arr:
        return

    minimum = min(arr) # 가장 작은 값 즉 사전상 가장 앞에 있는 단어를 뜻함
    idx = arr.index(minimum) # 해당 값의 인덱스 번호 추출
    result[start + idx] = minimum
    print("".join(result))

    sol(arr[idx+1:], start+idx+1) # idx의 오른쪽 부분
    sol(arr[:idx], start) # idx의 왼쪽부분

    # 우리가 맨 처음에 찾은 값이 가장 작은 값이기 때문에(ex. A) A의 왼쪽을 탐색하게 되면
    # A의 왼쪽에 값이 와서 사전순이 안돼서, A의 오른쪽을 먼저 탐색하게 됨.

sol(word, 0)