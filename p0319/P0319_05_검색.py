# 검색어가 포함이 되어 있는 모두 검색하는 방법
name = ['홍길동', '유관순', '이순신', '김구', '강감찬', '홍길순', '홍길자']
while True:
    search = input("이름을 입력하세요. : ")
    # 찾은 사람의 위치 저장
    search_list = []
    cnt = 0
    # 검색어로 검색
    for n in name:
        if n.find(search) != -1: # 검색어가 포함이 되어 있는지 확인
            print("찾는 사람이 있습니다. name 리스트 위치 : ", cnt)
            search_list.append(cnt)
        cnt += 1
    if len(search_list) == 0:
        print('찾는 사람이 없습니다.')
    else:
        print(f"{search}(으)로 검색된 사람 : ", end=" ")
        for i in search_list:
            print(name[i], end = " ")
        print()
        print()

# =================내가 한거===================
# name = ['홍길동', '유관순', '이순신', '김구', '강감찬', '홍길순', '홍길자']
# # 찾은 사람의 위치 저장
# search_list = []
# while True:
#     search = input("이름을 입력하세요 : ")
#     latter_list = []
#     for n in name:
#         if search in n:
#             latter_list.append(n)
#     if latter_list:
#         print("찾는 사람이 있습니다. 이름:", ', '.join(latter_list))
#     else:
#         print('찾는 사람이 없습니다.')


# 정확한 이름으로 찾는 방법
# name = ['홍길동','유관순','이순신','김구','강감찬','홍길순','홍길자']

# while True:
#     search = input("이름을 입력하세요 : ")
#     cnt = 0
#     for n in name:
#         if search == n:
#             print("찾는 사람이 있습니다. 위치 : ", cnt)
#             break
#         cnt += 1
#     if cnt >= len(name):
#         print('찾는 사람이 없습니다.')