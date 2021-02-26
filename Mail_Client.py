import subprocess
import smtplib
import os
import getpass
import sys
from smtplib import SMTPAuthenticationError
import time



def einstellungen():

   if env:
      os.system('cls')
   else:
      os.system('clear')

   print('###################################################################################')
   print('')
   print('                   Willkommen beim Mailspamer ihres Vertrauens                     ')
   print('        Bitte haben sie ein wenig Geduld es könnte zu Verzögerungen kommen         ')
   print('\n         Github: https://github.com/Just-a-normal-user?tab=repositories          ')
   print('')
   print('###################################################################################')
   print('')
   print("Wollen sie die Einstellungen des Mailspammers/Mailprogramms ändern (y/n) ? 'y'")
   print('')
   print('###################################################################################')
   print('')
   print('Einstellungsmöglichkeiten:')
   print('')
   print('Absender verändern:  ->absender / a')
   print('Betreff ändern:      ->betreff / b')
   print('Nachricht ändern:    ->text / t')
   print('')
   print('Wollen sie doch keine Einstellungen ändern? ->Enter drücken')
   print('')
   print('###################################################################################')
   print('')
   print('Welche Einstellungen wollen sie ändern? ')
   welche = input('>>> ')

   if welche == 'absender' or welche == 'a':
      email_und_passwort_aendern()

   elif welche == 'betreff' or welche == 'b':
      subject_aendern()

   elif welche == 'text' or welche == 't':
      body_aendern()




def email_und_passwort_aendern():
   print('')
   print('###################################################################################')
   print('')
   print("Geben sie eine neue, gültige Email-Addresse ein: ")
   MAIL_ADDRESS = input('>>> ')

   if MAIL_ADDRESS == '':
      print('')
      print('###################################################################################')
      print('')
      print('Bitte geben sie eine Email Addresse ein, von der die Email gesendet werden soll:')
      MAIL_ADDRESS = input('>>> ')


      if MAIL_ADDRESS == '':
         quit()

   print('\nDas Passwort wurde erfolgreich geändert.')

   if '@gmail' in MAIL_ADDRESS:
      smtp = 'smtp'
      mail = 'gmail'
      com = 'com'

   elif '@web' in MAIL_ADDRESS:
      smtp = 'smtp'
      mail = 'web'
      com = 'de'

   elif '@gmx' in MAIL_ADDRESS:
      smtp = 'mail'
      mail = 'gmx'
      com = 'net'

   elif '@outlook' in MAIL_ADDRESS:
      smtp = 'SMTP'
      mail = 'office365'
      com = 'com'

   elif '@t-online' in MAIL_ADDRESS:
      smtp = 'securesmtp'
      mail = 't-online'
      com = 'de'

   elif '@icloud' in MAIL_ADDRESS:
      smtp = 'smtp'
      mail = 'mail.me'
      com = 'com'

   elif '@aol' in MAIL_ADDRESS:
      smtp = 'smtp'
      mail = 'de.aol'
      com = 'com'

   elif '@mail' in MAIL_ADDRESS:
      smtp = 'smtp'
      mail = 'mail'
      com = 'de'

   elif '@yahoo' in MAIL_ADDRESS:
      smtp = 'smtp'
      mail = 'mail.yahoo'
      com = 'com'

   else:
      print('\nBitte lies die Anleitung(readme.txt)\n')
      print('Soll die Anleitung geöffnet werden? (y/n)')
      a = input('>>> ')
      if a == 'y':
         pass

   



   print('\nGeben sie das Passwort zu diesem Email Account an (wird nicht gespeichert) :')
   PASSWORD = input('>>> ')

   time.sleep(1)
   print('\nDas Passwort wurde erfolgreich geändert.')

   try:

      server = smtplib.SMTP(f'{smtp}.{mail}.{com}', 587)
      server.ehlo()
      server.starttls()
      server.ehlo()
      server.login(MAIL_ADDRESS, PASSWORD)

   except SMTPAuthenticationError as err:
      for i in range(5):
         q = 5 - i
         os.system(m)
         print('\nSie haben entweder ein falsches Passwort oder eine ungültige Email Addresse eingegeben.\n')
         print(f'Bitte versuchen sie es erneut in: {q} Sekunden erneut')
         time.sleep(1)
      einstellungen()
   
   else:
      pass
      
   print('')
   print('###################################################################################')
   print('')
   print('Wollen sie eine weitere Einstellung ändern? (y/n)')
   y = input('>>> ')

   if y == 'y':
      einstellungen()




def subject_aendern():
   global subject

   print('')
   print('###################################################################################')
   print('')
   print("Geben sie einen neuen Betreff ein: ")
   subject = input('>>> ')

   time.sleep(2)
   print('\nDer Betreff wurde erfolgreich geändert.')

   print('')
   print('###################################################################################')
   print('')
   print('Wollen sie eine weitere Einstellung ändern? (y/n)')
   y = input('>>> ')

   if y == 'y':
      einstellungen()


   

def body_aendern():
   global body

   print('')
   print('###################################################################################')
   print('')
   print("Geben sie eine neue Nachricht ein: ")
   body = input('>>> ')

   time.sleep(2)
   print('\nDie Nachricht wurde erfolgreich geändert.')

   print('')
   print('###################################################################################')
   print('')
   print('Wollen sie eine weitere Einstellung ändern? (y/n)')
   y = input('>>> ')

   if y == 'y':
      einstellungen()
   




def email_und_passwort():

   global server
   global MAIL_ADDRESS
   global PASSWORD

   os.system(m)

   print('###################################################################################')
   print('')
   print('                   Willkommen beim Mailspamer ihres Vertrauens                     ')
   print('        Bitte haben sie ein wenig Geduld es könnte zu Verzögerungen kommen         ')
   print('\n         Github: https://github.com/Just-a-normal-user?tab=repositories          ')
   print('')
   print('###################################################################################')
   print('')


   print('Bitte geben sie eine Email Addresse ein, von der die Email gesendet werden soll:')
   MAIL_ADDRESS = input('>>> ')

   if MAIL_ADDRESS == '':
      os.system(m)
      print('###################################################################################')
      print('')
      print('                   Willkommen beim Mailspamer ihres Vertrauens                     ')
      print('        Bitte haben sie ein wenig Geduld es könnte zu Verzögerungen kommen         ')
      print('\n         Github: https://github.com/Just-a-normal-user?tab=repositories          ')
      print('')
      print('###################################################################################')
      print('')
      print('Bitte geben sie eine Email Addresse ein, von der die Email gesendet werden soll:')
      MAIL_ADDRESS = input('>>> ')
      if MAIL_ADDRESS == '':
         quit()
   
   smtp = 'smtp'
   mail = 'gmail'
   com = 'com'


   if '@gmail' in MAIL_ADDRESS:
      smtp = 'smtp'
      mail = 'gmail'
      com = 'com'

   elif '@web' in MAIL_ADDRESS:
      smtp = 'smtp'
      mail = 'web'
      com = 'de'

   elif '@gmx' in MAIL_ADDRESS:
      smtp = 'mail'
      mail = 'gmx'
      com = 'net'

   elif '@outlook' in MAIL_ADDRESS:
      smtp = 'SMTP'
      mail = 'office365'
      com = 'com'

   elif '@t-online' in MAIL_ADDRESS:
      smtp = 'securesmtp'
      mail = 't-online'
      com = 'de'

   elif '@icloud' in MAIL_ADDRESS:
      smtp = 'smtp'
      mail = 'mail.me'
      com = 'com'

   elif '@aol' in MAIL_ADDRESS:
      smtp = 'smtp'
      mail = 'de.aol'
      com = 'com'

   elif '@mail' in MAIL_ADDRESS:
      smtp = 'smtp'
      mail = 'mail'
      com = 'de'

   elif '@yahoo' in MAIL_ADDRESS:
      smtp = 'smtp'
      mail = 'mail.yahoo'
      com = 'com'

   else:
      print('\nBitte lies die Anleitung(readme.txt)')





   # Passwort abfrage

   os.system(m)

   print('###################################################################################')
   print('')
   print('                   Willkommen beim Mailspamer ihres Vertrauens                     ')
   print('        Bitte haben sie ein wenig Geduld es könnte zu Verzögerungen kommen         ')
   print('\n         Github: https://github.com/Just-a-normal-user?tab=repositories          ')
   print('')
   print('###################################################################################')
   print('')
   print('Absender: ' + MAIL_ADDRESS)
   print('')
   print('###################################################################################')
   print('')


   print('Bitte geben sie das Passwort für den Email Account an:')
   PASSWORD = getpass.getpass('>>> ')

   if PASSWORD == '':
      os.system(m)
      print('###################################################################################')
      print('')
      print('                   Willkommen beim Mailspamer ihres Vertrauens                     ')
      print('        Bitte haben sie ein wenig Geduld es könnte zu Verzögerungen kommen         ')
      print('\n         Github: https://github.com/Just-a-normal-user?tab=repositories          ')
      print('')
      print('###################################################################################')
      print('')
      print('Absender:' + MAIL_ADDRESS)
      print('')
      print('###################################################################################')
      print('')
      print('Bitte geben sie das Passwort für den Email Account an:')
      PASSWORD = getpass.getpass('>>> ')
      if PASSWORD == '':
         quit()


   try:

      server = smtplib.SMTP(f'{smtp}.{mail}.{com}', 587)
      server.ehlo()
      server.starttls()
      server.ehlo()
      server.login(MAIL_ADDRESS, PASSWORD)

   except SMTPAuthenticationError as err:
      for i in range(5):
         q = 5 - i
         os.system(m)
         print('\nSie haben entweder ein falsches Passwort oder eine ungültige Email Addresse eingegeben.\n')
         print(f'Bitte versuchen sie es erneut in: {q} Sekunden erneut')
         time.sleep(1)
      email_und_passwort()
   
   else:
      pass




def empfaenger():
   global TO_ADDRESSE

   os.system(m)

   print('###################################################################################')
   print('')
   print('                   Willkommen beim Mailspamer ihres Vertrauens                     ')
   print('        Bitte haben sie ein wenig Geduld es könnte zu Verzögerungen kommen         ')
   print('\n         Github: https://github.com/Just-a-normal-user?tab=repositories          ')
   print('')
   print('###################################################################################')
   print('')
   print('Absender: ' + MAIL_ADDRESS)
   print('')
   print('###################################################################################')
   print('')
   print('Betreff: ' + subject)
   print('')
   print('###################################################################################')
   print('')
   print('Inhalt: ' + body)
   print('')
   print('###################################################################################')
   print('')

   print('An wen soll die Email gesendet werden? ')
   TO_ADDRESSE = input('>>> ')




def anzahl():
   global w
   os.system(m)
   print('###################################################################################')
   print('')
   print('                   Willkommen beim Mailspamer ihres Vertrauens                     ')
   print('        Bitte haben sie ein wenig Geduld es könnte zu Verzögerungen kommen         ')
   print('\n         Github: https://github.com/Just-a-normal-user?tab=repositories          ')
   print('')
   print('###################################################################################')
   print('')
   print('Absender: ' + MAIL_ADDRESS)
   print('')
   print('###################################################################################')
   print('')
   print('Betreff: ' + subject)
   print('')
   print('###################################################################################')
   print('')
   print('Inhalt: ' + body)
   print('')
   print('###################################################################################')
   print('')
   print('Empfänger: ' + TO_ADDRESSE)
   print('')
   print('###################################################################################')
   print('')

   print("Wie oft soll die Mail gesendet werden? ")

   try:
      w = int(input('>>> '))
      if w == 0:
         anzahl()
      elif w >= 10:
         print('')
         print('--------------------------------------------------------------')
         print('')
         print(f'Sind sie sich sicher, dass sie {w} Emails senden möchten (y/n)')
         x = input('>>> ')

         if x != 'y':
            anzahl()

   except ValueError:
      for i in range(5):
         q = 5 - i
         os.system(m)
         print('\nSie haben eine falsche Zahl/Buchstabe eingegeben.\n')
         print(f'Bitte versuchen sie es erneut in: {q} Sekunden erneut')
         time.sleep(1)
      anzahl()

   else:
      pass




w = 1

MAIL_ADDRESS = ''

TO_ADDRESSE = ''

PASSWORD = ''

server = ''

subject = ''

body = ''



env = sys.platform.startswith('win32')
if env:
   m = 'cls'

else:
   m = 'clear'



email_und_passwort()



os.system(m)

print('###################################################################################')
print('')
print('                   Willkommen beim Mailspamer ihres Vertrauens                     ')
print('        Bitte haben sie ein wenig Geduld es könnte zu Verzögerungen kommen         ')
print('\n         Github: https://github.com/Just-a-normal-user?tab=repositories          ')
print('')
print('###################################################################################')
print('')
print('Absender: ' + MAIL_ADDRESS)
print('')
print('###################################################################################')
print('')

print('Bitte geben sie den Betreff der Email ein:')
subject = input('>>> ')


# body

os.system(m)

print('###################################################################################')
print('')
print('                   Willkommen beim Mailspamer ihres Vertrauens                     ')
print('        Bitte haben sie ein wenig Geduld es könnte zu Verzögerungen kommen         ')
print('\n         Github: https://github.com/Just-a-normal-user?tab=repositories          ')
print('')
print('###################################################################################')
print('')
print('Absender: ' + MAIL_ADDRESS)
print('')
print('###################################################################################')
print('')
print('Betreff: ' + subject)
print('')
print('###################################################################################')
print('')


print('Bitte geben sie den Inhalt der Email ein:')
body = input('>>> ')





os.system(m)

print('###################################################################################')
print('')
print('                   Willkommen beim Mailspamer ihres Vertrauens                     ')
print('        Bitte haben sie ein wenig Geduld es könnte zu Verzögerungen kommen         ')
print('\n         Github: https://github.com/Just-a-normal-user?tab=repositories          ')
print('')
print('###################################################################################')
print('')
print('Absender: ' + MAIL_ADDRESS)
print('')
print('###################################################################################')
print('')
print('Betreff: ' + subject)
print('')
print('###################################################################################')
print('')
print('Inhalt: ' + body)
print('')
print('###################################################################################')
print('')

print('Wollen sie die Enstellungen/Angaben des Mailspammers/Mailprogramms noch einmal ändern (y/n) ? ')
e = input('>>> ')

if e == 'y':
   einstellungen()

else:
   pass


# Empfänger

empfaenger()

# Anzahl der Emails

anzahl()




# emails senden

os.system(m)

print('###################################################################################')
print('')
print('                   Willkommen beim Mailspamer ihres Vertrauens                     ')
print('        Bitte haben sie ein wenig Geduld es könnte zu Verzögerungen kommen         ')
print('\n         Github: https://github.com/Just-a-normal-user?tab=repositories          ')
print('')
print('###################################################################################')
print('')
print('Absender: ' + MAIL_ADDRESS)
print('')
print('###################################################################################')
print('')
print('Betreff: ' + subject)
print('')
print('###################################################################################')
print('')
print('Inhalt: ' + body)
print('')
print('###################################################################################')
print('')
print('Empfänger: ' + TO_ADDRESSE)
print('')
print('###################################################################################')
print('')
print('                  Die Email wird nun ' + str(w) + ' mal gesendet                   ')
print('')
print('###################################################################################')
print('')








d = 0

for i in range(w):

   message = f'Subject: {subject}\n\n{body}'
   server.sendmail(MAIL_ADDRESS, TO_ADDRESSE, message.encode('utf-8'))
   
   print('---------------------------------------------')
   print(f'Die {i+1}te Email wurde erfolgreich versandt')
   print('')




print('###################################################################################')

server.quit()

print('')
print('Wollen sie unsere Dienstleistungen noch ein weiteres Mal in Anspruch nehmen (y/n) ?')
nochmal = input('>>> ')



if nochmal == 'y':
   subprocess.call(['python', 'Mail_Client.py'])

else:
   os.system(m)
   print('Vielen Dank für den Support.\nIhr "Just-a-normal-user" Team.')
   time.sleep(5)
