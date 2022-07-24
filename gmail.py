import smtplib
import email.message

def enviar_email():
	corpo_email = ""
	<p>Parágrafo</p>
	<P>Parágrafo</p>
	"""

	msg = email.message.Message()
	msg['Subject'] = "Assunto"
	msg['From'] = 'remetente'
	msg['To'] = 'destinatario'
	password = 'senha'
	msg.add_header('Content-Type', 'Text/html')
	msg.set_payload(corpo_email)

	s = smtplib.SMTP('smtp.gmail.com: 587')
	s.starttls()
	#Login Credentials for sendig the mail
	s.login(msg['From'], password)
	s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
	print('Email enviado')