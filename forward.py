#!/usr/bin/env python
import sys
import re
import smtplib

content = sys.stdin.read()

from_regex = re.compile(r"From:(\s)?(?P<from>.*)", re.IGNORECASE)
subject_regex = re.compile(r"Subject:(\s)?(?P<subject>.*)", re.IGNORECASE)

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
