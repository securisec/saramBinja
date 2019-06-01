from binaryninja import *
import inspect
from saram_py2_scaffold import _saram_conf, saram_py2_new_section

__version__ = '1.0.0'
__author__ = 'Hapsida @securisec'

class SaramBinja(object):
    """
    The main class for SaramBinja. 
    All SaramBinja methods are prefixed with snb to avoid namespace pollution.

    :param token: A valid entry token for Saram
    :type token: str
    :param bv: The BinaryView class from binaryninja
    :type token: object

    >>> from saramBinja import SaramBinja
    >>> saram = SaramBinja('sometoken', bv)
    """

    def __init__(self, token, bv):
        self.token = token
        self.binja = bv
        self.output = None
        self.command = None

    def send(self):
        """
        Method that will send the output of any snb functions to the server
        """
        data = {
            "type": "tool",
            "output": self.output,
            "command": self.command,
            "user": _saram_conf['username'],
            "comment": [
                {
                    "username": _saram_conf['username'],
                    "avatar": _saram_conf['avatar'],
                    "text": "saramBinja"
                }
            ]
        }
        print(saram_py2_new_section(self.token, data))

    def snb_get_strings(self):
        """
        Get all strings from the binary

        >>> saram.snb_get_strings().send()
        """
        self.command = inspect.stack()[0][3] + ' ' + 'All strings'
        self.output = '\n'.join([
            '{offset} {value}'.format(offset=hex(x.start), value=x.value) for x in self.binja.strings
        ])
        print(self.output)
        return self

    def snb_get_functions(self):
        """
        Get all functions from the binary

        >>> saram.snb_get_functions().send()
        """
        self.command = inspect.stack()[0][3] + ' ' + 'All functions'
        self.output = '\n'.join([
            '{offset} {value}'.format(offset=hex(x.start), value=x.name) for x in self.binja.functions
        ])
        print(self.output)
        return self

    def snb_current_function_comments(self, current_function):
        """
        Get all comments from the current function where the cursor is

        :param current_function: The binaryninja current_function
        :type current_function: object

        >>> saram.snb_current_function_comments(current_function).send()
        """
        self.command = inspect.stack(
        )[0][3] + ' ' + 'Comments from: ' + current_function.name
        self.output = '\n'.join([
            '{offset} {comment}'.format(offset=hex(key), comment=value) for key, value in current_function.comments.items()
        ])
        print(self.output)
        return self

    def snb_current_function_references(self, current_function):
        """
        Get all cross references from the current function where the cursor is

        :param current_function: The binaryninja current_function
        :type current_function: object

        >>> saram.snb_current_function_references(current_function).send()
        """
        self.command = inspect.stack(
        )[0][3] + ' ' + 'Comments from: ' + current_function.name
        self.output = ''
        self.output += 'Function name: {name}\n\n'.format(
            name=current_function.name)
        self.output += 'Callers:\n'
        self.output += '\n'.join([
            '{name} {offset}'.format(name=refs.name, offset=hex(refs.start)) for refs in current_function.callers
        ])
        self.output += '\n\nCallees:\n'
        self.output += '\n'.join([
            '{name} {offset}'.format(name=refs.name, offset=hex(refs.start)) for refs in current_function.callees
        ])
        print(self.output)
        return self
