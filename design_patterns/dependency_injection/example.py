# Design Pattern: Dependency Injection


# this could be in a "detective episode scripts" module
class SolveBoringEpisode:
    def notice_butler_guilt_AGAIN():
        print("¬_¬")

    def mutter_to_himself_even_louder():
        print("mumble mumble...")


class SolveVeryBoringEpisode:
    def notice_butler_guilt_AGAIN():
        print("u¬_¬")

    def mutter_to_himself_even_louder():
        print("mumble mumble mumble mumble...")


class Detective:

    def __init__(self, name, sex_appeal, *args, **kwargs):
        self.name = name
        self.sex_appeal = sex_appeal

    def solve_the_case(self):
        self.notice_random_things()
        self.do_speech()


EPISODE_LIST = dict(enumerate([SolveBoringEpisode,
                               SolveBoringEpisode,
                               SolveVeryBoringEpisode], 1))


def run_example(episode):

    # preface
    print("""
    ************************************************
    Dependency Injection design pattern: Columbo 
    ************************************************
    """)

    # Something happened Lets call Colombo
    detective = Detective('Colombo', -1)
    print('We called detective %s to solve this case.' % detective.name)

    # depending on the script, could be dynamic too, depending on the season
    # share
    gather_episode_facts = EPISODE_LIST[episode].notice_butler_guilt_AGAIN
    do_episode_speech = EPISODE_LIST[episode].mutter_to_himself_even_louder
    # lets set the environment to define how detective will interact with it
    detective.notice_random_things = gather_episode_facts
    detective.do_speech = do_episode_speech
    detective.solve_the_case()

    print('THE END')
