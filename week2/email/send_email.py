import json
import smtplib
from email.message import EmailMessage

import magic


def compose_email(sender):
    message = EmailMessage()
    message["From"] = sender
    message["To"] = input("To: ")
    message["CC"] = input("CC: ")
    message["BCC"] = input("BCC: ")
    message["Subject"] = input("Subject: ")
    message.set_content(input("Body: "))
    attachments = input("Enter filename/path for attachment(s)(if any):")

    if attachments:
        for attachment in attachments.split(","):
            mimetype = magic.from_file(attachment, mime=True).strip().split("/")
            with open(attachment, "rb") as f:
                data = f.read()
                file_name = f.name

            message.add_attachment(
                data, filename=file_name, maintype=mimetype[0], subtype=mimetype[1]
            )
    return message


def main():
    with open("config.json", "r") as f:
        config = json.load(f)

    with smtplib.SMTP(config["email_server"], config["port"]) as smtp:
        # smtp.login(config['sender_email'],config['password']) #uncomment this if required
        message = compose_email(config["sender_email"])
        smtp.send_message(message)


if __name__ == "__main__":
    main()
