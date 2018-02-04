import requests

class User:

	#Constructora/variables de classe
	def __init__(self, id, username):
		self.id = id #identificador unic
		self.username = username
		self.numMsg #Missatges no dank seguits

	#Metodes associats
	#TODO