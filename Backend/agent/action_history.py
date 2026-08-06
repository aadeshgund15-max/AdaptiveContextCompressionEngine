"""
Adaptive Context Intelligence Engine (ACIE)

Action History

Responsible for:
- Recording agent actions
- Tracking execution timeline
- Storing tool usage
- Tracking failures
- Agent experience memory
"""


from datetime import datetime
from typing import Any
import uuid



class ActionHistory:


    def __init__(self):

        self.history = []

        self.session_id = str(uuid.uuid4())



    # -------------------------------------------------
    # Record Action
    # -------------------------------------------------

    def record(

        self,

        action:str,

        component:str,

        input_data:Any=None,

        output_data:Any=None,

        status:str="completed",

        metadata:dict|None=None

    ):


        event = {


            "id":

            str(uuid.uuid4()),


            "session_id":

            self.session_id,


            "timestamp":

            datetime.now().isoformat(),


            "action":

            action,


            "component":

            component,


            "input":

            input_data,


            "output":

            output_data,


            "status":

            status,


            "metadata":

            metadata or {}

        }



        self.history.append(event)


        return event



    # -------------------------------------------------
    # Record Task
    # -------------------------------------------------

    def record_task(

        self,

        task,

        result

    ):


        return self.record(

            action="task_execution",

            component="ExecutionEngine",

            input_data=task,

            output_data=result

        )



    # -------------------------------------------------
    # Record Tool Usage
    # -------------------------------------------------

    def record_tool(

        self,

        tool,

        arguments,

        result

    ):


        return self.record(

            action="tool_execution",

            component=tool,

            input_data=arguments,

            output_data=result

        )



    # -------------------------------------------------
    # Record Error
    # -------------------------------------------------

    def record_error(

        self,

        component,

        error

    ):


        return self.record(

            action="error",

            component=component,

            output_data=str(error),

            status="failed"

        )



    # -------------------------------------------------
    # Get History
    # -------------------------------------------------

    def get_history(

        self,

        limit=None

    ):


        if limit:

            return self.history[-limit:]


        return self.history



    # -------------------------------------------------
    # Filter Actions
    # -------------------------------------------------

    def filter_by_component(

        self,

        component

    ):


        return [

            item

            for item in self.history

            if item["component"] == component

        ]



    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    def statistics(self):


        total = len(

            self.history

        )


        completed = len(

            [

                x for x in self.history

                if x["status"]=="completed"

            ]

        )


        failed = len(

            [

                x for x in self.history

                if x["status"]=="failed"

            ]

        )


        return {


            "total_actions":

            total,


            "completed":

            completed,


            "failed":

            failed,


            "success_rate":

            (

                completed / total * 100

            )

            if total else 0


        }



    # -------------------------------------------------
    # Clear
    # -------------------------------------------------

    def clear(self):

        self.history = []



    # -------------------------------------------------
    # Export
    # -------------------------------------------------

    def export(self):


        return {


            "session_id":

            self.session_id,


            "history":

            self.history,


            "statistics":

            self.statistics()


        }



    # -------------------------------------------------
    # Status
    # -------------------------------------------------

    def status(self):


        return {


            "session":

            self.session_id,


            "actions":

            len(self.history)


        }



# -------------------------------------------------
# Test
# -------------------------------------------------

if __name__=="__main__":


    history = ActionHistory()


    history.record_task(

        "Retrieve Memories",

        {

            "count":5

        }

    )


    history.record_tool(

        "Retriever",

        {

            "query":"AI"

        },

        {

            "results":10

        }

    )


    history.record_error(

        "LLM",

        "Timeout"

    )


    print(

        history.statistics()

    )


    print(

        history.export()

    )