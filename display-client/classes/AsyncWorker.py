import threading


class StoppableThread(threading.Thread):
    '''Basic stoppable thread wrapper
    Adds Event for stopping the execution loop
    and exiting cleanly.
    '''
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()
        self.daemon = True                 

    def start(self):
        if self.isAlive() == False:
            self.stop_event.clear()
            threading.Thread.start(self)

    def stop(self):
        if self.isAlive() == True:
            # set event to signal thread to terminate
            self.stop_event.set()
            # block calling thread until thread really has terminated
            self.join()


class AsyncWorker(StoppableThread):
    '''Basic thread wrapper class for asyncronously running functions
    Basic thread wrapper class for running functions
    asyncronously. Return False from your function
    to abort looping.
    '''
    def __init__(self, todo, payload, param=None):
        StoppableThread.__init__(self)
        self.todo = todo
        self.payload = payload
        self.param = param

    def run(self):
        while self.stop_event.is_set() == False:
            if self.todo(self.payload, self.param) == False:
                self.stop_event.set()
                break

print 'hello'
