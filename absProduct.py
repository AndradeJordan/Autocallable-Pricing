import abc

class AbsProduct(abc.ABC):

    @abc.abstractmethod
    def simulation_Path(self):
        pass
    @abc.abstractmethod
    def premium(self):
        pass

