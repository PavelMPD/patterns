def make_bold(fn):
    def wrapped():
        return "<b>{}</b>".format(fn())

    return wrapped


def make_italic(fn):
    def wrapped():
        return "<i>{}</i>".format(fn())

    return wrapped


def make_p(fn):
    def wrapped(text):
        return "<p>{}</p>".format(fn(text))

    return wrapped


if __name__ == "__main__":
    @make_bold
    @make_italic
    def module_name():
        return __name__

    @make_p
    def add_block(text):
        return "block: {}".format(text)

    print("The module name:")
    print(module_name())
    print(make_bold(module_name)())
    print(add_block("new text"))
