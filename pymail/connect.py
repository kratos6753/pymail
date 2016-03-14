import poplib, os
from email import parser

username = os.environ['username']
password = os.environ['password']
pop_conn = poplib.POP3_SSL('pop.gmail.com')
try:
	pop_conn.user(username)
	pop_conn.pass_(password)
except poplib.error_proto as e:
	print "Username or Password are not correct!!"
else:
#Get messages from server:
	messages = [pop_conn.retr(i) for i in range(1, 10)]
	messages = ["\n".join(mssg[1]) for mssg in messages]
	messages = [parser.Parser().parsestr(mssg) for mssg in messages]
	for message in messages:
	    print message['subject']
	emailInfo = pop_conn.stat()
	print "Number of new emails %s (%s bytes)" % emailInfo
	pop_conn.quit()