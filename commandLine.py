import sys, getopt

class CommandLine:
    def __init__(self):
        self.args = sys.argv[1:]

    #return a list of arguments given in the command line (except the script file)
    def getArgs(self):
        return self.args

    #for example, if we call 'script.py open trade 100 EUR_USD'
    #this method will return '100' and 'EUR_USD'
    def getOptions(self):
        return self.args[1:]

    def showArgs(self):
        print(self.args)

    def contains(self, arg):
        if arg in self.getArgs():
            return True

        return False

    # def printHelp(self):
    #     progname = sys.argv[0]
    #     progname = progname.split('/')[-1] # strip off extended path
    #     help = __doc__.replace('<PROGNAME>', progname, 1)
    #     print(help, file=sys.stderr)


cmd = CommandLine()
cmd.getArgs()