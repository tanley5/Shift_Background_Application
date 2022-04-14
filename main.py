import sqlite3
import Shift

if __name__ == '__main__':
    db_name = ''
    conn = sqlite3.connect(db_name)
    # get shift_names from sql
    # Loop throught the shiftname list and create shift objects, pass the sql connection to the object
    # Trigger a continuos task thread until the shifts are all filled
    # Once all shifts are filled, end the thread by sending an email to me