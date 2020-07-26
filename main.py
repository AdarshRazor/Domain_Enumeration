import os
import time
os.system("clear")

cwd = os.getcwd()
DNSdumpster = "./API-dnsdumpster.com/dnsdumpster"
sublist3r = "./Sublist3r"
knock = "./knock-subdomain-scan/knockpy"
Url = "./URLextractor"

#domain = "reva.edu.in"
domain = input("\n\nEnter the domain : ")

"""
print("\n\nTools available : \n\t1. DNSdumpster\n\t2. Sublist3r\n\t3. knock-subdomain-scan\n\t4. URL Extractor")
choice = input("\nEnter your choice (1,2,3 or 4) : ")

if choice == "1":
	os.chdir(DNSdumpster)
	print ("\n\nRunning DNSdumpster....\n")
	os.system("python3 API_example.py %s"%domain)	
elif choice == "2":
	os.chdir(sublist3r)
	print ("\n\nRunning Sublist3r....\n")
	print ("\nPlease wait till complete execution of script....\n")
	os.system("python3 sublist3r.py -d %s"%domain)
elif choice == "3":
	os.chdir(knock)
	print ("\n\nRunning knock-subdomain-scan....\n")
	os.system("python2 knockpy.py %s"%domain)
elif choice == "4":
	os.chdir(Url)
	print("\nRunning Url extractor....\n")
	os.system("./extractor.sh %s"%domain)
else:
	print ("\n\nError!! Wrong input given, please try again!!\n\n")
	exit()
"""

os.system("mkdir ./OUTPUTS/%s"%domain)
output_dir = cwd+"/OUTPUTS/%s"%domain
print ("\n\nPlease wait, the script is running...\n\n")


###DNSDUMPTER
os.chdir(DNSdumpster)
#print ("\n\nRunning DNSdumpster....\n")
os.system("python3 API_example.py %s >> %s/dnsdumpster_%s.txt"%(domain,output_dir,domain))
print ("\nSTEP #1 complete...\n")
#time.sleep(0.5)

###Sublist3r
os.chdir(cwd)
os.chdir(sublist3r)
#print ("\n\nRunning Sublist3r....\n")
os.system("python3 sublist3r.py -d %s >> %s/sublist3r_%s.txt"%(domain,output_dir,domain))
print ("\nSTEP #2 complete...\n")
#time.sleep(0.5)

"""
###knock-subdomain-scan
###Please set-up api key with Virustotal.com to run this.
os.chdir(cwd)
os.chdir(knock)
#print ("\n\nRunning knock-subdomain-scan....\n")
os.system("python2 knockpy.py %s >> %s/knock-subdomain-scan_%s.txt"%(domain,output_dir,domain))
print ("\nSTEP #3 complete...\n")
time.sleep(0.5)
"""

###URLExtractor
os.chdir(cwd)
os.chdir(Url)
#print("\nRunning Url extractor....\n")
os.system("./extractor.sh %s >> %s/URLextractor_%s.txt"%(domain,output_dir,domain))
#os.system("./extractor.sh %s >> %s/URLextractor_%s.txt >/dev/null 2>&1"%(domain,output_dir,domain))
print ("\nSTEP #3 complete...\n")
#time.sleep(0.5)

print ("\n\nExecution complete.\n\n")
print ("The output is stored at %s \n\n"%output_dir)
os.system('xdg-open "%s"' %output_dir)



