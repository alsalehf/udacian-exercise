class Udacian:

    def __init__(self,name,city,enrollement,nanodegree,status):
        self.name = name
        self.city = city
        self.enrollement = enrollement
        self.nanodegree = nanodegree
        self.status = status

    def print_udacian(self):
        print(self.name + " is enrolled in " + self.city + " studying " + self.nanodegree + " with Ms. " + self.enrollement[0] +",He/She is " + self.status)


Fatima = Udacian("Fatima","Dammam",["Elham","am"],"Full Stack","On Track")

Fatima.print_udacian()
