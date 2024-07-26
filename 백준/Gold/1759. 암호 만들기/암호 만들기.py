from sys import stdin

input = stdin.readline

# 암호의 길이 L, 사용할 문자 개수 C 입력 받기
L, C = map(int, input().split())

# 사용할 문자들을 입력받아 사전 순으로 정렬
chars = sorted(input().split())

# 모음 집합 정의
vowels = set('aeiou')

def is_valid(password):
    """
    주어진 password가 유효한지 검사하는 함수
    조건:
    - 최소 1개의 모음 포함
    - 최소 2개의 자음 포함
    """
    # password에서 모음의 개수 세기
    num_vowels = sum(1 for char in password if char in vowels)
    # 전체 길이에서 모음의 개수를 뺀 것이 자음의 개수
    num_consonants = len(password) - num_vowels
    # 모음이 최소 1개 이상이고 자음이 최소 2개 이상인지 확인
    return num_vowels >= 1 and num_consonants >= 2

def backtrack(start, password):
    """
    백트래킹을 이용하여 가능한 모든 암호를 생성하는 함수
    """
    # 현재 password의 길이가 L과 같아지면
    if len(password) == L:
        # password가 유효한지 검사하여 유효하면 출력
        if is_valid(password):
            print(''.join(password))
        return
    
    # start부터 C까지 반복하여 다음 문자를 선택
    for i in range(start, C):
        # 다음 문자를 선택하여 password에 추가하고 재귀 호출
        backtrack(i + 1, password + [chars[i]])

# 백트래킹 시작: 처음에는 빈 password와 0번 인덱스부터 시작
backtrack(0, [])
