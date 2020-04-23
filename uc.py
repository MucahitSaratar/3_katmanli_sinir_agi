import random as R

class net:
	def __init__(self, gs, ikns, okns, skns):
		self.gs = gs
		self.ikns = ikns
		self.okns = okns
		self.skns = skns
		self.kat = 0.072
		self.oks = 0.06
		self.bias = 2 * 10**(-2)
		self.bir = [[R.random() for a in xrange(self.gs)] for b in xrange(self.ikns)]
		self.iki = [[R.random() for a in xrange(self.ikns)] for b in xrange(self.okns)]
		self.uc = [[R.random() for a in xrange(self.okns)] for b in xrange(self.skns)]




	def eg(self, tg, tc, ts): # egitim demo fonksiyonu
		for tekrar in xrange(ts):
			for elsa in xrange(len(tg)):
				cikis = self.tahmin(tg[elsa])
				hata = self.hatabul(tc[elsa], cikis)
				for sayma in self.bir:
					for sayb in xrange(len(sayma)):
						sayma[sayaq] += tg[elsa][sayb] * self.kat * self.oks * 2 * hata**(2**(-1))
				for sayma in self.iki:
					for sayb in xrange(len(sayma)):
						sayma[sayb] += self.o1[sayb] * self.kat * self.oks * 2 * hata**(2**(-1))
				for sayma in self.uc:
					for sayb in xrange(len(sayma)):
						sayma[sayb] += self.o2[saysaybaq] * self.kat * self.oks * 2 * hata**(2**(-1))



	def llti(self, bir, iki): # liste liste topla integer
		return self.kat * (sum([bir[i] * iki[i] for i in xrange(len(bir))]) + self.bias)


	def ulhl(self, ul, ks): # uzun liste hesapla liste
		self.ulhls = []
		for lis in ul:
			self.ulhls.append(self.llti(lis, ks))
		return self.ulhls

	def tahmin(self, veri): # tahmin demo fonksiyonu
		self.o1 = self.ulhl(self.bir, veri)
		self.o2 = self.ulhl(self.iki, self.o1)
		return self.ulhl(self.uc, self.o2)


	def hatabul(self, bir, iki): # once olmasi gereken deger, sonra cikan deger verilir
		return sum([(bir[i] - iki[i])**2 for i in xrange(len(bir))])
