# 12~2 겨울 3~5 봄 6~8 여름 9~11 겨울

season = input('월을 입력하세요.')
season1 = season[0:-1]
season2 = int(season1)

if 3<=season2<=5:
    print('봄입니다.')
elif 6<=season2<=8:
    print('여름입니다.')
elif 9<=season2<=11:
    print('가을입니다.')
elif season2 == 12 or 1<= season2 <=2:
    print('겨울입니다.')