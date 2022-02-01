#import statements if Required
from sys import *
import psutil
import os
import time
import json
import datetime


#Functions Used in our Script

def Create_Log(strX,listProcess):

	if not os.path.exists(strX):
		try:
			os.mkdir(strX)
		except:
			pass;

  name = datetime.datetime.now()
	Day = (str)(name.day)
	month = (str)(name.month)
	year = (str)(name.year);
	hour = (str)(name.hour);
	minute = (str)(name.minute);
	second = (str)(name.second);

	FileName = ("Create_Log_@"+Day+"-"+month+"-"+year+" "+hour+"-"+minute+"-"+second+".log");

	separator = "-" * 60
	log_path = os.path.join(strX,FileName)
	fd = open(log_path,'w')
	fd.write(separator+"\n\n");
	fd.write("          Abhijit Gadhave's Process Logger\n ");
	fd.write("         Created @ : "+time.ctime()+"\n\n")
	fd.write(separator+"\n\n")

	
	for ele in listProcess:
		fd.write(json.dumps(ele)+"\n")

	Sending_Mail(log_path);


def ProcessDisplay(strX):
	listProcess = []

	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs=['pid','name','username'])
			pinfo["vms"] = proc.memory_info().vms/(1024 * 1024)

			listProcess.append(pinfo);

		except(Exception):
			pass

	Create_Log(strX,listProcess);



#Entry point of Automation Script
def main():
	print("----------------Abhijit Gadhave's Automation Script-----------------")

	print("Script Name : ",argv[0]);
	print("Number of Arguments Accepted : ",len(argv)-1)

	if(len(argv) != 2):
		print("Invalid Number of Arguments")
		exit()

	if(argv[1]=='-u' or argv[1]=='-U'):
		print("Usage : Script is used to provide inforation all current processes which are running in your Machine")
		exit()

	if(argv[1]=='-h' or argv[1]== '-H'):
		print("Help : Name_of_Script Argument");
		print("Argument : Name of the Directory")
		exit()

	ProcessDisplay(argv[1]);


#Starter of Automation Script
if __name__ == "__main__":
	main()
