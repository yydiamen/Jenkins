class primitive_calc:
    def multiply(a:int,b:int):
        return a*b
    def add(a:int,b:int):
        return a+b
    def cube(a:int):
        return a*a*a
class person():
    def __init__(self,name:str,age:int,nick:str) -> None:
        self.name = name
        self.age = age
        self.nick = nick
    def __eq__(self, other: object) -> bool:
            if isinstance(other, person):
                newPerson = person(other.name, other.age, other.nick)
                if newPerson.name == self.name and newPerson.age == self.age:
                    return True
                else:
                    return False
            else:
                return False