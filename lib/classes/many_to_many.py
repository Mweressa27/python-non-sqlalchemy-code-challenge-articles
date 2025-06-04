from collections import Counter

class Article:
    _all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("author must be an Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be a Magazine")
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("title must be between 5 and 50 characters")

        self._author = author
        self._magazine = magazine
        self._title = title
        Article._all.append(self)

    @property
    def title(self):
        return self._title  # Immutable

    @title.setter
    def title(self, value):
        raise TypeError("title is immutable")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("author must be an Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("magazine must be a Magazine")
        self._magazine = value

    @classmethod
    def all(cls):
        return cls._all


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name  # Immutable

    # No setter to keep name immutable

    def articles(self):
        return [a for a in Article.all() if a.author == self]

    def magazines(self):
        # Return unique magazines authored by this author
        return list({a.magazine for a in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        # Unique categories of magazines this author has written for
        return list({mag.category for mag in self.magazines()})


class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        if not (2 <= len(value) <= 16):
            raise ValueError("name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("category must be a string")
        if len(value.strip()) == 0:
            raise ValueError("category cannot be empty")
        self._category = value

    def articles(self):
        return [a for a in Article.all() if a.magazine == self]

    def contributors(self):
        # Unique authors who have written articles for this magazine
        return list({a.author for a in self.articles()})

    def article_titles(self):
        return [a.title for a in self.articles()]

    def contributing_authors(self):
        # Authors who have more than 2 articles in this magazine
        authors = [a.author for a in self.articles()]
        counts = Counter(authors)
        return [author for author, count in counts.items() if count > 2]
