# 해보세요
# 1. 숫자 두개를 입력받아서 나누기값, 몫값, 나머지값을 출력
n1 = int(input("첫 번째 숫자를 입력해주세요:  "))
n2 = int(input("두 번째 숫자를 입력해주세요:  "))
print("두 수를 나눈 값은: {} \n몫 값: {} \n두 수를 나누고 나서의 나머지 값: {}".format(n1/n2, n1//n2, n1%n2))


# 2. 3개의 수의 합을 구하세요
s1, s2, s3 = '100', '100.123', '99.9' # 문자열
result = int(s1)+float(s2)+float(s3)

print("세 수의 합은 {} 입니다.".format(result))

