class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """Returns a string format"""
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """Returns the official representation of the object"""
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
    def __del__(self):
        """Deletes the instance of the class after executing"""
        print("Deleting", self.title)