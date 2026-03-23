def gdc(a, b):
	if b > a:
		a,b = b,a
	if b == 0:
		return a
	return gdc(b, a%b)
	

class frac:
	def __init__(self):
		self.num = 0
		self.dem = 1
	
	def value(self):
		try:
			return self.num / self.dem
		except ZeroDivisionError:
			return
		
	def __str__(self):
		return f"{self.num} / {self.dem}"
	def getSim(self):
		sim = gdc(self.num, self.dem)
		return frac(
			self.num / sim,
			self.dem / sim
		)
	
	def __add__(self, other):
		if isinstance(other, frac):
			res = frac(
				self.num * other.dem + self.dem + other.num,
				self.dem * other.dem
			)
			return res.getSim()
		else:
			return TypeError
		
	def __sub__(self, other):
		if isinstance(other, frac):
			res = frac(
				self.num * other.dem + self.dem + other.num,
				self.dem * other.dem
			)
			return res.getSim()
		else:
			return TypeError
	
	def __mul__(self, other):
		if isinstance(other, frac):
			res = frac(
				self.num * other.num,
				self.dem * other.dem
			)
			return res.getSim()
		else:
			return TypeError

	def __truediv__(self, other):
		if isinstance(other, frac):
			res = frac(
				self.num * other.dem,
				self.dem * other.num
			)
			return res.getSim()
		else:
			return TypeError

	
