import sys
from time import sleep
logo = '''
███████╗███╗░░░███╗░█████╗░██╗██╗░░░░░  ███████╗██╗██╗░░░░░████████╗███████╗██████╗░
██╔════╝████╗░████║██╔══██╗██║██║░░░░░  ██╔════╝██║██║░░░░░╚══██╔══╝██╔════╝██╔══██╗
█████╗░░██╔████╔██║███████║██║██║░░░░░  █████╗░░██║██║░░░░░░░░██║░░░█████╗░░██████╔╝
██╔══╝░░██║╚██╔╝██║██╔══██║██║██║░░░░░  ██╔══╝░░██║██║░░░░░░░░██║░░░██╔══╝░░██╔══██╗
███████╗██║░╚═╝░██║██║░░██║██║███████╗  ██║░░░░░██║███████╗░░░██║░░░███████╗██║░░██║
╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝  ╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
    << BY LORD >>
       # Instagram : @00017z #
       '''
print(logo)
mlist = input("List Path : ")

for email in open(mlist, 'r'):
    email = email.strip()
    if '@gmail' in email:
        gmail = open('gmail.txt', 'a+')
        gmail.write(email + '\n')
        gmail.close()
        print('[GMAIL] -', email)
    elif '@yahoo' in email:
        yahoo = open('yahoo.txt', 'a+')
        yahoo.write(email + '\n')
        yahoo.close()
        print('[YAHOO] -', email)
    elif '@hotmail' in email:
        hotmail = open('hotmail.txt', 'a+')
        hotmail.write(email + '\n')
        hotmail.close()
        print('[HOTMAIL] -', email)
    elif '@aol.com' in email:
        hotmail = open('aol.txt', 'a+')
        hotmail.write(email + '\n')
        hotmail.close()
        print('[AOL] -', email)
    elif '@yandex.ru' in email:
        hotmail = open('yandex-ru.txt', 'a+')
        hotmail.write(email + '\n')
        hotmail.close()
        print('[YANDEX] -', email)
    else:
        other = open('other.txt', 'a+')
        other.write(email + '\n')
        other.close()
print("-------------------------------")
print("Done ! -", len(open(mlist, 'r').readlines()), ' ;)')
sleep(2)

