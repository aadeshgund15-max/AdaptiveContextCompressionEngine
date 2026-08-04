"""
Adaptive Context Intelligence Engine (ACIE)
Prompt Builder
"""


class PromptBuilder:

    def __init__(self):

        self.default_system_prompt = """
You are ACIE (Adaptive Context Intelligence Engine).

Responsibilities:
- Answer accurately.
- Use retrieved memories whenever possible.
- Follow the reasoning plan.
- Never hallucinate facts.
- If context is insufficient, clearly mention it.
- Produce professional and well-structured responses.
"""

    # -------------------------------------------------
    # Build Prompt
    # -------------------------------------------------

    def build(

        self,

        query,

        context_window,

        reasoning_plan,

        conversation=None,

        metadata=None,

        system_instruction=None

    ):

        if conversation is None:
            conversation = []

        if metadata is None:
            metadata = {}

        if system_instruction is None:
            system_instruction = self.default_system_prompt

        prompt = ""

        # ==================================================
        # SYSTEM
        # ==================================================

        prompt += "================ SYSTEM ================\n"

        prompt += system_instruction.strip()

        prompt += "\n\n"

        # ==================================================
        # CONVERSATION
        # ==================================================

        if conversation:

            prompt += "========== CONVERSATION HISTORY ==========\n"

            for msg in conversation:

                if isinstance(msg, dict):

                    role = msg.get("role", "user")

                    content = msg.get("content", "")

                    prompt += f"{role.upper()}: {content}\n"

                else:

                    prompt += f"{msg}\n"

            prompt += "\n"

        # ==================================================
        # USER QUERY
        # ==================================================

        prompt += "=============== USER QUERY ===============\n"

        prompt += query

        prompt += "\n\n"

        # ==================================================
        # RETRIEVED MEMORIES
        # ==================================================

        prompt += "============ RETRIEVED MEMORIES ============\n"

        memories = context_window.get(

            "selected_memories",

            []

        )

        if not memories:

            prompt += "No relevant memories retrieved.\n"

        else:

            for index, memory in enumerate(memories, start=1):

                if isinstance(memory, dict):

                    text = memory.get("text", str(memory))

                else:

                    text = str(memory)

                prompt += f"{index}. {text}\n"

        prompt += "\n"

        # ==================================================
        # REASONING PLAN
        # ==================================================

        prompt += "============= REASONING PLAN =============\n"

        plan = reasoning_plan.get("plan", [])

        if not plan:

            prompt += "No reasoning plan available.\n"

        else:

            for step in plan:

                prompt += (

                    f"Step {step.get('step', '?')}: "

                    f"{step.get('task', '')}\n"

                )

        prompt += "\n"

        # ==================================================
        # METADATA
        # ==================================================

        if metadata:

            prompt += "================ METADATA ================\n"

            for key, value in metadata.items():

                prompt += f"{key}: {value}\n"

            prompt += "\n"

        # ==================================================
        # FINAL TASK
        # ==================================================

        prompt += "================= TASK ==================\n"

        prompt += (
            "Generate the best possible response using the "
            "retrieved memories and reasoning plan. "
            "If the provided context is insufficient, state "
            "that additional information is required instead "
            "of inventing facts."
        )

        prompt += "\n\n"

        prompt += "============== RESPONSE =================\n"

        return prompt


if __name__ == "__main__":

    builder = PromptBuilder()

    context = {

        "selected_memories": [

            {

                "text": "Adaptive Context Compression reduces token usage."

            },

            {

                "text": "Semantic retrieval improves memory relevance."

            }

        ]

    }

    plan = {

        "plan": [

            {

                "step": 1,

                "task": "Retrieve Memories"

            },

            {

                "step": 2,

                "task": "Reason"

            },

            {

                "step": 3,

                "task": "Generate Response"

            }

        ]

    }

    conversation = [

        {

            "role": "user",

            "content": "What is semantic retrieval?"

        },

        {

            "role": "assistant",

            "content": "Semantic retrieval finds information by meaning."

        }

    ]

    prompt = builder.build(

        query="Explain Adaptive Context Compression.",

        context_window=context,

        reasoning_plan=plan,

        conversation=conversation,

        metadata={

            "Intent": "Research",

            "Complexity": "High"

        }

    )

    print(prompt)