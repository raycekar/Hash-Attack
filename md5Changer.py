import os
import subprocess
import random
from math import floor


paths = []


def hashAttack(file, path):
    print("Hashing: " + file)
    print("    Old Hash: " + getMd5(path + file))
    hashFile(path + file)
    print("    New Hash: " + getMd5(path + file))


def getMd5(filePath):
    #print("md5sum " + "\"" + filePath + "\"")
    return subprocess.check_output("md5sum " + "\"" + filePath + "\"", shell=True, universal_newlines=True)

def hashFile(filePath):
    rand = floor(random.uniform(11,23))
    cmd = "truncate " + "-s " + "+" + str(rand) + " \"" + filePath + "\""
    #print(cmd)
    subprocess.call(cmd, shell=True)

def startHashing(path):
    root, dirs, files = os.walk(path).__next__()
    for file in files:
        #print(root + "/" + file)
        hashAttack(file, root + "/")
    for dir in dirs:
        startHashing(root + "/" + dir)

for path in paths:
    startHashing(path)