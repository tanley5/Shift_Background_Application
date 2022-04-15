import sqlite3
import win32com.client

class Shift:
    def __init__(self, report_name, sqlconnection):
        # Initial Constants
        self.report_name = report_name
        self.sql_obj = sqlconnection
        self.iteration = 0
        self.complete = False
        
        # Additional Methods For object
        self.cur = self.create_cursor()
        self.email_object = self.set_email_object()
        self.all_rows = self.get_all_shift_rows()
        self.empty_rows = self.get_empty_rows()
        self.filled_rows = self.get_filled_rows()
        self.current_sent = self.get_current_sent()

        # Additional identifies
        self.empty_rows_number = len(self.empty_rows)
        self.filled_rows_number = len(self.filled_rows)
        
        
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

    def set_all_shift_rows(self):
        self.all_rows = self.get_all_shift_rows()
    
    def set_empty_rows(self):
        self.empty_rows = self.get_empty_rows()
    
    def set_filled_rows(self):
        self.filled_rows = self.get_filled_rows()

    def set_current_sent(self):
        self.current_sent = self.get_current_sent()

    def update_object(self):
        self.set_all_shift_rows()
        self.set_empty_rows()
        self.set_empty_rows()
        self.set_filled_rows()
        self.set_current_sent()

    # def check_updates(self):

    #     if len(self.filled_rows) == len(self.all_rows):
    #         self.complete = True
    #         print(f"Report Name: {self.report_name}; Status: Complete")
    #     elif len(self.empty_rows) != self.empty_rows_number:
    #         self.set_filled_rows()
    #         self.empty_rows_number = len(self.empty_rows)
    #         print(f"Report Name: {self.report_name}; Status: Updated")
        