import abc



class Instructions(abc.ABC):
    
    @abc.abstractmethod
    def validate(self):
        pass
    
    @abc.abstractmethod
    def next_step(self):
        pass
    
    

    