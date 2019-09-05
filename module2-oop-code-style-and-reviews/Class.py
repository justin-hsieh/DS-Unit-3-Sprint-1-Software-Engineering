
class Complex:
    def __init__(self, realpart, imagpart):        
        self.realpart = realpart
        self.imagpart = imagpart

    def add(self, other):
        return (self.realpart + other.realpart,
                       self.imagpart + other.imagpart)
    
    def subtract(self, other):
        return (self.realpart - other.realpart,
                       self.imagpart - other.imagpart)

    def multiply(self, other):
        return (self.realpart*other.realpart - self.imagpart*other.imagpart,
                       self.imagpart*other.realpart + self.realpart*other.imagpart) 
        
    def divide(self, other):
        
        r = float(other.realpart**2 + other.imagpart**2)
        return ((self.realpart*other.realpart+self.imagpart*other.imagpart)/r, 
                       (self.imagpart*other.realpart-self.realpart*other.imagpart)/r)   
x = Complex(3.0, -4.5)
y = Complex(2.0, 1.0)


print(x.add(y))
print(x.subtract(y))
print(x.multiply(y))
print(x.divide(y))


