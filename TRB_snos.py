import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from colorama import Fore, init

# Инициализация colorama
init(autoreset=True)

# ASCII-арт приветствия
ascii_banner = r"""
 _________    ________      ________     
|\___   ___\ |\   __  \    |\   __  \    
\|___ \  \_| \ \  \|\  \   \ \  \|\ /_   
     \ \  \   \ \   _  _\   \ \   __  \  
      \ \  \   \ \  \\  \|   \ \  \|\  \ 
       \ \__\   \ \__\\ _\    \ \_______\
        \|__|    \|__|\|__|    \|_______|
"""

# Цветной баннер
def print_colored_banner():
    print(Fore.MAGENTA + ascii_banner)

# Словари отправителей и получателей
senders = {
    'korlithiobtennick@mail.ru': 'feDLSiueGT89APb81v74',
    'avyavya.vyaavy@mail.ru': 'zmARvx1MRvXppZV6xkXj',
    'gdfds98@mail.ru': '1CtFuHTaQxNda8X06CaQ',
    'dfsdfdsfdf51@mail.ru': 'SXxrCndCR59s5G9sGc6L',
    'aria.therese.svensson@mail.com': 'Zorro1ab',
    'taterbug@verizon.net': 'Holly1!',
    'ejbrickner@comcast.net': 'Pass1178',
    'teressapeart@cox.net': 'Quinton2329!',
    'liznees@verizon.net': 'Dancer008',
    'olajakubovich@mail.com': 'OlaKub2106OlaKub2106',
    'kcdg@charter.net': 'Jennifer3*',
    'bean_118@hotmail.com': 'Liverpool118!',
    'dsdhjas@mail.com': 'LONGHACH123',
    'robitwins@comcast.net': 'May241996',
    'wasina@live.com': 'Marlas21',
    'aruzhan.01@mail.com': '1234567!',
    'rob.tackett@live.com': 'metallic',
    'lindahallenbeck@verizon.net': 'Anakin@2014',
    'hlaw82@mail.com': 'Snoopy37$$',
    'paintmadman@comcast.net': 'mycat2200*',
    'prideandjoy@verizon.net': 'Ihatejen12',
    'sdgdfg56@mail.com': 'kenwood4201',
    'garrett.danelz@comcast.net': 'N11golfer!',
    'gillian_1211@hotmail.com': 'Gilloveu1211',
    'sunpit16@hotmail.com': 'Putter34!',
    'fdshelor@verizon.net': 'Masco123*',
    'yeags1@cox.net': 'Zoomom1965!',
    'amine002@usa.com': 'iScrRoXAei123',
    'bbarcelo16@cox.net': 'Bsb161089$$',
    'laliebert@hotmail.com': 'pirates2',
    'vallen285@comcast.net': 'Delft285!1!',
    'sierra12@email.com': 'tegen1111',
    'luanne.zapevalova@mail.com': 'FqWtJdZ5iN@',
    'kmay@windstream.net': 'Nascar98',
    'redbrick1@mail.com': 'Redbrick11',
    'ivv9ah7f@mail.com': 'K226nw8duwg',
    'erkobir@live.com': 'floydLAWTON019',
    'Misscarter@mail.com': 'ashtray19',
    'carlieruby10@cox.net': 'Lollypop789$',
    'blackops2013@mail.com': 'amason123566',
    'caroline_cullum@comcast.net': 'carter14',
    'dpb13@live.com': 'Ic&ynum13',
    'heirhunter@usa.com': 'Noguys@714',
    'sherri.edwards@verizon.net': 'Dreaming123#',
    'rami.rami1980@hotmail.com': 'ramirami1980',
    'jmsingleton2@comcast.net': '151728Jn$$',
    'aberancho@aol.com': '10diegguuss10',
    'dgidel@iowatelecom.net': 'Buster48',
    'gpopandopul@mail.com': 'GEORG62A',
    'bolgodonsk@mail.com': '012345678!',
    'colbycolb@cox.net': 'Signals@1',
    'nicrey4@comcast.net': 'Dabears54',
    'mordechai@mail.com': 'Mordechai',
    'inemrzoya@mail.com': 'rLS1elaUrLS1elaU',
    'tarabedford@comcast.net': 'Money4me',
    'mycockneedsit@mail.com': 'benjamin3',
    'saralaine@mail.com': 'sarlaine12!1',
    'jonb2006@verizon.net': '1969Camaro',
    'rjhssa1@verizon.net': 'Donna613*',
    'cameron.doug@charter.net': 'Jake2122$',
    'bridget.shappell@comcast.net': 'Brennan1',
    'rugs8@comcast.net': 'baseball46',
    'averyjacobs3@mail.com': '1960682644!',
    'lstefanick@hotmail.com': 'Luv2dance2',
    'bchavez123@mail.com': 'aadrianachavez',
    'lukejamesjones@mail.com': 'tinkerbell1',
    'emahoney123@comcast.net': 'Shieknmme3#',
    'mandy10.mcevoy@btinternet.com': 'Tr1plets3',
    'jet747@cox.net': 'Sadie@1234',
    'landsgascareservices@mail.com': 'Alisha25@',
    'samantha224@mail.com': 'Madden098!@',
    'kbhamil@wowway.com': 'Carol1940',
    'email@bjasper.com': 'Lhsnh4us123!',
    'biggsbrian@cox.net': 'Trains@2247Trains@2247',
    'dzzeblnd@aol.com': 'Geosgal@1',
    'jtrego@indy.rr.com': 'Jackwill14!',
    'chrisphonte.rj@comcast.net': 'Junior@3311',
    'tvwifi.guy@comcast.net': 'Bill#0101',
    'defenestrador@mail.com': 'm0rb1d8ss',
    'glangley@gmx.com': 'ironhide',
    'charlotte2850@hotmail.com': 'kelalu2850'
}
receivers = ['sms@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org',
             'sticker@telegram.org', 'support@telegram.org']

def menu():
    print(Fore.MAGENTA + "Снос: ")
    print(Fore.MAGENTA + "1. Аккаунта")
    print(Fore.MAGENTA + "2. Канала")
    choice = input(Fore.MAGENTA + "Введите: ")
    return choice

def send_email(receiver, sender_email, sender_password, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver, msg.as_string())
        time.sleep(3)
        server.quit()
        return True
    except Exception as e:
        return False

def main():
    print_colored_banner()
    sent_emails = 0
    choice = menu()
    if choice == '1':
        print(Fore.MAGENTA + "1. Спам")
        print(Fore.MAGENTA + "2. Докс")
        print(Fore.MAGENTA + "3. Троллинг")
        print(Fore.MAGENTA + "4. Снос ссесий")
        comp_choice = input(Fore.MAGENTA + "Введите: ")
        if comp_choice in ["1", "2", "3", "5", "6"]:
            username = input(Fore.MAGENTA + "Юзернейм: ")
            id = input(Fore.MAGENTA + "Телграм айди: ")
            chat_link = input(Fore.MAGENTA + "Ссылка на чат(если нету enter): ")
            violation_link = input(Fore.MAGENTA + "Violation Link: ")
            comp_texts = {
                "1": f"Dear Support,\n\nI found a user who is sending a lot of unwanted messages - SPAM. Username: {username}, ID: {id}, Chat Link: {chat_link}, Violation Link: {violation_link}. Please take action against this user.",
                "2": f"Dear Support,\n\nI found a user who is spreading personal data without consent. Username: {username}, ID: {id}, Chat Link: {chat_link}, Violation Link: {violation_link}. Please take action by blocking this user's account.",
                "3": f"Dear Support,\n\nI found a user who is openly using abusive language and spamming in chats. Username: {username}, ID: {id}, Chat Link: {chat_link}, Violation Link: {violation_link}. Please take action by blocking this user's account.",
                "5": f"Dear Support,\n\nAccount {username} ({id}) is using a virtual number purchased from a website for number activation. This number is not related to them. Please investigate.",
                "6": f"Dear Support,\n\nAccount {username} ({id}) has purchased premium features to send spam messages and bypass Telegram restrictions. Please review this complaint and take appropriate action."
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts.get(comp_choice, "Invalid choice selected")
                    comp_body = comp_text.format(username=username.strip(), id=id.strip(), chat_link=chat_link.strip(), violation_link=violation_link.strip())
                    if send_email(receiver, sender_email, sender_password, 'Account Complaint', comp_body):
                        sent_emails += 1
                        print(Fore.GREEN + f"Отправлено на {receiver} от {sender_email}!")
                    else:
                        print(Fore.RED + f"Не отправлено на {receiver} от {sender_email}")
                    time.sleep(5)

    elif choice == '2':
        print(Fore.MAGENTA + "1. Личные данные")
        print(Fore.MAGENTA + "2. Живодерство")
        print(Fore.MAGENTA + "3. Детская порнография")
        print(Fore.MAGENTA + "4. Докс и сват")
        ch_choice = input(Fore.MAGENTA + "Выберите: ")
        if ch_choice in ["1", "2", "3", "4"]:
            channel_link = input(Fore.MAGENTA + "Ссылка на канал: ")
            channel_violation = input(Fore.MAGENTA + "Ссылка на нарушение: ")
            comp_texts = {
                "1": f"Dear Support,\n\nI found a channel that is spreading personal data of innocent people. Channel Link: {channel_link}, Violation Link: {channel_violation}. Please block this channel.",
                "2": f"Dear Support,\n\nI found a channel that is spreading animal cruelty content. Channel Link: {channel_link}, Violation Link: {channel_violation}. Please block this channel.",
                "3": f"Dear Support,\n\nI found a channel that is spreading child pornography. Channel Link: {channel_link}, Violation Link: {channel_violation}. Please block this channel.",
                "4": f"Dear Support,\n\nI found a channel that is selling doxing and swatting services. Channel Link: {channel_link}, Violation Link: {channel_violation}. Please block this channel."
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts.get(ch_choice, "Invalid choice selected")
                    comp_body = comp_text.format(channel_link=channel_link.strip(), channel_violation=channel_violation.strip())
                    if send_email(receiver, sender_email, sender_password, 'Channel Complaint', comp_body):
                        sent_emails += 1
                        print(Fore.GREEN + f"Успешно отправлено на {receiver} от {sender_email}!")
                    else:
                        print(Fore.RED + f"Ошибка при отправке на {receiver} от {sender_email}")
                    time.sleep(5)

    else:
        print(Fore.RED + "Неверный выбор")

if __name__ == "__main__":
    main()
