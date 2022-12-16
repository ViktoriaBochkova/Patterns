from abc import ABC, abstractmethod


class CookingBlog:

    def __init__(self):
        self.__recipe = set()

    def attach(self, author):
        self.__recipe.add(author)

    def notify(self):
        for author in self.__recipe:
            author.make_recipe()


class AbstractAuthor(ABC):
    @abstractmethod
    def make_recipe(self):
        pass


class Recipe(AbstractAuthor):

    def __init__(self, name):
        self.name = name

    def make_recipe(self):
        print('{} добавил рецепт'.format(self.name))


author1 = Recipe('Автор статьи "Мир кулинарии"')
author2 = Recipe('Автор книги "Еда спасет мир"')
author_system = CookingBlog()
author_system.attach(author1)
author_system.attach(author2)
author_system.notify()

