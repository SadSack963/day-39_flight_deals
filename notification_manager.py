import smtplib
import os
from dotenv import load_dotenv
from flight_data import FlightData


load_dotenv("E:/Python/EnvironmentVariables/.env")
YAHOO_SENDER = os.getenv("SMTP_YAHOO_SENDER")
YAHOO_USERNAME = os.getenv("SMTP_YAHOO_USERNAME")
YAHOO_EMAIL = os.getenv("SMTP_YAHOO_EMAIL")
YAHOO_PASSWORD = os.getenv("SMTP_YAHOO_PASSWORD")
YAHOO_RECIPIENT = os.getenv("SMTP_YAHOO_RECIPIENT")


def send_mail(fd: FlightData):
    # YAHOO
    message = f"From: \"{YAHOO_SENDER}\" <{YAHOO_EMAIL}>\n" \
              f"To: {YAHOO_RECIPIENT}\n" \
              f"Subject: Cheap flight\n\n" \
              f"Price: £{fd.price}\n" \
              f"From:  {fd.city_from} {fd.airport_from}\n" \
              f"To:    {fd.city_to} {fd.airport_to}\n" \
              f"Dep:   {fd.date_dep}\n" \
              f"Ret:   {fd.date_ret}\n\n" \
              f"Book Now!".encode("utf-8")

    print(message, end="\n\n")

    # Sent the email
    with smtplib.SMTP(host="smtp.mail.yahoo.co.uk", port=587) as connection:
        # Secure the connection
        connection.starttls()
        connection.login(user=YAHOO_USERNAME, password=YAHOO_PASSWORD)
        connection.sendmail(from_addr=YAHOO_EMAIL, to_addrs=YAHOO_RECIPIENT, msg=message)
