class Binary:
    def __init__(self, num, value = 2):
        self.num = num
        self.value = value
    def __add__(self, other):
        return Binary(bin(int(self.num, self.value) + int(other.num, self.value))[2:])
    def __sub__(self, other):
        return Binary(bin(int(self.num, self.value) - int(other.num, self.value))[2:])
    def __mul__(self, other):
        return Binary(bin(int(self.num, self.value) * int(other.num, self.value))[2:])
    def __floordiv__(self, other):
        return Binary(bin(int(self.num, self.value) // int(other.num, self.value))[2:])
    def __str__(self):
        return str(int(self.num,self.value))


w1 = Binary('101')
w2 = Binary('10')
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