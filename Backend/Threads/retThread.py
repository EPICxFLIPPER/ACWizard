##Implementation of a thread that can hold a return value
from threading import Thread

##RetThread extends thread, allowing for return values, accessed via the join function
class RetThread(Thread):
    def __init__(self,group=None,target=None,name=None,args=(),kwargs={}, Verbose=None):
        Thread.__init__(self,group,target,name,args,kwargs)
        self._return = None

    def run(self):
        if (self._target is not None):
            self._return = self._target(*self._args, **self._kwargs)

    def join(self):
        Thread.join(self)
        return self._return
    
