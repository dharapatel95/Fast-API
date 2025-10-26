from abc import * 
class bank(ABC):
     
     @abstractmethod
     def calc(self):
          pass
     
class account(bank):
     pass

a1=account()
print(a1.__dict__)