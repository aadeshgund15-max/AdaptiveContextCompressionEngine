"""
Adaptive Context Intelligence Engine (ACIE)

Agent Configuration

Responsible for:
- Central agent settings
- Model configuration
- Memory configuration
- Runtime behavior
- Feature control
"""


from dataclasses import dataclass, field
from typing import Dict, Any



# -------------------------------------------------
# LLM Configuration
# -------------------------------------------------

@dataclass
class LLMConfig:


    provider: str = "gemini"


    model: str = "gemini-2.0-flash"


    temperature: float = 0.3


    max_tokens: int = 2048


    streaming: bool = True



# -------------------------------------------------
# Memory Configuration
# -------------------------------------------------

@dataclass
class MemoryConfig:


    enable_long_term_memory: bool = True


    enable_working_memory: bool = True


    enable_conversation_memory: bool = True


    max_memory_results: int = 5


    similarity_threshold: float = 0.75



# -------------------------------------------------
# Retrieval Configuration
# -------------------------------------------------

@dataclass
class RetrievalConfig:


    enabled: bool = True


    top_k: int = 5


    token_budget: int = 1000


    reranking: bool = True


    multi_hop: bool = True



# -------------------------------------------------
# Agent Behavior Configuration
# -------------------------------------------------

@dataclass
class AgentBehaviorConfig:


    autonomous_mode: bool = True


    reflection_enabled: bool = True


    planning_enabled: bool = True


    self_correction: bool = True


    max_iterations: int = 10



# -------------------------------------------------
# Tool Configuration
# -------------------------------------------------

@dataclass
class ToolConfig:


    tools_enabled: bool = True


    allow_external_tools: bool = False


    max_tool_calls: int = 10



# -------------------------------------------------
# Runtime Configuration
# -------------------------------------------------

@dataclass
class RuntimeConfig:


    debug: bool = True


    save_history: bool = True


    enable_metrics: bool = True


    timeout_seconds: int = 120



# -------------------------------------------------
# Main Agent Configuration
# -------------------------------------------------

@dataclass
class AgentConfig:


    name: str = (

        "Adaptive Context Intelligence Engine"

    )


    version: str = "1.0.0"



    llm: LLMConfig = field(

        default_factory=LLMConfig

    )


    memory: MemoryConfig = field(

        default_factory=MemoryConfig

    )


    retrieval: RetrievalConfig = field(

        default_factory=RetrievalConfig

    )


    behavior: AgentBehaviorConfig = field(

        default_factory=AgentBehaviorConfig

    )


    tools: ToolConfig = field(

        default_factory=ToolConfig

    )


    runtime: RuntimeConfig = field(

        default_factory=RuntimeConfig

    )



    # -------------------------------------------------

    # Export Configuration

    # -------------------------------------------------

    def export(self)->Dict[str,Any]:


        return {


            "name":

            self.name,


            "version":

            self.version,


            "llm":

            self.llm.__dict__,


            "memory":

            self.memory.__dict__,


            "retrieval":

            self.retrieval.__dict__,


            "behavior":

            self.behavior.__dict__,


            "tools":

            self.tools.__dict__,


            "runtime":

            self.runtime.__dict__

        }



    # -------------------------------------------------

    # Update Config

    # -------------------------------------------------

    def update(

        self,

        section:str,

        values:dict

    ):


        target = getattr(

            self,

            section,

            None

        )


        if target is None:

            raise ValueError(

                f"Unknown config section {section}"

            )


        for key,value in values.items():

            if hasattr(target,key):

                setattr(

                    target,

                    key,

                    value

                )



    # -------------------------------------------------

    # Status

    # -------------------------------------------------

    def status(self):


        return {


            "agent":

            self.name,


            "version":

            self.version,


            "model":

            self.llm.model,


            "provider":

            self.llm.provider,


            "autonomous":

            self.behavior.autonomous_mode


        }



# -------------------------------------------------
# Default Global Config
# -------------------------------------------------

DEFAULT_CONFIG = AgentConfig()



# -------------------------------------------------
# Test
# -------------------------------------------------

if __name__=="__main__":


    config = AgentConfig()


    print(

        config.status()

    )


    print()


    print(

        config.export()

    )


    config.update(

        "llm",

        {

            "temperature":0.7

        }

    )


    print()

    print(

        config.llm.temperature

    )