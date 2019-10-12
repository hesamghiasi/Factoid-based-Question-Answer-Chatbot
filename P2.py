# Author : Vaibhaw Raj
# Created on : Sun, Feb 11 2018
# Description : Entry point for Simple Question Answer Chatbot
# Program Argument :
#		datasetName = "Name of dataset text file" eg. "Beyonce.txt"
# Usage :
#		$ python3 P2.py dataset/IPod

print("ربات> در حال بارگذاری وابستگی ها. لطفا صبر کنید")
from DocumentRetrievalModel import DocumentRetrievalModel as DRM
from ProcessedQuestion import ProcessedQuestion as PQ
import re
import sys

if len(sys.argv) == 1:
	try:
		datasetFile = open("./dataset/windows_8.txt","r")
	except FileNotFoundError:
		print("ربات> فایلی یافت نشد")
		exit()
	# print("ربات -> ")
	# print("ربات> Please! Rerun me using following syntax")
	# print("\t\t$ python3 P2.py <datasetName>")
	# print("ربات> You can find dataset name in \"dataset\" folder")
	# print("ربات> Thanks! Bye")
	# exit()
else:
	datasetName = sys.argv[1]
	# Loading Dataset
	try:
		datasetFile = open(datasetName,"r")
	except FileNotFoundError:
		print("ربات> Oops! I am unable to locate \"" + datasetName + "\"")
		exit()

# Retrieving paragraphs : Assumption is that each paragraph in dataset is
# separated by new line character
paragraphs = []
for para in datasetFile.readlines():
	if(len(para.strip()) > 0):
		paragraphs.append(para.strip())

# Processing Paragraphs
drm = DRM(paragraphs,True,True)

print("ربات> Hey! I am ready. Ask me factoid based questions only :P")
print("ربات> You can say me Bye anytime you want")

# Greet Pattern
greetPattern = re.compile("^\ *((hi+)|((good\ )?morning|evening|afternoon)|(he((llo)|y+)))\ *$",re.IGNORECASE)

isActive = True
while isActive:
	userQuery = input("You> ")
	if(not len(userQuery)>0):
		print("ربات> You need to ask something")

	elif greetPattern.findall(userQuery):
		response = "Hello!"
	elif userQuery.strip().lower() == "bye":
		response = "Bye Bye!"
		isActive = False
	else:
		# Proocess Question
		pq = PQ(userQuery,True,False,True)

		# Get Response From Bot
		response =drm.query(pq)
	print("ربات>",response)