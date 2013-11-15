# 20131115 Lab 22:40
# Keep moving. Keep moving.
import sys
import re
from handles import *
from util import *
from rules import *

class Parser:
    """
    A parser reada a text file, applying rules and controlling a 
    hanlder.
    """
    
    def __init__(self, hanlder):
        self.handler = hanlder
        self.rules = []
        self.filters = []

    def addRules(self, rule):
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):

