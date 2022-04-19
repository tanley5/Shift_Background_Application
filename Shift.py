import sqlite3
import pandas as pd

class Shift:
    def __init__(self, report_name):
        # Initial Constants
        self.report_name = report_name
        self.sent_to_admin = False
        self.complete = False
        # Additional Attributes
        self.current_seniority = None
        self.all_shifts = None
        self.filled_shifts = None
        self.empty_shifts = None
        self.all_seniority = None

    def initial_attributes_update(self,sql_connection):
        # queries to run
        all_shift_query = f"select shift.agent_email, shift.datetime_modified, shift.shift, sb.report_name from shift_shift shift JOIN shiftbid_shiftbid sb on sb.id = shift.report_id WHERE sb.report_name = '{self.report_name}'"
        filled_shift_query = f"select shift.agent_email, shift.datetime_modified, shift.shift, sb.report_name from shift_shift shift JOIN shiftbid_shiftbid sb on sb.id = shift.report_id WHERE sb.report_name = '{self.report_name}' and shift.agent_email != ''"
        empty_shifts_query = f"select shift.agent_email, shift.datetime_modified, shift.shift, sb.report_name from shift_shift shift JOIN shiftbid_shiftbid sb on sb.id = shift.report_id WHERE sb.report_name = '{self.report_name}' and shift.agent_email = ''"
        all_seniority_query = f"select seniority.agent_net_id, seniority.agent_email, seniority.seniority_number, sb.report_name from seniority_seniority seniority JOIN shiftbid_shiftbid sb on sb.id = seniority.report_id WHERE sb.report_name = '{self.report_name}'"
        current_seniority_query = f" select seniority.agent_net_id, seniority.agent_email, seniority.seniority_number, sb.report_name from seniority_seniority seniority JOIN shiftbid_shiftbid sb on sb.id = seniority.report_id WHERE sb.report_name = '{self.report_name}'	AND seniority.seniority_number = (SELECT min(seniority.seniority_number) from seniority_seniority seniority join shiftbid_shiftbid sb on sb.id = seniority.report_id join shift_shift shift on shift.report_id = sb.id where sb.report_name = '{self.report_name}' AND shift.agent_email = '') "
        # updating the attributes
        self.all_shifts =  pd.read_sql_query(all_shift_query,sql_connection)
        self.filled_shifts = pd.read_sql_query(filled_shift_query,sql_connection)
        self.empty_shifts = pd.read_sql_query(empty_shifts_query,sql_connection)
        self.all_seniority = pd.read_sql_query(all_seniority_query,sql_connection)
        self.current_seniority = pd.read_sql_query(current_seniority_query,sql_connection)
        print(self.all_seniority)

    def check_if_updated(self,sql_connection):
        filled_shift_query = f"select shift.agent_email, shift.datetime_modified, shift.shift, sb.report_name from shift_shift shift JOIN shiftbid_shiftbid sb on sb.id = shift.report_id WHERE sb.report_name = '{self.report_name}' and shift.agent_email != ''"
        empty_shifts_query = f"select shift.agent_email, shift.datetime_modified, shift.shift, sb.report_name from shift_shift shift JOIN shiftbid_shiftbid sb on sb.id = shift.report_id WHERE sb.report_name = '{self.report_name}' and shift.agent_email = ''"

        queried_state_filled_shift = pd.read_sql_query(filled_shift_query,sql_connection)
        queried_state_empty_shift = pd.read_sql_query(empty_shifts_query,sql_connection)

        if len(queried_state_filled_shift) == len(self.filled_shifts) and len(queried_state_empty_shift) == len(self.empty_shifts):
            return False
        else:
            return True
    
    def subsequent_attributes_update(self,sql_connection):
        # queries
        filled_shift_query = f"select shift.agent_email, shift.datetime_modified, shift.shift, sb.report_name from shift_shift shift JOIN shiftbid_shiftbid sb on sb.id = shift.report_id WHERE sb.report_name = '{self.report_name}' and shift.agent_email != ''"
        empty_shifts_query = f"select shift.agent_email, shift.datetime_modified, shift.shift, sb.report_name from shift_shift shift JOIN shiftbid_shiftbid sb on sb.id = shift.report_id WHERE sb.report_name = '{self.report_name}' and shift.agent_email = ''"
        #updating attributes
        self.filled_shifts = pd.read_sql_query(filled_shift_query,sql_connection)
        self.empty_shifts = pd.read_sql_query(empty_shifts_query,sql_connection)

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