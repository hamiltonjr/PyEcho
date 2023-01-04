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

    def help(self):
        print("PyEcho 0.1.0 written in 2023.")
        print("Hamilton G. Jr <hamiltonjr2010@gmail.com>.")
        print()
        print("USAGE: echo [FLAGS] <TEXT>")
        print("FLAGS:")
        print("-h, --help Prints help information")
        print("-n Do not print newline")
        print("-v, --version Prints version information")
        print("ARGS:")
        print("<TEXT>... Input text")

    def version(self):
        print("PyEcho 0.1.0 written in 2023.")
        print("Hamilton G. Jr <hamiltonjr2010@gmail.com>.")


if __name__ == "__main__":
    echo = Echo(sys.argv)
    echo.separate_arguments()
    echo.separate_message()

    if "h" in echo.arguments:
        echo.help()
        sys.exit(NO_ERRORS)
    if "v" in echo.arguments:
        echo.version()
        sys.exit(NO_ERRORS)
    if "n" in echo.arguments:
        echo.ret = False

    # with or without <ENTER>
    if echo.ret:
        print(echo.message.strip())
    else:
        print(echo.message.strip(), end="")
