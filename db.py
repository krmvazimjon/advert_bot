import sqlite3

class Sql:
	def __init__(self):
		self.connection = sqlite3.connect("user_info.db")
		self.cursor = self.connection.cursor()

	def base_create(self):
		self.cursor.execute("""CREATE TABLE IF NOT EXISTS user(
			id integer,
			username varchar(60),
			first_name varchar(60),
			tel integer NULL,
			cor1 bigint NULL,
			cor2 bigint NULL
			)""")

	def user_add(self,idi,username,first_name):
		self.cursor.execute("INSERT INTO user VALUES ({}, '{}', '{}', NULL, NULL, NULL, NULL)".format(idi, username, first_name))
		return self.connection.commit()

	def id_user(self,idi):
		self.cursor.execute(f"SELECT id FROM user WHERE id = {idi}")
		data = self.cursor.fetchone()
		return data

	# def advert(self,idi):
	# 	self.cursor.execute(f"UPDATE user SET text = {text1} WHERE id = {idi}")
	# 	advertdata = self.cursor.fetchall()
	# 	return advertdata

	def contact_update(self,idi,number):
		self.cursor.execute(f"UPDATE user SET tel = {number} WHERE id = {idi}")
		return self.connection.commit()

	def location_update(self,idi,cor1,cor2):
		self.cursor.execute(f"UPDATE user SET cor1 = {cor1}, cor2 = {cor2} WHERE id = {idi}")
		return self.connection.commit()

	def admin_send(self,idi):
		self.cursor.execute(f"SELECT * FROM user WHERE id = {idi}")
		data = self.cursor.fetchone()
		return data

