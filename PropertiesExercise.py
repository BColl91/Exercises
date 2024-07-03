class Book:
	def __init__(self, title, author):
		self.__title = title  #private attribute
		self.author = author
	@property
	def title(self):
		return self.__title
	@title.setter
	def title(self, new_title):
		if new_title == "":
			print("Error: Title cannot be an empty string.")
		else:
			self.__title = new_title

novel = Book("The Fix", "David Baldacci")

print("Title:", novel.title)
print("Author:", novel.author)
novel.title = "The Last Mile"
print("\nTitle after change:", novel.title)

print("\nTitle after attempting to set to an empty string:")
novel.title = ""
print(""" """)
print("The book is currently titled", end= " ")
print(novel.title)