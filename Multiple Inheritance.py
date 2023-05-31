class Base1:
    company = "Google"
    ecode = 31


class Base2:
    company = "Microsoft"
    num = 7


class Derived(Base2, Base1):
    name = "Employee"


Vedant = Derived()
print(
    f"The company is {Vedant.company}")  # The class written before during the time of inheritance is given more preference as compared to the other one.
