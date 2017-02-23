import subprocess
import os

def matchfiles(path,regex):
        try:
            os.chdir(path)
        except IOError as e:
            print "hit exception", e

        PIPE = subprocess.PIPE

        process = subprocess.Popen(['git', 'grep', regex], stdout=PIPE, stderr=PIPE)
        stdoutput, stderroutput = process.communicate()

        if 'fatal' in stdoutput:
            raise OSError
        else:
            return [x.split(':')[0] for x in stdoutput.split('\n') if len(x) > 0]


def commithistory(path, file_name):
    """
    Description : Get commit history for the file passed
    as a paramter
    :param self: Object
    :param file_name: Str
    :return: Str
    """
    try:
        os.chdir(path)
    except IOError as e:
        print "hit exception", e
    PIPE = subprocess.PIPE
    process = subprocess.Popen(['git', 'log', '-p', file_name], stdout=PIPE, stderr=PIPE)
    stdoutput, stderroutput = process.communicate()
    if stdoutput:
        return stdoutput.split('diff --git')[0]
    else:
        return "no commit history found"
def matchandcommithistory(path,regex):
    file_list = [x.split(':')[0] for x in matchfiles(path, regex).split('\n') if len(x) > 0]
    data = []
    for file in file_list:
       data.append(commithistory(path, file))
    return data
