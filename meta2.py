import os

def avg(a, b):
	if(b!=0):
		return a/b
	else:
		return 0

#totalTrialCnt : 모든 시행 수
totalTrialCnt = 0

#lNSumWhenLN[levelNum-1] : levelNum단계수로 나눈 실험에서 목표값이 N일 때 N의 Pre Force Time 합
l1SumWhenL1=[]
l2SumWhenL2=[]
l3SumWhenL3=[]
l4SumWhenL4=[]
l5SumWhenL5=[]
l6SumWhenL6=[]
l7SumWhenL7=[]
l8SumWhenL8=[]
l9SumWhenL9=[]
l10SumWhenL10=[]
for i in range(10):
	l1SumWhenL1.append(0)
	l2SumWhenL2.append(0)
	l3SumWhenL3.append(0)
	l4SumWhenL4.append(0)
	l5SumWhenL5.append(0)
	l6SumWhenL6.append(0)
	l7SumWhenL7.append(0)
	l8SumWhenL8.append(0)
	l9SumWhenL9.append(0)
	l10SumWhenL10.append(0)


#lNCnt[levelNum-1] : levelNum단계수로 나눈 실험에서 N을 시도한 횟수(모든 피험자의 총합)
l1Cnt=[]
l2Cnt=[]
l3Cnt=[]
l4Cnt=[]
l5Cnt=[]
l6Cnt=[]
l7Cnt=[]
l8Cnt=[]
l9Cnt=[]
l10Cnt=[]
for i in range(10):
	l1Cnt.append(0)
	l2Cnt.append(0)
	l3Cnt.append(0)
	l4Cnt.append(0)
	l5Cnt.append(0)
	l6Cnt.append(0)
	l7Cnt.append(0)
	l8Cnt.append(0)
	l9Cnt.append(0)
	l10Cnt.append(0)

#lNTryCntWhenLN[levelNum-1] : levelNum단계수로 나눈 실험에서 Goal이 N일 때 N단계에 돌입한 횟수
l1TryCntWhenL1=[]
l2TryCntWhenL2=[]
l3TryCntWhenL3=[]
l4TryCntWhenL4=[]
l5TryCntWhenL5=[]
l6TryCntWhenL6=[]
l7TryCntWhenL7=[]
l8TryCntWhenL8=[]
l9TryCntWhenL9=[]
l10TryCntWhenL10=[]
for i in range(10):
	l1TryCntWhenL1.append(0)
	l2TryCntWhenL2.append(0)
	l3TryCntWhenL3.append(0)
	l4TryCntWhenL4.append(0)
	l5TryCntWhenL5.append(0)
	l6TryCntWhenL6.append(0)
	l7TryCntWhenL7.append(0)
	l8TryCntWhenL8.append(0)
	l9TryCntWhenL9.append(0)
	l10TryCntWhenL10.append(0)

#trialCnt[levelNum-1] : levelNum단계수로 나눈 실험에서 Trial 횟수
trialCnt=[]
for i in range(10):
	trialCnt.append(0)


#lNSuccessCntWhenLN[levelNum-1] : levelNum단계수로 나눈 실험에서 Goal이 N일 때 N단계에 돌입하여 목표 시간(default:10초)를 넘긴 횟수
l1SuccessCntWhenL1=[]
l2SuccessCntWhenL2=[]
l3SuccessCntWhenL3=[]
l4SuccessCntWhenL4=[]
l5SuccessCntWhenL5=[]
l6SuccessCntWhenL6=[]
l7SuccessCntWhenL7=[]
l8SuccessCntWhenL8=[]
l9SuccessCntWhenL9=[]
l10SuccessCntWhenL10=[]
for i in range(10):
	l1SuccessCntWhenL1.append(0)
	l2SuccessCntWhenL2.append(0)
	l3SuccessCntWhenL3.append(0)
	l4SuccessCntWhenL4.append(0)
	l5SuccessCntWhenL5.append(0)
	l6SuccessCntWhenL6.append(0)
	l7SuccessCntWhenL7.append(0)
	l8SuccessCntWhenL8.append(0)
	l9SuccessCntWhenL9.append(0)
	l10SuccessCntWhenL10.append(0)


print('''===============================================================================
File Name : 파일이름
Try # : 몇 번째 시행인가를 나타냄
Level N Pre Force Time : 힘의 세기가 Level N-1에서 Level N이 되기 전까지 걸린 시간
Sum of Pre Force Time : Level 1~10 Pre Force Time의 합

Result부분
When Level N : 힘을 N단계로 나눈 시행에서
Average LN Pre Force Time : 주어진 목표값이 Level N일 때 성공하기 전까지 걸린 평균 시간
Average L1~L10 Pre Force Time : 위 값들의 평균
LN Failure Rate : 주어진 목표값이 Level N일 때, 해당 값에 성공하기까지 트라이한 실패율, (Try횟수-성공횟수)/(Try횟수)

※ 모든 Pre Force Time의 합과 관련된 값은 원본 데이터 자체에 Pre Force Time이 제대로 안찍히고
씹혀서 연달아 찍혀 나오는 오류가 있기 때문에 따로 더한 값을 사용함.
즉, L1 Pre Force Time + ... + L2 Pre Force Time <= Sum of Pre Force Time

===============================================================================''')

#sum은 데이터 자체에 Pre Force Time이 데이터가 제대로 안찍히고 씹혀서 연달아 찍혀 나오는 오류가 있기 때문에 따로 더했음.

for root, dirs, files in os.walk('.' + os.path.sep):
	for filename in files:
		if (os.path.splitext(filename)[-1]) == '.txt':
			subjectNum = ((os.path.splitext(filename)[0]).split('_'))[0]
			levelNum = int(((os.path.splitext(filename)[0]).split('_'))[4])
			try:
				with open(filename, 'r') as f:
					print("\n\nFILE NAME : ", filename)

					tryNum=0
					l1PreForceTime=0
					l2PreForceTime=0
					l3PreForceTime=0
					l4PreForceTime=0
					l5PreForceTime=0
					l6PreForceTime=0
					l7PreForceTime=0
					l8PreForceTime=0
					l9PreForceTime=0
					l10PreForceTime=0


					tFlag=0
					flag=0
					firstPreFlag=1
					for line in f:
						if tFlag==1:
							if line!="\n":
								continue
							elif line=="\n":
								tFlag=0
						if line=="\n":
							l1PreForceTime=0
							l2PreForceTime=0
							l3PreForceTime=0
							l4PreForceTime=0
							l5PreForceTime=0
							l6PreForceTime=0
							l7PreForceTime=0
							l8PreForceTime=0
							l9PreForceTime=0
							l10PreForceTime=0


							continue

						tempList=line.split()
						if tempList[0]==subjectNum:
							firstPreFlag=1
							tryNum=tryNum+1
							trialCnt[levelNum-1] = trialCnt[levelNum-1]+1
							totalTrialCnt = totalTrialCnt+1
							print("\nTry # : %d" % (tryNum))
							goalTouchForce=tempList[3]
							preForceSum=0

						if goalTouchForce=="1":
							if flag==1:
								if tempList[0]=="1":
									l1TryCntWhenL1[levelNum-1] = l1TryCntWhenL1[levelNum-1] + 1
									l1Cnt[levelNum-1]=l1Cnt[levelNum-1]+1
									l1PreForceTime=l1PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="2":
									l2Cnt[levelNum-1]=l2Cnt[levelNum-1]+1
									l2PreForceTime=l2PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="3":
									l3Cnt[levelNum-1]=l3Cnt[levelNum-1]+1
									l3PreForceTime=l3PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="4":
									l4Cnt[levelNum-1]=l4Cnt[levelNum-1]+1
									l4PreForceTime=l4PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="5":
									l5Cnt[levelNum-1]=l5Cnt[levelNum-1]+1
									l5PreForceTime=l5PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="6":
									l6Cnt[levelNum-1]=l6Cnt[levelNum-1]+1
									l6PreForceTime=l6PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="7":
									l7Cnt[levelNum-1]=l7Cnt[levelNum-1]+1
									l7PreForceTime=l7PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="8":
									l8Cnt[levelNum-1]=l8Cnt[levelNum-1]+1
									l8PreForceTime=l8PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="9":
									l9Cnt[levelNum-1]=l9Cnt[levelNum-1]+1
									l9PreForceTime=l9PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="10":
									l10Cnt[levelNum-1]=l10Cnt[levelNum-1]+1
									l10PreForceTime=l10PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0

							if tempList[0] == "Touch" and firstPreFlag==1:
								tempPreForceTime = float(tempList[4])
							if tempList[0] == "Pre":

								if firstPreFlag == 0:
									preForceSum = preForceSum + float(tempList[3])
									tempPreForceTime=float(tempList[3])
									flag=1
								elif firstPreFlag == 1:
									firstPreFlag =0
									flag=1


							if tempList[0]=="1" and float(tempList[1])>=10:
								if tFlag==0:
									l1SuccessCntWhenL1[levelNum-1] = l1SuccessCntWhenL1[levelNum-1] + 1
									print("Goal Touch Level : %s" % goalTouchForce)

									l1SumWhenL1[levelNum-1] = l1SumWhenL1[levelNum-1] + preForceSum

									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, preForceSum))

								tFlag=1


						elif goalTouchForce=="2":

							if flag==1:
								if tempList[0]=="1":
									l1Cnt[levelNum-1]=l1Cnt[levelNum-1]+1
									l1PreForceTime=l1PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="2":
									l2TryCntWhenL2[levelNum-1] = l2TryCntWhenL2[levelNum-1] + 1
									l2Cnt[levelNum-1]=l2Cnt[levelNum-1]+1
									l2PreForceTime=l2PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="3":
									l3Cnt[levelNum-1]=l3Cnt[levelNum-1]+1
									l3PreForceTime=l3PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="4":
									l4Cnt[levelNum-1]=l4Cnt[levelNum-1]+1
									l4PreForceTime=l4PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="5":
									l5Cnt[levelNum-1]=l5Cnt[levelNum-1]+1
									l5PreForceTime=l5PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="6":
									l6Cnt[levelNum-1]=l6Cnt[levelNum-1]+1
									l6PreForceTime=l6PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="7":
									l7Cnt[levelNum-1]=l7Cnt[levelNum-1]+1
									l7PreForceTime=l7PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="8":
									l8Cnt[levelNum-1]=l8Cnt[levelNum-1]+1
									l8PreForceTime=l8PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="9":
									l9Cnt[levelNum-1]=l9Cnt[levelNum-1]+1
									l9PreForceTime=l9PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="10":
									l10Cnt[levelNum-1]=l10Cnt[levelNum-1]+1
									l10PreForceTime=l10PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0

							if tempList[0] == "Touch" and firstPreFlag==1:
								tempPreForceTime = float(tempList[4])
							if tempList[0] == "Pre":

								if firstPreFlag == 0:
									preForceSum = preForceSum + float(tempList[3])
									tempPreForceTime=float(tempList[3])
									flag=1
								elif firstPreFlag == 1:
									firstPreFlag =0
									flag=1


							if tempList[0]=="2" and float(tempList[1])>=10:
								if tFlag==0:
									l2SuccessCntWhenL2[levelNum-1] = l2SuccessCntWhenL2[levelNum-1] + 1
									print("Goal Touch Level : %s" % goalTouchForce)


									l2SumWhenL2[levelNum-1] = l2SumWhenL2[levelNum-1] + preForceSum

									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, preForceSum))

								tFlag=1

						elif goalTouchForce=="3": 

							if flag==1:
								if tempList[0]=="1":
									l1Cnt[levelNum-1]=l1Cnt[levelNum-1]+1
									l1PreForceTime=l1PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="2":
									l2Cnt[levelNum-1]=l2Cnt[levelNum-1]+1
									l2PreForceTime=l2PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="3":
									l3TryCntWhenL3[levelNum-1] = l3TryCntWhenL3[levelNum-1] + 1
									l3Cnt[levelNum-1]=l3Cnt[levelNum-1]+1
									l3PreForceTime=l3PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="4":
									l4Cnt[levelNum-1]=l4Cnt[levelNum-1]+1
									l4PreForceTime=l4PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="5":
									l5Cnt[levelNum-1]=l5Cnt[levelNum-1]+1
									l5PreForceTime=l5PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="6":
									l6Cnt[levelNum-1]=l6Cnt[levelNum-1]+1
									l6PreForceTime=l6PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="7":
									l7Cnt[levelNum-1]=l7Cnt[levelNum-1]+1
									l7PreForceTime=l7PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="8":
									l8Cnt[levelNum-1]=l8Cnt[levelNum-1]+1
									l8PreForceTime=l8PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="9":
									l9Cnt[levelNum-1]=l9Cnt[levelNum-1]+1
									l9PreForceTime=l9PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="10":
									l10Cnt[levelNum-1]=l10Cnt[levelNum-1]+1
									l10PreForceTime=l10PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0

							if tempList[0] == "Touch" and firstPreFlag==1:
								tempPreForceTime = float(tempList[4])
							if tempList[0] == "Pre":

								if firstPreFlag == 0:
									preForceSum = preForceSum + float(tempList[3])
									tempPreForceTime=float(tempList[3])
									flag=1
								elif firstPreFlag == 1:
									firstPreFlag =0
									flag=1


							if tempList[0]=="3" and float(tempList[1])>=10:
								if tFlag==0:
									l3SuccessCntWhenL3[levelNum-1] = l3SuccessCntWhenL3[levelNum-1] + 1
									print("Goal Touch Level : %s" % goalTouchForce)

									
									l3SumWhenL3[levelNum-1] = l3SumWhenL3[levelNum-1] + preForceSum
									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, preForceSum))

								tFlag=1
						elif goalTouchForce=="4": 

							if flag==1:
								if tempList[0]=="1":
									l1Cnt[levelNum-1]=l1Cnt[levelNum-1]+1
									l1PreForceTime=l1PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="2":
									l2Cnt[levelNum-1]=l2Cnt[levelNum-1]+1
									l2PreForceTime=l2PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="3":
									l3Cnt[levelNum-1]=l3Cnt[levelNum-1]+1
									l3PreForceTime=l3PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="4":
									l4TryCntWhenL4[levelNum-1] = l4TryCntWhenL4[levelNum-1] + 1
									l4Cnt[levelNum-1]=l4Cnt[levelNum-1]+1
									l4PreForceTime=l4PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="5":
									l5Cnt[levelNum-1]=l5Cnt[levelNum-1]+1
									l5PreForceTime=l5PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="6":
									l6Cnt[levelNum-1]=l6Cnt[levelNum-1]+1
									l6PreForceTime=l6PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="7":
									l7Cnt[levelNum-1]=l7Cnt[levelNum-1]+1
									l7PreForceTime=l7PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="8":
									l8Cnt[levelNum-1]=l8Cnt[levelNum-1]+1
									l8PreForceTime=l8PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="9":
									l9Cnt[levelNum-1]=l9Cnt[levelNum-1]+1
									l9PreForceTime=l9PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="10":
									l10Cnt[levelNum-1]=l10Cnt[levelNum-1]+1
									l10PreForceTime=l10PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0

							if tempList[0] == "Touch" and firstPreFlag==1:
								tempPreForceTime = float(tempList[4])
							if tempList[0] == "Pre":

								if firstPreFlag == 0:
									preForceSum = preForceSum + float(tempList[3])
									tempPreForceTime=float(tempList[3])
									flag=1
								elif firstPreFlag == 1:
									firstPreFlag =0
									flag=1


							if tempList[0]=="4" and float(tempList[1])>=10:
								if tFlag==0:
									l4SuccessCntWhenL4[levelNum-1] = l4SuccessCntWhenL4[levelNum-1]+1
									print("Goal Touch Level : %s" % goalTouchForce)

									
									l4SumWhenL4[levelNum-1] = l4SumWhenL4[levelNum-1] + preForceSum
									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, preForceSum))

								tFlag=1
						elif goalTouchForce=="5": 

							if flag==1:
								if tempList[0]=="1":
									l1Cnt[levelNum-1]=l1Cnt[levelNum-1]+1
									l1PreForceTime=l1PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="2":
									l2Cnt[levelNum-1]=l2Cnt[levelNum-1]+1
									l2PreForceTime=l2PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="3":
									l3Cnt[levelNum-1]=l3Cnt[levelNum-1]+1
									l3PreForceTime=l3PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="4":
									l4Cnt[levelNum-1]=l4Cnt[levelNum-1]+1
									l4PreForceTime=l4PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="5":
									l5TryCntWhenL5[levelNum-1] = l5TryCntWhenL5[levelNum-1]+1
									l5Cnt[levelNum-1]=l5Cnt[levelNum-1]+1
									l5PreForceTime=l5PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="6":
									l6Cnt[levelNum-1]=l6Cnt[levelNum-1]+1
									l6PreForceTime=l6PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="7":
									l7Cnt[levelNum-1]=l7Cnt[levelNum-1]+1
									l7PreForceTime=l7PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="8":
									l8Cnt[levelNum-1]=l8Cnt[levelNum-1]+1
									l8PreForceTime=l8PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="9":
									l9Cnt[levelNum-1]=l9Cnt[levelNum-1]+1
									l9PreForceTime=l9PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="10":
									l10Cnt[levelNum-1]=l10Cnt[levelNum-1]+1
									l10PreForceTime=l10PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0

							if tempList[0] == "Touch" and firstPreFlag==1:
								tempPreForceTime = float(tempList[4])
							if tempList[0] == "Pre":

								if firstPreFlag == 0:
									preForceSum = preForceSum + float(tempList[3])
									tempPreForceTime=float(tempList[3])
									flag=1
								elif firstPreFlag == 1:
									firstPreFlag =0
									flag=1


							if tempList[0]=="5" and float(tempList[1])>=10:
								if tFlag==0:
									l5SuccessCntWhenL5[levelNum-1] = l5SuccessCntWhenL5[levelNum-1]+1
									print("Goal Touch Level : %s" % goalTouchForce)

									
									l5SumWhenL5[levelNum-1] = l5SumWhenL5[levelNum-1] + preForceSum
									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, preForceSum))

								tFlag=1
						elif goalTouchForce=="6": 

							if flag==1:
								if tempList[0]=="1":
									l1Cnt[levelNum-1]=l1Cnt[levelNum-1]+1
									l1PreForceTime=l1PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="2":
									l2Cnt[levelNum-1]=l2Cnt[levelNum-1]+1
									l2PreForceTime=l2PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="3":
									l3Cnt[levelNum-1]=l3Cnt[levelNum-1]+1
									l3PreForceTime=l3PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="4":
									l4Cnt[levelNum-1]=l4Cnt[levelNum-1]+1
									l4PreForceTime=l4PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="5":
									l5Cnt[levelNum-1]=l5Cnt[levelNum-1]+1
									l5PreForceTime=l5PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="6":
									l6TryCntWhenL6[levelNum-1] = l6TryCntWhenL6[levelNum-1]+1
									l6Cnt[levelNum-1]=l6Cnt[levelNum-1]+1
									l6PreForceTime=l6PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="7":
									l7Cnt[levelNum-1]=l7Cnt[levelNum-1]+1
									l7PreForceTime=l7PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="8":
									l8Cnt[levelNum-1]=l8Cnt[levelNum-1]+1
									l8PreForceTime=l8PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="9":
									l9Cnt[levelNum-1]=l9Cnt[levelNum-1]+1
									l9PreForceTime=l9PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="10":
									l10Cnt[levelNum-1]=l10Cnt[levelNum-1]+1
									l10PreForceTime=l10PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0

							if tempList[0] == "Touch" and firstPreFlag==1:
								tempPreForceTime = float(tempList[4])
							if tempList[0] == "Pre":

								if firstPreFlag == 0:
									preForceSum = preForceSum + float(tempList[3])
									tempPreForceTime=float(tempList[3])
									flag=1
								elif firstPreFlag == 1:
									firstPreFlag =0
									flag=1


							if tempList[0]=="6" and float(tempList[1])>=10:
								if tFlag==0:
									l6SuccessCntWhenL6[levelNum-1] = l6SuccessCntWhenL6[levelNum-1]+1
									print("Goal Touch Level : %s" % goalTouchForce)

									
									l6SumWhenL6[levelNum-1] = l6SumWhenL6[levelNum-1] + preForceSum
									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, preForceSum))

								tFlag=1
						elif goalTouchForce=="7": 

							if flag==1:
								if tempList[0]=="1":
									l1Cnt[levelNum-1]=l1Cnt[levelNum-1]+1
									l1PreForceTime=l1PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="2":
									l2Cnt[levelNum-1]=l2Cnt[levelNum-1]+1
									l2PreForceTime=l2PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="3":
									l3Cnt[levelNum-1]=l3Cnt[levelNum-1]+1
									l3PreForceTime=l3PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="4":
									l4Cnt[levelNum-1]=l4Cnt[levelNum-1]+1
									l4PreForceTime=l4PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="5":
									l5Cnt[levelNum-1]=l5Cnt[levelNum-1]+1
									l5PreForceTime=l5PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="6":
									l6Cnt[levelNum-1]=l6Cnt[levelNum-1]+1
									l6PreForceTime=l6PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="7":
									l7TryCntWhenL7[levelNum-1] = l7TryCntWhenL7[levelNum-1]+1
									l7Cnt[levelNum-1]=l7Cnt[levelNum-1]+1
									l7PreForceTime=l7PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="8":
									l8Cnt[levelNum-1]=l8Cnt[levelNum-1]+1
									l8PreForceTime=l8PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="9":
									l9Cnt[levelNum-1]=l9Cnt[levelNum-1]+1
									l9PreForceTime=l9PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="10":
									l10Cnt[levelNum-1]=l10Cnt[levelNum-1]+1
									l10PreForceTime=l10PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0

							if tempList[0] == "Touch" and firstPreFlag==1:
								tempPreForceTime = float(tempList[4])
							if tempList[0] == "Pre":

								if firstPreFlag == 0:
									preForceSum = preForceSum + float(tempList[3])
									tempPreForceTime=float(tempList[3])
									flag=1
								elif firstPreFlag == 1:
									firstPreFlag =0
									flag=1


							if tempList[0]=="7" and float(tempList[1])>=10:
								if tFlag==0:
									l7SuccessCntWhenL7[levelNum-1] = l7SuccessCntWhenL7[levelNum-1]+1
									print("Goal Touch Level : %s" % goalTouchForce)

									
									l7SumWhenL7[levelNum-1] = l7SumWhenL7[levelNum-1] + preForceSum
									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, preForceSum))

								tFlag=1
						elif goalTouchForce=="8": 

							if flag==1:
								if tempList[0]=="1":
									l1Cnt[levelNum-1]=l1Cnt[levelNum-1]+1
									l1PreForceTime=l1PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="2":
									l2Cnt[levelNum-1]=l2Cnt[levelNum-1]+1
									l2PreForceTime=l2PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="3":
									l3Cnt[levelNum-1]=l3Cnt[levelNum-1]+1
									l3PreForceTime=l3PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="4":
									l4Cnt[levelNum-1]=l4Cnt[levelNum-1]+1
									l4PreForceTime=l4PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="5":
									l5Cnt[levelNum-1]=l5Cnt[levelNum-1]+1
									l5PreForceTime=l5PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="6":
									l6Cnt[levelNum-1]=l6Cnt[levelNum-1]+1
									l6PreForceTime=l6PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="7":
									l7Cnt[levelNum-1]=l7Cnt[levelNum-1]+1
									l7PreForceTime=l7PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="8":
									l8TryCntWhenL8[levelNum-1]+l8TryCntWhenL8[levelNum-1]+1
									l8Cnt[levelNum-1]=l8Cnt[levelNum-1]+1
									l8PreForceTime=l8PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="9":
									l9Cnt[levelNum-1]=l9Cnt[levelNum-1]+1
									l9PreForceTime=l9PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="10":
									l10Cnt[levelNum-1]=l10Cnt[levelNum-1]+1
									l10PreForceTime=l10PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0

							if tempList[0] == "Touch" and firstPreFlag==1:
								tempPreForceTime = float(tempList[4])
							if tempList[0] == "Pre":

								if firstPreFlag == 0:
									preForceSum = preForceSum + float(tempList[3])
									tempPreForceTime=float(tempList[3])
									flag=1
								elif firstPreFlag == 1:
									firstPreFlag =0
									flag=1


							if tempList[0]=="8" and float(tempList[1])>=10:
								if tFlag==0:
									l8SuccessCntWhenL8[levelNum-1] = l8SuccessCntWhenL8[levelNum-1]+1
									print("Goal Touch Level : %s" % goalTouchForce)

									
									l8SumWhenL8[levelNum-1] = l8SumWhenL8[levelNum-1] + preForceSum
									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, preForceSum))

								tFlag=1
						elif goalTouchForce=="9": 

							if flag==1:
								if tempList[0]=="1":
									l1Cnt[levelNum-1]=l1Cnt[levelNum-1]+1
									l1PreForceTime=l1PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="2":
									l2Cnt[levelNum-1]=l2Cnt[levelNum-1]+1
									l2PreForceTime=l2PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="3":
									l3Cnt[levelNum-1]=l3Cnt[levelNum-1]+1
									l3PreForceTime=l3PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="4":
									l4Cnt[levelNum-1]=l4Cnt[levelNum-1]+1
									l4PreForceTime=l4PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="5":
									l5Cnt[levelNum-1]=l5Cnt[levelNum-1]+1
									l5PreForceTime=l5PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="6":
									l6Cnt[levelNum-1]=l6Cnt[levelNum-1]+1
									l6PreForceTime=l6PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="7":
									l7Cnt[levelNum-1]=l7Cnt[levelNum-1]+1
									l7PreForceTime=l7PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="8":
									l8Cnt[levelNum-1]=l8Cnt[levelNum-1]+1
									l8PreForceTime=l8PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="9":
									l9TryCntWhenL9[levelNum-1]=l9TryCntWhenL9[levelNum-1]+1
									l9Cnt[levelNum-1]=l9Cnt[levelNum-1]+1
									l9PreForceTime=l9PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="10":
									l10Cnt[levelNum-1]=l10Cnt[levelNum-1]+1
									l10PreForceTime=l10PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0

							if tempList[0] == "Touch" and firstPreFlag==1:
								tempPreForceTime = float(tempList[4])
							if tempList[0] == "Pre":

								if firstPreFlag == 0:
									preForceSum = preForceSum + float(tempList[3])
									tempPreForceTime=float(tempList[3])
									flag=1
								elif firstPreFlag == 1:
									firstPreFlag =0
									flag=1


							if tempList[0]=="9" and float(tempList[1])>=10:
								if tFlag==0:
									l9SuccessCntWhenL9[levelNum-1]=l9SuccessCntWhenL9[levelNum-1]+1
									print("Goal Touch Level : %s" % goalTouchForce)

									
									l9SumWhenL9[levelNum-1] = l9SumWhenL9[levelNum-1] + preForceSum
									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, preForceSum))

								tFlag=1
						elif goalTouchForce=="10": 

							if flag==1:
								if tempList[0]=="1":
									l1Cnt[levelNum-1]=l1Cnt[levelNum-1]+1
									l1PreForceTime=l1PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="2":
									l2Cnt[levelNum-1]=l2Cnt[levelNum-1]+1
									l2PreForceTime=l2PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="3":
									l3Cnt[levelNum-1]=l3Cnt[levelNum-1]+1
									l3PreForceTime=l3PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="4":
									l4Cnt[levelNum-1]=l4Cnt[levelNum-1]+1
									l4PreForceTime=l4PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="5":
									l5Cnt[levelNum-1]=l5Cnt[levelNum-1]+1
									l5PreForceTime=l5PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="6":
									l6Cnt[levelNum-1]=l6Cnt[levelNum-1]+1
									l6PreForceTime=l6PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="7":
									l7Cnt[levelNum-1]=l7Cnt[levelNum-1]+1
									l7PreForceTime=l7PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="8":
									l8Cnt[levelNum-1]=l8Cnt[levelNum-1]+1
									l8PreForceTime=l8PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="9":
									l9Cnt[levelNum-1]=l9Cnt[levelNum-1]+1
									l9PreForceTime=l9PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="10":
									l10TryCntWhenL10[levelNum-1]=l10TryCntWhenL10[levelNum-1]+1
									l10Cnt[levelNum-1]=l10Cnt[levelNum-1]+1
									l10PreForceTime=l10PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0

							if tempList[0] == "Touch" and firstPreFlag==1:
								tempPreForceTime = float(tempList[4])
							if tempList[0] == "Pre":

								if firstPreFlag == 0:
									preForceSum = preForceSum + float(tempList[3])
									tempPreForceTime=float(tempList[3])
									flag=1
								elif firstPreFlag == 1:
									firstPreFlag =0
									flag=1


							if tempList[0]=="10" and float(tempList[1])>=10:
								if tFlag==0:
									l10SuccessCntWhenL10[levelNum-1]=l10SuccessCntWhenL10[levelNum-1]+1
									print("Goal Touch Level : %s" % goalTouchForce)

									
									l10SumWhenL10[levelNum-1] = l10SumWhenL10[levelNum-1] + preForceSum
									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, preForceSum))

								tFlag=1


			except Exception as e:
				print(e)

#totalCnt=l1Cnt+l2Cnt+l3Cnt+l4Cnt+l5Cnt+l6Cnt+l7Cnt+l8Cnt+l9Cnt+l10Cnt
print("\n\n")
print("=============================Result=============================")

for i in range(10):
#	print("When Level %i : \nAverage L1 Pre Force Time : %f\nAverage L2 Pre Force Time : %f\nAverage L3 Pre Force Time : %f\nAverage L4 Pre Force Time : %f\nAverage L5 Pre Force Time : %f\nAverage L6 Pre Force Time : %f\nAverage L7 Pre Force Time : %f\nAverage L8 Pre Force Time : %f\nAverage L9 Pre Force Time : %f\nAverage L10 Pre Force Time : %f\nAverage Sum of Pre Force Time : %f"%(i+1, avg(l1SumWhenL1[i], l1Cnt[i]), avg(l2SumWhenL2[i], l2Cnt[i]), avg(l3SumWhenL3[i], l3Cnt[i]), avg(l4SumWhenL4[i], l4Cnt[i]), avg(l5SumWhenL5[i], l5Cnt[i]), avg(l6SumWhenL6[i], l6Cnt[i]), avg(l7SumWhenL7[i], l7Cnt[i]), avg(l8SumWhenL8[i],l8Cnt[i]), avg(l9SumWhenL9[i],l9Cnt[i]), avg(l10SumWhenL10[i],l10Cnt[i]), (totalL1Sum+totalL2Sum+totalL3Sum+totalL4Sum+totalL5Sum+totalL6Sum+totalL7Sum+totalL8Sum+totalL9Sum+totalL10Sum)/totalCnt))
	if i==0 or i==1:
		continue
	print("\nWhen Level %i : \nAverage L1 Pre Force Time : %f(When goal is L1)\nAverage L2 Pre Force Time : %f(When goal is L2)\nAverage L3 Pre Force Time : %f(When goal is L3)\nAverage L4 Pre Force Time : %f(When goal is L4)\nAverage L5 Pre Force Time : %f(When goal is L5)\nAverage L6 Pre Force Time : %f(When goal is L6)\nAverage L7 Pre Force Time : %f(When goal is L7)\nAverage L8 Pre Force Time : %f(When goal is L8)\nAverage L9 Pre Force Time : %f(When goal is L9)\nAverage L10 Pre Force Time : %f(When goal is L10)\nAverage L1~L10 Pre Force Time : %f"%(i+1, avg(l1SumWhenL1[i], trialCnt[i]), avg(l2SumWhenL2[i], trialCnt[i]), avg(l3SumWhenL3[i], trialCnt[i]), avg(l4SumWhenL4[i], trialCnt[i]), avg(l5SumWhenL5[i], trialCnt[i]), avg(l6SumWhenL6[i], trialCnt[i]), avg(l7SumWhenL7[i], trialCnt[i]), avg(l8SumWhenL8[i],trialCnt[i]), avg(l9SumWhenL9[i],trialCnt[i]), avg(l10SumWhenL10[i],trialCnt[i]),avg(l1SumWhenL1[i]+l2SumWhenL2[i]+l3SumWhenL3[i]+l4SumWhenL4[i]+l5SumWhenL5[i]+l6SumWhenL6[i]+l7SumWhenL7[i]+l8SumWhenL8[i]+l9SumWhenL9[i]+l10SumWhenL10[i],trialCnt[i])))
#	print("\nL1 sum when L1 : %i\nL2 sum when L2 : %i\nL3 sum when L3 : %i\nL4 sum when L4 : %i\nL5 sum when L5 : %i\nL6 sum when L6 : %i\nL7 sum when L7 : %i\nL8 sum when L8 : %i\nL9 sum when L9 : %i\nL10 sum when L10 : %i"%(l1SumWhenL1[i], l2SumWhenL2[i], l3SumWhenL3[i], l4SumWhenL4[i], l5SumWhenL5[i], l6SumWhenL6[i], l7SumWhenL7[i], l8SumWhenL8[i], l9SumWhenL9[i], l10SumWhenL10[i]))
#	print("\nL1 Count : %i\nL2 Count : %i\nL3 Count : %i\nL4 Count : %i\nL5 Count : %i\nL6 Count : %i\nL7 Count : %i\nL8 Count : %i\nL9 Count : %i\nL10 Count : %i"%(l1Cnt[i], l2Cnt[i], l3Cnt[i], l4Cnt[i], l5Cnt[i], l6Cnt[i], l7Cnt[i], l8Cnt[i], l9Cnt[i], l10Cnt[i]))
	print("\nL1 Failure Rate : %f(When goal is L1)\nL2 Failure Rate : %f(When goal is L2)\nL3 Failure Rate : %f(When goal is L3)\nL4 Failure Rate : %f(When goal is L4)\nL5 Failure Rate : %f(When goal is L5)\nL6 Failure Rate : %f(When goal is L6)\nL7 Failure Rate : %f(When goal is L7)\nL8 Failure Rate : %f(When goal is L8)\nL9 Failure Rate : %f(When goal is L9)\nL10 Failure Rate : %f(When goal is L10)\nTotal Failure Rate : %f"%(avg(l1TryCntWhenL1[i]-l1SuccessCntWhenL1[i], l1TryCntWhenL1[i]), avg(l2TryCntWhenL2[i]-l2SuccessCntWhenL2[i], l2TryCntWhenL2[i]), avg(l3TryCntWhenL3[i]-l3SuccessCntWhenL3[i], l3TryCntWhenL3[i]), avg(l4TryCntWhenL4[i]-l4SuccessCntWhenL4[i], l4TryCntWhenL4[i]), avg(l5TryCntWhenL5[i]-l5SuccessCntWhenL5[i], l5TryCntWhenL5[i]), avg(l6TryCntWhenL6[i]-l6SuccessCntWhenL6[i], l6TryCntWhenL6[i]), avg(l7TryCntWhenL7[i]-l7SuccessCntWhenL7[i], l7TryCntWhenL7[i]), avg(l8TryCntWhenL8[i]-l8SuccessCntWhenL8[i],l8TryCntWhenL8[i]), avg(l9TryCntWhenL9[i]-l9SuccessCntWhenL9[i],l9TryCntWhenL9[i]), avg(l10TryCntWhenL10[i]-l10SuccessCntWhenL10[i],l10TryCntWhenL10[i]),avg(l1TryCntWhenL1[i]+l2TryCntWhenL2[i]+l3TryCntWhenL3[i]+l4TryCntWhenL4[i]+l5TryCntWhenL5[i]+l6TryCntWhenL6[i]+l7TryCntWhenL7[i]+l8TryCntWhenL8[i]+l9TryCntWhenL9[i]+l10TryCntWhenL10[i]-l1SuccessCntWhenL1[i]-l2SuccessCntWhenL2[i]-l3SuccessCntWhenL3[i]-l4SuccessCntWhenL4[i]-l5SuccessCntWhenL5[i]-l6SuccessCntWhenL6[i]-l7SuccessCntWhenL7[i]-l8SuccessCntWhenL8[i]-l9SuccessCntWhenL9[i]-l10SuccessCntWhenL10[i], l1TryCntWhenL1[i]+l2TryCntWhenL2[i]+l3TryCntWhenL3[i]+l4TryCntWhenL4[i]+l5TryCntWhenL5[i]+l6TryCntWhenL6[i]+l7TryCntWhenL7[i]+l8TryCntWhenL8[i]+l9TryCntWhenL9[i]+l10TryCntWhenL10[i])))
print("================================================================")

#for debug
#print("totalTrialCnt : %i\n"%(totalTrialCnt))


