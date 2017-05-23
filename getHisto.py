from ij import IJ
import os

# ----------------------------------------------------------------
fileDir = 'F:\\PHD\\HUMAN\\Intact\\Scan_Data\\G41-11_All\\Aligned'
thresholds = [22.0, 255.0]
# ----------------------------------------------------------------


def editInImJ(folderF, fileDirF):

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

    print(len(listOfFiles)/2)
    IJ.run(imp, "Histogram", str(len(listOfFiles)/2))
    IJ.run(imp, "Save", "save=["+fileDirF +
           "\\Histogram of "+listOfFiles[0]+".tif]")
    print(fileDirF+"\\Histogram of "+listOfFiles[0])
    IJ.run("Close")
    IJ.run("Close")

if __name__ == "__main__":

    os.chdir(fileDir)
    # Scan through them separating them.
    listOfFolderNames = sorted(os.listdir(fileDir))
    for folder in listOfFolderNames:
        editInImJ(folder, fileDir)
