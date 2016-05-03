import os

subjectNum=0
weakSum=0
middleSum=0
strongSum=0

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
					tFlag=0
					flag=0
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
							continue

						tempList=line.split()

						if tempList[0]==pNum:
							tryNum=tryNum+1
							print("\nTry # : %d" % (tryNum))
							# try:
							# 	with open("result.txt", 'a') as wFile:
							# 		wFile.write("\nTry # : %d" % (tryNum))
							# except Exception as e:
							# 	print(e)
							touchType=tempList[3]

						if touchType=="Weak":
							if flag==1:
								if tempList[0]=="weak_force":
									weakPreForceTime=tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="middle_force":
									middlePreForceTime=tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="strong_force":
									strongPreForceTime=tempPreForceTime
									tempPreForceTime=0
									flag=0

							if tempList[0] == "Pre":
								tempPreForceTime=float(tempList[3])
								flag=1

							if tempList[0]=="weak_force" and float(tempList[1])>=10:
								if tFlag==0:
									print("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakPreForceTime, middlePreForceTime, strongPreForceTime, weakPreForceTime+middlePreForceTime+strongPreForceTime))
									weakSum = weakSum+weakPreForceTime
									middleSum=middleSum+middlePreForceTime
									strongSum=strongSum+strongPreForceTime
									# try:
									# 	with open("result.txt", 'a') as wFile:
									# 		wFile.write("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakPreForceTime, middlePreForceTime, strongPreForceTime, weakPreForceTime+middlePreForceTime+strongPreForceTime))
									# except Exception as e:
									# 	print(e)
								tFlag=1


						elif touchType=="Middle":
							if flag==1:
								if tempList[0]=="weak_force":
									weakPreForceTime=tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="middle_force":
									middlePreForceTime=tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="strong_force":
									strongPreForceTime=tempPreForceTime
									tempPreForceTime=0
									flag=0

							if tempList[0] == "Pre":
								tempPreForceTime=float(tempList[3])
								flag=1

							if tempList[0]=="middle_force" and float(tempList[1])>=10:
								if tFlag==0:
									print("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakPreForceTime, middlePreForceTime, strongPreForceTime, weakPreForceTime+middlePreForceTime+strongPreForceTime))
									weakSum = weakSum+weakPreForceTime
									middleSum=middleSum+middlePreForceTime
									strongSum=strongSum+strongPreForceTime
									# try:
									# 	with open("result.txt", 'a') as wFile:
									# 		wFile.write("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakPreForceTime, middlePreForceTime, strongPreForceTime, weakPreForceTime+middlePreForceTime+strongPreForceTime))
									# except Exception as e:
									# 	print(e)
								tFlag=1

						elif touchType=="Strong":
							if flag==1:
								if tempList[0]=="weak_force":
									weakPreForceTime=tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="middle_force":
									middlePreForceTime=tempPreForceTime
									tempPreForceTime=0
									flag=0
								elif tempList[0]=="strong_force":
									strongPreForceTime=tempPreForceTime
									tempPreForceTime=0
									flag=0

							if tempList[0] == "Pre":
								tempPreForceTime=float(tempList[3])
								flag=1

							if tempList[0]=="strong_force" and float(tempList[1])>=10:
								if tFlag==0:
									print("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakPreForceTime, middlePreForceTime, strongPreForceTime, weakPreForceTime+middlePreForceTime+strongPreForceTime))
									weakSum = weakSum+weakPreForceTime
									middleSum=middleSum+middlePreForceTime
									strongSum=strongSum+strongPreForceTime
									# try:
									# 	with open("result.txt", 'a') as wFile:
									# 		wFile.write("Weak Pre Force Time : %f\nMiddle Pre Force Time : %f\nStrong Pre Force Time : %f\nSum of Pre Force Time : %f"%(weakPreForceTime, middlePreForceTime, strongPreForceTime, weakPreForceTime+middlePreForceTime+strongPreForceTime))
									# except Exception as e:
									# 	print(e)
								tFlag=1



			except Exception as e:
				print(e)

print("weaksum : %f\n" % weakSum)
print("Average Weak Pre Force Time : %f\nAverage Middle Pre Force Time : %f\nAverage Strong Pre Force Time : %f\nAverage Sum of Pre Force Time : %f"%(weakSum/subjectNum, middleSum/subjectNum, strongSum/subjectNum, (weakSum+middleSum+strongSum)/subjectNum))