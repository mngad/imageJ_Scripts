from ij import IJ
import os

# ----------------------------------------------------------------
fileDir = 'F:\\PHD\\HUMAN\\Intact\\Scan_Data\\G17-11_All\\Aligned'
# ----------------------------------------------------------------


def editInImJ(folderF, fileDirF):

    listOfFiles = sorted(os.listdir(fileDirF + "\\" + folder))
    mid_slice = len(listOfFiles)/2

    imp = IJ.run(
        "Image Sequence...",
        "open=[" +
        fileDirF +
        "\\" +
        folderF +
        "\\" +
        listOfFiles[0] +
        "] number=1 starting=" +
        str(mid_slice) +
        " sort")

    print(mid_slice)
    imp = IJ.getImage()
    stats = imp.getStatistics()
    IJ.run(imp, "Histogram", "")
    imp = IJ.getImage()
    IJ.run(imp, "Save", "save=[" + fileDirF +
           "\\Histogram_of_" + listOfFiles[mid_slice] + "]")

    GS = 0
    print(stats.histogram[0:])
    fil = open(fileDirF + "\\" +
               listOfFiles[mid_slice][:-5] + '_histogram.csv', 'w')
    print(fileDirF + "\\" + listOfFiles[mid_slice][:-5] + '_histogram.csv')
    for i in stats.histogram[0:]:
        fil.write(str(GS) + ', ' + str(i) + '\n')
        GS += 1
    fil.close()
    IJ.run("Close")
    IJ.run("Close")

if __name__ == "__main__":

    os.chdir(fileDir)
    # Scan through them separating them.
    listOfFolderNames = sorted(os.listdir(fileDir))
    for folder in listOfFolderNames:
        if not "istogram" in folder:
            editInImJ(folder, fileDir)
