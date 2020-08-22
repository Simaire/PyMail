#Client de messagerie par Simaire V0.1#

import smtplib

expéditeur = input("VOTRE ADRESSE MAIL: ")
destinataire = input("ADRESSE MAIL DU DESTINATAIRE: ")
mdp = input("VOTRE MOT DE PASSE: ")
#suj = input("Sujet du mail: ")
msg = input("Votre message: ")

serveur = smtplib.SMTP('smtp.gmail.com', 587)
serveur.starttls()
serveur.login(expéditeur, mdp)
serveur.sendmail(expéditeur, destinataire, msg)
serveur.quit()








#cc = ["ADRESSE MAIL DU 1er DESTINATAIRE", "ADRESSE MAIL DU 2nd DESTINATAIRE"]
#bcc = "ADRESSE MAIL DU 3ème DESTINATAIRE" 

#message = MIMEMultipart() 
#message['From'] = expéditeur
#message['To'] = Toadd
#message['CC'] = ",".join(cc)
#message['BCC'] = bcc
#message['Subject'] = suj
#messageattach(MIMEText(msg.encode('utf-8'), 'plain', 'utf-8'))

#serveur = smtplib.SMTP('smtp.gmail.com', 587)
#serveur.starttls()
#serveur.login(expéditeur, mdp)
#texte= message.as_string().encode('utf-8')
#Toadds = [Toadd] + cc + [bcc]
#serveur.sendmail(expéditeur, Toadds, texte)
#serveur.quit()