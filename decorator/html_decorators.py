def make_bold(fn):
    def wrapped():
        return "<b>{}</b>".format(fn())

    return wrapped


def make_italic(fn):
    def wrapped():
        return "<i>{}</i>".format(fn())

    return wrapped


if __name__ == "__main__":
    @make_bold
    @make_italic
    def module_name():
        return __name__


    print("The module name:")
    print(module_name())
