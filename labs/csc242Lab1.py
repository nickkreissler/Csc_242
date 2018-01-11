# Lab 2
#
# Nick Kreissler
#
# Your None
#

class Worker(object):

    def __init__(self, name = 'Jane Doe', hourrate = 8.25, ):
        self.name = name
        self.hourrate = hourrate

    def changeRate(self, hourrate):
        self.hourrate = hourrate

    def weeklyPay(self, hours):
        return "Not Implemented"

    def __repr__(self):
        return "Worker({}, {}".format(self.name, self.hourrate)

class HourlyWorker(Worker):
    def __init__(self, name, hourrate):
        super(HourlyWorker, self).__init__(name, hourrate)

    def weeklyPay(self, hours):
        if hours > 40:
            x = (40*self.hourrate)+((hours-40)*(2*self.hourrate))
        else:
            x = hours*self.hourrate
        return x

class SalariedWorker(Worker):
    def __init__(self, name, hourrate):
        super(SalariedWorker, self).__init__(name, hourrate)

    def weeklyPay(self, hours):
        x = self.hourrate*40
        return x

