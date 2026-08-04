"""
Adaptive Context Intelligence Engine (ACIE)
Session Manager
"""

import uuid
from datetime import datetime


class SessionManager:

    def __init__(self):

        self.sessions = {}

    # --------------------------------------------------
    # Create Session
    # --------------------------------------------------

    def create_session(self):

        session_id = str(uuid.uuid4())

        self.sessions[session_id] = {

            "created_at": datetime.now().isoformat(),

            "updated_at": datetime.now().isoformat(),

            "conversation": [],

            "retrieved_memories": [],

            "documents": [],

            "active_model": None,

            "metadata": {}

        }

        return session_id

    # --------------------------------------------------
    # Session Exists
    # --------------------------------------------------

    def exists(self, session_id):

        return session_id in self.sessions

    # --------------------------------------------------
    # Get Session
    # --------------------------------------------------

    def get_session(self, session_id):

        return self.sessions.get(session_id)

    # --------------------------------------------------
    # Add Conversation Message
    # --------------------------------------------------

    def add_message(

        self,

        session_id,

        role,

        content

    ):

        if not self.exists(session_id):

            return

        self.sessions[session_id]["conversation"].append({

            "role": role,

            "content": content,

            "timestamp": datetime.now().isoformat()

        })

        self.sessions[session_id]["updated_at"] = datetime.now().isoformat()

    # --------------------------------------------------
    # Store Retrieved Memories
    # --------------------------------------------------

    def set_memories(

        self,

        session_id,

        memories

    ):

        if not self.exists(session_id):

            return

        self.sessions[session_id]["retrieved_memories"] = memories

    # --------------------------------------------------
    # Store Documents
    # --------------------------------------------------

    def set_documents(

        self,

        session_id,

        documents

    ):

        if not self.exists(session_id):

            return

        self.sessions[session_id]["documents"] = documents

    # --------------------------------------------------
    # Set Active Model
    # --------------------------------------------------

    def set_model(

        self,

        session_id,

        model

    ):

        if not self.exists(session_id):

            return

        self.sessions[session_id]["active_model"] = model

    # --------------------------------------------------
    # Metadata
    # --------------------------------------------------

    def update_metadata(

        self,

        session_id,

        key,

        value

    ):

        if not self.exists(session_id):

            return

        self.sessions[session_id]["metadata"][key] = value

    # --------------------------------------------------
    # Conversation
    # --------------------------------------------------

    def conversation(

        self,

        session_id

    ):

        if not self.exists(session_id):

            return []

        return self.sessions[session_id]["conversation"]

    # --------------------------------------------------
    # Delete Session
    # --------------------------------------------------

    def delete_session(

        self,

        session_id

    ):

        if self.exists(session_id):

            del self.sessions[session_id]

    # --------------------------------------------------
    # List Sessions
    # --------------------------------------------------

    def list_sessions(self):

        return list(self.sessions.keys())

    # --------------------------------------------------
    # Summary
    # --------------------------------------------------

    def summary(self):

        return {

            "active_sessions": len(self.sessions),

            "session_ids": self.list_sessions()

        }


if __name__ == "__main__":

    manager = SessionManager()

    session = manager.create_session()

    manager.add_message(

        session,

        "user",

        "Explain Adaptive Context Compression."

    )

    manager.add_message(

        session,

        "assistant",

        "Adaptive Context Compression is..."

    )

    manager.set_model(

        session,

        "gemini"

    )

    print()

    print(manager.get_session(session))

    print()

    print(manager.summary())