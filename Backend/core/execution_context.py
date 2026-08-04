"""
Adaptive Context Intelligence Engine (ACIE)
Execution Context
"""

import uuid
from datetime import datetime


class ExecutionContext:

    def __init__(self):

        self.reset()

    # --------------------------------------------------
    # Reset Context
    # --------------------------------------------------

    def reset(self):

        self.execution_id = str(uuid.uuid4())

        self.start_time = datetime.now()

        self.end_time = None

        self.query = ""

        self.session_id = None

        self.conversation = []

        self.documents = []

        self.intent = None

        self.complexity = None

        self.selected_model = None

        self.prompt = ""

        self.response = ""

        self.memory_result = None

        self.retrieval_result = None

        self.reasoning_result = None

        self.tool_calls = []

        self.errors = []

        self.metadata = {}

    # --------------------------------------------------
    # Query
    # --------------------------------------------------

    def set_query(self, query):

        self.query = query

    # --------------------------------------------------
    # Session
    # --------------------------------------------------

    def set_session(self, session_id):

        self.session_id = session_id

    # --------------------------------------------------
    # Conversation
    # --------------------------------------------------

    def set_conversation(self, conversation):

        self.conversation = conversation

    # --------------------------------------------------
    # Documents
    # --------------------------------------------------

    def set_documents(self, documents):

        self.documents = documents

    # --------------------------------------------------
    # Intent
    # --------------------------------------------------

    def set_intent(self, intent):

        self.intent = intent

    # --------------------------------------------------
    # Complexity
    # --------------------------------------------------

    def set_complexity(self, complexity):

        self.complexity = complexity

    # --------------------------------------------------
    # Memory
    # --------------------------------------------------

    def set_memory_result(self, result):

        self.memory_result = result

    # --------------------------------------------------
    # Retrieval
    # --------------------------------------------------

    def set_retrieval_result(self, result):

        self.retrieval_result = result

    # --------------------------------------------------
    # Reasoning
    # --------------------------------------------------

    def set_reasoning_result(self, result):

        self.reasoning_result = result

    # --------------------------------------------------
    # Prompt
    # --------------------------------------------------

    def set_prompt(self, prompt):

        self.prompt = prompt

    # --------------------------------------------------
    # Model
    # --------------------------------------------------

    def set_model(self, model):

        self.selected_model = model

    # --------------------------------------------------
    # Response
    # --------------------------------------------------

    def set_response(self, response):

        self.response = response

    # --------------------------------------------------
    # Tool Calls
    # --------------------------------------------------

    def add_tool_call(self, tool_name, result=None):

        self.tool_calls.append({

            "tool": tool_name,

            "result": result,

            "timestamp": datetime.now().isoformat()

        })

    # --------------------------------------------------
    # Errors
    # --------------------------------------------------

    def add_error(self, error):

        self.errors.append(str(error))

    # --------------------------------------------------
    # Metadata
    # --------------------------------------------------

    def add_metadata(self, key, value):

        self.metadata[key] = value

    # --------------------------------------------------
    # Finish
    # --------------------------------------------------

    def finish(self):

        self.end_time = datetime.now()

    # --------------------------------------------------
    # Execution Time
    # --------------------------------------------------

    def execution_time(self):

        if self.end_time is None:

            return None

        return round(

            (self.end_time - self.start_time).total_seconds(),

            3

        )

    # --------------------------------------------------
    # Summary
    # --------------------------------------------------

    def summary(self):

        return {

            "execution_id": self.execution_id,

            "session_id": self.session_id,

            "query": self.query,

            "intent": self.intent,

            "complexity": self.complexity,

            "model": self.selected_model,

            "execution_time": self.execution_time(),

            "tool_calls": len(self.tool_calls),

            "errors": len(self.errors)

        }

    # --------------------------------------------------
    # Export
    # --------------------------------------------------

    def to_dict(self):

        return {

            "execution_id": self.execution_id,

            "session_id": self.session_id,

            "query": self.query,

            "conversation": self.conversation,

            "documents": self.documents,

            "intent": self.intent,

            "complexity": self.complexity,

            "selected_model": self.selected_model,

            "prompt": self.prompt,

            "response": self.response,

            "memory_result": self.memory_result,

            "retrieval_result": self.retrieval_result,

            "reasoning_result": self.reasoning_result,

            "tool_calls": self.tool_calls,

            "errors": self.errors,

            "metadata": self.metadata,

            "execution_time": self.execution_time()

        }


if __name__ == "__main__":

    context = ExecutionContext()

    context.set_query(

        "Explain Adaptive Context Compression."

    )

    context.set_session(

        "SESSION-001"

    )

    context.set_intent(

        "research"

    )

    context.set_complexity(

        "HIGH"

    )

    context.set_model(

        "gemini"

    )

    context.add_tool_call(

        "Memory Retriever"

    )

    context.set_response(

        "Adaptive Context Compression is..."

    )

    context.finish()

    print()

    print(context.summary())

    print()

    print(context.to_dict())