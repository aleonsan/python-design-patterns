# Design Pattern: Visitor
# Visited object
class Sword(object):

    def accept(self, visitor):
        """ Here we declare the relationiship btw objects """
        visitor.visit(self)

    def shine(self, believer):
        print(self, "shines holded by ", believer)

    def do_nothing(self, skeptical):
        print(self, "do nothing in presence of ", skeptical)

class MythologicSword(Sword):
    pass

class FakeSword(Sword):

    def shine(self, believer):
        print(self, "looks fake holded by ", believer)

# Visitor object
class Knight: pass

class Believer(Knight):
    def visit(self, sword):
        """ Here we declare the how will be the relationiship btw objects """
        sword.shine(self)

class Skeptical(Knight):
    def visit(self, sword):
        """ Here we declare the how will be the relationiship btw objects """
        sword.do_nothing(self)


def run_example():

    print("""
    ************************************************
    Visitor design pattern: Knights & swords
    ************************************************

    This design pattern shows how objects can interact in different ways
    depending on its own nature, and not coupling it behaviour to the visited
    object
    """)

    # two knights
    lancelot = Skeptical()
    arthur = Believer()

    # two swords
    excalibur = MythologicSword()
    heskalibug = FakeSword()

    # the facts
    excalibur.accept(lancelot)
    heskalibug.accept(arthur)
    excalibur.accept(arthur)
