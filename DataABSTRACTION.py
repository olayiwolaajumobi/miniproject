# abstract class has no body


class car:
    def max_speed(self):
        pass

class Toyota(car):
    def max_speed(self):
        return 200

class Mercedes(car):
    def max_speed(self):
        return 250


toyota = Toyota()
print(toyota.max_speed())


toyota.max_speed()
print(Mercedes)
