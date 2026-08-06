"""
Evaluation Dataset
"""


class EvaluationDataset:


    def __init__(self):

        self.samples = []



    def add_sample(
        self,
        original,
        compressed
    ):

        self.samples.append({

            "original":
                original,

            "compressed":
                compressed

        })



    def get_samples(self):

        return self.samples