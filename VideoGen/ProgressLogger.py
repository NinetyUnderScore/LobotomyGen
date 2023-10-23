from proglog import TqdmProgressBarLogger, ProgressBarLogger

class MyBarLogger(ProgressBarLogger):

    def bars_callback(self, bar, attr, value, old_value):
        total = self.bars[bar]['total']
        print(value/total)

logger = MyBarLogger()

def getLogger():
    return logger