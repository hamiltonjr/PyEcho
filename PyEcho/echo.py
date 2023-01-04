import sys
NO_ERRORS = 0

"""
    This class represents the echo and your command-line arguments
    for processing like Linux Echo.
"""


class Echo:
    def __init__(self, cl_args):
        """Constructor"""
        self.command_line_args = cl_args
        self.arguments = []
        self.message = ""
        self.ret = True

    def separate_arguments(self):
        """
            Separate command-line arguments and put it in arguments 
            attribute
        """
        only_args = []
        for argument in self.command_line_args[1:]:
            if argument.startswith("--"):
                only_args.append(argument[2])
                self.command_line_args.remove(argument)
            elif argument.startswith("-"):
                for ch in argument[1:]:
                    only_args.append(ch)
                self.command_line_args.remove(argument)
        self.arguments = only_args

    def separate_message(self):
        """
            Separate words of message and put it in a message atribute
        """
        words = []
        for word in self.command_line_args[1:]:
            if not word.startswith("-"):
                words.append(word)
        self.message = " ".join(words)


if __name__ == "__main__":
    echo = Echo(sys.argv)
    echo.separate_arguments()
    echo.separate_message()

    if "h" in echo.arguments:
        print("Echo help")
        print("This command has the following arguments:")
        print("-h / --help: show this help.")
        print("-v / --version: how how development this app is.")
        sys.exit(NO_ERRORS)
    if "v" in echo.arguments:
        print("Echo version 1.0 in Python.")
        print("Written by Hamilton G. Jr.")
        sys.exit(NO_ERRORS)
    if "n" in echo.arguments:
        echo.ret = False

    # with or without <ENTER>
    if echo.ret:
        print(echo.message.strip())
    else:
        print(echo.message.strip(), end="")
