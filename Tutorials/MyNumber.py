class MyNumber:
    def __init__(self, value):
        self.value = value


    def __iadd__(self, other):  # += operatörünü aşırı yükler
        if other == 1:
            self.value = self.value + 1
        else:
            self.value = self.value + (other + 8)
        return "selam"


    def __add__(self, other):  # + operatörünü aşırı yükler
        if other == 1:
            return self.value + 1
        else:
            return self.value + other + 200

    def __repr__(self):
        return f"{self.value}"

sayi = MyNumber(75)

print(sayi)

print(sayi + 0)

print(sayi)