import sqlite3
import pickle
import os
import Shift
import threading

if __name__ == '__main__':
    db_name = 'C:/Users/tbench/Documents/django-projects/shiftbid_stuff/Shift_Seniority_Updated/db.sqlite3'
    conn = sqlite3.connect(db_name)
    if any(os.scandir("./pickle")):
        # If pickle directory is not empty, load the pickle object, run the task, pickle object, and go to sleep
        print("Not Empty")
    else:
        # if pickle directory is empty, create the object from the DB, run the task, pickle the object, and go to sleep
        print("Empty")
        if (conn):
            print("Connected to sqlite3")

            cur = conn.cursor()
            for row in cur.execute('''SELECT report_name FROM shiftbid_shiftbid'''):
                #print(row[0])
                shift = Shift.Shift(row[0],conn)
                print(shift.report_name)

    # Initially, create object from database and marshall object and put tasks to sleep
    # get shift_names from sql
    # Subsequently, unmarshall objects and run the file, remarshall object and put task to sleep
    # Loop through the shiftname list and create shift objects, pass the sql connection to the object
    # Trigger a continuos task thread until the shifts are all filled
    # Once all shifts are filled, end the thread by sending an email to me