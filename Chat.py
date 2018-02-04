import requests
import User

class Chat:

	#Constructora/variables de classe
	def __init__(self, id, chatName = None):
		self.id = id
		self.users = {} #Diccionari d'usuaris
		if chatName:
			self.chatName = chatName
		else:
			self.chatName = None

	#Funció que incrementa el numero de missatges de l'usuari especificat
	#Retorna el numero de missatges un cop s'ha fet l'increment, -1 si va malament
	def incrementaMsg(userID):
		if users.has_key(userID):
			users['userID'].numMsg += 1
			return users['userID'].numMsg
		else:
			return -1

	#Funció que mira si te un usuari dins el chat
	def hasUser(userID):
		return users.has_key(userID)

	#Funcio que afegeix usuari al chat
	def addUser(userID, username = None):
		user = User(userID, username)
		users['userID'] = user

	#Elimina usuari del chat
	def delUser(userID):
		del users['userID']