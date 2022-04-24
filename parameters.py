
class Parameters:
    def __init__(self):
        self.parameters = {}
        self.param_file = 'parameters.conf'

    def read_parameters(self):
        f = open(self.param_file, 'r')
        self.parameters = eval(f.read())
        f.close()
        return False

    def save_parameters(self):
        f = open(self.param_file, 'w')
        f.write(str(self.parameters))
        f.close()
        self.read_parameters()
        return False


