notorious=["DARSHAN","ANUJ","ROHIT"]
names=["ANUJ","DARSHAN","ROHIT","JACK","PRIYA","BALA","RAI","RAM","RAJ","BEN"]
SCORE=[2,5,6,8,3,5,6,9,8,2]
for i in range(len(names)):
    if SCORE[i] > 5 and names[i] not in notorious:
        print(names[i],SCORE[i])