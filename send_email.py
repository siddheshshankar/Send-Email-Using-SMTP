from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(body):

    message = MIMEMultipart()
    message['Subject'] = 'Top 5 Economies of the World!'
    message['From'] = '<sender>@gmail.com'
    message['To'] = '<receiver>@gmail.com'

    body_content = body
    message.attach(MIMEText(body_content, "html"))
    msg_body = message.as_string()

    server = SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(message['From'], 'Unique password')
    server.sendmail(message['From'], message['To'], msg_body)
    server.quit()
