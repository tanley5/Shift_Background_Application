import sqlite3
import pandas as pd

class Shift:
    def __init__(self, report_name):
        # Initial Constants
        self.report_name = report_name
        self.sent_to_admin = False
        self.complete = False
        # Additional Attributes
        self.all_shifts = None
        self.filled_shifts = None
        self.empty_shifts = None
        self.all_seniotiry = None

    def initial_attributes_update(self,sql_connection):
        # queries to run
        all_shift_query = f"select shift.agent_email, shift.datetime_modified, shift.shift, sb.report_name from shift_shift shift JOIN shiftbid_shiftbid sb on sb.id = shift.report_id WHERE sb.report_name = '{self.report_name}'"
        # filled_shift_query = ""
        # empty_shifts_query = ""
        # all_seniority_query = ""
        # updating the attributes
        self.all_shifts =  pd.read_sql_query(all_shift_query,sql_connection)# sql_cursor.execute(all_shift_query)
        # cls.filled_shifts = cur.execute(filled_shift_query)
        # cls.empty_shifts = cur.execute(empty_shifts_query)
        # cls.all_seniotiry = cur.execute(all_seniority_query)


    @classmethod
    def send_email(cls,email_object):
        email = email_object
        to = cls.current_sent
        fr = "tanley.bench@usanainc.com"
        subject = f"{cls.report_name} Shiftbid"
        # send email
    
    @classmethod
    def send_email_admin(cls,email_object):
        email = email_object
        to = "tanley.bench@usanainc.com"
        fr = "tanley.bench@usanainc.com"
        subject = f"{cls.report_name} Shiftbid Completed"
        #add attachement 
        #send email

    def __str__(self):
        return f"Report: {self.report_name}; Status: {self.complete}"