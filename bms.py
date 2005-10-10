#!/usr/bin/env python
# A simple milter that has grown quite a bit.
# $Log$
# Revision 1.26  2005/10/07 03:23:40  customdesigned
# Banned users option.  Experimental feature to supply Sender when
# missing and MFROM domain doesn't match From.  Log cipher bits for
# SMTP AUTH.  Sketch access file feature.
#
# Revision 1.25  2005/09/08 03:55:08  customdesigned
# Handle perverse MFROM quoting.
#
# Revision 1.24  2005/08/18 03:36:54  customdesigned
# Don't innoculate with SCREENED mail.
#
# Revision 1.23  2005/08/17 19:35:27  customdesigned
# Send DSN before adding message to quarantine.
#
# Revision 1.22  2005/08/11 22:17:58  customdesigned
# Consider SMTP AUTH connections internal.
#
# Revision 1.21  2005/08/04 21:21:31  customdesigned
# Treat fail like softfail for selected (braindead) domains.
# Treat mail according to extended processing results, but
# report any PermError that would officially result via DSN.
#
# Revision 1.20  2005/08/02 18:04:35  customdesigned
# Keep screened honeypot mail, but optionally discard honeypot only mail.
#
# Revision 1.19  2005/07/20 03:30:04  customdesigned
# Check pydspam version for honeypot, include latest pyspf changes.
#
# Revision 1.18  2005/07/17 01:25:44  customdesigned
# Log as well as use extended result for best guess.
#
# Revision 1.17  2005/07/15 20:25:36  customdesigned
# Use extended results processing for best_guess.
#
# Revision 1.16  2005/07/14 03:23:33  customdesigned
# Make SES package optional.  Initial honeypot support.
#
# Revision 1.15  2005/07/06 04:05:40  customdesigned
# Initial SES integration.
#
# Revision 1.14  2005/07/02 23:27:31  customdesigned
# Don't match hostnames for internal connects.
#
# Revision 1.13  2005/07/01 16:30:24  customdesigned
# Always log trusted Received and Received-SPF headers.
#
# Revision 1.12  2005/06/20 22:35:35  customdesigned
# Setreply for rejectvirus.
#
# Revision 1.11  2005/06/17 02:07:20  customdesigned
# Release 0.8.1
#
# Revision 1.10  2005/06/16 18:35:51  customdesigned
# Ignore HeaderParseError decoding header
#
# Revision 1.9  2005/06/14 21:55:29  customdesigned
# Check internal_domains for outgoing mail.
#
# Revision 1.8  2005/06/06 18:24:59  customdesigned
# Properly log exceptions from pydspam
#
# Revision 1.7  2005/06/04 19:41:16  customdesigned
# Fix bugs from testing RPM
#
# Revision 1.6  2005/06/03 04:57:05  customdesigned
# Organize config reader by section.  Create defang section.
#
# Revision 1.5  2005/06/02 15:00:17  customdesigned
# Configure banned extensions.  Scan zipfile option with test case.
#
# Revision 1.4  2005/06/02 04:18:55  customdesigned
# Update copyright notices after reading article on /.
#
# Revision 1.3  2005/06/02 02:09:00  customdesigned
# Record timestamp in send_dsn.log
#
# Revision 1.2  2005/06/02 01:00:36  customdesigned
# Support configurable templates for DSNs.
#
#
# Revision 1.134  2005/05/25 15:36:43  stuart
# Use dynip module.
# Support smart aliasing of wiretap destination.
# Always send DSN for SOFTFAIL.
# Close forged bounce loophole when there are no headers.
#
# Revision 1.133  2005/03/16 21:58:04  stuart
# Auto DSN feature.
#
# Revision 1.132  2005/02/12 02:11:10  stuart
# Pass unit tests with python2.4.
#
# Revision 1.131  2005/02/11 18:34:13  stuart
# Handle garbage after quote in boundary.
#
# Revision 1.130  2005/02/10 01:10:58  stuart
# Fixed MimeMessage.ismodified()
#
# Revision 1.129  2005/02/10 00:56:48  stuart
# Runs with python2.4.  Defang not working correctly - more work needed.
#
# Revision 1.128  2005/02/09 17:53:34  stuart
# Optionally run dspam on internal mail.
#
# Revision 1.127  2004/12/03 14:26:21  stuart
# Mark DYN PTR, REJECT softfail, log Received-SPF from trusted MTA.
#
# Revision 1.126  2004/11/24 14:39:38  stuart
# Also accept softfail if valid PTR or HELO.
#
# Revision 1.125  2004/11/19 16:40:14  stuart
# Block softfail except for listed domains.
#
# Revision 1.124  2004/11/19 06:18:04  stuart
# block softfail for configured domains only
#
# Revision 1.123  2004/11/18 20:36:49  stuart
# Recognize more dynamic hosts.  Ignore dynamic PTR for best_guess.
#
# Revision 1.122  2004/11/18 17:16:10  stuart
# Recognize more dynamic ips.
#
# Revision 1.121  2004/11/09 22:37:48  stuart
# Don't accept helo names which are dynamic IP addresses.
#
# Revision 1.120  2004/11/09 20:33:50  stuart
# Recognize more dynamic PTR variations.
#
# Revision 1.118  2004/08/30 21:19:50  stuart
# Try best guess for HELO, expand setreply for common errors
#
# Revision 1.117  2004/08/23 02:27:53  stuart
# Allow multi rcpt CBV.  Add some multiline replies.
#
# Revision 1.116  2004/08/20 22:27:52  stuart
# Generate TEMPFAIL for SPF softfail.
#
# Revision 1.115  2004/08/19 20:55:49  stuart
# Always show reversed SRS path.
# Check if encodings are an ASCII superset.  Some messages were encoded as
# BIG5 and getting rejected even though chars were all in ascii subset.
#
# Revision 1.114  2004/07/27 00:40:12  stuart
# Make reject on no PTR optional.
#
# Revision 1.113  2004/07/23 23:11:14  stuart
# Log known malformed messages differently than general processing exceptions.
#
# Revision 1.112  2004/07/21 19:18:33  stuart
# Punt on UnicodeDecodeError when decoding headers.
# Accept a pass with default SPF for missing reverse IP.
#
# Revision 1.111  2004/07/18 13:13:31  stuart
# Reject invalid SRS only for SRS domain (which is the only one we
# know the key for).
# Reject senders that have neither reverse IP nor SPF.
#
# Revision 1.110  2004/06/12 03:13:18  stuart
# Block bounces only for SRS domain.  Also treat mail from
# postmaster or mailer-daemon as DSN for SRS/SES checking purposes.
#
# Revision 1.109  2004/05/01 02:56:55  stuart
# Let multiple screeners share work.
#
# Revision 1.108  2004/04/29 20:36:23  stuart
# Require HELO name
#
# Revision 1.107  2004/04/24 22:55:29  stuart
# Move some files to make the RPM more standard.
#
# Revision 1.106  2004/04/21 18:29:08  stuart
# Validate hello name with SPF.
#
# Revision 1.105  2004/04/20 15:16:00  stuart
# Release 0.6.9
#
# Revision 1.104  2004/04/19 21:56:26  stuart
# Support SPF best_guess and get_header
#
# Revision 1.103  2004/04/10 02:31:01  stuart
# Fix timeout config
#
# Revision 1.102  2004/04/08 20:25:11  stuart
# Make libmilter timeout a config option
#
# Revision 1.101  2004/04/08 19:18:16  stuart
# Preserve case of local part in sender
#
# Revision 1.100  2004/04/08 18:41:15  stuart
# Reject numeric hello names
#
# Revision 1.99  2004/04/06 19:46:39  stuart
# Reject invalid SRS immediately for benefit of CallBack Verifiers.
#
# Revision 1.98  2004/04/06 15:28:20  stuart
# Release 0.6.8-2
#
# Revision 1.97  2004/04/06 13:07:43  stuart
# Pass original header name to check_header
#
# Revision 1.96  2004/04/06 03:27:03  stuart
# bugs from Redhat 9 testing
#
# Revision 1.95  2004/04/05 22:37:08  stuart
# Include Received-SPF headers in dspam.
#
# Revision 1.94  2004/04/05 22:16:50  stuart
# Separate check_header method taking decoded header.
# Reject multiple recipients for a bounce.
#
# Revision 1.93  2004/04/01 20:57:45  stuart
# Report only SRS like addresses as spoofed.
# Return TEMPFAIL on SPF error.
#
# Revision 1.92  2004/03/25 17:45:53  stuart
# Make spf_reject_neutral global in bms.py
#
# Revision 1.91  2004/03/25 03:38:02  stuart
# Reject neutral SPF result for selected domains.
#
# Revision 1.90  2004/03/25 03:27:33  stuart
# Support delegation of SPF records.
#
# Revision 1.89  2004/03/23 22:02:49  stuart
# Header decoding bug.
#
# Revision 1.88  2004/03/23 05:08:45  stuart
# Decode headers, indirect srs config.
#
# Revision 1.87  2004/03/18 02:21:16  stuart
# SRS checking
#
# Revision 1.86  2004/03/11 05:00:37  stuart
# Don't wipe out fail messages from SPF records.
# Hello blacklist
#
# Revision 1.85  2004/03/10 01:49:22  stuart
# Enhanced SPF support.
#
# Revision 1.84  2004/03/09 17:04:49  stuart
# Received-SPF header.
#
# Revision 1.83  2004/03/08 20:23:26  stuart
# SPF support
#
# Revision 1.82  2004/03/01 18:56:50  stuart
# Support progress reporting.
#
# Revision 1.81  2004/03/01 18:36:09  stuart
# Trusted relay.
#
# Revision 1.80  2004/01/12 21:10:58  stuart
# Support wildcard user for smart_alias
#
# Revision 1.79  2003/12/04 23:46:06  stuart
# Release 0.6.4
#
# Author: Stuart D. Gathman <stuart@bmsi.com>
# Copyright 2001,2002,2003,2004,2005 Business Management Systems, Inc.
# This code is under the GNU General Public License.  See COPYING for details.

import sys
import os
import StringIO
import rfc822
import mime
import email.Errors
import Milter
import tempfile
import traceback
import ConfigParser
import time
import re
import anydbm
import Milter.dsn as dsn
from Milter.dynip import is_dynip as dynip

from fnmatch import fnmatchcase
from email.Header import decode_header

# Import pysrs if available
try:
  import SRS
  srsre = re.compile(r'^SRS[01][+-=]',re.IGNORECASE)
except: SRS = None
try:
  import SES
except: SES = None

# Import spf if available
try: import spf
except: spf = None

ip4re = re.compile(r'^[1-9][0-9]*\.[1-9][0-9]*\.[1-9][0-9]*\.[1-9][0-9]*$')
#import syslog
#syslog.openlog('milter')

# Thanks to Chris Liechti for config parsing suggestions

# Global configuration defaults suitable for test framework.
socketname = "/tmp/pythonsock"
reject_virus_from = ()
wiretap_users = {}
discard_users = {}
wiretap_dest = None
blind_wiretap = True
check_user = {}
block_forward = {}
hide_path = ()
log_headers = False
block_chinese = False
spam_words = ()
porn_words = ()
banned_exts = mime.extlist.split(',')
scan_zip = False
scan_html = True
scan_rfc822 = True
internal_connect = ()
trusted_relay = ()
internal_domains = ()
banned_users = ()
hello_blacklist = ()
smart_alias = {}
dspam_dict = None
dspam_users = {}
dspam_userdir = None
dspam_exempt = {}
dspam_whitelist = {}
dspam_screener = ()
dspam_internal = True	# True if internal mail should be dspammed
dspam_reject = ()
dspam_sizelimit = 180000
srs = None
ses = None
srs_reject_spoofed = False
srs_domain = None
spf_reject_neutral = ()
spf_accept_softfail = ()
spf_accept_fail = ()
spf_best_guess = False
spf_reject_noptr = False
supply_sender = False
access_file = None
time_format = '%Y%b%d %H:%M:%S %Z'
timeout = 600
cbv_cache = {}
try:
  too_old = time.time() - 7*24*60*60	# 7 days
  for ln in open('send_dsn.log'):
    try:
      rcpt,ts = ln.strip().split(None,1)
      l = time.strptime(ts,time_format)
      t = time.mktime(l)
      if t > too_old:
	cbv_cache[rcpt] = None
    except:
      cbv_cache[ln.strip()] = None
except IOError: pass

class MilterConfigParser(ConfigParser.ConfigParser):

  def getlist(self,sect,opt):
    if self.has_option(sect,opt):
      return [q.strip() for q in self.get(sect,opt).split(',')]
    return []

  def getaddrset(self,sect,opt):
    if not self.has_option(sect,opt):
      return {}
    s = self.get(sect,opt)
    d = {}
    for q in s.split(','):
      q = q.strip()
      if q.startswith('file:'):
        domain = q[5:]
	d[domain] = d.setdefault(domain,[]) + open(domain,'r').read().split()
      else:
	user,domain = q.split('@')
	d.setdefault(domain,[]).append(user)
    return d
  
  def getaddrdict(self,sect,opt):
    if not self.has_option(sect,opt):
      return {}
    d = {}
    for q in self.get(sect,opt).split(','):
      q = q.strip()
      if self.has_option(sect,q):
        l = self.get(sect,q)
	for addr in l.split(','):
	  addr = addr.strip()
	  if addr.startswith('file:'):
	    fname = addr[5:]
	    for a in open(fname,'r').read().split():
	      d[a] = q
	  else:
	    d[addr] = q
    return d

  def getdefault(self,sect,opt,default=None):
    if self.has_option(sect,opt):
      return self.get(sect,opt)
    return default

def read_config(list):
  cp = MilterConfigParser({
    'tempdir': "/var/log/milter/save",
    'socket': "/var/run/milter/pythonsock",
    'timeout': '600',
    'scan_html': 'no',
    'scan_rfc822': 'yes',
    'scan_zip': 'no',
    'block_chinese': 'no',
    'log_headers': 'no',
    'blind_wiretap': 'yes',
    'maxage': '8',
    'hashlength': '8',
    'reject_spoofed': 'no',
    'reject_noptr': 'no',
    'supply_sender': 'no',
    'best_guess': 'no',
    'dspam_internal': 'yes'
  })
  cp.read(list)

  # milter section
  tempfile.tempdir = cp.get('milter','tempdir')
  global socketname, timeout, check_user, log_headers
  global internal_connect, internal_domains, trusted_relay, hello_blacklist
  socketname = cp.get('milter','socket')
  timeout = cp.getint('milter','timeout')
  check_user = cp.getaddrset('milter','check_user')
  log_headers = cp.getboolean('milter','log_headers')
  internal_connect = cp.getlist('milter','internal_connect')
  internal_domains = cp.getlist('milter','internal_domains')
  trusted_relay = cp.getlist('milter','trusted_relay')
  hello_blacklist = cp.getlist('milter','hello_blacklist')

  # defang section
  global scan_rfc822, scan_html, block_chinese, scan_zip, block_forward
  global banned_exts, porn_words, spam_words
  if cp.has_section('defang'):
    section = 'defang'
    # for backward compatibility,
    # banned extensions defaults to empty only when defang section exists
    banned_exts = cp.getlist(section,'banned_exts')
  else:	# use milter section if no defang section for compatibility
    section = 'milter'
  scan_rfc822 = cp.getboolean(section,'scan_rfc822')
  scan_zip = cp.getboolean(section,'scan_zip')
  scan_html = cp.getboolean(section,'scan_html')
  block_chinese = cp.getboolean(section,'block_chinese')
  block_forward = cp.getaddrset(section,'block_forward')
  porn_words = cp.getlist(section,'porn_words')
  spam_words = cp.getlist(section,'spam_words')

  # scrub section
  global hide_path, reject_virus_from
  hide_path = cp.getlist('scrub','hide_path')
  reject_virus_from = cp.getlist('scrub','reject_virus_from')

  # wiretap section
  global blind_wiretap, wiretap_users, wiretap_dest, discard_users
  blind_wiretap = cp.getboolean('wiretap','blind')
  wiretap_users = cp.getaddrset('wiretap','users')
  discard_users = cp.getaddrset('wiretap','discard')
  wiretap_dest = cp.getdefault('wiretap','dest')
  if wiretap_dest: wiretap_dest = '<%s>' % wiretap_dest

  global smart_alias
  for sa in cp.getlist('wiretap','smart_alias'):
    sm = cp.getlist('wiretap',sa)
    if len(sm) < 2:
      print 'malformed smart alias:',sa
      continue
    if len(sm) == 2: sm.append(sa)
    key = (sm[0],sm[1])
    smart_alias[key] = sm[2:]

  # dspam section
  global dspam_dict, dspam_users, dspam_userdir, dspam_exempt, dspam_internal
  global dspam_screener,dspam_whitelist,dspam_reject,dspam_sizelimit
  dspam_dict = cp.getdefault('dspam','dspam_dict')
  dspam_exempt = cp.getaddrset('dspam','dspam_exempt')
  dspam_whitelist = cp.getaddrset('dspam','dspam_whitelist')
  dspam_users = cp.getaddrdict('dspam','dspam_users')
  dspam_userdir = cp.getdefault('dspam','dspam_userdir')
  dspam_screener = cp.getlist('dspam','dspam_screener')
  dspam_reject = cp.getlist('dspam','dspam_reject')
  dspam_internal = cp.getboolean('dspam','dspam_internal')
  if cp.has_option('dspam','dspam_sizelimit'):
    dspam_sizelimit = cp.getint('dspam','dspam_sizelimit')

  # spf section
  global spf_reject_neutral,spf_best_guess,SRS,spf_reject_noptr
  global spf_accept_softfail,spf_accept_fail,supply_sender,access_file
  if spf:
    spf.DELEGATE = cp.getdefault('spf','delegate')
    spf_reject_neutral = cp.getlist('spf','reject_neutral')
    spf_accept_softfail = cp.getlist('spf','accept_softfail')
    spf_accept_fail = cp.getlist('spf','accept_fail')
    spf_best_guess = cp.getboolean('spf','best_guess')
    spf_reject_noptr = cp.getboolean('spf','reject_noptr')
    supply_sender = cp.getboolean('spf','supply_sender')
    access_file = cp.getdefault('spf','access_file')
  srs_config = cp.getdefault('srs','config')
  if srs_config: cp.read([srs_config])
  srs_secret = cp.getdefault('srs','secret')
  if SRS and srs_secret:
    global ses,srs,srs_reject_spoofed,srs_domain,banned_users
    database = cp.getdefault('srs','database')
    srs_reject_spoofed = cp.getboolean('srs','reject_spoofed')
    maxage = cp.getint('srs','maxage')
    hashlength = cp.getint('srs','hashlength')
    separator = cp.getdefault('srs','separator','=')
    if database:
      import SRS.DB
      srs = SRS.DB.DB(database=database,secret=srs_secret,
        maxage=maxage,hashlength=hashlength,separator=separator)
    else:
      srs = SRS.Guarded.Guarded(secret=srs_secret,
        maxage=maxage,hashlength=hashlength,separator=separator)
    if SES:
      ses = SES.new(secret=srs_secret,expiration=maxage)
      srs_domain = cp.getlist('srs','ses')
    else:
      srs_domain = []
    srs_domain.append(cp.getdefault('srs','fwdomain'))
    banned_users = cp.getlist('srs','banned_users')
    #print srs_domain

def parse_addr(t):
  """Split email into user,domain.

  >>> parse_addr('user@example.com')
  ['user', 'example.com']
  >>> parse_addr('"user@example.com"')
  ['"user@example.com"']
  >>> parse_addr('"user@bar"@example.com')
  ['"user@bar"','example.com']
  >>> parse_addr('foo')
  ['foo']
  """
  if t.startswith('<') and t.endswith('>'): t = t[1:-1]
  if t.startswith('"'):
    if t.endswith('"'): return [t[1:-1]]
    pos = t.find('"@')
    if pos > 0: return [t[1:pos],t[pos+2:]]
  return t.split('@')

def parse_header(val):
  """Decode headers gratuitously encoded to hide the content.
  """
  try:
    h = decode_header(val)
    if not len(h) or (not h[0][1] and len(h) == 1): return val
    u = []
    for s,enc in h:
      if enc:
        try:
	  u.append(unicode(s,enc))
	except LookupError:
	  u.append(unicode(s))
      else:
	u.append(unicode(s))
    u = ''.join(u)
    for enc in ('us-ascii','iso-8859-1','utf8'):
      try:
	return u.encode(enc)
      except UnicodeError: continue
  except UnicodeDecodeError: pass
  except LookupError: pass
  except email.Errors.HeaderParseError: pass
  return val

class SPFPolicy(object):
  "Get SPF policy by result, defaulting to classic policy from pymilter.cfg"
  def __init__(self,domain):
    self.domain = domain.lower()
    if access_file:
      try: acf = anydbm.open(access_file,'r')
      except: acf = None
    else: acf = None
    self.acf = acf

  def getPolicy(self,pfx):
    acf = self.acf
    if not acf: return None
    try:
      return acf[pfx + self.domain]
    except KeyError:
      try:
	return acf[pfx]
      except KeyError:
        return None

  def getFailPolicy(self):
    policy = self.getPolicy('SPF-Fail:')
    if not policy:
      if self.domain in spf_accept_fail:
        policy = 'CBV'
      else:
	policy = 'REJECT'
    return policy

  def getNonePolicy(self):
    policy = self.getPolicy('SPF-None:')
    if not policy:
      if spf_reject_noptr:
	policy = 'REJECT'
      else:
        policy = 'CBV'
    return policy

  def getSoftfailPolicy(self):
    policy = self.getPolicy('SPF-Softfail:')
    if not policy:
      if self.domain in spf_accept_softfail:
        policy = 'OK'
      elif self.domain in spf_reject_neutral:
        policy = 'REJECT'
      else:
        policy = 'CBV'
    return policy

  def getNeutralPolicy(self):
    policy = self.getPolicy('SPF-Neutral:')
    if not policy:
      if self.domain in spf_reject_neutral:
        policy = 'REJECT'
      policy = 'OK'
    return policy

  def getPermErrorPolicy(self):
    policy = self.getPolicy('SPF-PermError:')
    if not policy:
      policy = 'REJECT'
    return policy

  def getPassPolicy(self):
    policy = self.getPolicy('SPF-Pass:')
    if not policy:
      policy = 'OK'
    return policy

class bmsMilter(Milter.Milter):
  """Milter to replace attachments poisonous to Windows with a WARNING message,
     check SPF, and other anti-forgery features, and implement wiretapping
     and smart alias redirection."""

  def log(self,*msg):
    print "%s [%d]" % (time.strftime('%Y%b%d %H:%M:%S'),self.id),
    for i in msg: print i,
    print

  def __init__(self):
    self.tempname = None
    self.mailfrom = None	# sender in SMTP form
    self.canon_from = None	# sender in end user form
    self.fp = None
    self.bodysize = 0
    self.id = Milter.uniqueID()

  # delrcpt can only be called from eom().  This accumulates recipient
  # changes which can then be applied by alter_recipients()
  def del_recipient(self,rcpt):
    rcpt = rcpt.lower()
    if not rcpt in self.discard_list:
      self.discard_list.append(rcpt)

  # addrcpt can only be called from eom().  This accumulates recipient
  # changes which can then be applied by alter_recipients()
  def add_recipient(self,rcpt):
    rcpt = rcpt.lower()
    if not rcpt in self.redirect_list:
      self.redirect_list.append(rcpt)

  # addheader can only be called from eom().  This accumulates added headers
  # which can then be applied by alter_headers()
  def add_header(self,name,val):
    self.new_headers.append((name,val))
    self.log('%s: %s' % (name,val))

  def connect(self,hostname,unused,hostaddr):
    self.internal_connection = False
    self.trusted_relay = False
    self.receiver = self.getsymval('j')
    if hostaddr and len(hostaddr) > 0:
      ipaddr = hostaddr[0]
      for pat in internal_connect:
	if fnmatchcase(ipaddr,pat):
	  self.internal_connection = True
	  break
      for pat in trusted_relay:
	if fnmatchcase(ipaddr,pat):
	  self.trusted_relay = True
	  break
    else: ipaddr = ''
    self.connectip = ipaddr
    self.missing_ptr = dynip(hostname,self.connectip)
    if self.internal_connection:
      connecttype = 'INTERNAL'
    else:
      connecttype = 'EXTERNAL'
    if self.trusted_relay:
      connecttype += ' TRUSTED'
    if self.missing_ptr:
      connecttype += ' DYN'
    self.log("connect from %s at %s %s" % (hostname,hostaddr,connecttype))
    self.hello_name = None
    self.connecthost = hostname
    if hostname == 'localhost' and not ipaddr.startswith('127.') \
    or hostname == '.':
      self.log("REJECT: PTR is",hostname)
      self.setreply('550','5.7.1', '"%s" is not a reasonable PTR name'%hostname)
      return Milter.REJECT
    return Milter.CONTINUE

  def hello(self,hostname):
    self.hello_name = hostname
    self.log("hello from %s" % hostname)
    if ip4re.match(hostname):
      self.log("REJECT: numeric hello name:",hostname)
      self.setreply('550','5.7.1','hello name cannot be numeric ip')
      return Milter.REJECT
    if not self.internal_connection and hostname in hello_blacklist:
      self.log("REJECT: spam from self:",hostname)
      self.setreply('550','5.7.1','I hate talking to myself.')
      return Milter.REJECT
    return Milter.CONTINUE

  def smart_alias(self,to):
    if smart_alias:
      t = parse_addr(to.lower())
      if len(t) == 2:
	ct = '@'.join(t)
      else:
	ct = t[0]
      cf = self.canon_from
      cf0 = cf.split('@',1)
      if len(cf0) == 2:
	cf0 = '@' + cf0[1]
      else:
	cf0 = cf
      for key in ((cf,ct),(cf0,ct)):
	if smart_alias.has_key(key):
	  self.del_recipient(to)
	  for t in smart_alias[key]:
	    self.add_recipient('<%s>'%t)

  # multiple messages can be received on a single connection
  # envfrom (MAIL FROM in the SMTP protocol) seems to mark the start
  # of each message.
  def envfrom(self,f,*str):
    self.log("mail from",f,str)
    self.fp = StringIO.StringIO()
    self.tempname = None
    self.mailfrom = f
    self.forward = True
    self.bodysize = 0
    self.hidepath = False
    self.discard = False
    self.dspam = True
    self.reject_spam = True
    self.data_allowed = True
    self.trust_received = self.trusted_relay
    self.trust_spf = self.trusted_relay
    self.redirect_list = []
    self.discard_list = []
    self.new_headers = []
    self.recipients = []
    self.cbv_needed = None
    t = parse_addr(f)
    if len(t) == 2: t[1] = t[1].lower()
    self.canon_from = '@'.join(t)
    # Some braindead MTAs can't be relied upon to properly flag DSNs.
    # This heuristic tries to recognize such.
    self.is_bounce = (f == '<>' or t[0].lower() in banned_users
        #and t[1] == self.hello_name
    )

    # Check SMTP AUTH, also available:
    #   auth_authen  authenticated user
    #   auth_author  (ESMTP AUTH= param)
    #   auth_ssf     (connection security, 0 = unencrypted)
    #   auth_type    (authentication method, CRAM-MD5, DIGEST-MD5, PLAIN, etc)
    # cipher_bits  SSL encryption strength
    # cert_subject SSL cert subject
    # verify       SSL cert verified

    self.user = self.getsymval('{auth_authen}')
    if self.user:
      # Very simple SMTP AUTH policy by defaul:
      #   any successful authentication is considered INTERNAL
      # FIXME: configure allowed MAIL FROM by user
      self.internal_connection = True
      self.log(
        "SMTP AUTH:",self.user, self.getsymval('{auth_type}'),
        "sslbits =",self.getsymval('{cipher_bits}'),
        "ssf =",self.getsymval('{auth_ssf}'), "INTERNAL"
      )
      if self.getsymval('{verify}'):
	self.log("SSL AUTH:",
	  self.getsymval('{cert_subject}'),
	  "verify =",self.getsymval('{verify}')
	)

    self.fp.write('From %s %s\n' % (self.canon_from,time.ctime()))
    if len(t) == 2:
      user,domain = t
      if not self.internal_connection:
	for pat in internal_domains:
	  if fnmatchcase(domain,pat):
	    self.log("REJECT: spam from self",pat)
	    self.setreply('550','5.7.1','I hate talking to myself.')
	    return Milter.REJECT
      elif internal_domains:
	for pat in internal_domains:
	  if fnmatchcase(domain,pat): break
	else:
	  self.log("REJECT: zombie PC at ",self.connectip," sending MAIL FROM ",
	  	self.canon_from)
	  self.setreply('550','5.7.1',
	  'Your PC is using an unauthorized MAIL FROM.',
	  'It is either badly misconfigured or controlled by organized crime.'
	  )
	  return Milter.REJECT
      self.rejectvirus = domain in reject_virus_from
      if user in wiretap_users.get(domain,()):
        self.add_recipient(wiretap_dest)
	self.smart_alias(wiretap_dest)
      if user in discard_users.get(domain,()):
	self.discard = True
      exempt_users = dspam_whitelist.get(domain,())
      if user in exempt_users or '' in exempt_users:
	self.dspam = False
    else:
      self.rejectvirus = False
    if not self.hello_name:
      self.log("REJECT: missing HELO")
      self.setreply('550','5.7.1',"It's polite to say HELO first.")
      return Milter.REJECT
    if not (self.internal_connection or self.trusted_relay)	\
    	and self.connectip and spf:
      return self.check_spf()
    self.spf = None
    return Milter.CONTINUE

  def check_spf(self):
    receiver = self.receiver
    q = spf.query(self.connectip,self.canon_from,self.hello_name,
    	receiver=receiver,strict=False)
    q.set_default_explanation(
      'SPF fail: see http://openspf.com/why.html?sender=%s&ip=%s' % (q.s,q.i))
    res,code,txt = q.check()
    q.result = res
    if res in ('unknown','permerror') and q.perm_error and q.perm_error.ext:
      self.cbv_needed = q	# report SPF syntax error to sender
      res,code,txt = q.perm_error.ext	# extended (lax processing) result
      txt = 'EXT: ' + txt
    p = SPFPolicy(q.o)
    if res in ('none','softfail','deny','fail','neutral'):
      if self.mailfrom != '<>':
	# check hello name via spf unless spf pass
	h = spf.query(self.connectip,'',self.hello_name,receiver=receiver)
	hres,hcode,htxt = h.check()
	if hres in ('deny','fail','neutral','softfail'):
	  self.log('REJECT: hello SPF: %s 550 %s' % (hres,htxt))
	  self.setreply('550','5.7.1',htxt,
	    "The hostname given in your MTA's HELO response is not listed",
	    "as a legitimate MTA in the SPF records for your domain.  If you",
	    "get this bounce, the message was not in fact a forgery, and you",
	    "should IMMEDIATELY notify your email administrator of the problem."
	  )
	  return Milter.REJECT
	if hres == 'none' and spf_best_guess \
	  and not dynip(self.hello_name,self.connectip):
	  hres,hcode,htxt = h.best_guess()
      else: hres = res
      ores = res
      if spf_best_guess and res == 'none':
	#self.log('SPF: no record published, guessing')
	q.set_default_explanation(
		'SPF guess: see http://spf.pobox.com/why.html')
	# best_guess should not result in fail
	if self.missing_ptr:
	  # ignore dynamic PTR for best guess
	  res,code,txt = q.best_guess('v=spf1 a/24 mx/24')
	else:
	  res,code,txt = q.best_guess()
	receiver += ': guessing'
        if q.perm_error:	# FIXME: should never happen?
          res,code,txt = q.perm_error.ext	# extended result
	  txt = 'EXT: ' + txt
      if self.missing_ptr and ores == 'none' and res != 'pass' \
      		and hres != 'pass':
	policy = p.getNonePolicy()
	if policy == 'CBV':
	  if self.mailfrom != '<>':
	    q.result = ores
	    self.cbv_needed = q	# accept, but inform sender via DSN
	elif policy != 'OK':
	  self.log('REJECT: no PTR, HELO or SPF')
	  self.setreply('550','5.7.1',
    "You must have a reverse lookup or publish SPF: http://spf.pobox.com",
    "Contact your mail administrator IMMEDIATELY!  Your mail server is",
    "severely misconfigured.  It has no PTR record (dynamic PTR records",
    "that contain your IP don't count), an invalid HELO, and no SPF record."
	  )
	  return Milter.REJECT
    if res in ('deny', 'fail'):
      policy = p.getFailPolicy()
      if hres == 'pass' and policy == 'CBV':
	if self.mailfrom != '<>':
	  self.cbv_needed = q
      elif policy != 'OK':
	self.log('REJECT: SPF %s %i %s' % (res,code,txt))
	self.setreply(str(code),'5.7.1',txt)
	# A proper SPF fail error message would read:
	# forger.biz [1.2.3.4] is not allowed to send mail with the domain
	# "forged.org" in the sender address.  Contact <postmaster@forged.org>.
	return Milter.REJECT
    if res == 'softfail':
      policy = p.getSoftfailPolicy()
      if policy == 'CBV' and hres == 'pass':
	if self.mailfrom != '<>':
	  self.cbv_needed = q
      elif policy != 'OK':
	self.log('REJECT: SPF %s %i %s' % (res,code,txt))
	self.setreply('550','5.7.1',
	  'SPF softfail: If you get this Delivery Status Notice, your email',
	  'was probably legitimate.  Your administrator has published SPF',
	  'records in a testing mode.  The SPF record reported your email as',
	  'a forgery, which is a mistake if you are reading this.  Please',
	  'notify your administrator of the problem immediately.'
	)
	return Milter.REJECT
    if res == 'neutral' and q.o in spf_reject_neutral:
      policy = p.getNeutralPolicy()
      if policy == 'CBV' and hres == 'pass':
	if self.mailfrom != '<>':
	  self.cbv_needed = q
      elif policy != 'OK':
	self.log('REJECT: SPF neutral for',q.s)
	self.setreply('550','5.7.1',
	  'mail from %s must pass SPF: http://spf.pobox.com/why.html' % q.o,
	  'The %s domain is one that spammers love to forge.  Due to' % q.o,
	  'the volume of forged mail, we can only accept mail that',
	  'the SPF record for %s explicitly designates as legitimate.' % q.o,
	  'Sending your email through the recommended outgoing SMTP',
	  'servers for %s should accomplish this.' % q.o
	)
	return Milter.REJECT
    if res in ('unknown','permerror'):
      policy = p.getPermErrorPolicy()
      if policy == 'CBV' and hres == 'pass':
	if self.mailfrom != '<>':
	  self.cbv_needed = q
      elif policy != 'OK':
	self.log('REJECT: SPF %s %i %s' % (res,code,txt))
	# latest SPF draft recommends 5.5.2 instead of 5.7.1
	self.setreply(str(code),'5.5.2',txt,
	  'There is a fatal syntax error in the SPF record for %s' % q.o,
	  'We cannot accept mail from %s until this is corrected.' % q.o
	)
	return Milter.REJECT
    if res in ('error','temperror'):
      self.log('TEMPFAIL: SPF %s %i %s' % (res,code,txt))
      self.setreply(str(code),'4.3.0',txt)
      return Milter.TEMPFAIL
    self.add_header('Received-SPF',q.get_header(res,receiver))
    self.spf = q
    return Milter.CONTINUE

  # hide_path causes a copy of the message to be saved - until we
  # track header mods separately from body mods - so use only
  # in emergencies.
  def envrcpt(self,to,*str):
    # mail to MAILER-DAEMON is generally spam that bounced
    if to.startswith('<MAILER-DAEMON@'):
      self.log('DISCARD: RCPT TO:',to,str)
      return Milter.DISCARD
    self.log("rcpt to",to,str)
    t = parse_addr(to.lower())
    if len(t) == 2:
      user,domain = t
      if self.is_bounce and srs and domain in srs_domain:
	oldaddr = '@'.join(parse_addr(to))
	try:
	  if ses:
	    newaddr = ses.verify(oldaddr)
	  else:
	    newaddr = oldaddr,
	  if len(newaddr) > 1:
	    self.log("ses rcpt:",newaddr[0])
	  else:
	    newaddr = srs.reverse(oldaddr)
	    # Currently, a sendmail map reverses SRS.  We just log it here.
	    self.log("srs rcpt:",newaddr)
	except:
	  if not (self.internal_connection or self.trusted_relay):
	    if srsre.match(oldaddr):
	      self.log("REJECT: srs spoofed:",oldaddr)
	      self.setreply('550','5.7.1','Invalid SRS signature')
	      return Milter.REJECT
	    if oldaddr.startswith('SES='):
	      self.log("REJECT: ses spoofed:",oldaddr)
	      self.setreply('550','5.7.1','Invalid SES signature')
	      return Milter.REJECT
	    self.data_allowed = not srs_reject_spoofed

      # non DSN mail to SRS address will bounce due to invalid local part
      self.recipients.append('@'.join(t))
      users = check_user.get(domain)
      if self.discard:
        self.del_recipient(to)
      if users and not user in users:
        self.log('REJECT: RCPT TO:',to)
	return Milter.REJECT
      if user in block_forward.get(domain,()):
        self.forward = False
      exempt_users = dspam_exempt.get(domain,())
      if user in exempt_users or '' in exempt_users:
	self.dspam = False
      if domain in hide_path:
        self.hidepath = True
      if not domain in dspam_reject:
        self.reject_spam = False
    self.smart_alias(to)
    #rcpt = self.getsymval("{rcpt_addr}")
    #self.log("rcpt-addr",rcpt);
    return Milter.CONTINUE

  # Heuristic checks for spam headers
  def check_header(self,name,val):
    lname = name.lower()
    # val is decoded header value
    if lname == 'subject':
      
      # check for common spam keywords
      for wrd in spam_words:
        if val.find(wrd) >= 0:
	  self.log('REJECT: %s: %s' % (name,val))
	  self.setreply('550','5.7.1','That subject is not allowed')
	  return Milter.REJECT

      # check for spam that claims to be legal
      lval = val.lower().strip()
      for adv in ("adv:","adv.","adv ","[adv]","(adv)","advt:","advert:"):
        if lval.startswith(adv):
	  self.log('REJECT: %s: %s' % (name,val))
	  self.setreply('550','5.7.1','Advertising not accepted here')
	  return Milter.REJECT
      for adv in ("adv","(adv)","[adv]"):
        if lval.endswith(adv):
	  self.log('REJECT: %s: %s' % (name,val))
	  self.setreply('550','5.7.1','Advertising not accepted here')
	  return Milter.REJECT

      # check for porn keywords
      for w in porn_words:
        if lval.find(w) >= 0:
          self.log('REJECT: %s: %s' % (name,val))
	  self.setreply('550','5.7.1','That subject is not allowed')
          return Milter.REJECT

      # check for annoying forwarders
      if not self.forward:
	if lval.startswith("fwd:") or lval.startswith("[fw"):
	  self.log('REJECT: %s: %s' % (name,val))
	  self.setreply('550','5.7.1','I find unedited forwards annoying')
	  return Milter.REJECT

    # check for invalid message id
    if lname == 'message-id' and len(val) < 4:
      self.log('REJECT: %s: %s' % (name,val))
      return Milter.REJECT

    # check for common bulk mailers
    if lname == 'x-mailer':
      mailer = val.lower()
      if mailer in ('direct email','calypso','mail bomber') \
	or mailer.find('optin') >= 0:
        self.log('REJECT: %s: %s' % (name,val))
        return Milter.REJECT
    return Milter.CONTINUE

  def forged_bounce(self):
    if self.mailfrom != '<>':
      self.log("REJECT: bogus DSN")
      self.setreply('550','5.7.1',
	"I do not accept mail from postmaster, mailer-daemon, or clamav.",
	"All such mail has turned out to be Delivery Status Notifications",
	"which failed to be marked as such.  Please send a real DSN if",
	"you need to.  Use another MAIL FROM if you need to send me mail."
      )
    else:
      self.log('REJECT: bounce with no SRS encoding')
      self.setreply('550','5.7.1',
	"I did not send you that message. Please consider implementing SPF",
	"(http://openspf.com) to avoid bouncing mail to spoofed senders.",
	"Thank you."
      )
    return Milter.REJECT
    
  def header(self,name,hval):
    if not self.data_allowed:
      return self.forged_bounce()
	  
    lname = name.lower()
    # decode near ascii text to unobfuscate
    val = parse_header(hval)
    if not self.internal_connection:
      # even if we wanted the Taiwanese spam, we can't read Chinese
      if block_chinese and lname == 'subject':
	if val.startswith('=?big5') or val.startswith('=?ISO-2022-JP'):
	  self.log('REJECT: %s: %s' % (name,val))
	  self.setreply('550','5.7.1',"We don't understand chinese")
	  return Milter.REJECT
      rc = self.check_header(name,val)
      if rc != Milter.CONTINUE: return rc
    # log selected headers
    if log_headers or lname in ('subject','x-mailer'):
      self.log('%s: %s' % (name,val))
    elif self.trust_received and lname == 'received':
      self.trust_received = False
      self.log('%s: %s' % (name,val.splitlines()[0]))
    elif self.trust_spf and lname == 'received-spf':
      self.trust_spf = False
      self.log('%s: %s' % (name,val.splitlines()[0]))
    if self.fp:
      try:
        val = val.encode('us-ascii')
      except:
	val = hval
      self.fp.write("%s: %s\n" % (name,val))	# add header to buffer
    return Milter.CONTINUE

  def eoh(self):
    if not self.fp: return Milter.TEMPFAIL	# not seen by envfrom
    if not self.data_allowed:
      return self.forged_bounce()
    for name,val in self.new_headers:
      self.fp.write("%s: %s\n" % (name,val))	# add new headers to buffer
    self.fp.write("\n")				# terminate headers
    # log when neither sender nor from domains matches mail from domain
    if supply_sender and self.mailfrom != '<>':
      mf_domain = self.canon_from.split('@')[-1]
      self.fp.seek(0)
      msg = rfc822.Message(self.fp)
      for rn,hf in msg.getaddrlist('from')+msg.getaddrlist('sender'):
	t = parse_addr(hf)
	if len(t) == 2 and t[1].lower() == mf_domain:
	  break
      else:
	for f in msg.getallmatchingheaders('from'):
	  self.log(f)
	sender = msg.getallmatchingheaders('sender')
	if sender:
	  for f in sender:
	    self.log(f)
	else:
	  self.log("NOTE: Supplying MFROM as Sender");
	  self.add_header('Sender',self.mailfrom)
      del msg
    # copy headers to a temp file for scanning the body
    self.fp.seek(0)
    headers = self.fp.getvalue()
    self.fp.close()
    fd,fname = tempfile.mkstemp(".defang")
    self.tempname = fname
    self.fp = os.fdopen(fd,"w+b")
    self.fp.write(headers)	# IOError (e.g. disk full) causes TEMPFAIL
    # check if headers are really spammy
    if dspam_dict and not self.internal_connection:
      ds = dspam.dspam(dspam_dict,dspam.DSM_PROCESS,
        dspam.DSF_CHAINED|dspam.DSF_CLASSIFY)
      try:
        ds.process(headers)
        if ds.probability > 0.93 and self.dspam:
          self.log('REJECT: X-DSpam-HeaderScore: %f' % ds.probability)
	  self.setreply('550','5.7.1','Your Message looks spammy')
	  return Milter.REJECT
	self.add_header('X-DSpam-HeaderScore','%f'%ds.probability)
      finally:
        ds.destroy()
    return Milter.CONTINUE

  def body(self,chunk):		# copy body to temp file
    if self.fp:
      self.fp.write(chunk)	# IOError causes TEMPFAIL in milter
      self.bodysize += len(chunk)
    return Milter.CONTINUE

  def _headerChange(self,msg,name,value):
    if value:	# add header
      self.addheader(name,value)
    else:	# delete all headers with name
      h = msg.getheaders(name)
      if h:
	for i in range(len(h),0,-1):
	  self.chgheader(name,i-1,'')

  def _chk_ext(self,name):
    "Check a name for dangerous Winblows extensions."
    if not name: return name
    lname = name.lower()
    for ext in self.bad_extensions:
      if lname.endswith(ext): return name
    return None

    
  def _chk_attach(self,msg):
    "Filter attachments by content."
    # check for bad extensions
    mime.check_name(msg,self.tempname,ckname=self._chk_ext,scan_zip=scan_zip)
    # remove scripts from HTML
    if scan_html:
      mime.check_html(msg,self.tempname)	
    # don't let a tricky virus slip one past us
    if scan_rfc822:
      msg = msg.get_submsg()
      if isinstance(msg,email.Message.Message):
	return mime.check_attachments(msg,self._chk_attach)
    return Milter.CONTINUE

  def alter_recipients(self,discard_list,redirect_list):
    for rcpt in discard_list:
      if rcpt in redirect_list: continue
      self.log("DISCARD RCPT: %s" % rcpt)	# log discarded rcpt
      self.delrcpt(rcpt)
    for rcpt in redirect_list:
      if rcpt in discard_list: continue
      self.log("APPEND RCPT: %s" % rcpt)	# log appended rcpt
      self.addrcpt(rcpt)
      if not blind_wiretap:
        self.addheader('Cc',rcpt)

  # check spaminess for recipients in dictionary groups
  # if there are multiple users getting dspammed, then
  # a signature tag for each is added to the message.

  # FIXME: quarantine messages rejected via fixed patterns above
  #	   this will give a fast start to stats

  def check_spam(self):
    "return True/False if self.fp, else return Milter.REJECT/TEMPFAIL/etc"
    if not dspam_userdir: return False
    ds = Dspam.DSpamDirectory(dspam_userdir)
    ds.log = self.log
    ds.headerchange = self._headerChange
    modified = False
    for rcpt in self.recipients:
      if dspam_users.has_key(rcpt):
        user = dspam_users.get(rcpt)
	if user:
	  try:
	    self.fp.seek(0)
	    txt = self.fp.read()
	    if user == 'spam' and self.internal_connection:
	      sender = dspam_users.get(self.canon_from)
	      if sender:
	        self.log("SPAM: %s" % sender)	# log user for FP
		ds.add_spam(sender,txt)
		txt = None
		self.fp = None
		return Milter.DISCARD
	    elif user == 'falsepositive' and self.internal_connection:
	      sender = dspam_users.get(self.canon_from)
	      if sender:
	        self.log("FP: %s" % sender)	# log user for FP
	        txt = ds.false_positive(sender,txt)
		self.fp = StringIO.StringIO(txt)
		self.delrcpt('<%s>' % rcpt)
		self.recipients = None
		self.rejectvirus = False
		return True
	    elif not self.internal_connection or dspam_internal:
	      if len(txt) > dspam_sizelimit:
		self.log("Large message:",len(txt))
		return False
	      if user == 'honeypot' and Dspam.VERSION >= '1.1.9':
	        keep = False	# keep honeypot mail
		self.fp = None
	        if len(self.recipients) > 1:
		  self.log("HONEYPOT:",rcpt,'SCREENED')
		  if self.spf:
		    # check that sender accepts quarantine DSN
		    msg = mime.message_from_file(StringIO.StringIO(txt))
		    rc = self.send_dsn(self.spf,msg,'quarantine.txt')
		    del msg
		    if rc != Milter.CONTINUE:
		      return rc	
		  ds.check_spam(user,txt,self.recipients,quarantine=True,
		  	force_result=dspam.DSR_ISSPAM)
		else:
		  ds.check_spam(user,txt,self.recipients,quarantine=keep,
		  	force_result=dspam.DSR_ISSPAM)
		  self.log("HONEYPOT:",rcpt)
		return Milter.DISCARD
	      txt = ds.check_spam(user,txt,self.recipients)
	      if not txt:
	        # DISCARD if quarrantined for any recipient.  It
		# will be resent to all recipients if they submit
		# as a false positive.
		self.log("DSPAM:",user,rcpt)
		self.fp = None
		return Milter.DISCARD
	      self.fp = StringIO.StringIO(txt)
	      modified = True
	  except Exception,x:
	    self.log("check_spam:",x)
	    traceback.print_exc()
    # screen if no recipients are dspam_users
    if not modified and dspam_screener and not self.internal_connection \
    	and self.dspam:
      self.fp.seek(0)
      txt = self.fp.read()
      if len(txt) > dspam_sizelimit:
	self.log("Large message:",len(txt))
	return False
      screener = dspam_screener[self.id % len(dspam_screener)]
      if not ds.check_spam(screener,txt,self.recipients,
      	classify=True,quarantine=False):
	if self.reject_spam:
	  self.log("DSPAM:",screener,
	  	'REJECT: X-DSpam-Score: %f' % ds.probability)
	  self.setreply('550','5.7.1','Your Message looks spammy')
	  self.fp = None
	  return Milter.REJECT
	self.log("DSPAM:",screener,"SCREENED")
	if self.spf:
	  # check that sender accepts quarantine DSN
	  self.fp.seek(0)
	  msg = mime.message_from_file(self.fp)
	  rc = self.send_dsn(self.spf,msg,'quarantine.txt')
	  if rc != Milter.CONTINUE:
	    self.fp = None
	    return rc
	  del msg
	if not ds.check_spam(screener,txt,self.recipients,classify=True):
	  self.fp = None
	  return Milter.DISCARD
	# Message no longer looks spammy, deliver normally. We lied in the DSN.
    return modified

  def eom(self):
    if not self.fp:
      return Milter.ACCEPT	# no message collected - so no eom processing

    try:
      # analyze external mail for spam
      spam_checked = self.check_spam()	# tag or quarantine for spam
      if not self.fp:
        return spam_checked

      # analyze all mail for dangerous attachments and scripts
      self.fp.seek(0)
      msg = mime.message_from_file(self.fp)
      # pass header changes in top level message to sendmail
      msg.headerchange = self._headerChange

      # filter leaf attachments through _chk_attach
      assert not msg.ismodified()
      self.bad_extensions = ['.' + x for x in banned_exts]
      rc = mime.check_attachments(msg,self._chk_attach)
    except:	# milter crashed trying to analyze mail
      exc_type,exc_value = sys.exc_info()[0:2]
      if dspam_userdir and exc_type == dspam.error:
        if not exc_value.strerror:
	  exc_value.strerror = exc_value.args[0]
	if exc_value.strerror == 'Lock failed':
	  self.log("LOCK: BUSY")	# log filename
	  self.setreply('450','4.2.0',
		'Too busy discarding spam.  Please try again later.')
	  return Milter.TEMPFAIL
      fname = tempfile.mktemp(".fail")	# save message that caused crash
      os.rename(self.tempname,fname)
      self.tempname = None
      if exc_type == email.Errors.BoundaryError:
	self.log("MALFORMED: %s" % fname)	# log filename
        if self.internal_connection:
	  # accept anyway for now
	  return Milter.ACCEPT
	self.setreply('554','5.7.7',
		'Boundary error in your message, are you a spammer?')
        return Milter.REJECT
      if exc_type == email.Errors.HeaderParseError:
	self.log("MALFORMED: %s" % fname)	# log filename
	self.setreply('554','5.7.7',
		'Header parse error in your message, are you a spammer?')
        return Milter.REJECT
      # let default exception handler print traceback and return 451 code
      self.log("FAIL: %s" % fname)	# log filename
      raise
    if rc == Milter.REJECT: return rc;
    if rc == Milter.DISCARD: return rc;

    if rc == Milter.CONTINUE: rc = Milter.ACCEPT # for testbms.py compat

    defanged = msg.ismodified()

    if self.hidepath: del msg['Received']

    if self.recipients == None:
      # false positive being recirculated
      self.recipients = msg.get_all('x-dspam-recipients',[])
      if self.recipients:
	for rcptlist in self.recipients:
	  for rcpt in rcptlist.split(','):
	    self.addrcpt('<%s>' % rcpt.strip())
	del msg['x-dspam-recipients']
      else:
	self.addrcpt(self.mailfrom)
    else:
      self.alter_recipients(self.discard_list,self.redirect_list)
    for name,val in self.new_headers:
      self.addheader(name,val)

    if self.cbv_needed:
      q = self.cbv_needed
      if q.result in ('softfail','fail','deny'):
	template_name = 'softfail.txt'
      elif q.result in ('unknown','permerror'):
	template_name = 'permerror.txt'
      elif q.result == 'neutral':
        template_name = 'neutral.txt'
      else:
	template_name = 'strike3.txt'
      rc = self.send_dsn(q,msg,template_name)
      self.cbv_needed = None
      if rc != Milter.CONTINUE: return rc

    if not defanged and not spam_checked:
      os.remove(self.tempname)
      self.tempname = None	# prevent re-removal
      self.log("eom")
      return rc			# no modified attachments

    # Body modified, copy modified message to a temp file 
    if defanged:
      if self.rejectvirus and not self.hidepath:
	self.log("REJECT virus from",self.mailfrom)
	self.setreply('550','5.7.1','Attachment type not allowed.',
		'You attempted to send an attachment with a banned extension.')
	self.tempname = None
	return Milter.REJECT
      self.log("Temp file:",self.tempname)
      self.tempname = None	# prevent removal of original message copy
    out = tempfile.TemporaryFile()
    try:
      msg.dump(out)
      out.seek(0)
      msg = rfc822.Message(out)
      msg.rewindbody()
      while True:
	buf = out.read(8192)
	if len(buf) == 0: break
	self.replacebody(buf)	# feed modified message to sendmail
      if spam_checked: self.log("dspam")
      return rc
    finally:
      out.close()
    return Milter.TEMPFAIL

  def send_dsn(self,q,msg,template_name):
    sender = q.s
    cached = cbv_cache.has_key(sender)
    if cached:
      self.log('CBV:',sender,'(cached)')
      res = cbv_cache[sender]
    else:
      self.log('CBV:',sender)
      try:
	template = file(template_name).read()
      except IOError: template = None
      m = dsn.create_msg(q,self.recipients,msg,template)
      m = m.as_string()
      print >>open('last_dsn','w'),m
      res = dsn.send_dsn(sender,self.receiver,m)
    if res:
      desc = "CBV: %d %s" % res[:2]
      if 400 <= res[0] < 500:
	self.log('TEMPFAIL:',desc)
	self.setreply('450','4.2.0',*desc.splitlines())
	return Milter.TEMPFAIL
      if len(res) < 3: res += time.time(),
      cbv_cache[sender] = res
      self.log('REJECT:',desc)
      self.setreply('550','5.7.1',*desc.splitlines())
      return Milter.REJECT
    cbv_cache[sender] = res
    if not cached:
      s = time.strftime(time_format,time.localtime())
      print >>open('send_dsn.log','a'),sender,s # log who we sent DSNs to
    return Milter.CONTINUE

  def close(self):
    sys.stdout.flush()		# make log messages visible
    if self.tempname:
      os.remove(self.tempname)	# remove in case session aborted
    if self.fp:
      self.fp.close()
    sys.stdout.flush()
    return Milter.CONTINUE

  def abort(self):
    self.log("abort after %d body chars" % self.bodysize)
    return Milter.CONTINUE

def main():
  Milter.factory = bmsMilter
  flags = Milter.CHGBODY + Milter.CHGHDRS + Milter.ADDHDRS
  if wiretap_dest or smart_alias or dspam_userdir:
    flags = flags + Milter.ADDRCPT
  if srs or len(discard_users) > 0 or smart_alias or dspam_userdir:
    flags = flags + Milter.DELRCPT
  Milter.set_flags(flags)
  print "%s bms milter startup" % time.strftime('%Y%b%d %H:%M:%S')
  sys.stdout.flush()
  Milter.runmilter("pythonfilter",socketname,timeout)
  print "%s bms milter shutdown" % time.strftime('%Y%b%d %H:%M:%S')

if __name__ == "__main__":
  read_config(["/etc/mail/pymilter.cfg","milter.cfg"])
  if dspam_dict:
    import dspam	# low level spam check
  if dspam_userdir:
    import dspam
    import Dspam	# high level spam check
    try:
      dspam_version = Dspam.VERSION
    except:
      dspam_version = '1.1.4'
    assert dspam_version >= '1.1.5'
  main()
