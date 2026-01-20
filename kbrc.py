questionLis=[{"question":"who is the father of nation","option":["A.narendra modi","B.Rahul gandhi","c.jacson"],"correctans":"d"},{"question":"who is the father of love","option":["A.gulab","B.ppp","c.haa"],"correctans":"b"}]

x=0
total=0
amountList=[1000,2000]
for q in questionLis:
    print(f"apke samne pesh {x+1} for amount {amountList[x]}:\n",q["question"])
    for option in q["option"]:
        print(option)
    user_input =input("choose your answer from a b c:")
    if (user_input==q["correctans"]):
        total+=amountList[x]
        print("Next question")
        print(total)
        x+=1
    else:
        print(total)
        print("galat")
        break