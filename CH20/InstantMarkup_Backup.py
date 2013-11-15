# 20131115 Lab 22:40
# Keep moving. Keep moving.
import sys
import re
from handlers import *
from util import *
from rules import *

class Parser:
    """
    A parser reada a text file, applying rules and controlling a 
    hanlder.
    """
    
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []

    def addRules(self, rule):
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last: break
        self.handler.end('document')


class BasicTextParser(Parser):
    """
    A specific Parser that adds rules and filters in its
    constructor.
    """
    
    def __init__(self, handler):
        Parser.__init__(self, Handler)
        self.addRules(ListRule())
        self.addRules(ListItemRule())
        self.addRules(TitleRule())
        self.addRules(HeadingRule())
        self.addRules(ParagraphRule())
        
        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+)', 'mail')

        
handler = HTMLRenderer()
parser = BasicTextParser(handler)
    

parser.parse(sys.stdin)
