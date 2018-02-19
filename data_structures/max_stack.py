class MaxStack(object):

    def __init__(self):
        self.maximum = None
        self.array = []

    def push(self, value):
        if not self.array:
            self.array.append(value)
            self.maximum = value
        elif value <= self.maximum:
            self.array.append(value)
        else:
            self.maximum = value
            self.array.append(value*2 - self.maximum)

    def pop(self):
        if self.array:
            value = self.array.pop()
            if value <= self.maximum:
                return value
            else:
                to_return = min(self.maximum, value)
                self.maximum = self.maximum*2 - value
                return to_return
