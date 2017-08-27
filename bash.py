import subprocess

SVN_COMMAND_CLIENT = "svn log -r {`date +%Y-%m-%d --date='-1 day'`}:{`date +%Y-%m-%d`} http://192.168.161.36/svn/NEPSE/Development/Code/NOTS/nots-client | grep -A2 'Nepaltrn03' | grep -v -e '^[[:space:]]*$' | sed '/Nepaltrn03/d' | sed '/--/d' | paste -s -d, -"

SVN_COMMAND_SERVER = "svn log -r {`date +%Y-%m-%d --date='-1 day'`}:{`date +%Y-%m-%d`} http://192.168.161.36/svn/NEPSE/Development/Code/NOTS/nots-service | grep -A2 'Nepaltrn03' | grep -v -e '^[[:space:]]*$' | sed '/Nepaltrn03/d' | sed '/--/d' | paste -s -d, -"


def getParsedSvnCommits():
    return parsedCommits(SVN_COMMAND_CLIENT) +","+parsedCommits(SVN_COMMAND_SERVER)


def parsedCommits(SVN_COMMAND):
    p = subprocess.Popen(SVN_COMMAND, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    return output[:-1]

    
