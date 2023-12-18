class Subject:
    def __init__(self) -> None:
        super().__init__()
        self._observers = []

    def attach(self, obj):
        self._observers.append(obj)

    def detach(self, obj):
        try:
            self._observers.remove(obj)
        except ValueError:
            pass

    def notify(self, value):
        for obj in self._observers:
            obj.update(value)


class Lever(Subject):
    def __init__(self) -> None:
        super().__init__()
        self.apply = 0

    def pull(self):
        self.apply = 1 - self.apply
        self.notify(self.apply)


class Object:

    def __init__(self) -> None:
        super().__init__()

    def update(self, *values):
        raise NotImplementedError()


class Bulb(Object):
    def __init__(self) -> None:
        super().__init__()
        self.value = 0

    def update(self, value):
        self.value = value

    def check(self):
        print(f"- {bool(self.value)}")

