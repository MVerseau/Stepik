class PhoneNumber:
    def __init__(self, phone_number):
        self.phone_number=phone_number.replace(' ', '')

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.phone_number}')"

    def __str__(self):
        return f'({self.phone_number[0:3]}) {self.phone_number[3:6]}-{self.phone_number[6:]}'

phone1 = PhoneNumber('9173963385')
phone2 = PhoneNumber('918 396 3389')
phone3 = PhoneNumber('919 333 3344')

print(phone1, phone2, phone3, sep=', ')
print([phone1, phone2, phone3])
