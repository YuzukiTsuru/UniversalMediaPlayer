import shlex
import threading
import subprocess
import random

from utils.logger import *


class MPlayer:
    def __init__(self, logger):
        self.logger = logger
        self.fifo_file = get_custom_fifo_file_name()
        self.controller = self.MPlayerController(logger, self.fifo_file)
        pass

    def get_state(self):
        return self.controller.state

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

    def mplayer_exec(self):
        self.command_runner('sudo mkfifo {}'.format(self.fifo_file), wait=True)
        self.command_runner('sudo mplayer -slave -input file={}'.format(self.fifo_file))

    class MPlayerController:

        def __init__(self, logger, fifo):
            self.state = 'stop'
            self.logger = logger
            self.fifo = fifo

        def fifo_writer(self, command):
            def random_id():
                return random.randint(0, 100)

            # Thread for writing fifo
            class FifoThread(threading.Thread):
                def __init__(self, thread_id, name, counter, fifo, logger):
                    threading.Thread.__init__(self)
                    self.threadID = thread_id
                    self.name = name
                    self.counter = counter
                    self.fifo = fifo
                    self.logger = logger

                def run(self):
                    self.logger.info("Fifo Thread [{}] Start".format(self.name))
                    with open(self.fifo) as f:
                        f.writelines(command)
                        f.close()
                    self.logger.info("Fifo Thread [{}] End".format(self.name))

            fifo_thread = FifoThread(random_id(), command, self.fifo, self.logger)
            fifo_thread.start()
            fifo_thread.join()

        def Play(self):
            self.fifo_writer('play')
            self.state = 'play'
