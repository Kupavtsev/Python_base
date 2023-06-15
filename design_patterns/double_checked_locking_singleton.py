# Double Checked Locking singleton pattern   
import threading   
class Single_Checked(object):   
  
   # resources shared by each and every   
   # instance   
  
   __single_acq_lock = threading.Lock()   
   __singleton_instance = None  
  
   # define the classmethod   
   @classmethod  
   def instance(cls):   
  
      # check for the singleton instance   
      if not cls.__singleton_instance:   
         with cls.__single_acq_lock:   
            if not cls.__singleton_instance:   
               cls.__singleton_instance = cls()   
  
      # return the singleton instance   
      return cls.__singleton_instance   
  
# main method   
if __name__ == '__main__':   
  
   # create class A   
   class A(Single_Checked):   
      pass  
  
   # create class B  
   class B(Single_Checked):   
      pass  
  
   X1, X2 = A.instance(), A.instance()   
   Y1, Y2 = B.instance(), B.instance()   
  
   assert X1 is not Y1   
   assert X1 is X2   
   assert Y1 is Y2   
  
   print('X1 : ', X1)   
   print('X2 : ', X2)   
   print('Y1 : ', Y1)   
   print('Y2 : ', Y2)  