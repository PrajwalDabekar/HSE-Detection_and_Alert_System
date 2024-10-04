import smtplib

HOST = "smtp-mail.outlook.com"
PORT = 587

FROM_EMAIL = "sanketmecs121@gst.sies.edu.in"
TO_EMAIL = "ssanket.1403@gmail.com"
PASSWORD = "8108456446Sms"  # Replace with your real password (not recommended)

MESSAGE = """Subject:ALERT MESSAGE"""

smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] Starting TLS connection: {status_code} {response}")

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Logging in: {status_code} {response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
smtp.quit()