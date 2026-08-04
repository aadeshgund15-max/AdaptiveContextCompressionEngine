"""
Adaptive Context Intelligence Engine (ACIE)
LLM Router
"""

from Backend.llm.model_registry import ModelRegistry


class LLMRouter:

    def __init__(self):

        self.registry = ModelRegistry()

    # -------------------------------------------------
    # Select Best Model
    # -------------------------------------------------

    def select_model(

        self,

        request

    ):

        intent = request.get(

            "intent",

            "general"

        ).lower()

        complexity = request.get(

            "complexity",

            "LOW"

        ).upper()

        require_vision = request.get(

            "vision",

            False

        )

        require_coding = request.get(

            "coding",

            False

        )

        offline = request.get(

            "offline",

            False

        )

        # -----------------------------------------
        # Vision
        # -----------------------------------------

        if require_vision or intent == "vision":

            return "gemini"

        # -----------------------------------------
        # Coding
        # -----------------------------------------

        if require_coding or intent == "coding":

            return "gpt"

        # -----------------------------------------
        # Research
        # -----------------------------------------

        if intent == "research":

            return "claude"

        # -----------------------------------------
        # Mathematics
        # -----------------------------------------

        if intent == "math":

            return "deepseek"

        # -----------------------------------------
        # Offline
        # -----------------------------------------

        if offline:

            return "ollama"

        # -----------------------------------------
        # Fast Queries
        # -----------------------------------------

        if complexity == "LOW":

            return "groq"

        # -----------------------------------------
        # Long Reasoning
        # -----------------------------------------

        if complexity == "HIGH":

            return "claude"

        # -----------------------------------------
        # Default
        # -----------------------------------------

        return "gemini-2.5-flash-lite"

    # -------------------------------------------------
    # Route Request
    # -------------------------------------------------

    def route(

        self,

        request

    ):

        requested_model = self.select_model(

            request

        )

        info = self.registry.get_model(

            requested_model

        )

        # -----------------------------------------
        # Fallback
        # -----------------------------------------

        if info is None:

            requested_model = "gemini"

            info = self.registry.get_model(

                "gemini"

            ) or {}

        return {

            "selected_model": requested_model,

            "provider": info.get(

                "provider"

            ),

            "model_name": info.get(

                "model_name"

            ),

            "capabilities": info.get(

                "capabilities"

            )

        }

    # -------------------------------------------------
    # Supported Providers
    # -------------------------------------------------

    def available_models(self):

        return self.registry.available_models()


if __name__ == "__main__":

    router = LLMRouter()

    examples = [

        {

            "intent": "general",

            "complexity": "LOW"

        },

        {

            "intent": "coding",

            "complexity": "HIGH"

        },

        {

            "intent": "research",

            "complexity": "HIGH"

        },

        {

            "intent": "vision",

            "vision": True

        },

        {

            "intent": "math"

        },

        {

            "offline": True

        }

    ]

    for request in examples:

        print()

        print(router.route(request))