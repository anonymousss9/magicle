import re
import dns.resolver
import smtplib


def validate_email_address(email):
    # Check the syntax and format of the email address using regex
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False

    # Check the domain of the email address using DNS
    try:
        domain = email.split('@')[1]
        records = dns.resolver.query(domain, 'MX')
        mx_record = str(records[0].exchange)
        server = smtplib.SMTP()
        server.connect(mx_record)
        server.quit()
    except Exception as e:
        return False

    # Check the existence of the email address using SMTP
    try:
        server = smtplib.SMTP()
        server.connect(mx_record)
        server.helo()
        server.mail('me@domain.com')
        code, message = server.rcpt(str(email))
        server.quit()
        if code == 250:
            return True
        else:
            return False
    except Exception as e:
        return False

    # Check the email address against a list of disposable email domains
    disposable_domains = [
        'mailinator.com',
        'guerrillamail.com',
        '10minutemail.com',
        'tempmail.com',
        'trashmail.com',
        'maildrop.cc',
        # Add more disposable email domains here
    ]
    domain = email.split('@')[1]
    if domain in disposable_domains:
        return False

    return True


# Test the email validation function with a sample email address
email = 'example@example.com'
is_valid = validate_email_address(email)
print('The email', email, 'is', 'valid' if is_valid else 'not valid')
