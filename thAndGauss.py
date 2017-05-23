# Open the image given its path and store it in the variable 'image'
from ij import IJ
import os
import shutil
import time

# ----------------------------------------------------------------
fileDir = 'F:\\PHD\\HUMAN\\Intact\\Scan_Data\\G41-11_All\\Aligned'
thresholds = [22.0, 255.0]
# ----------------------------------------------------------------


def editInImJ(folderF, fileDirF, newFolderNameF):

    listOfFiles = sorted(os.listdir(fileDir + "\\" + folder))

    imp = IJ.run(
        "Image Sequence...",
        "open=[" +
        fileDirF +
        "\\" +
        folderF +
        "\\" +
        listOfFiles[0] +
        "] sort")

    IJ.run(imp, "Gaussian Blur 3D...", "x=1 y=1 z=1")

    # IJ.setAutoThreshold(imp, "Default dark")
    IJ.setThreshold(thresholds[0], thresholds[1])
    IJ.run(imp, "Convert to Mask", "method=Default background=Dark black")
    # IJ.run("Close")
    IJ.run(
        imp,
        "Image Sequence... ",
        "format=TIFF name=" +
        newFolderName +
        " save=" +
        fileDir +
        "_Processed\\")

    IJ.run("Close")


def moveFiles(folderF, fileDirF, newFolderNameF):

    if not os.path.exists(fileDirF + "_Processed"):
        os.makedirs(fileDirF + "_Processed")

    if not os.path.exists(fileDirF + "_Processed\\" + newFolderNameF):
        os.makedirs(fileDirF + "_Processed\\" + newFolderNameF)

    listOfFiles = sorted(os.listdir(fileDirF + "_Processed\\"))
    for files in listOfFiles:
        if newFolderNameF in files:
            if "tif" in files:
                shutil.move(
                    fileDirF +
                    "_Processed\\" +
                    files,
                    fileDirF +
                    "_Processed\\" +
                    newFolderNameF +
                    "\\" +
                    files)


if __name__ == "__main__":

    os.chdir(fileDir)
    # Scan through them separating them.
    listOfFolderNames = sorted(os.listdir(fileDir))
    newFolderName = folder + "_B_W_Gauss_22_"

    for folder in listOfFolderNames:
        editInImJ(folder, fileDir, newFolderName)
        moveFiles(folder, fileDir, newFolderName)
