from typing import Optional, List
import smtplib
import mimetypes
from email.message import EmailMessage
from pathlib import Path


def send_email(
    sender: str,
    password: str,
    receiver: str,
    subject: str,
    body: str,
    attached_paths: Optional[List] = None,
) -> None:
    """Gmail and UdeC Webmail (https://webmail.udec.cl/) email sender to integrate with other apps.
    You need a Gmail or UdeC account to be able to use this utility. This is not a secure way to
    send emails, and you may need to activate 'Less secure app access' to be able to use it in your
    Gmail account.

    Args:
        sender: Email of the sender, it can be gmail or UdeC. Ex. 'crvillanueva@udec.cl'.
        password: Password of the sender's email account.
        receiver: Email of the destinatary.
        body: Body of the message to send.
        subject: Text of the email's subject.
        attached_paths: List of paths of files to attach to the mail

    Returns:
        None
    """
    # Set email contents
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)

    if attached_paths:
        for file_path in attached_paths:
            with open(file_path, "rb") as fp:
                ctype, _ = mimetypes.guess_type(file_path)
                maintype, subtype = ctype.split("/", 1)
                f_read = fp.read()
                filename = Path(file_path).name

                msg.add_attachment(f_read, maintype=maintype, subtype=subtype, filename=filename)

    # Send email
    account = sender.split("@")[0]
    provider = sender.split("@")[1]
    smtp = f"smtp.{provider}"

    with smtplib.SMTP(smtp, 587) as smtp:
        smtp.ehlo()
        smtp.starttls() # enable security
        smtp.ehlo()
        smtp.login(account, password)
        smtp.send_message(msg)
