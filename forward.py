#!/usr/bin/env python

"""Script for getting emails from procmail and forwarding their
from and subject to another address

Used for bouncing mails to a PUSH server without sending the whole
email.
"""

import sys
import re
import smtplib

__author__ = "Kura"
__copyright__ = "None"
__credits__ = ["Kura"]
__license__ = "Free"
__version__ = "0.1 Beta"
__maintainer__ = "Kura"
__email__ = "kura@deviling.net"
__status__ = "Beta/Test"

content = sys.stdin.read()

from_regex = re.compile(r"[^a-z0-9\-\:\|\s]+From:(\s)?(?P<from>.*)")
subject_regex = re.compile(r"[^a-z0-9\-\:\|\s]+Subject:(\s)?(?P<subject>.*)")

to_addr = <<<ADDRESS_HERE>>>
from_addr = from_regex.search(content).group('from')
subject = subject_regex.search(content).group('subject')

message = """From: %s
To: %s
Subject: %s
""" % (from_addr, to_addr, subject)

smtp = smtplib.SMTP("localhost")
smtp.sendmail(from_addr, to_addr, message)
smtp.quit()
