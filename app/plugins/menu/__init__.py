import sys
from app.commands import Command


class MenuCommand(Command):
    def execute(self):
        print('Welcome to the Basic Calculator.\nSelect the operation to be performed\nAdd\nSubtract\nMultiply\nDivide')