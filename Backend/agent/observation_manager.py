"""
ACIE Observation Manager

Tracks agent actions,
outputs and execution history.
"""


class ObservationManager:


    def __init__(self):

        self.observations=[]


    def record(
        self,
        task,
        result
    ):

        self.observations.append(
            {
                "task":task,
                "result":result
            }
        )


    def get_observations(self):

        return self.observations


    def clear(self):

        self.observations=[]