## Simple Email Notification via google smtp relay

import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("todd.alfke@gmail.com", "---this is your password---")

msg = "YOUR MESSAGE!"
server.sendmail("todd.alfke@gmail.com", "todd.alfke@gmail.com", msg)
server.quit()
