import os

subjectNum=0
totalWeakSum=0
totalMiddleSum=0
totalStrongSum=0
weakSumWhenWeak =0
middleSumWhenMiddle=0
strongSumWhenStrong=0
weakCnt=0
middleCnt=0
strongCnt=0
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
					weakPreForceTime=0
					middlePreForceTime=0
					strongPreForceTime=0
					weakSum=0
					middleSum=0
					strongSum=0
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
							weakPreForceTime=0
							middlePreForceTime=0
							strongPreForceTime=0
							weakSum=0
							middleSum=0
							strongSum=0
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

						if touchType=="Weak":
							weakCnt=weakCnt+1
							if flag==1:
								if tempList[0]=="weak_force":
									weakPreForceTime=weakPreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="middle_force":
									middlePreForceTime=middlePreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="strong_force":
									strongPreForceTime=strongPreForceTime+tempPreForceTime
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


							if tempList[0]=="weak_force" and float(tempList[1])>=10:
								if tFlag==0:
									print("Goal Touch Type : %s" % touchType)
									weakSum = weakSum+weakPreForceTime
									totalWeakSum = totalWeakSum+weakSum
									middleSum=middleSum+middlePreForceTime+weakSum
									totalMiddleSum = totalMiddleSum + middleSum
									strongSum=strongSum+strongPreForceTime+middleSum
									totalStrongSum = totalStrongSum + strongSum
									weakSumWhenWeak = weakSumWhenWeak + weakPreForceTime+middlePreForceTime+strongPreForceTime
									print("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakPreForceTime, middlePreForceTime, strongPreForceTime, weakPreForceTime+middlePreForceTime+strongPreForceTime))
									#print("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakSum, middleSum, strongSum, weakSum+middleSum+strongSum))
									# try:
									# 	with open("result.txt", 'a') as wFile:
									# 		wFile.write("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakPreForceTime, middlePreForceTime, strongPreForceTime, weakPreForceTime+middlePreForceTime+strongPreForceTime))
									# except Exception as e:
									# 	print(e)
								tFlag=1


						elif touchType=="Middle":
							middleCnt=middleCnt+1
							if flag==1:
								if tempList[0]=="weak_force":
									weakPreForceTime=weakPreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="middle_force":
									middlePreForceTime=middlePreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="strong_force":
									strongPreForceTime=strongPreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0


							if tempList[0] == "Touch" and firstPreFlag==1:
								tempPreForceTime = float(tempList[4])
							if tempList[0] == "Pre":
								if firstPreFlag == 0:
									tempPreForceTime=tempPreForceTime+float(tempList[3])
									flag=1
								elif firstPreFlag == 1:
									firstPreFlag =0
									flag=1
							if tempList[0]=="middle_force" and float(tempList[1])>=10:
								if tFlag==0:
									print("Goal Touch Type : %s" % touchType)
									weakSum = weakSum+weakPreForceTime
									totalWeakSum = totalWeakSum+weakSum
									middleSum=middleSum+middlePreForceTime+weakSum
									totalMiddleSum = totalMiddleSum + middleSum
									strongSum=strongSum+strongPreForceTime+middleSum
									totalStrongSum = totalStrongSum + strongSum
									middleSumWhenMiddle = middleSumWhenMiddle + weakPreForceTime+middlePreForceTime+strongPreForceTime
									print("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakPreForceTime, middlePreForceTime, strongPreForceTime, weakPreForceTime+middlePreForceTime+strongPreForceTime))
									# print("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakSum, middleSum, strongSum, weakSum+middleSum+strongSum))
									# try:
									# 	with open("result.txt", 'a') as wFile:
									# 		wFile.write("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakPreForceTime, middlePreForceTime, strongPreForceTime, weakPreForceTime+middlePreForceTime+strongPreForceTime))
									# except Exception as e:
									# 	print(e)
								tFlag=1

						elif touchType=="Strong":
							strongCnt=strongCnt+1
							if flag==1:
								if tempList[0]=="weak_force":
									weakPreForceTime=weakPreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="middle_force":
									middlePreForceTime=middlePreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="strong_force":
									strongPreForceTime=strongPreForceTime+tempPreForceTime
									tempPreForceTime=0
									flag=0


							if tempList[0] == "Touch" and firstPreFlag==1:
								tempPreForceTime = float(tempList[4])
							if tempList[0] == "Pre":
								if firstPreFlag == 0:
									tempPreForceTime=tempPreForceTime+float(tempList[3])
									flag=1
								elif firstPreFlag == 1:
									firstPreFlag =0
									flag=1

							if tempList[0]=="strong_force" and float(tempList[1])>=10:
								if tFlag==0:
									print("Goal Touch Type : %s" % touchType)
									weakSum = weakSum+weakPreForceTime
									totalWeakSum = totalWeakSum+weakSum
									middleSum=middleSum+middlePreForceTime+weakSum
									totalMiddleSum = totalMiddleSum + middleSum
									strongSum=strongSum+strongPreForceTime+middleSum
									totalStrongSum = totalStrongSum + strongSum
									strongSumWhenStrong = strongSumWhenStrong + weakPreForceTime+middlePreForceTime+strongPreForceTime
									print("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakPreForceTime, middlePreForceTime, strongPreForceTime, weakPreForceTime+middlePreForceTime+strongPreForceTime))
									# print("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakSum, middleSum, strongSum, weakSum+middleSum+strongSum))
									# try:
									# 	with open("result.txt", 'a') as wFile:
									# 		wFile.write("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakPreForceTime, middlePreForceTime, strongPreForceTime, weakPreForceTime+middlePreForceTime+strongPreForceTime))
									# except Exception as e:
									# 	print(e)
								tFlag=1



			except Exception as e:
				print(e)

#print("weaksum : %f\n" % weakSum)
totalCnt=weakCnt+middleCnt+strongCnt
print("\n\n")
print("===================Result===================")
print("Average Weak Pre Force Time : %f\nAverage Middle Pre Force Time : %f\nAverage Strong Pre Force Time : %f\nAverage Sum of Pre Force Time : %f"%(weakSumWhenWeak/weakCnt, middleSumWhenMiddle/middleCnt, strongSumWhenStrong/strongCnt, (totalWeakSum+totalMiddleSum+totalStrongSum)/totalCnt))
print("============================================")
