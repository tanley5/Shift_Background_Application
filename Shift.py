import sqlite3
import win32com.client

class Shift:
    def __init__(self, report_name, sqlconnection):
        # Initial Constants
        self.report_name = report_name
        self.sql_obj = sqlconnection
        self.iteration = 0
        self.complete = False
        
        # Additional Identities For object
        self.cur = self.create_cursor()
        self.email_object = self.set_email_object()
        self.total_rows = self.get_all_shift_rows()
        self.empty_rows = self.get_empty_rows()
        self.filled_rows = self.get_filled_rows()
        self.current_sent = self.get_current_sent()
        
        
    def create_cursor(self):
        return self.sql_obj.cursor()
    
    def set_email_object(self):
        outlook = win32com.client.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        return mail
    
    def get_all_shift_rows(self):
        query = ''
        return self.cur.execute(query)

    def get_empty_rows(self):
        query = ''
        return self.cur.execute(query)

    def get_filled_rows(self):
        query = ''
        return self.cur.execute(query)

    def get_current_sent(self):
        query = ''
        return self.cur.execute(query)

    def update_obj(self):
        self.set_all_shift_rows()
        self.set_empty_rows()
        self.set_filled_rows()
        self.set_current_sent()
        self.set_iteration()
