def two_fer(name="you"):
    """
    Creates sentence "One for [name], one for me." with parameter name inserted

    :param name: string indicating person's name, defaults to "you"
    :return: sentence with person's name included
    """
    return "One for {}, one for me.".format(name)
