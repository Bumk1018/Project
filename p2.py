# 프로젝트 문제 2번
input = ")))()"

def problem2(input):
    # 이 곳에 코드를 작성하세요.

    # 주어진 괄호열이 올바른 괄호열로 복원하기 위해 추가해야 할 '('와 ')'의 최소 개수를 구하는 함수
    def min_add_to_make_valid(s):
        open_needed = 0
        close_needed = 0
        
        for char in s:
            if char == '(':
                close_needed += 1
            elif char == ')':
                if close_needed > 0:
                    close_needed -= 1
                else:
                    open_needed += 1
        
        return open_needed, close_needed
    
    # 올바른 괄호열로 복원하기 위해 추가해야 할 '('와 ')'의 최소 개수 반환
    open_needed, close_needed = min_add_to_make_valid(input)
    
    # 앞과 뒤에 붙여야 할 괄호의 최소 개수를 각각 출력
    print(f"앞에 붙여야 할 '('의 개수: {open_needed}")
    print(f"뒤에 붙여야 할 ')'의 개수: {close_needed}")
    
    return open_needed + close_needed
    
    
    # 입력 힌트
    for char in input:
        print(char)

    result = 0
    return result

result = problem2(input)

assert result == 3
print("정답입니다.")


"""
스택을 사용한 버전입니다.


input = ")))(())"

def problem2(input):
    # 이 곳에 코드를 작성하세요.

    # 주어진 괄호열이 올바른 괄호열로 복원하기 위해 추가해야 할 '('와 ')'의 최소 개수를 구하는 함수
    def min_add_to_make_valid(s):
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(char)
        
        # stack에는 처리되지 못한 '('와 ')'가 남아있음
        open_needed = stack.count('(')
        close_needed = stack.count(')')
        
        return open_needed, close_needed
    
    # 올바른 괄호열로 복원하기 위해 추가해야 할 '('와 ')'의 최소 개수 반환
    open_needed, close_needed = min_add_to_make_valid(input)
    
    # 앞과 뒤에 붙여야 할 괄호의 최소 개수를 각각 출력
    print(f"앞에 붙여야 할 '('의 개수: {close_needed}")
    print(f"뒤에 붙여야 할 ')'의 개수: {open_needed}")
    
    return open_needed + close_needed


result = problem2(input)

assert result == 3
print("정답입니다.")
"""
