import smtplib, ssl

port = 465  # For SSL
password = 'CC3ngLabs!'

sender_email = "automationproductsafety@gmail.com"
receiver_email = "he.Charlie@yahoo.com"
message = """\
Subject: Thermal Test Automation

Your thermal test automation is complete, come back to the automation station!"""

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    # TODO: Send email here
    server.sendmail(sender_email, receiver_email, message)
