#!/usr/bin/python2
import os,sys,time
import commands
import cgi,cgitb

cgitb.enable()
print "Content-type:text/html\r\n\r\n"

#Data is retrieved
data=cgi.FieldStorage()
choice=data.getvalue('platform')




if  choice == "python":
	commands.getoutput('sudo docker start 0f04e9f65783')
	x=commands.getoutput('sudo docker exec -it 0f04e9f65783 /usr/bin/python')
	print "<a href='http://192.168.122.163:4200'>"
	print "Username is pyuser and password is 'q' to start coding"
	print "</a>"
	
	
elif  choice == "perl":

	commands.getoutput('sudo docker start 0f04e9f65783')
	x=commands.getoutput('sudo docker exec -it 0f04e9f65783 /usr/bin/perl')
	print "<a href='http://192.168.122.163:4200'>"
	print "Username is perluser and password is 'q' to start coding"
	print "</a>"
	

elif  choice == "ruby":

	commands.getoutput('sudo docker start 0f04e9f65783')
	x=commands.getoutput('sudo docker exec -it 0f04e9f65783 /usr/bin/irb')
	print "<a href='http://192.168.122.163:4200'>"
	print "Username is rubyuser and password is 'q' to start coding"
	print "</a>"
