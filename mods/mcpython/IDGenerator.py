import random


#These class is part of the autobahn.util libary published under MIT-licence
#modified by me

class IdGenerator(object):
    def __init__(self):
        self._next = 0  # starts at 1; next() pre-increments
        self.used = []
        print("[IDGENERATOR/INFO] generating ids")
        self.unused = list(range(1, 1000000))
        self.dimensionids = [[], 0]

    def next(self):
        """
        Returns next ID.

        :returns: The next ID.
        :rtype: int
        """
        self._next += 1
        if self._next > 1000000:
            self._next = 1
        if not self._next in self.unused:
            if len(self.unused) == 0:
                raise MemoryError("can't get new id: no id's are arrival")
            return self.next()
        self.used.append(self._next)
        self.unused.remove(self._next)
        return self._next

    # generator protocol
    def __next__(self):
        return self.next()

    def getRandom(self):
        if len(self.unused) == 0:
            raise MemoryError("can't get new id: no id's are arrival")
        id = random.choice(self.unused)
        self.unused.remove(id)
        self.used.append(id)
        return id

    def getDimensionId(self):
        id = self.dimensionids[1]
        self.dimensionids[1] += 1
        self.dimensionids[0].append(id)
        return id

handler = IdGenerator()