import os

def avg(a, b):
	if(b!=0):
		return a/b
	else:
		return 0


subjectNum=0
totalL1Sum=0
totalL2Sum=0
totalL3Sum=0
totalL4Sum=0
totalL5Sum=0
totalL6Sum=0
totalL7Sum=0
totalL8Sum=0
totalL9Sum=0
totalL10Sum=0

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


"""
print("===============================================================================\n")
print("Weak Pre Force Time : 힘의 세기가 weak 도달 이전까지 걸린 시간\n")
print("Middle Pre Force Time : 힘의 세기가 weak이후 middle 도달 이전까지 걸린 시간\n")
print("Strong Pre Force Time : 힘의 세기가 middle이후 strong 도달 이전까지 걸린 시간\n")
print("Sum of Pre Force Time : 위 세 가지 Pre Force Time의 합\n\n")

print("Average Weak Pre Force Time : 목표 힘의 세기가 weak일 때, Weak Pre Force Time의 평균\n")
print("Average Middle Pre Force Time : 목표 힘의 세기가 middle일 때, Middle Pre Force Time의 평균\n")
print("Average Strong Pre Force Time : 목표 힘의 세기가 strong일 때, Strong Pre Force Time의 평균\n")
print("Average Sum of Pre Force Time : 모든 시행에 대한 Pre Force Time의 평균\n")
print("===============================================================================\n\n")
"""

for root, dirs, files in os.walk('.' + os.path.sep):
	for filename in files:
		if (os.path.splitext(filename)[-1]) == '.txt':
			pNum = ((os.path.splitext(filename)[0]).split('_'))[0]
			levelNum = int(((os.path.splitext(filename)[0]).split('_'))[4])
			subjectNum=subjectNum+1
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
						if tempList[0]==pNum:
							firstPreFlag=1
							tryNum=tryNum+1
							print("\nTry # : %d" % (tryNum))
							goalTouchForce=tempList[3]


						if goalTouchForce=="1":
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
									l10Cnt[levelNum-1]=l10Cnt[levelNum-1]+1
									l10PreForceTime=l10PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0

							if tempList[0] == "Touch" and firstPreFlag==1:
								tempPreForceTime = float(tempList[4])
							if tempList[0] == "Pre":
								if firstPreFlag == 0:
									tempPreForceTime=float(tempList[3])
									flag=1
								elif firstPreFlag == 1:
									firstPreFlag =0
									flag=1


							if tempList[0]=="1" and float(tempList[1])>=10:
								if tFlag==0:
									print("Goal Touch Level : %s" % goalTouchForce)

									l1SumWhenL1[levelNum-1] = l1SumWhenL1[levelNum-1] + l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime
									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime))

								tFlag=1


						elif goalTouchForce=="2":

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
									l10Cnt[levelNum-1]=l10Cnt[levelNum-1]+1
									l10PreForceTime=l10PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0

							if tempList[0] == "Touch" and firstPreFlag==1:
								tempPreForceTime = float(tempList[4])
							if tempList[0] == "Pre":
								if firstPreFlag == 0:
									tempPreForceTime=float(tempList[3])
									flag=1
								elif firstPreFlag == 1:
									firstPreFlag =0
									flag=1


							if tempList[0]=="2" and float(tempList[1])>=10:
								if tFlag==0:
									print("Goal Touch Level : %s" % goalTouchForce)


									l2SumWhenL2[levelNum-1] = l2SumWhenL2[levelNum-1] + l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime
									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime))

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
									tempPreForceTime=float(tempList[3])
									flag=1
								elif firstPreFlag == 1:
									firstPreFlag =0
									flag=1


							if tempList[0]=="3" and float(tempList[1])>=10:
								if tFlag==0:
									print("Goal Touch Level : %s" % goalTouchForce)

									
									l3SumWhenL3[levelNum-1] = l3SumWhenL3[levelNum-1] + l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime
									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime))

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
									tempPreForceTime=float(tempList[3])
									flag=1
								elif firstPreFlag == 1:
									firstPreFlag =0
									flag=1


							if tempList[0]=="4" and float(tempList[1])>=10:
								if tFlag==0:
									print("Goal Touch Level : %s" % goalTouchForce)

									
									l4SumWhenL4[levelNum-1] = l4SumWhenL4[levelNum-1] + l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime
									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime))

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
									tempPreForceTime=float(tempList[3])
									flag=1
								elif firstPreFlag == 1:
									firstPreFlag =0
									flag=1


							if tempList[0]=="5" and float(tempList[1])>=10:
								if tFlag==0:
									print("Goal Touch Level : %s" % goalTouchForce)

									
									l5SumWhenL5[levelNum-1] = l5SumWhenL5[levelNum-1] + l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime
									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime))

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
									tempPreForceTime=float(tempList[3])
									flag=1
								elif firstPreFlag == 1:
									firstPreFlag =0
									flag=1


							if tempList[0]=="6" and float(tempList[1])>=10:
								if tFlag==0:
									print("Goal Touch Level : %s" % goalTouchForce)

									
									l6SumWhenL6[levelNum-1] = l6SumWhenL6[levelNum-1] + l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime
									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime))

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
									tempPreForceTime=float(tempList[3])
									flag=1
								elif firstPreFlag == 1:
									firstPreFlag =0
									flag=1


							if tempList[0]=="7" and float(tempList[1])>=10:
								if tFlag==0:
									print("Goal Touch Level : %s" % goalTouchForce)

									
									l7SumWhenL7[levelNum-1] = l7SumWhenL7[levelNum-1] + l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime
									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime))

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
									tempPreForceTime=float(tempList[3])
									flag=1
								elif firstPreFlag == 1:
									firstPreFlag =0
									flag=1


							if tempList[0]=="8" and float(tempList[1])>=10:
								if tFlag==0:
									print("Goal Touch Level : %s" % goalTouchForce)

									
									l8SumWhenL8[levelNum-1] = l8SumWhenL8[levelNum-1] + l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime
									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime))

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
									tempPreForceTime=float(tempList[3])
									flag=1
								elif firstPreFlag == 1:
									firstPreFlag =0
									flag=1


							if tempList[0]=="9" and float(tempList[1])>=10:
								if tFlag==0:
									print("Goal Touch Level : %s" % goalTouchForce)

									
									l9SumWhenL9[levelNum-1] = l9SumWhenL9[levelNum-1] + l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime
									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime))

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
									l10Cnt[levelNum-1]=l10Cnt[levelNum-1]+1
									l10PreForceTime=l10PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0

							if tempList[0] == "Touch" and firstPreFlag==1:
								tempPreForceTime = float(tempList[4])
							if tempList[0] == "Pre":
								if firstPreFlag == 0:
									tempPreForceTime=float(tempList[3])
									flag=1
								elif firstPreFlag == 1:
									firstPreFlag =0
									flag=1


							if tempList[0]=="10" and float(tempList[1])>=10:
								if tFlag==0:
									print("Goal Touch Level : %s" % goalTouchForce)

									
									l10SumWhenL10[levelNum-1] = l10SumWhenL10[levelNum-1] + l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime
									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime))

								tFlag=1


			except Exception as e:
				print(e)

#print("weaksum : %f\n" % weakSum)
#totalCnt=l1Cnt+l2Cnt+l3Cnt+l4Cnt+l5Cnt+l6Cnt+l7Cnt+l8Cnt+l9Cnt+l10Cnt
print("\n\n")
print("===================Result===================")
for i in range(10):
#	print("When Level %i : \nAverage L1 Pre Force Time : %f\nAverage L2 Pre Force Time : %f\nAverage L3 Pre Force Time : %f\nAverage L4 Pre Force Time : %f\nAverage L5 Pre Force Time : %f\nAverage L6 Pre Force Time : %f\nAverage L7 Pre Force Time : %f\nAverage L8 Pre Force Time : %f\nAverage L9 Pre Force Time : %f\nAverage L10 Pre Force Time : %f\nAverage Sum of Pre Force Time : %f"%(i+1, avg(l1SumWhenL1[i], l1Cnt[i]), avg(l2SumWhenL2[i], l2Cnt[i]), avg(l3SumWhenL3[i], l3Cnt[i]), avg(l4SumWhenL4[i], l4Cnt[i]), avg(l5SumWhenL5[i], l5Cnt[i]), avg(l6SumWhenL6[i], l6Cnt[i]), avg(l7SumWhenL7[i], l7Cnt[i]), avg(l8SumWhenL8[i],l8Cnt[i]), avg(l9SumWhenL9[i],l9Cnt[i]), avg(l10SumWhenL10[i],l10Cnt[i]), (totalL1Sum+totalL2Sum+totalL3Sum+totalL4Sum+totalL5Sum+totalL6Sum+totalL7Sum+totalL8Sum+totalL9Sum+totalL10Sum)/totalCnt))
	# print("When Level %i : \nAverage L1 Pre Force Time : %f\nAverage L2 Pre Force Time : %f\nAverage L3 Pre Force Time : %f\nAverage L4 Pre Force Time : %f\nAverage L5 Pre Force Time : %f\nAverage L6 Pre Force Time : %f\nAverage L7 Pre Force Time : %f\nAverage L8 Pre Force Time : %f\nAverage L9 Pre Force Time : %f\nAverage L10 Pre Force Time : %f"%(i+1, avg(l1SumWhenL1[i], l1Cnt[i]), avg(l2SumWhenL2[i], l2Cnt[i]), avg(l3SumWhenL3[i], l3Cnt[i]), avg(l4SumWhenL4[i], l4Cnt[i]), avg(l5SumWhenL5[i], l5Cnt[i]), avg(l6SumWhenL6[i], l6Cnt[i]), avg(l7SumWhenL7[i], l7Cnt[i]), avg(l8SumWhenL8[i],l8Cnt[i]), avg(l9SumWhenL9[i],l9Cnt[i]), avg(l10SumWhenL10[i],l10Cnt[i])))
	print("When Level %i : \nL1 sum when L1 : %i\nL2 sum when L2 : %i\nL3 sum when L3 : %i\nL4 sum when L4 : %i\nL5 sum when L5 : %i\nL6 sum when L6 : %i\nL7 sum when L7 : %i\nL8 sum when L8 : %i\nL9 sum when L9 : %i\nL10 sum when L10 : %i"%(i+1, l1SumWhenL1[i], l2SumWhenL2[i], l3SumWhenL3[i], l4SumWhenL4[i], l5SumWhenL5[i], l6SumWhenL6[i], l7SumWhenL7[i], l8SumWhenL8[i], l9SumWhenL9[i], l10SumWhenL10[i]))
	print("When Level %i : \nL1 Count : %i\nL2 Count : %i\nL3 Count : %i\nL4 Count : %i\nL5 Count : %i\nL6 Count : %i\nL7 Count : %i\nL8 Count : %i\nL9 Count : %i\nL10 Count : %i"%(i+1, l1Cnt[i], l2Cnt[i], l3Cnt[i], l4Cnt[i], l5Cnt[i], l6Cnt[i], l7Cnt[i], l8Cnt[i], l9Cnt[i], l10Cnt[i]))
print("============================================")
