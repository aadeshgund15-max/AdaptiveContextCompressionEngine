"""
Adaptive Context Intelligence Engine (ACIE)
Streaming Generator
"""

import time


class StreamingGenerator:

    def __init__(self):

        pass

    # ---------------------------------------
    # Stream Text
    # ---------------------------------------

    def stream(

        self,

        text,

        delay=0.05

    ):

        print("\n========== STREAMING ==========\n")

        words = text.split()

        for word in words:

            print(

                word,

                end=" ",

                flush=True

            )

            time.sleep(delay)

        print()

    # ---------------------------------------
    # Yield Tokens
    # ---------------------------------------

    def token_stream(

        self,

        text

    ):

        words = text.split()

        for word in words:

            yield word

    # ---------------------------------------
    # Collect Stream
    # ---------------------------------------

    def collect(

        self,

        generator

    ):

        output = ""

        for token in generator:

            output += token + " "

        return output.strip()


if __name__ == "__main__":

    response = (

        "Adaptive Context Intelligence Engine "

        "streams responses token by token "

        "to provide a real-time experience."

    )

    streamer = StreamingGenerator()

    streamer.stream(

        response,

        delay=0.1

    )

    print("\nCollected Output:\n")

    tokens = streamer.token_stream(

        response

    )

    print(

        streamer.collect(

            tokens

        )

    )