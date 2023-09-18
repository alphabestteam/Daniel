class People:
    
    def __init__(self) -> None:
        self._people = []

    def __iter__(self) -> None:
        self.current_index = 0
        return self
        
    def __next__(self):
        if self.current_index < len(self._people):
            person = self._people[self.current_index]
            del self._people[self.current_index]
            return person
        else:
            raise StopIteration
    def add_person(self, name):
        self._people.append(name)

p1 = People()
p1.add_person("Alice")
p1.add_person("Bob")
p1.add_person("Charlie")

iteration = iter(p1)
for person in iteration:
    print(person)

