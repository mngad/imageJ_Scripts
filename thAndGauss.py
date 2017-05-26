import os

import shutil

from ij import IJ

# ----------------------------------------------------------------
fileDir = 'F:\\PHD\\HUMAN\\Intact\\Scan_Data\\G41-11_All\\Aligned'
thresholds = [18.0, 255.0]
# ----------------------------------------------------------------


def edit_in_imj(folder_f, file_dir_f, new_folder_name_f):

    list_of_files = sorted(os.listdir(file_dir_f + "\\" + folder_f))

    imp = IJ.run(
        "Image Sequence...",
        "open=[" +
        file_dir_f +
        "\\" +
        folder_f +
        "\\" +
        list_of_files[0] +
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


def move_files(folder_f, file_dir_f, new_folder_name_f):

    if not os.path.exists(file_dir_f + "_Processed"):
        os.makedirs(file_dir_f + "_Processed")

    if not os.path.exists(file_dir_f + "_Processed\\" + new_folder_name_f):
        os.makedirs(file_dir_f + "_Processed\\" + new_folder_name_f)

    list_of_files = sorted(os.listdir(file_dir_f + "_Processed\\"))
    for files in list_of_files:
        if new_folder_name_f in files:
            if "tif" in files:
                shutil.move(
                    file_dir_f +
                    "_Processed\\" +
                    files,
                    file_dir_f +
                    "_Processed\\" +
                    new_folder_name_f +
                    "\\" +
                    files)


if __name__ == "__main__":

    os.chdir(fileDir)
    # Scan through them separating them.
    listOfFolderNames = sorted(os.listdir(fileDir))

    for folder in listOfFolderNames:
        newFolderName = folder + "_B_W_Gauss_" + str(int(thresholds[0])) + "_"
        print(newFolderName[:-1])
        edit_in_imj(folder, fileDir, newFolderName)
        move_files(folder, fileDir, newFolderName)
