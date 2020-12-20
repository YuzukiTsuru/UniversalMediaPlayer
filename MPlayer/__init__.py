import shlex

from utils.logger import *
import subprocess


class Mplayer:
    def __init__(self, logger):
        self.logger = logger
        self.fifo_file = get_custom_fifo_file_name()
        pass

    def command_runner(self, command, wait=False):
        cmd = shlex.split(command)

        p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while p.poll() is None:
            line = p.stdout.readline()
            line = str(line.strip(), encoding='utf-8')
            if line:
                self.logger.info('Subprogram output: [{}]'.format(line))
        if wait:
            p.wait()
        if p.returncode == 0:
            self.logger.info('Subprogram {} success'.format(command))
            return 0
        else:
            return -1

    def exec(self):
        self.command_runner('sudo mkfifo {}'.format(self.fifo_file), wait=True)
        self.command_runner('sudo mplayer -slave -input file={}'.format(self.fifo_file))
