class Memory:
    def __init__(self):
        self.profile = {}

    def set(self, key, value):
        self.profile[key] = value

    def get(self, key):
        return self.profile.get(key)

    def has(self, key):
        return key in self.profile
