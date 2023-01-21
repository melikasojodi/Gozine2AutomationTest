import os
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email:
    def send_email(self):
        sender = "melikasojodi@gmail.com"  # replace with sender's email address
        receiver = "melikasojodi1376@gmail.com"  # replace with receiver's email address
        password = "xmhxpdzjftqjgsci"  # replace with your password
        host = 'smtp.gmail.com'  # replace with your host, e.g. gmail = smtp.gmail.com
        port = 465  # replace with your port, e.g. gmail = 465

        s = smtplib.SMTP_SSL(host, port)
        # s.set_debuglevel(1)
        s.login(sender, password)

        html_mail = """<meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Thank you for your Interest</title>
        <h1> Login Test & EstimateRank Test </h1>
        <p> در این تست ورود با یوزرنیم و پسورد معتبر و غیر معتبر سنجیده میشود
        و همچنین تخمین رتبه با دیتای معتبر و غیر معتبر سنجیده میشود
        </p>
        """

        msg = MIMEMultipart('alternative')
        msg['Subject'] = f"Test Automated Email"  # replace with your subject
        msg['From'] = sender
        msg['To'] = receiver

        Root_path = os.path.join(
            os.path.dirname(__file__),
            os.pardir,
        )
        attachment_path = Root_path + "\HTML_Test_Runner_ReportTest.html"  # replace with path of your PDF file
        with open(attachment_path, "rb") as f:
            attach = MIMEApplication(f.read(), _subtype="html")
            attach.add_header('Content-Disposition', 'attachment', filename=str(attachment_path))
        msg.attach(attach)

        html = html_mail
        part2 = MIMEText(html, 'html')

        msg.attach(part2)

        s.sendmail(sender, receiver, msg.as_string())

        s.quit()
