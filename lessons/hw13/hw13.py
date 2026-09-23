class TestCase:
    def __init__(self, name, status="new", duration=None):
        self.name = name
        self.status = status
        self.duration = duration

    def can_run(self):
        return self.status == "new"

    def finish(self, result, duration):
        if self.status != "new":
            return False

        if result != "passed" and result != "failed":
            return False

        self.status = result
        self.duration = duration
        return True

    def is_slow(self):
        if self.duration is None:
            return None
        return self.duration >= 5


test1 = TestCase("Login")

test2 = TestCase("Registration")
test2.finish("passed", 7)

test3 = TestCase("Payment")
test3.finish("wrong", 3)

print(test1.name, test1.can_run(), test1.is_slow(), test1.status)
print(test2.name, test2.can_run(), test2.is_slow(), test2.status)
print(test3.name, test3.can_run(), test3.is_slow(), test3.status)
