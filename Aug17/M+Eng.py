math=int(input("whats's your math score?"))
Eng=int(input("what's your eng score?"))

if (math>=0 and math<=100) and (Eng>=0 and Eng<=100):
    if (math>=90) and (Eng>=90):
        print("有獎品!")
    elif(math<60) and (Eng<60):
        print("接受處罰")
    elif math<60 or Eng<60:
        print("加油!")
else:
    print("think befor you type !!!!!!!!")
     
                 


