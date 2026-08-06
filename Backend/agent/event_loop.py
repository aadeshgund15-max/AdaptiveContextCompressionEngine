"""
Adaptive Context Intelligence Engine (ACIE)

Autonomous Agent Event Loop

Responsible for:
- Task execution cycle
- State management
- Observation tracking
- Reflection
- Agent lifecycle
"""


import time
from typing import Any


from Backend.agent.task_manager import TaskManager
from Backend.agent.state_manager import StateManager
from Backend.agent.execution_engine import ExecutionEngine


class EventLoop:


    def __init__(
        self,
        task_manager=None,
        state_manager=None,
        execution_engine=None,
        observation_manager=None,
        reflection_engine=None
    ):


        self.task_manager = (
            task_manager
            or TaskManager()
        )


        self.state_manager = (
            state_manager
            or StateManager()
        )


        self.execution_engine = (
            execution_engine
            or ExecutionEngine(
                self.task_manager,
                self.state_manager
            )
        )


        self.observation_manager = observation_manager


        self.reflection_engine = reflection_engine


        self.running = False


        self.step_count = 0



    # -------------------------------------------------
    # Start Agent Loop
    # -------------------------------------------------


    def start(self):


        print(
            "\n========== AGENT EVENT LOOP STARTED ==========\n"
        )


        self.running = True


        self.state_manager.start()



        while self.running:


            try:


                task = (
                    self.task_manager.get_next_task()
                )


                # No task available

                if task is None:


                    time.sleep(0.5)

                    continue



                self.step_count += 1



                print(
                    f"\n[STEP {self.step_count}]"
                )


                print(
                    "Executing Task:",
                    task
                )



                # ---------------------------------
                # Execute Task
                # ---------------------------------


                result = (
                    self.execution_engine.execute_task(
                        task
                    )
                )



                # ---------------------------------
                # Observation
                # ---------------------------------


                if self.observation_manager:


                    self.observation_manager.record(

                        task,

                        result

                    )



                # ---------------------------------
                # Reflection
                # ---------------------------------


                if self.reflection_engine:

                    observations = None
                    if self.observation_manager:
                        observations = self.observation_manager.get_observations()

                    reflection = self.reflection_engine.reflect(observations)

                    print("Reflection:", reflection)



                # ---------------------------------
                # Shutdown Condition
                # ---------------------------------


                if (

                    task.lower()

                    in

                    [

                        "shutdown",

                        "finish",

                        "complete"

                    ]

                ):


                    self.stop()



            except Exception as e:



                print(

                    "\nAgent Loop Error:",

                    str(e)

                )


                self.state_manager.set_reasoning(

                    f"error: {str(e)}"

                )


                self.stop()



    # -------------------------------------------------
    # Stop Agent
    # -------------------------------------------------


    def stop(self):


        print(

            "\n========== EVENT LOOP STOPPED ==========\n"

        )


        self.running = False


        self.state_manager.stop()



    # -------------------------------------------------
    # Add Task
    # -------------------------------------------------


    def add_task(
        self,
        task:str
    ):


        self.task_manager.add_task(task)



    # -------------------------------------------------
    # Status
    # -------------------------------------------------


    def status(self)->dict[str,Any]:


        return {


            "running":

            self.running,


            "steps":

            self.step_count,


            "tasks":

            self.task_manager.status()


        }





if __name__ == "__main__":


    loop = EventLoop()


    loop.add_task(
        "Collect Context"
    )


    loop.add_task(
        "Retrieve Memories"
    )


    loop.add_task(
        "Reason"
    )


    loop.add_task(
        "Generate Response"
    )


    loop.add_task(
        "Shutdown"
    )


    loop.start()



    print(

        loop.status()

    )