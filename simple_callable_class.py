
class Spam:
    def __call__(self, whom):
        print("Hello", whom)

s = Spam()

s('world')
s('sis')