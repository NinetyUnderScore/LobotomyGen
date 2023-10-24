from proglog import TqdmProgressBarLogger, ProgressBarLogger
from flask import session
import webserv

class MyBarLogger(ProgressBarLogger):
    progre = 1.0

    def bars_callback(self, bar, attr, value, old_value):
        total = self.bars[bar]['total']
        session["progress"] = (value/total)
        progre = value/total

logger = MyBarLogger()

def getLogger():
    return logger