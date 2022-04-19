import sqlite3


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