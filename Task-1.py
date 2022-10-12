class Observer:

    """Observer class initialisation to create instances 
    of technicians AKA observers"""
    def __init__(self, name):
        self.name = name

    ##Add in From when figured out the first half of the code
    def update(self, machine ,state):
        message = '{}. Machine "{}" has changed to "{}"'.format(self.name, machine, state)
        print(message)


class Subject:

    """Create attribute set for multiple instances and the initial 
    state of the machine """
    def __init__(self):

        self.observers = set()
        self.state = None

    #Sets the state of each machine
    def setState(self, state):
        self.state = state

    #Adds an observer(user) to the set, to 
    def attach(self, user):
        self.observers.add(user)

    #Loops through the set and sends notification to users about 
    #the current observable
    def notifyAllObservers(self, machine):

        for users in self.observers:
            users.update(machine, self.state)



#Create the child classes here

"""I tried to implement the subclasses for each parent class 
based upon the design requirements, but couldn't get them to function correctly, when trying
to override methods from them parent class Observer. This is some inisght into how I went 
about achieving this after doing research on Observer patterns"""
class Employee(Observer):
    
    def __init__(self, role, name):
        self.role = role
        super().__init__(name)
    
    def update(self, name, machine, state, role):
        message = 'Hi "{}" , "{}". Machine "{}" has changed to "{}"'.format(name, role, machine, state)
        print(message)

#Test instances

"""After researching about the Observer design pattern I created the following instances below to highlight what I had learnt."""

#Set the state of current machine
sub = Subject()
sub.setState('IDLE')

#Add observers
sam = Observer('Sam')
bob = Observer('Bob')
sub.attach(bob)
sub.attach(sam)

#Notify observers of change in machines behaviour
sub.notifyAllObservers("A")