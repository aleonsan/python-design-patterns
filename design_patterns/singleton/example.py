# Design Pattern: Singleton
# Example description: There can be only one


class Highlander:

    def __new__(cls, *arg, **kwargs):
        """
        __new__ is the first step in object creation,
        returning the new instance
        """
        if not hasattr(cls, '_highlander'):
            cls._highlander = super(Highlander, cls).__new__(cls)

        # Here, we have THE instance of Highlander
        return cls._highlander

    def __init__(self, name):
        """ Just name her/him """
        self.name = name


def run_example():

    # preface
    print("""
    ******************************************
    Singleton design pattern: Highlanders
    ******************************************
    """)

    # release El Kurgan
    kurgan = Highlander('El Kurgan')
    print('Here there is the great %s.' % kurgan.name)

    # release Connor McLeod
    connor = Highlander('Connor McLeod')
    print('But then, here there is the great %s too.' % connor.name)

    print('So, we have %s in %s and %s in %s. Errr....' % (kurgan.name,
                                                           id(kurgan),
                                                           connor.name,
                                                           id(connor)))

    if id(connor) == id(kurgan):
        print('There can be only ONE!')
    else:
        print('Singleton doesnt work')
