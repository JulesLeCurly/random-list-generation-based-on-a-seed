#V4 module de création de liste
import hashlib
from tqdm import tqdm

class v5(object):
	def sha256_decimal(self, text):
		# Calculer le hachage SHA-256
		hash_object = hashlib.sha256(text.encode('utf-8'))
		hex_digest = hash_object.hexdigest()

		# Convertir le résultat hexadécimal en décimal
		decimal_value = int(hex_digest, 16)

		return decimal_value
    
	def calculate_large_number(self, seed):
		current_number = self.sha256_decimal(str(seed))
		turns_count = 1
		while current_number < 10 ** 1030:
			turns_count += 1
			chaos = str(self.sha256_decimal(str(current_number+turns_count)))[0]
			current_number += current_number * turns_count * (int(chaos)+1)

		text = str(current_number)
		if len(text) > 1000:
			text = text[:-(len(text)-1000)]

		return int(text)
    
	def generate(self, seed, Fin, MIN, MAX, show=False):
		seed = int(seed)
		liste = []
		turns_count = 0
		difference = MAX - MIN
		difference_in_leng = len(str(difference))
		difference_in_leng_max = int('9'*difference_in_leng)
		turns_count_large_number = 0

		large_number = str(self.calculate_large_number(seed))

		if show:
			for turns_count in tqdm(range(Fin)):
				if turns_count_large_number+difference_in_leng > 900:
					large_number = str(self.calculate_large_number(seed+turns_count))
					turns_count_large_number = 0
				
				t = -1
				curent_number = ""
				while t+1 != difference_in_leng:
					t += 1
					turns_count_large_number += 1
					curent_number += large_number[t+turns_count_large_number]
				
				curent_number = int(curent_number)
				curent_number = (curent_number*difference)/difference_in_leng_max
				liste.append(round(curent_number) + MIN)
			return liste
		else:
			for turns_count in range(Fin):
				if turns_count_large_number+difference_in_leng > 900:
					large_number = str(self.calculate_large_number(seed+turns_count))
					turns_count_large_number = 0
				
				t = -1
				curent_number = ""
				while t+1 != difference_in_leng:
					t += 1
					turns_count_large_number += 1
					curent_number += large_number[t+turns_count_large_number]
				
				curent_number = int(curent_number)
				curent_number = (curent_number*difference)/difference_in_leng_max
				liste.append(round(curent_number) + MIN)
			return liste