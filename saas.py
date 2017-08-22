#!/usr/bin/python
import cgi,os,commands

print "content-type:text/html\r\n\r\n"
data=cgi.FieldStorage()
output=data.getvalue('soft')
if output=="firefox":
	commands.getstatusoutput('sudo tar cvf /var/www/html/firefox.tar firefox.sh') 

	print "<META HTTP-EQUIV='refresh' content='0; url=/firefox.tar' target='_blank'/>"

if output=="vlc":
	commands.getstatusoutput('sudo tar cvf /var/www/html/vlc.tar vlc.sh') 

	print "<META HTTP-EQUIV='refresh' content='0; url=/vlc.tar' target='_blank'/>"

if output=="cheese":
	commands.getstatusoutput('sudo tar cvf /var/www/html/cheese.tar cheese.sh') 

	print "<META HTTP-EQUIV='refresh' content='0; url=/cheese.tar' target='_blank'/>"

if output=="office":
	commands.getstatusoutput('sudo tar cvf /var/www/html/office.tar office.sh') 

	print "<META HTTP-EQUIV='refresh' content='0; url=/office.tar' target='_blank'/>"

if output=="calc":
	commands.getstatusoutput('sudo tar cvf /var/www/html/calc.tar calc.sh') 

	print "<META HTTP-EQUIV='refresh' content='0; url=/calc.tar' target='_blank'/>"

if output=="screenshot":
	commands.getstatusoutput('sudo tar cvf /var/www/html/screenshot.tar screenshot.sh') 

	print "<META HTTP-EQUIV='refresh' content='0; url=/screenshot.tar' target='_blank'/>"

if output=="eog":
	commands.getstatusoutput('sudo tar cvf /var/www/html/eog.tar eog.sh') 

	print "<META HTTP-EQUIV='refresh' content='0; url=/eog.tar' target='_blank'/>"
