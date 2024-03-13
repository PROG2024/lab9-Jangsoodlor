"""A singleton counter.

   counter = Counter()  get a reference to the counter. Initial count is 0.
   counter.count        property returns the current count
   counter.increment()  add 1 to current count and also return the new value

   Requirements:
   1. in Counter, do not use any static methods except __new__.
      You may not have a __new__ depending on how you implement the singleton.
"""

class Counter:
    """Singleton Counter class"""
    __instance = None

    def __init__(self):
        if not self.__initialized:
            self.__initialized = True
            self.__count = 0

    def __str__(self):
        return f"{self.__count}"

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
            cls.__instance.__initialized = False
        return cls.__instance

    @property
    def count(self):
        """returns the current count"""
        return self.__count

    def increment(self):
        """add 1 to current count and also return the new value"""
        self.__count += 1
        return self.count
