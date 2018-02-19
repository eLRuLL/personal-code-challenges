class MinStack(object):

    def __init__(self):
        self.minimum = None
        self.array = []

    def push(self, value):
        if not self.array:
            self.minimum = value
            self.array.append(value)
        elif value >= self.minimum:
            self.array.append(value)
        else:
            self.array.append(value*2 - self.minimum)
            self.minimum = value

    def pop(self):
        if self.array:
            value = self.array.pop()
            if value >= self.minimum:
                return value
            else:
                to_return = max(value, self.minimum)
                self.minimum = self.minimum*2 - value
                return to_return
