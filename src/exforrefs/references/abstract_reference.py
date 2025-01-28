from abc import ABC, abstractmethod


class AbstractReference(ABC):
    """<class short description>

    Parameters
    ----------
    doi_dictionary : dict
        Given by the 'parse_doi' function, provides formattable information.

    abstract_only : bool, optional, default is False
        True if only an abstract is the source for an entry.

    entry_number : str, optional, default is None
        Represents the Exfor entry number. can be inputted as an argument in
        the parse_doi function.

    Attributes
    ----------
    author : str
        Author(s) of the text associated with the given doi. Authors are
        formatted the same across all dois. Unformatted author list can be found
        in doi_dictionary['author']

    title: str
        Title of the text associated with the given doi. Titles are formatted
        the same across all dois.

    bib_section : dict
        See Exfor format manual for formatting information, and Exfor dictionary 2
        for a list of information identifiers. It is initially formatted with the
        reference, author, and title sections. It is up to the user to add
        additional information.

    entry_number : str
        Represents the Exfor entry number. Does not include any subentry number.
        Can be inputted as an argument in the parse_doi function.

    reference : list
        Reference section used in the bib section of the exfor entry.

    Methods
    -------
    get_author

    get_title

    get_bib

    get_reference

    get_date

    new_entry

    """

    # Attributes

    # for later: add code to format the reference into a string in the get_reference method
    reference = []

    # Methods
    # fill in the parameters that you expect for all kinds of references (replace parameter1)
    def __init__(self, doi_dictionary, abstract_only=False, entry_number=None):

        # set attributes you expect for all kinds of references (replace parameter1)
        self.doi_dictionary = doi_dictionary

        self.abstract_only = abstract_only

        self.entry_number = entry_number

        self.get_author()

        self.get_title()

        self.get_date()

        self.get_reference()

        self.get_bib()

        self.new_entry()

        # add a get_date function + date attribute

    def get_author(self):
        a = ""
        i = 0
        counter = 2
        while i != len(self.doi_dictionary["author"]):
            # remove the whitespaces in the name
            a_split = self.doi_dictionary["author"][i].split(" ")
            # change the order of first name and initials and add them to the authors
            if len(a_split) > 2:
                b = a_split[1] + a_split[2] + a_split[0]
            else:
                b = a_split[1] + a_split[0]
            a += b
            # maintain a counter of the length of "a" so I know when to insert a newline to keep up with exfor format
            counter += len(b)

            if i != len(self.doi_dictionary["author"]) - 1:
                # add a comma after every name except the last
                a += ","
                counter += 1
                # iterate here so that the position of the newline is considered based off of how many
                # characters there would be after adding the next name
                i += 1

                if counter + len(b) > 55:

                    if "\n" in a:
                        continue
                    a += "\n"

            else:
                # when the if condition is not met, the loop still needs to be iterated
                i += 1

            author = "(" + a + ")"
        self.author = author
        return self.author

    def get_title(self):
        self.title = self.doi_dictionary["title"]
        return self.title

    def get_bib(self):
        self.bib_section = {
            "REFERENCE": self.reference,
            "AUTHOR": self.author.upper(),
            "TITLE": self.title.upper(),
        }
        return self.bib_section

    @abstractmethod
    def get_reference(self):

        return None

    def new_entry(self):
        first_sub_number = self.entry_number + "001"
        new_entry = {self.entry_number: {first_sub_number: {"BIB": self.bib_section}}}

        new_entry[self.entry_number][first_sub_number]["__entryid"] = self.entry_number
        new_entry[self.entry_number][first_sub_number]["__subentid"] = first_sub_number

        self.new_entry = new_entry
        return new_entry

    def get_date(self):
        # define date to first be the year, then check if there's month and day and add those
        day = self.doi_dictionary["day"]
        date = self.doi_dictionary["year"]
        if "month" in self.doi_dictionary:
            month = self.doi_dictionary["month"]
            match month:
                case "jan":
                    date += "01"
                case "feb":
                    date += "02"
                case "mar":
                    date += "03"
                case "apr":
                    date += "04"
                case "may":
                    date += "05"
                case "jun":
                    date += "06"
                case "jul":
                    date += "07"
                case "aug":
                    date += "08"
                case "sep":
                    date += "09"
                case "oct":
                    date += "10"
                case "nov":
                    date += "11"
                case "dec":
                    date += "12"

            if "day" in self.doi_dictionary:
                date += f"{day:>02}"
        self.date = date

    """def get_reference(self):
        #the reference should be added as a property so that when the user adds to the list, it is updated through the get_reference method into a string
        self.referenceList = []
        refString = "("
        for i in range(len(refList)):
            refString += f"{refList[i-1]}"
            if i != len(refList) - 1:
                refString += ","
            if i == len(refList) - 1:
                refString += ")"
        self.referenceString = refString"""
