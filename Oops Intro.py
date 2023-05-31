class Railways:
    formType = "Railway Form"

    def __init__(self):
        self.name = None
        self.num = None

    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train No. is {self.num}")
VedantApplication = Railways()
VedantApplication.name = "Vedant"
VedantApplication.num = 65
VedantApplication.printData()
# If we want to change formType, then this can be done by Railways.formType = XYZ.
