# mail sending --
from smtplib import SMTP


# Send Mail
def get_details(data_json):
    usr_name = data_json['name']
    usr_mail = data_json['email']
    usr_msg = data_json['message']
    send_mail(name=usr_name, mail=usr_mail, msg=usr_msg)


MY_EMAIL = 'rajdwivedi008@outlook.com'
MY_PASS = 'mmzqlihifpmstnir'


def send_mail(name: str, mail: str, msg: str):
    with SMTP('smtp-mail.outlook.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f'Subject:{f"Support request from {mail}"}\n\n'
                                f'Name: {name}\n'
                                f'{msg}')
        print("Email Sent!")
