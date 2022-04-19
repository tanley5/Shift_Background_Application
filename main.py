from fnmatch import fnmatch
import sqlite3
import pickle
import os
from venv import create
import Shift
import threading
import glob
import win32com.client

def create_email_object():
    outlook = win32com.client.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    return mail

if __name__ == '__main__':
    db_string = 'C:/Users/tbench/Documents/django-projects/shiftbid_stuff/Shift_Seniority_Updated/db.sqlite3'
    conn = sqlite3.connect(db_string)
    cur = conn.cursor()
    email = create_email_object()
    if any(os.scandir("./pickle")):
        # If pickle directory is not empty, load the pickle object, run the task, pickle object, and go to sleep
        print("Not Empty")
        for f_name in glob.glob('./pickle/*.pickle'):
            #print(f_name)
            with open(f_name,'rb') as f:
                o = pickle.load(f)
                if o.check_complete(conn,email):
                    print("Report complete")
                else:
                    if o.check_if_updated(conn):
                        print("Updated")
                        o.subsequent_attributes_update(conn,email)
                    else:
                        print("No update")
    else:
        # if pickle directory is empty, create the object from the DB, run the task, pickle the object, and go to sleep
        print("Empty")
        if (conn):
            print("Connected to sqlite3")

            for row in cur.execute('''SELECT report_name FROM shiftbid_shiftbid'''):
                #print(row[0])
                shift = Shift.Shift(row[0])
                #print(shift.report_name)
                shift.initial_attributes_update(conn)
                #print(shift.all_shifts)
                #[print(sh) for sh in shift.all_shifts.iterrows()]
                #[print(row) for row in shift.all_shifts]
                with open(f"./pickle/{shift.report_name}.pickle",'wb') as ob:
                    pickle.dump(shift,ob)
                print(shift.report_name)

    # Initially, create object from database and marshall object and put tasks to sleep
    # get shift_names from sql
    # Subsequently, unmarshall objects and run the file, remarshall object and put task to sleep
    # Loop through the shiftname list and create shift objects, pass the sql connection to the object
    # Trigger a continuos task thread until the shifts are all filled
    # Once all shifts are filled, end the thread by sending an email to me