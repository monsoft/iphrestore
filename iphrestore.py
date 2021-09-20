#!/usr/bin/env python3

import sqlite3
import os
import shutil
import argparse


print("iPhone backup pictures extractor v.0.1 (c) 2021 by Irek 'Monsoft' Pelech")
print("")

parser = argparse.ArgumentParser(description='This small script will extract pictures and videos from iPhone backup.')
parser.add_argument('DirWithBackup', metavar='backup_dir', type=str, help='directory where iPhone backup is located')
parser.add_argument('Dir2Restore', metavar='restore_dir', type=str, help='directory to save restored pictures')

args = parser.parse_args()

# get path from class and assign them to variables
backupdir = args.DirWithBackup
backup_restore = args.Dir2Restore

# Variable declaration
picdir = "Media/DCIM"
sqlDB = "Manifest.db"

# Connection to DB

try:
    slqdb_location = os.path.join(backupdir, sqlDB)
    con = sqlite3.connect(slqdb_location)

except sqlite3.OperationalError:
    print("Could not read file:", slqdb_location)
    os._exit(0)

cur = con.cursor()

# Get row in loop
for row in cur.execute('SELECT fileID,relativePath FROM Files WHERE domain="CameraRollDomain" AND relativePath LIKE "%Media/DCIM%" AND relativePath LIKE "%IMG_%"'):
    fileID = row[0]
    filePath = row[1]
    fileDIR = fileID[:2]
    
    dest_dirname, _ = os.path.split(filePath)
    full_dest_dir = os.path.join(backup_restore, dest_dirname)

    # Create destination directory
    os.makedirs(full_dest_dir, exist_ok=True)
    
    # Create system paths to source and destination files
    source_file = os.path.join(backupdir, fileDIR, fileID)
    dest_file = os.path.join(backup_restore, filePath)

    # Copy files
    shutil.copy(source_file, dest_file)
    print('.', end='', flush=True)


con.close()
print("\n", "Job Done !!!")