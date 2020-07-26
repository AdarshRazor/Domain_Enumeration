"Domain_Enumeration" 

This script or github project is meant only for LINUX distributions as of now. Tested on KALI LINUX and Ubuntu 18.04


###INSTALLATION###

	1. Unzip the ###Project_name.zip
	2. In your terminal, change directory to ###Project_name. 
	   (probably like: cd ~/Downloads/###Project_name)
	3. Run the following command : "python3 run.py"
	4. That's it, you are good to go.

###RUNNING###

	NOTE : Follow this step only if installation process above is taken care of.

	1. In your terminal, change directory to ###Project_name. 
	   (probably like: cd ~/Downloads/###Project_name)
	2. Run the following command : "python3 main.py"
	3. Enter the website address, try avoiding adding "https" or "www" in the url. Keep it precise,
	   eg : uber.com, microsoft.com, etc.
	4. Wait for the program to execute, it may take a long time depending on the URL (eg: microsoft.com has multiple subdomains so it takes a long time to execute)
	5. The folder containing all the txt files output containing subdomains will pop up.
	
	NOTE : Running the same domain (Eg : microsoft.com), increments the output in the same  txt, i.e., the same txt file is edited again and new output is added to it at the bottom 
	with a time stamp for your reference. It also does not attempt to delete the directory
	(microsoft.com in this example) and again make a new directory. It just uses the existing directory again.

-> NOTE : When you run the main.py file, it usually takes a long time to run "STEP #2" which
          is Sublist3r, please be patient, the code is working fine as long as you don't get errors.

-> NOTE : Please don't delete any folder or files, even the "OUTPUTS" folder which is initially empty.
