import abc

class SampleAbstractClass:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def sample_one(self):
        return 0

    @abc.abstractmethod
    def sample_two(self):
        print('Alright, al fucking right!')


class MyClass(SampleAbstractClass):
    def sample_one(self):
        pass

    def sample_two(self):
        pass

klas = MyClass()
