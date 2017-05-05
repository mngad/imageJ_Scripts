# Open the image given its path and store it in the variable 'image'
from ij import IJ
import os
import shutil


fileDir = 'F:\PHD\HUMAN\Intact\Scan_Data\G17-11_All\Aligned'

os.chdir(fileDir)
    # Scan through them separating them.
listOfFolderNames = os.listdir(fileDir)
listOfFolderNames.sort()  # Sort alphabetically - important for plotting

for folder in listOfFolderNames:
	
	listOfFiles = os.listdir(fileDir + "\\" + folder)
	listOfFiles.sort()
	imp = IJ.run("Image Sequence...", "open=" + fileDir + "\\" + folder + "\\" + listOfFiles[0] +  " sort")
	#imp = IJ.run("Image Sequence...", "open=F:\\PHD\\HUMAN\\Intact\\Scan_Data\\G17-11_All\\Aligned\\G17-11_L1_aligned\\G17-11_L1_000.tiff number=10 sort")
	IJ.run(imp, "Gaussian Blur 3D...", "x=1 y=1 z=1")
	
	#IJ.setAutoThreshold(imp, "Default dark")
	IJ.setThreshold(22.0, 255.0); 
	IJ.run(imp, "Convert to Mask", "method=Default background=Dark black")
	#IJ.run("Close")
	newFolderName = folder+"_B_W_Gauss_22_"
	IJ.run(imp, "Image Sequence... ", "format=TIFF name="+ newFolderName + " save=" + fileDir + "_Processed\\" );
	
	
	if not os.path.exists(fileDir + "_Processed"):
		os.makedirs(fileDir + "_Processed")
	
	if not os.path.exists(fileDir + "_Processed\\"+newFolderName):
		os.makedirs(fileDir + "_Processed\\"+newFolderName)
    	
	listOfFiles = os.listdir(fileDir + "_Processed\\")
	listOfFiles.sort()
	for files in listOfFiles:
		if newFolderName in files:
			if "tif" in files:
				shutil.move(fileDir + "_Processed\\" + files, fileDir + "_Processed\\" +newFolderName +"\\"+  files) 