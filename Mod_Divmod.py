class Farhad:
    def __init__(self,a,b,):
        self.a=a
        self.b=b
    def Calculation(self):
        div = self.a / self.b
        mod = self.a % self.b
    #def show(self):
        print(int(div))
        print(mod)
        print(f"({int(div)},{mod})")
farhad=Farhad(a=int(input()),b=int(input()))
farhad.Calculation()