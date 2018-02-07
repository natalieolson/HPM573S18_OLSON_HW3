class patient:
    def __init__(self, name):
        self.name = name

    def discharge(self):
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

class emergencypatient(patient):
    def __init__(self, name):
        patient.__init__(self,name)
        self.expectedcost=1000

    def discharge(self):
        print(self.name, "Emergency")

class hospitalizedpatient(patient):
    def __init__(self,name):
        patient.__init__(self, name)
        self.expectedcost=2000

    def discharge(self):
        print(self.name, "Hospitalized")

class hospital(patient):
    def __init__(self):
        self.cost =0
        self.patient =[]

    def admit(self,patient):
        self.patient.append(patient)

    def discharge_all(self):
        for patient in self.patient:
            patient.discharge()
            self.cost+=patient.expectedcost
    def get_total_cost(self):
        return self.cost

p1=  hospitalizedpatient('p1')
p2=  hospitalizedpatient('p2')
p3=  emergencypatient('p3')
p4=  emergencypatient('p4')
p5=  emergencypatient('p5')

YNHH=hospital()
YNHH.admit(p1)
YNHH.admit(p2)
YNHH.admit(p3)
YNHH.admit(p4)
YNHH.admit(p5)
YNHH.discharge_all()
print(YNHH.get_total_cost())
