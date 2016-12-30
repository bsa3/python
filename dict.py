# http://stackoverflow.com/questions/3743532/is-there-a-python-equivalent-to-ruby-symbols
# As others have said, there is no symbol in Python, but strings work well.
# To avoid quoting strings as keys, use the dict() constructor syntax:

d = dict(
    a = 1,
    b = 2,
    c = "Hello there",
    )
