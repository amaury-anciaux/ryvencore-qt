from .Base import Base, Signal

from .InfoMsgs import InfoMsgs


class Connection(Base):
    """
    The base class for both types of abstract connections. All data is transmitted through a connection from an output
    port to some connected input port. The classes ExecConnection and DataConnection are ready for reimplementation,
    so users can add additional functionality to connections (like "weights"). As the Session manages the class
    references, custom reimplementations must be given in the Session constructor.
    """

    def __init__(self, params):
        super().__init__()

        self.out, self.inp, self.flow = params

    def activate(self):
        """Causes forward propagation of information"""
        pass



class ExecConnection(Connection):

    def activate(self):
        """Causes an update in the input port"""
        InfoMsgs.write('exec connection activated')

        self.inp.update()


class DataConnection(Connection):

    def __init__(self, params):
        super().__init__(params)

        self.data = None

    def get_val(self):
        """Gets the value of the output port"""
        InfoMsgs.write('data connection getting value')

        # request data backwards
        self.data = self.out.get_val()

        return self.data

    def activate(self, data=None):
        """Passes data to the input port and causes update"""
        InfoMsgs.write('data connection activated')

        # store data
        self.data = data

        # propagate data forward
        self.inp.update(data)
