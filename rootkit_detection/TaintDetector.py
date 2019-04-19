import os

# Check a given log file for tainting logs
def readLogFile(log):
	try:
		print((log.split("/"))[3]+":")

		with open(log) as logFile:
			for line in logFile:
				if "taint" in line:
					print(line.strip("\n"))
	except:
		pass

# Iterate the sysfs for taint by checking taint files
def CheckSysFS():
	sysModules = os.listdir("/sys/module")

	print("Checking SysFS:")

	for module in sysModules:
		try:
			with open("/sys/module/"+module+"/taint") as taintFile:
				for line in taintFile:
					if line != "\n":
						print("/sys/module/"+module)
		except:
			continue

if __name__ == "__main__":
	sysLogPath = "/var/log/syslog.1"
	kernLogPath = "/var/log/kern.log"
	dmesgPath = "/var/log/dmesg"

	readLogFile(sysLogPath)
	print()
	readLogFile(kernLogPath)
	print()
	readLogFile(dmesgPath)
	print()
	CheckSysFS()