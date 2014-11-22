import urllib2
import smtplib

# Username and pass for gmail
uname = "USERNAME"
pword = "PASS"

# To and from addresses
frm = "ADDRESS"
to  = "ADDRESS"

# sendMessage used to send message
def sendMessage(message):

	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText
	
	msg = MIMEMultipart("alternative")
	msg["Subject"] = "Server down :("
	msg["From"] = frm
	msg["To"] = to

	body = "Bummers, your server is down: %s" + message

	msg.attach(MIMEText(body, "plain"))

	server = smtplib.SMTP("smtp.gmail.com:587")
	server.starttls()
	server.login(uname,pword)
	server.sendmail(frm, to, msg.as_string())
	server.quit()

# call used to make request 
def call():
	from urllib2 import Request, urlopen, URLError
	try:
		a = urllib2.urlopen(req)
	
	except URLError as e:
        	
        	sendMessage(str(e))
    		
# main
def main():
	call()

# ========================
if __name__ == "__main__":
	main();
