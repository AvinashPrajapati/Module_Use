import configparser


def read_ini(filename="none", selection="none"):
    if filename == "none":
        return "no file name provided"

    if selection == "none":
        return "please provide selection"

    reader = configparser.ConfigParser()
    file = reader.read(filenames=filename)
    print("FIlename:", file)

    obj = {}
    if reader.has_section(selection):
        params = reader.items(selection)
        for param in params:
            obj[params[0]] = params[1]
    else:
        raise Exception("provided selection {0} is not available".format(selection))
    return obj
