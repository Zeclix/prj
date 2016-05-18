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

l1SumWhenL1=0
l2SumWhenL2=0
l3SumWhenL3=0
l4SumWhenL4=0
l5SumWhenL5=0
l6SumWhenL6=0
l7SumWhenL7=0
l8SumWhenL8=0
l9SumWhenL9=0
l10SumWhenL10=0


l1Cnt=0
l2Cnt=0
l3Cnt=0
l4Cnt=0
l5Cnt=0
l6Cnt=0
l7Cnt=0
l8Cnt=0
l9Cnt=0
l10Cnt=0

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
			subjectNum=subjectNum+1
			try:
				with open(filename, 'r') as f:
					print("\n\nFILE NAME : ", filename)
					# try:
					# 	with open("result.txt", 'a') as wFile:
					# 		wFile.write("\n\nFILE NAME : ", filename)
					# except Exception as e:
					# 	print(e)
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

					l1Sum=0
					l2Sum=0
					l3Sum=0
					l4Sum=0
					l5Sum=0
					l6Sum=0
					l7Sum=0
					l8Sum=0
					l9Sum=0
					l10Sum=0

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

							l1Sum=0
							l2Sum=0
							l3Sum=0
							l4Sum=0
							l5Sum=0
							l6Sum=0
							l7Sum=0
							l8Sum=0
							l9Sum=0
							l10Sum=0
							continue

						tempList=line.split()
						if tempList[0]==pNum:
							firstPreFlag=1
							tryNum=tryNum+1
							print("\nTry # : %d" % (tryNum))
							# try:
							# 	with open("result.txt", 'a') as wFile:
							# 		wFile.write("\nTry # : %d" % (tryNum))
							# except Exception as e:
							# 	print(e)
							touchType=tempList[3]

						if touchType=="1":
							l1Cnt=l1Cnt+1
							if flag==1:
								if tempList[0]=="1":
									l1PreForceTime=l1PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="2":
									l2PreForceTime=l2PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="3":
									l3PreForceTime=l3PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="4":
									l4PreForceTime=l4PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="5":
									l5PreForceTime=l5PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="6":
									l6PreForceTime=l6PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="7":
									l7PreForceTime=l7PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="8":
									l8PreForceTime=l8PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="9":
									l9PreForceTime=l9PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="10":
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
									print("Goal Touch Level : %s" % touchType)
									l1Sum = l1Sum+l1PreForceTime
									totalL1Sum = totalL1Sum+l1Sum
									l2Sum = l2Sum+l2PreForceTime
									totalL2Sum = totalL2Sum+l2Sum
									l3Sum = l3Sum+l3PreForceTime
									totalL3Sum = totalL3Sum+l3Sum
									l4Sum = l4Sum+l4PreForceTime
									totalL4Sum = totalL4Sum+l4Sum
									l5Sum = l5Sum+l5PreForceTime
									totalL5Sum = totalL5Sum+l5Sum
									l6Sum = l6Sum+l6PreForceTime
									totalL6Sum = totalL6Sum+l6Sum
									l7Sum = l7Sum+l7PreForceTime
									totalL7Sum = totalL7Sum+l7Sum
									l8Sum = l8Sum+l8PreForceTime
									totalL8Sum = totalL8Sum+l8Sum
									l9Sum = l9Sum+l9PreForceTime
									totalL9Sum = totalL9Sum+l9Sum
									l10Sum = l10Sum+l10PreForceTime
									totalL10Sum = totalL10Sum+l10Sum


									l1SumWhenL1 = l1SumWhenL1 + l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime
									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime))
									#print("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakSum, middleSum, strongSum, weakSum+middleSum+strongSum))
									# try:
									# 	with open("result.txt", 'a') as wFile:
									# 		wFile.write("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakPreForceTime, middlePreForceTime, strongPreForceTime, weakPreForceTime+middlePreForceTime+strongPreForceTime))
									# except Exception as e:
									# 	print(e)
								tFlag=1


						elif touchType=="2":
							l2Cnt=l2Cnt+1
							if flag==1:
								if tempList[0]=="1":
									l1PreForceTime=l1PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="2":
									l2PreForceTime=l2PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="3":
									l3PreForceTime=l3PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="4":
									l4PreForceTime=l4PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="5":
									l5PreForceTime=l5PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="6":
									l6PreForceTime=l6PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="7":
									l7PreForceTime=l7PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="8":
									l8PreForceTime=l8PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="9":
									l9PreForceTime=l9PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="10":
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
									print("Goal Touch Level : %s" % touchType)
									l1Sum = l1Sum+l1PreForceTime
									totalL1Sum = totalL1Sum+l1Sum
									l2Sum = l2Sum+l2PreForceTime
									totalL2Sum = totalL2Sum+l2Sum
									l3Sum = l3Sum+l3PreForceTime
									totalL3Sum = totalL3Sum+l3Sum
									l4Sum = l4Sum+l4PreForceTime
									totalL4Sum = totalL4Sum+l4Sum
									l5Sum = l5Sum+l5PreForceTime
									totalL5Sum = totalL5Sum+l5Sum
									l6Sum = l6Sum+l6PreForceTime
									totalL6Sum = totalL6Sum+l6Sum
									l7Sum = l7Sum+l7PreForceTime
									totalL7Sum = totalL7Sum+l7Sum
									l8Sum = l8Sum+l8PreForceTime
									totalL8Sum = totalL8Sum+l8Sum
									l9Sum = l9Sum+l9PreForceTime
									totalL9Sum = totalL9Sum+l9Sum
									l10Sum = l10Sum+l10PreForceTime
									totalL10Sum = totalL10Sum+l10Sum


									l2SumWhenL2 = l2SumWhenL2 + l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime
									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime))
									#print("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakSum, middleSum, strongSum, weakSum+middleSum+strongSum))
									# try:
									# 	with open("result.txt", 'a') as wFile:
									# 		wFile.write("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakPreForceTime, middlePreForceTime, strongPreForceTime, weakPreForceTime+middlePreForceTime+strongPreForceTime))
									# except Exception as e:
									# 	print(e)
								tFlag=1

						elif touchType=="3": #here
							l3Cnt=l3Cnt+1 #here
							if flag==1:
								if tempList[0]=="1":
									l1PreForceTime=l1PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="2":
									l2PreForceTime=l2PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="3":
									l3PreForceTime=l3PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="4":
									l4PreForceTime=l4PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="5":
									l5PreForceTime=l5PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="6":
									l6PreForceTime=l6PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="7":
									l7PreForceTime=l7PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="8":
									l8PreForceTime=l8PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="9":
									l9PreForceTime=l9PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="10":
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


							if tempList[0]=="3" and float(tempList[1])>=10:#here
								if tFlag==0:
									print("Goal Touch Level : %s" % touchType)
									l1Sum = l1Sum+l1PreForceTime
									totalL1Sum = totalL1Sum+l1Sum
									l2Sum = l2Sum+l2PreForceTime
									totalL2Sum = totalL2Sum+l2Sum
									l3Sum = l3Sum+l3PreForceTime
									totalL3Sum = totalL3Sum+l3Sum
									l4Sum = l4Sum+l4PreForceTime
									totalL4Sum = totalL4Sum+l4Sum
									l5Sum = l5Sum+l5PreForceTime
									totalL5Sum = totalL5Sum+l5Sum
									l6Sum = l6Sum+l6PreForceTime
									totalL6Sum = totalL6Sum+l6Sum
									l7Sum = l7Sum+l7PreForceTime
									totalL7Sum = totalL7Sum+l7Sum
									l8Sum = l8Sum+l8PreForceTime
									totalL8Sum = totalL8Sum+l8Sum
									l9Sum = l9Sum+l9PreForceTime
									totalL9Sum = totalL9Sum+l9Sum
									l10Sum = l10Sum+l10PreForceTime
									totalL10Sum = totalL10Sum+l10Sum

									#here
									l3SumWhenL3 = l3SumWhenL3 + l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime
									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime))
									#print("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakSum, middleSum, strongSum, weakSum+middleSum+strongSum))
									# try:
									# 	with open("result.txt", 'a') as wFile:
									# 		wFile.write("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakPreForceTime, middlePreForceTime, strongPreForceTime, weakPreForceTime+middlePreForceTime+strongPreForceTime))
									# except Exception as e:
									# 	print(e)
								tFlag=1
						elif touchType=="4": #here
							l4Cnt=l4Cnt+1 #here
							if flag==1:
								if tempList[0]=="1":
									l1PreForceTime=l1PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="2":
									l2PreForceTime=l2PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="3":
									l3PreForceTime=l3PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="4":
									l4PreForceTime=l4PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="5":
									l5PreForceTime=l5PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="6":
									l6PreForceTime=l6PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="7":
									l7PreForceTime=l7PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="8":
									l8PreForceTime=l8PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="9":
									l9PreForceTime=l9PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="10":
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


							if tempList[0]=="4" and float(tempList[1])>=10:#here
								if tFlag==0:
									print("Goal Touch Level : %s" % touchType)
									l1Sum = l1Sum+l1PreForceTime
									totalL1Sum = totalL1Sum+l1Sum
									l2Sum = l2Sum+l2PreForceTime
									totalL2Sum = totalL2Sum+l2Sum
									l3Sum = l3Sum+l3PreForceTime
									totalL3Sum = totalL3Sum+l3Sum
									l4Sum = l4Sum+l4PreForceTime
									totalL4Sum = totalL4Sum+l4Sum
									l5Sum = l5Sum+l5PreForceTime
									totalL5Sum = totalL5Sum+l5Sum
									l6Sum = l6Sum+l6PreForceTime
									totalL6Sum = totalL6Sum+l6Sum
									l7Sum = l7Sum+l7PreForceTime
									totalL7Sum = totalL7Sum+l7Sum
									l8Sum = l8Sum+l8PreForceTime
									totalL8Sum = totalL8Sum+l8Sum
									l9Sum = l9Sum+l9PreForceTime
									totalL9Sum = totalL9Sum+l9Sum
									l10Sum = l10Sum+l10PreForceTime
									totalL10Sum = totalL10Sum+l10Sum

									#here
									l4SumWhenL4 = l4SumWhenL4 + l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime
									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime))
									#print("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakSum, middleSum, strongSum, weakSum+middleSum+strongSum))
									# try:
									# 	with open("result.txt", 'a') as wFile:
									# 		wFile.write("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakPreForceTime, middlePreForceTime, strongPreForceTime, weakPreForceTime+middlePreForceTime+strongPreForceTime))
									# except Exception as e:
									# 	print(e)
								tFlag=1
						elif touchType=="5": #here
							l5Cnt=l5Cnt+1 #here
							if flag==1:
								if tempList[0]=="1":
									l1PreForceTime=l1PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="2":
									l2PreForceTime=l2PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="3":
									l3PreForceTime=l3PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="4":
									l4PreForceTime=l4PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="5":
									l5PreForceTime=l5PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="6":
									l6PreForceTime=l6PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="7":
									l7PreForceTime=l7PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="8":
									l8PreForceTime=l8PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="9":
									l9PreForceTime=l9PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="10":
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


							if tempList[0]=="5" and float(tempList[1])>=10:#here
								if tFlag==0:
									print("Goal Touch Level : %s" % touchType)
									l1Sum = l1Sum+l1PreForceTime
									totalL1Sum = totalL1Sum+l1Sum
									l2Sum = l2Sum+l2PreForceTime
									totalL2Sum = totalL2Sum+l2Sum
									l3Sum = l3Sum+l3PreForceTime
									totalL3Sum = totalL3Sum+l3Sum
									l4Sum = l4Sum+l4PreForceTime
									totalL4Sum = totalL4Sum+l4Sum
									l5Sum = l5Sum+l5PreForceTime
									totalL5Sum = totalL5Sum+l5Sum
									l6Sum = l6Sum+l6PreForceTime
									totalL6Sum = totalL6Sum+l6Sum
									l7Sum = l7Sum+l7PreForceTime
									totalL7Sum = totalL7Sum+l7Sum
									l8Sum = l8Sum+l8PreForceTime
									totalL8Sum = totalL8Sum+l8Sum
									l9Sum = l9Sum+l9PreForceTime
									totalL9Sum = totalL9Sum+l9Sum
									l10Sum = l10Sum+l10PreForceTime
									totalL10Sum = totalL10Sum+l10Sum

									#here
									l5SumWhenL5 = l5SumWhenL5 + l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime
									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime))
									#print("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakSum, middleSum, strongSum, weakSum+middleSum+strongSum))
									# try:
									# 	with open("result.txt", 'a') as wFile:
									# 		wFile.write("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakPreForceTime, middlePreForceTime, strongPreForceTime, weakPreForceTime+middlePreForceTime+strongPreForceTime))
									# except Exception as e:
									# 	print(e)
								tFlag=1
						elif touchType=="6": #here
							l6Cnt=l6Cnt+1 #here
							if flag==1:
								if tempList[0]=="1":
									l1PreForceTime=l1PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="2":
									l2PreForceTime=l2PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="3":
									l3PreForceTime=l3PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="4":
									l4PreForceTime=l4PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="5":
									l5PreForceTime=l5PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="6":
									l6PreForceTime=l6PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="7":
									l7PreForceTime=l7PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="8":
									l8PreForceTime=l8PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="9":
									l9PreForceTime=l9PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="10":
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


							if tempList[0]=="6" and float(tempList[1])>=10:#here
								if tFlag==0:
									print("Goal Touch Level : %s" % touchType)
									l1Sum = l1Sum+l1PreForceTime
									totalL1Sum = totalL1Sum+l1Sum
									l2Sum = l2Sum+l2PreForceTime
									totalL2Sum = totalL2Sum+l2Sum
									l3Sum = l3Sum+l3PreForceTime
									totalL3Sum = totalL3Sum+l3Sum
									l4Sum = l4Sum+l4PreForceTime
									totalL4Sum = totalL4Sum+l4Sum
									l5Sum = l5Sum+l5PreForceTime
									totalL5Sum = totalL5Sum+l5Sum
									l6Sum = l6Sum+l6PreForceTime
									totalL6Sum = totalL6Sum+l6Sum
									l7Sum = l7Sum+l7PreForceTime
									totalL7Sum = totalL7Sum+l7Sum
									l8Sum = l8Sum+l8PreForceTime
									totalL8Sum = totalL8Sum+l8Sum
									l9Sum = l9Sum+l9PreForceTime
									totalL9Sum = totalL9Sum+l9Sum
									l10Sum = l10Sum+l10PreForceTime
									totalL10Sum = totalL10Sum+l10Sum

									#here
									l6SumWhenL6 = l6SumWhenL6 + l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime
									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime))
									#print("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakSum, middleSum, strongSum, weakSum+middleSum+strongSum))
									# try:
									# 	with open("result.txt", 'a') as wFile:
									# 		wFile.write("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakPreForceTime, middlePreForceTime, strongPreForceTime, weakPreForceTime+middlePreForceTime+strongPreForceTime))
									# except Exception as e:
									# 	print(e)
								tFlag=1
						elif touchType=="7": #here
							l7Cnt=l7Cnt+1 #here
							if flag==1:
								if tempList[0]=="1":
									l1PreForceTime=l1PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="2":
									l2PreForceTime=l2PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="3":
									l3PreForceTime=l3PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="4":
									l4PreForceTime=l4PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="5":
									l5PreForceTime=l5PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="6":
									l6PreForceTime=l6PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="7":
									l7PreForceTime=l7PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="8":
									l8PreForceTime=l8PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="9":
									l9PreForceTime=l9PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="10":
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


							if tempList[0]=="7" and float(tempList[1])>=10:#here
								if tFlag==0:
									print("Goal Touch Level : %s" % touchType)
									l1Sum = l1Sum+l1PreForceTime
									totalL1Sum = totalL1Sum+l1Sum
									l2Sum = l2Sum+l2PreForceTime
									totalL2Sum = totalL2Sum+l2Sum
									l3Sum = l3Sum+l3PreForceTime
									totalL3Sum = totalL3Sum+l3Sum
									l4Sum = l4Sum+l4PreForceTime
									totalL4Sum = totalL4Sum+l4Sum
									l5Sum = l5Sum+l5PreForceTime
									totalL5Sum = totalL5Sum+l5Sum
									l6Sum = l6Sum+l6PreForceTime
									totalL6Sum = totalL6Sum+l6Sum
									l7Sum = l7Sum+l7PreForceTime
									totalL7Sum = totalL7Sum+l7Sum
									l8Sum = l8Sum+l8PreForceTime
									totalL8Sum = totalL8Sum+l8Sum
									l9Sum = l9Sum+l9PreForceTime
									totalL9Sum = totalL9Sum+l9Sum
									l10Sum = l10Sum+l10PreForceTime
									totalL10Sum = totalL10Sum+l10Sum

									#here
									l7SumWhenL7 = l7SumWhenL7 + l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime
									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime))
									#print("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakSum, middleSum, strongSum, weakSum+middleSum+strongSum))
									# try:
									# 	with open("result.txt", 'a') as wFile:
									# 		wFile.write("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakPreForceTime, middlePreForceTime, strongPreForceTime, weakPreForceTime+middlePreForceTime+strongPreForceTime))
									# except Exception as e:
									# 	print(e)
								tFlag=1
						elif touchType=="9": #here
							l9Cnt=l9Cnt+1 #here
							if flag==1:
								if tempList[0]=="1":
									l1PreForceTime=l1PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="2":
									l2PreForceTime=l2PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="3":
									l3PreForceTime=l3PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="4":
									l4PreForceTime=l4PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="5":
									l5PreForceTime=l5PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="6":
									l6PreForceTime=l6PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="7":
									l7PreForceTime=l7PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="8":
									l8PreForceTime=l8PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="9":
									l9PreForceTime=l9PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="10":
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


							if tempList[0]=="9" and float(tempList[1])>=10:#here
								if tFlag==0:
									print("Goal Touch Level : %s" % touchType)
									l1Sum = l1Sum+l1PreForceTime
									totalL1Sum = totalL1Sum+l1Sum
									l2Sum = l2Sum+l2PreForceTime
									totalL2Sum = totalL2Sum+l2Sum
									l3Sum = l3Sum+l3PreForceTime
									totalL3Sum = totalL3Sum+l3Sum
									l4Sum = l4Sum+l4PreForceTime
									totalL4Sum = totalL4Sum+l4Sum
									l5Sum = l5Sum+l5PreForceTime
									totalL5Sum = totalL5Sum+l5Sum
									l6Sum = l6Sum+l6PreForceTime
									totalL6Sum = totalL6Sum+l6Sum
									l7Sum = l7Sum+l7PreForceTime
									totalL7Sum = totalL7Sum+l7Sum
									l8Sum = l8Sum+l8PreForceTime
									totalL8Sum = totalL8Sum+l8Sum
									l9Sum = l9Sum+l9PreForceTime
									totalL9Sum = totalL9Sum+l9Sum
									l10Sum = l10Sum+l10PreForceTime
									totalL10Sum = totalL10Sum+l10Sum

									#here
									l9SumWhenL9 = l9SumWhenL9 + l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime
									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime))
									#print("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakSum, middleSum, strongSum, weakSum+middleSum+strongSum))
									# try:
									# 	with open("result.txt", 'a') as wFile:
									# 		wFile.write("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakPreForceTime, middlePreForceTime, strongPreForceTime, weakPreForceTime+middlePreForceTime+strongPreForceTime))
									# except Exception as e:
									# 	print(e)
								tFlag=1
						elif touchType=="10": #here
							l10Cnt=l10Cnt+1 #here
							if flag==1:
								if tempList[0]=="1":
									l1PreForceTime=l1PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="2":
									l2PreForceTime=l2PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="3":
									l3PreForceTime=l3PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="4":
									l4PreForceTime=l4PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="5":
									l5PreForceTime=l5PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="6":
									l6PreForceTime=l6PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="7":
									l7PreForceTime=l7PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="8":
									l8PreForceTime=l8PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="9":
									l9PreForceTime=l9PreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="10":
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


							if tempList[0]=="10" and float(tempList[1])>=10:#here
								if tFlag==0:
									print("Goal Touch Level : %s" % touchType)
									l1Sum = l1Sum+l1PreForceTime
									totalL1Sum = totalL1Sum+l1Sum
									l2Sum = l2Sum+l2PreForceTime
									totalL2Sum = totalL2Sum+l2Sum
									l3Sum = l3Sum+l3PreForceTime
									totalL3Sum = totalL3Sum+l3Sum
									l4Sum = l4Sum+l4PreForceTime
									totalL4Sum = totalL4Sum+l4Sum
									l5Sum = l5Sum+l5PreForceTime
									totalL5Sum = totalL5Sum+l5Sum
									l6Sum = l6Sum+l6PreForceTime
									totalL6Sum = totalL6Sum+l6Sum
									l7Sum = l7Sum+l7PreForceTime
									totalL7Sum = totalL7Sum+l7Sum
									l8Sum = l8Sum+l8PreForceTime
									totalL8Sum = totalL8Sum+l8Sum
									l9Sum = l9Sum+l9PreForceTime
									totalL9Sum = totalL9Sum+l9Sum
									l10Sum = l10Sum+l10PreForceTime
									totalL10Sum = totalL10Sum+l10Sum

									#here
									l10SumWhenL10 = l10SumWhenL10 + l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime
									print("Level 1 Pre Force Time : %f\nLevel 2 Pre Force Time : %f\nLevel 3 Pre Force Time : %f\nLevel 4 Pre Force Time : %f\nLevel 5 Pre Force Time : %f\nLevel 6 Pre Force Time : %f\nLevel 7 Pre Force Time : %f\nLevel 8 Pre Force Time : %f\nLevel 9 Pre Force Time : %f\nLevel 10 Pre Force Time : %f\nSum of Pre Force Time : %f"%(l1PreForceTime, l2PreForceTime, l3PreForceTime, l4PreForceTime, l5PreForceTime, l6PreForceTime, l7PreForceTime, l8PreForceTime, l9PreForceTime, l10PreForceTime, l1PreForceTime+l2PreForceTime+l3PreForceTime+l4PreForceTime+l5PreForceTime+l6PreForceTime+l7PreForceTime+l8PreForceTime+l9PreForceTime+l10PreForceTime))
									#print("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakSum, middleSum, strongSum, weakSum+middleSum+strongSum))
									# try:
									# 	with open("result.txt", 'a') as wFile:
									# 		wFile.write("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakPreForceTime, middlePreForceTime, strongPreForceTime, weakPreForceTime+middlePreForceTime+strongPreForceTime))
									# except Exception as e:
									# 	print(e)
								tFlag=1


			except Exception as e:
				print(e)

#print("weaksum : %f\n" % weakSum)
totalCnt=l1Cnt+l2Cnt+l3Cnt+l4Cnt+l5Cnt+l6Cnt+l7Cnt+l8Cnt+l9Cnt+l10Cnt
print("\n\n")
print("===================Result===================")
print("Average L1 Pre Force Time : %f\nAverage L2 Pre Force Time : %f\nAverage L3 Pre Force Time : %f\nAverage L4 Pre Force Time : %f\nAverage L5 Pre Force Time : %f\nAverage L6 Pre Force Time : %f\nAverage L7 Pre Force Time : %f\nAverage L8 Pre Force Time : %f\nAverage L9 Pre Force Time : %f\nAverage L10 Pre Force Time : %f\nAverage Sum of Pre Force Time : %f"%(avg(l1SumWhenL1, l1Cnt), avg(l2SumWhenL2, l2Cnt), avg(l3SumWhenL3, l3Cnt), avg(l4SumWhenL4, l4Cnt), avg(l5SumWhenL5, l5Cnt), avg(l6SumWhenL6, l6Cnt), avg(l7SumWhenL7, l7Cnt), avg(l8SumWhenL8,l8Cnt), avg(l9SumWhenL9,l9Cnt), avg(l10SumWhenL10,l10Cnt), (totalL1Sum+totalL2Sum+totalL3Sum+totalL4Sum+totalL5Sum+totalL6Sum+totalL7Sum+totalL8Sum+totalL9Sum+totalL10Sum)/totalCnt))
print("============================================")

