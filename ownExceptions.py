__author__ = 'steveleec'
#ownExceptions.py

class WrongChoiceGA(Exception):
    pass

def checkChoiceGA(opt):
    if opt != "A":
        raise WrongChoiceGA

def printChoiceExceptionGA():
    print "That option is not available. Try again."
    print "MENU:"
    print "Apply Trading Strategy-- (A)"
    print ""
