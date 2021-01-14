#docstring is 1st line in function and is enclosed in 3 double quotes
def format_name(f_name, l_name):
    """ Take a first and last name, format them 
        in Title case, and concatenate them
        separated with a space. """
    f_name = f_name.title()
    l_name = l_name.title()
    return f_name + " " + l_name

print(format_name("sean","bLessing"))