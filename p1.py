# 프로젝트 문제 1번
input = [10, 40, 30, 60, 30]

def problem1(input):
    # 이곳에 코드를 작성하세요.
    mean = sum(input) // len(input)
    
    input.sort()
    median = input[len(input)//2]
    result = [0,0]
    
    result[0] = mean
    result[1] = median

    print(f"{mean}")
    print(f"{median}")

    return result

result = problem1(input)

assert result == [34, 30]
print("정답입니다.")

"""
stastistics 모듈을 이용한 버전입니다.

import statistics

input = [10, 40, 30, 60, 30]

def problem1(input):
    mean = (statistics.mean(input))
    median = (statistics.median(input))
    result = [0,0]
    
    result[0] = mean
    result[1] = median

    print(f"{mean}")
    print(f"{median}")

    return result

result = problem1(input)

assert result == [34, 30]
print("정답입니다.")
"""