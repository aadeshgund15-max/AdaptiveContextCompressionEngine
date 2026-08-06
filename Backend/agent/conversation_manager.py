"""
Adaptive Context Intelligence Engine (ACIE)

Conversation Manager

Responsible for:
- Multi-turn conversation handling
- Chat history management
- Context tracking
- Conversation compression
- Session management
"""


from __future__ import annotations

from datetime import datetime
from typing import Any, List, Dict



class ConversationManager:


    def __init__(self):

        self.sessions = {}

        self.current_session = None


    # -------------------------------------------------
    # Create Session
    # -------------------------------------------------

    def create_session(

        self,

        session_id: str

    ):


        self.sessions[session_id] = {


            "created_at":

            datetime.now().isoformat(),


            "messages":[]


        }


        self.current_session = session_id


        return session_id



    # -------------------------------------------------
    # Select Session
    # -------------------------------------------------

    def set_session(

        self,

        session_id:str

    ):


        if session_id in self.sessions:

            self.current_session = session_id



    # -------------------------------------------------
    # Add Message
    # -------------------------------------------------

    def add_message(

        self,

        role:str,

        content:str,

        metadata:dict|None=None

    ):


        if self.current_session is None:

            self.create_session(

                "default"

            )


        message = {


            "role":

            role,


            "content":

            content,


            "timestamp":

            datetime.now().isoformat(),


            "metadata":

            metadata or {}

        }


        self.sessions[

            self.current_session

        ]["messages"].append(message)



    # -------------------------------------------------
    # User Message
    # -------------------------------------------------

    def add_user_message(

        self,

        message:str

    ):


        self.add_message(

            "user",

            message

        )



    # -------------------------------------------------
    # Agent Message
    # -------------------------------------------------

    def add_agent_message(

        self,

        message:str,

        metadata:dict|None=None

    ):


        self.add_message(

            "agent",

            message,

            metadata

        )



    # -------------------------------------------------
    # Get History
    # -------------------------------------------------

    def get_history(

        self,

        limit=None

    ):


        if self.current_session is None:

            return []


        messages = self.sessions[

            self.current_session

        ]["messages"]


        if limit:

            return messages[-limit:]


        return messages



    # -------------------------------------------------
    # Build Context
    # -------------------------------------------------

    def build_context(

        self,

        max_messages=10

    ):


        history = self.get_history(

            max_messages

        )


        context = ""


        for message in history:


            context += (

                f"{message['role']}: "

                f"{message['content']}\n"

            )


        return context



    # -------------------------------------------------
    # Compression
    # -------------------------------------------------

    def compress_history(

        self,

        max_length=3000

    ):


        context = self.build_context()


        if len(context) <= max_length:

            return context


        return context[-max_length:]



    # -------------------------------------------------
    # Clear Session
    # -------------------------------------------------

    def clear_session(self):


        if self.current_session:

            self.sessions[

                self.current_session

            ]["messages"] = []



    # -------------------------------------------------
    # Delete Session
    # -------------------------------------------------

    def delete_session(

        self,

        session_id

    ):


        if session_id in self.sessions:

            del self.sessions[session_id]



    # -------------------------------------------------
    # Export
    # -------------------------------------------------

    def export(self):


        return {


            "current_session":

            self.current_session,


            "sessions":

            self.sessions


        }



    # -------------------------------------------------
    # Status
    # -------------------------------------------------

    def status(self):


        return {


            "sessions":

            len(self.sessions),


            "active_session":

            self.current_session,


            "messages":

            len(

                self.get_history()

            )


        }



# -------------------------------------------------
# Test
# -------------------------------------------------

if __name__=="__main__":


    manager = ConversationManager()


    manager.create_session(

        "user_001"

    )


    manager.add_user_message(

        "Explain AI agents"

    )


    manager.add_agent_message(

        "AI agents are autonomous systems."

    )


    print(

        manager.status()

    )


    print()

    print(

        manager.build_context()

    )