from abc import ABC, abstractmethod


class AbstractReference(ABC):
    """<class short description>

    Parameters
    ----------
    <required input parameter name> : <type>
        <short description>

    <optional input parameter name> : <type>, optional, default is <default value>
        <short description>

    Attributes
    ----------
    <attribute name> : <type>
        <short description>

    Methods
    -------
    <method name>
        <method short description>

    """

    # fill in the parameters that you expect for all kinds of references (replace parameter1)
    def __init__(self, parameter1):

        # set attributes you expect for all kinds of references (replace parameter1)
        self.parameter1 = parameter1

        # call the process doi method - you can leave this
        self.process_doi_dictionary()

    @abstractmethod
    def process_doi_dictionary(self):
        """<method short description>"""

        # because this is an abstract method, you can leave this as it is, just returning None
        return None
