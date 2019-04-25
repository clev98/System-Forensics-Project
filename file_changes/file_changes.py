from shutil import copy2 as cp
import os
import difflib
import time
import csv

def backup_files(directory, watchfile):
    # make the backup folder
    os.mkdir(directory)

    # copy the files to the backup folder
    openfile = open(watchfile, "r")
    files = openfile.read().strip("\n").split("\n")
    for file in files:
        cp(file, directory)
    openfile.close()

def get_severity(text):
    # find changes involving the word "root"
    root = text.find("root")
    if root != -1:
        return "HIGH"
    else:
        return "MEDIUM"

def log_and_restore(bpath, opath, text):
    # get incident details
    localtime = time.asctime(time.localtime(time.time()))
    formatted_text = text.replace(",", "")
    severity = get_severity(text)

    # log incident details to csv for graph
    with open('graph.csv', 'a', newline='') as graph_file:
        filewriter = csv.writer(graph_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow([localtime, opath, formatted_text, severity])
    graph_file.close()

    # report to console
    print(localtime, "::", opath, "::", formatted_text, "::", severity)

    # restore
    cp(bpath, opath)

def find_differences(directory, watchfile):
    # get the file list
    openfile = open(watchfile, "r")
    files = openfile.read().strip("\n").split("\n")
    openfile.close()

    # loop and check for changes until exit
    try:
        print("Now actively monitoring files for changes... press Ctrl+C to exit.")
        while 1:
            time.sleep(5)   # change check interval
            for file in files:
                # get the old and new file names
                orig_path = file.strip("\n")
                name = orig_path.split("/")[-1]
                backup_path = directory + "/" + name

                # read the files
                backup_file = open(backup_path, "r")
                backup_text = backup_file.read().strip().splitlines()
                backup_file.close()
                orig_file = open(orig_path, "r")
                orig_text = orig_file.read().strip().splitlines()
                orig_file.close()

                # record differences, and restore if found
                d = difflib.Differ().compare(backup_text, orig_text)
                diff_text = "\n".join(d).split("\n")
                for line in diff_text:
                    if line != "" and (line[0] == "+" or line[0] == "-"):
                        log_and_restore(backup_path, orig_path, line)

    # ctrl+c to exit
    except KeyboardInterrupt:
        print("Exiting...")
        pass

def main():

    # get the path of the backup directory and check if it exists
    directory = input("Backup directory location [" + os.getcwd() + "/backup]: ")
    if directory == "":
        directory = r"./backup"
    if os.path.isdir(os.getcwd() + "/backup") is True:
        overwrite = input("Directory already exists. Overwrite? [n]: ")
        if overwrite.lower() == "y" or "yes":
            os.system("rm -rf " + os.getcwd() + "/backup")
        else:
            directory = directory + "1"

    # get the path of the watchfile
    watchfile = "file_changes/watchfiles.txt"

    # create the csv for graphing
    with open('graph.csv', 'w+', newline='') as graph_file:
        filewriter = csv.writer(graph_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['time', 'data changed', 'severity'])
    graph_file.close()

    backup_files(directory, watchfile)
    find_differences(directory, watchfile)

    print('File changes successfully written to log.')
