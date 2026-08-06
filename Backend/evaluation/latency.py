"""
Latency Evaluation
"""


import time



class LatencyEvaluator:


    @staticmethod
    def measure(function, *args, **kwargs):


        start = time.perf_counter()


        result = function(
            *args,
            **kwargs
        )


        end = time.perf_counter()


        return {


            "result":
                result,


            "latency":
                round(
                    end - start,
                    4
                )

        }