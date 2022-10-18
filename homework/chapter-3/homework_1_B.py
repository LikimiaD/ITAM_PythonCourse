def transfer(value, n):
        lst = []
        while value >= n:
            lst.append(value%n)
            value //= n
        lst.append(value)
        lst = reversed(lst)
        return ''.join(map(str, lst))
class Ternary:
    def __init__(self, num, value = 3):
        self.num = num
        self.value = value
    def __add__(self, other):
        return Ternary(transfer((int(self.num, self.value) + int(other.num, self.value)), self.value))
    def __sub__(self, other):
        return Ternary(transfer((int(self.num, self.value) - int(other.num, self.value)), self.value))
    def __mul__(self, other):
        return Ternary(transfer((int(self.num, self.value) * int(other.num, self.value)), self.value))
    def __floordiv__(self, other):
        return Ternary(transfer((int(self.num, self.value) // int(other.num, self.value)), self.value))
    def __str__(self):
        return str(int(self.num,self.value))


w1 = Ternary('10')
w2 = Ternary('2')
add_ = w1+w2
print(add_.num)
sub_ = w1-w2
print(sub_.num)
mul_ = w1*w2
print(mul_.num)
floordiv_ = w1 // w2
print(floordiv_.num)
print(str(w1))
print(str(w2))