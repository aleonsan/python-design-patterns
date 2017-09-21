# Design Pattern: Decorator
from enum import Enum
from datetime import datetime


class TaskCriticality(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 20
    VERY_HIGH = 100
    HELL_ON_EARTH = 9000


TASK_CRITICALITY_MAPPING = {
    'direct_push_to_master': TaskCriticality.HELL_ON_EARTH,
    'direct_push_to_develop': TaskCriticality.MEDIUM
}


class WeekendException(Exception):
    pass


class StahpItException(Exception):
    pass


class SysOpsDecorator:

    def __init__(self, f, *args, **kwargs):
        self.f = f

        # thats not maybe the best aprox to get one by one
        self.task_criticality = \
            TASK_CRITICALITY_MAPPING[self.f.__name__].value \
            if self.f.__name__ in TASK_CRITICALITY_MAPPING.keys() \
            else TaskCriticality.LOW.value

    def __call__(self, *args, **kwargs):
        is_weekend = datetime.today().weekday() > 5
        if is_weekend:
            raise WeekendException("Its weekend, so... Come on...")
        elif self.task_criticality > TaskCriticality.MEDIUM.value:
            print("[{task}] Cooling hell on earth, saving the day of {task}..."
                  .format(task=self.f.__name__))
            return

        print("[{task}] Executing {task}".format(task=self.f.__name__))
        self.f(*args, **kwargs)


@SysOpsDecorator
def direct_push_to_master():
    print("[direct_push_to_master] Ok its Hell on Earth now.")


@SysOpsDecorator
def direct_push_to_develop():
    print("[direct_push_to_develop] Tomorrow will fix it if necessary.")


def run_example():

    print("""
    ************************************************
    Decorator design pattern: SysOps
    ************************************************
    """)

    direct_push_to_master()
    direct_push_to_develop()
