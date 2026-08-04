"""
Adaptive Context Intelligence Engine (ACIE)
Provider Registry
"""


class ProviderRegistry:

    def __init__(self):

        self.providers = {}

    def register(

        self,

        name,

        provider

    ):

        self.providers[name.lower()] = provider

    def get(

        self,

        name

    ):

        return self.providers.get(

            name.lower()

        )

    def available_models(self):

        return list(

            self.providers.keys()

        )