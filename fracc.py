def mdc(a, b): #algoritimo de euclides: útil para simplificar frações
	a = abs(a) #É necessário usar o módulo das entradas para simplificar corretamente subtrações
	b = abs(b)
	if b > a:
		a,b = b,a
	if b == 0:
		return int(a)
	return mdc(b, a%b)
	

class frac:
	def __init__(self, num, den):
		assert isinstance(num, int) or isinstance(den, int), "Numerador ou numerador não inteiros" #necessário para simplificações corretas
		if den == 0: raise ZeroDivisionError
		self.num = num
		self.den = den

	

		
	def __str__(self): 
		return f"{self.num} / {self.den}"
	
	def getSim(self): #retorna fração simplificada
		sim = mdc(self.num, self.den)
		return frac(
			self.num // sim, #necessário para correta simplificação
			self.den // sim
		)
	
	def __add__(self, other):   
		if isinstance(other, frac):
			res = frac(
				self.num * other.den + self.den * other.num,
				self.den * other.den
			)
			return res.getSim()
		
	def __sub__(self, other):
		if isinstance(other, frac):
			res = frac(
				self.num * other.den - self.den * other.num,
				self.den * other.den
			)
			return res.getSim()
		
	
	def __mul__(self, other):
		if isinstance(other, frac):
			res = frac(
				self.num * other.num,
				self.den * other.den
			)
			return res.getSim()
		

	def __truediv__(self, other):
		if isinstance(other, frac):
			res = frac(
				self.num * other.den,
				self.den * other.num
			)
			return res.getSim()
		

#teste das operações	
um_meio = frac(1,2)
tres_quartos = frac(3,4)


print(um_meio + tres_quartos)
print(tres_quartos - um_meio)
print(um_meio - tres_quartos)
print(um_meio * tres_quartos)
print(tres_quartos / um_meio)

#zero_zero = frac(1, 0) #descomentar esta operação gera erro, como esperado

