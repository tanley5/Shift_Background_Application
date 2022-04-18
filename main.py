import sqlite3
import pickle
import os
import Shift
import threading

if __name__ == '__main__':
    db_name = ''
    conn = sqlite3.connect(db_name)
    if any(os.scandir("./pickle")):
        # If pickle directory is not empty, load the pickle object, run the task, pickle object, and go to sleep
        print("Not Empty")
    else:
        # if pickle directory is empty, create the object from the DB, run the task, pickle the object, and go to sleep
        print("Empty")
    # Initially, create object from database and marshall object and put tasks to sleep
    # get shift_names from sql
    # Subsequently, unmarshall objects and run the file, remarshall object and put task to sleep
    # Loop through the shiftname list and create shift objects, pass the sql connection to the object
    # Trigger a continuos task thread until the shifts are all filled
    # Once all shifts are filled, end the thread by sending an email to me