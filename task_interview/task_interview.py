class Stack:

    def __init__(self) -> None:
        self.list_ = []

    def is_empty(self) -> bool:
        if self.list_:
            return False
        else: 
            return True

    def push(self, item: any) -> None:
        self.list_.append(item)

    def pop(self) -> list[any] | str:
        if self.is_empty() == False:
            return self.list_.pop()
        else:
            return 'Stack is empty'
    
    def peek(self) -> list[any] | str:
        if self.is_empty() == False:
            return self.list_[-1]
        else:
            return 'Stack is empty'
        
    def size(self) -> int:
        return len(self.list_)
  
# if __name__ == '__main__':
#     stack = Stack()
#     print(stack.is_empty())
#     print(stack.pop())
#     stack.push('gog')
#     print(stack.peek())
#     print(stack.size())
#     print(stack.pop())
#     print(stack.peek())
#     print(stack.size())

"""ПРОВЕРКА ИДЕАЛЬНОГО БАЛАНСА"""

def task(s: str) -> bool:
    stack = Stack()
    for i in s:
        if i in ['(', '[', '{']:
            stack.push(i)
        elif i in [')', ']', '}']:
            last_el = stack.pop()
            if i == '}' and last_el != '{' or i == ')' and last_el != '(' or i == ']' and last_el != '[':
                return 'Не сбалансировано'
    return 'Сбалансировано'

"""РЕФАКТОРИНГ КОДА"""

import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart

class EmailClient:
    def __init__(self):
        self.GMAIL_SMTP = "smtp.gmail.com"
        self.GMAIL_IMAP = "imap.gmail.com"
        self.l = 'login@gmail.com'
        self.passwORD = 'qwerty'


    def send_message(self, recipients, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.l
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(self.GMAIL_SMTP, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(self.l, self.passwORD)
        ms.sendmail(self.l, ms, msg.as_string())

        return ms.quit()

    def revieve(self, header=None):
        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail.login(self.l, self.passwORD)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        return mail.logout()

# if __name__ == '__main__':
#     recipience = ['vasya@email.com', 'petya@email.com']
#     subject = 'Subject'
#     message = 'Message'
#     header = None
#     Client = EmailClient
#     Client.send_message(recipients=recipience, subject=subject, message=message)
#     Client.revieve(header)