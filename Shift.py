import sqlite3
import win32com.client

class Shift:
    def __init__(self, report_name, sql_connection_path):
        # Initial Constants
        self.report_name = report_name
        self.sql_connection_path = sql_connection_path
        self.sent_to_admin = False
        self.complete = False
        
        # Additional Methods For object
        # self.cur = self.create_cursor()
        # self.email_object = self.set_email_object()
        # self.all_rows = self.get_all_shift_rows()
        # self.empty_rows = self.get_empty_rows()
        # self.filled_rows = self.get_filled_rows()
        # self.current_sent = self.get_current_sent()

        # # Additional identifies
        # self.empty_rows_number = len(self.empty_rows)
        # self.filled_rows_number = len(self.filled_rows)
        
        
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

    def send_email(self):
        email = self.email_object
        to = self.current_sent
        fr = "tanley.bench@usanainc.com"
        subject = f"{self.report_name} Shiftbid"
        # send email
    
    def send_email_admin(self):
        email = self.email_object
        to = "tanley.bench@usanainc.com"
        fr = "tanley.bench@usanainc.com"
        subject = f"{self.report_name} Shiftbid Completed"
        #add attachement 
        #send email

    def check_updates(self):
        if self.filled_rows_number == len(self.all_rows):
            self.complete = True
            print(f"Report: {self.report_name}; Status: Complete")
            return False
        else:
            filled_rows = self.get_filled_rows()
            empty_rows = self.get_empty_rows()
            
            if len(filled_rows) != self.filled_rows_number and len(empty_rows) != self.empty_rows_number:
                return True
            else:
                return False
    
    def run_report(self):
        status = self.check_updates()
        if self.sent_to_admin == True:
            pass
        else:
            if self.complete:
                self.send_email_admin()
                self.sent_to_admin = True
            else:
                if status == True:
                    self.update_object()
                    self.send_email()
                else:
                    pass
