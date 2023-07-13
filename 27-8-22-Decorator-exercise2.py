# print("This is bold text looks like:",'\033[1m' + 'Python' + '\033[0m')
def make_bold(fn):
    def wrapped():
        return "<b>" + '\033[1m' + fn() + '\033[0m' + "</b>"
    return wrapped

def make_italic(fn):
    def wrapped():
        return "<i>" + '\033[3m' + fn() + '\033[0m' + "</i>"
    return wrapped

def make_underline(fn):
    def wrapped():
        return "<u>" + '\033[4m' + fn() + '\033[0m' + "</u>"
    return wrapped
@make_bold
@make_italic
@make_underline
def hello():
    return "hello world"
print(hello()) ## returns "<b><i><u>hello world</u></i></b>"
