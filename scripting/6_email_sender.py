import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Sevag B'
email['to'] = 'lil_soccaplaya7@hotmail.com'
email['subject'] = 'You won 1, 000, 000 dollars'

email.set_content('I am a Python Master')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sevag_boghossian@hotmail.com', 'sev19boghoss')
    smtp.send_message(email)
    print('all good boss!')