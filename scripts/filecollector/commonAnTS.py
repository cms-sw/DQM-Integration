import os, datetime, time,  sys, shutil, glob, re, subprocess as sp, tempfile
TIME_OUT=700
DEBUG=False

def debugMsg(level,message):
  LEVELS=["INFO","WARNING","ERROR"]
  d=datetime.datetime.today()
  timeStamp=d.strftime("%Y/%m/%d\t%H:%M:%S")
  msg="%s\t%s:\t%s\n" % (timeStamp,LEVELS[level],message)
  sys.stdout.write(msg)
  return True
  
  
def executeCmd(cmd):
  stdOutFile=tempfile.TemporaryFile(bufsize=0)
  stdErrFile=tempfile.TemporaryFile(bufsize=0)
  cmdHdl=sp.Popen(cmd,shell=True,stdout=stdOutFile,stderr=stdErrFile)
  t=0
  cmdHdl.poll()
  while cmdHdl.returncode == None and t<TIME_OUT:
    t=t+1
    cmdHdl.poll()
    time.sleep(1)
  if t >= TIME_OUT and not cmdHdl.returncode:
    try:
      os.kill(cmdHdl.pid,9)
      debugMsg(2,"Execution timed out on Command: '%s'" % cmd)
    except:
      DEBUG and debugMsg(1,"Execution timed out on Command: '%s' but it ended while trying to kill it, adjust timer" % cmd)
  cmdHdl.poll()
  DEBUG and debugMsg(0,"End of Execution cicle of Command: '%s' " % cmd)
  stdOutFile.seek(0)
  stdErrFile.seek(0)
  return (stdOutFile,stdErrFile,cmdHdl.returncode)
  
  
def sendmail(EmailAddress,run=123456789,body=""):
  import os, smtplib
  from email.MIMEText import MIMEText
  server=os.getenv("HOSTNAME")
  print server
  s=smtplib.SMTP("localhost")
  tolist=[EmailAddress] #[EmailAddress, "lat@cern.ch"]
  if not body: body="File copy to dropbox failed by unknown reason for run:%09d on server: %s" % (run,server)
  msg = MIMEText(body)
  msg['Subject'] = "File merge failed."
  msg['From'] = ServerMail
  msg['To'] = EmailAddress
  s.sendmail(ServerMail,tolist,msg.as_string())
  s.quit()
