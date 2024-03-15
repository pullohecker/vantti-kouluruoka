# vantti-kouluruoka
a python script that sends the food info of Vantti school food of the current day to your email. The code is for Koivukylä school, but I checked that Vanttis food is the same everywhere.


usage: python3 ruokaservice.py [-h] server port username password mailbox

positional arguments:

  server      The address or ip of your smtp server

  port        The port of your smtp server
  
  username    The username of your smtp server
  
  password    The password of you'r smtp server
  
  mailbox     The email address that you want the food info to be sent

options:
  
  -h, --help  show this help message and exit

  The script needs smtplib, selenium and chromedriver. Additionally you need to have a running smtp server. I myself use Mailgun, but you can also setup your own smtp server. Mailgun is completely free, but does have some minor restrictions.

  If you want, you can schedule the script to run every morning so you get the days food info every day. If you are lazy, you can run time_ruokapalvelu.py. It sends the food info every day at 7 o'clock in the morning. I do warn that time_ruokapalvelu.py is SUPER shitty and I do recommend just scheduling the execution of ruokapalvelu.py. Also, your machine has to be constantly on.
