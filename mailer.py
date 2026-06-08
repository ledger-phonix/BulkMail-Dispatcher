import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_bulk_email(smtp_server, smtp_port, sender_email, sender_password, recipients, subject, body, attachment=None):
    """Sends an HTML email to a list of recipients with an optional attachment."""
    if not recipients:
        return False, "No recipients found."

    try:
        # Establish SMTP Connection
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        for recipient in recipients:
            # 1. 'mixed' root container allows both a body and file attachments
            msg = MIMEMultipart('mixed')
            msg['From'] = sender_email
            msg['To'] = recipient
            msg['Subject'] = subject
            
            # 2. 'alternative' container forces the client to look for HTML rendering
            msg_alternative = MIMEMultipart('alternative')
            
            # Attach the HTML body with explicit UTF-8 character encoding
            html_part = MIMEText(body, 'html', 'utf-8')
            msg_alternative.attach(html_part)
            
            # Put the text/html section into the main message
            msg.attach(msg_alternative)

            # 3. Handle attachment if present
            if attachment is not None:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename={attachment.name}',
                )
                msg.attach(part)
                # Reset file pointer for the next recipient loop iteration
                attachment.seek(0)

            server.send_message(msg)
        
        server.quit()
        return True, f"Successfully sent  emails to {len(recipients)} recipients!"
    except Exception as e:
        return False, f"Failed to send emails: {str(e)}"