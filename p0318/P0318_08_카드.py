class Card: # 4개의 변수 : kind,number,width,height
    width = 0 # 클래스 변수
    height = 0 # 클래스 변수
    kind = ""
    number = ""

    def __init__(self,kind,number):
        self.kind = kind
        self.number = number
        Card.width = 100
        Card.height = 200
    
# # 52장 카드 생성
# shape = ["SPADE","DIAMOND","HEART","CLOVER"]
# number = ["A","2","3","4","5","6","7","8","9","10","11","12","13"]
# card_list = []
# for i in range(4):
#     for j in range(13):
#         c = card_list.append(Card(shape[i],number[j])) # 객체선언
#         card_list.append(c) # 리스트 추가

# for i in range(52):
#     print('카드 출력 : ', card_list[i].shape, card_list[i].number)
        
# 클래스 5개를 생성해서 kind = "spade", number = 1,2,3,4,5
# 클래스를 출력
        
# c1 = Card('spade',"1")
# c2 = Card('spade',"2")
# c3 = Card('spade',"3")
# c4 = Card('spade',"4")
# c5 = Card('spade',"5")

card_list = []
# card_list.append(Card('spade',"A"))
# card_list.append(Card('spade',"2"))
# card_list.append(Card('spade',"3"))
# card_list.append(Card('spade',"4"))
# card_list.append(Card('spade',"5"))
# card_list.append(Card('spade',"6"))
# card_list.append(Card('spade',"7"))
# card_list.append(Card('spade',"8"))
# card_list.append(Card('spade',"9"))
# card_list.append(Card('spade',"10"))
# card_list.append(Card('spade',"J"))
# card_list.append(Card('spade',"Q"))
# card_list.append(Card('spade',"K"))


for i in range(13):
    card_list.append(Card('spade',i+1))

print('리스트 개수 : ', len(card_list))

for i in range(13):
    print('리스트 출력 : ',card_list[i].kind, card_list[i].number)