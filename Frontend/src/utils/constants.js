/*
=====================================================

Adaptive Context Intelligence Engine (ACIE)

Frontend Constants

Responsible for:
- API configuration
- Application metadata
- Navigation data
- System configuration

=====================================================
*/





// -----------------------------------------
// Application Information
// -----------------------------------------


export const APP_CONFIG = {


    name:

        "ACIE",


    fullName:

        "Adaptive Context Intelligence Engine",


    version:

        "1.0.0",


    description:

        "Autonomous AI Context Intelligence Platform"


};








// -----------------------------------------
// Backend Configuration
// -----------------------------------------


export const API_CONFIG = {


    BASE_URL:

        "http://127.0.0.1:8000",



    ENDPOINTS:{


        CHAT:

            "/chat",



        MEMORY:

            "/memories",



        HEALTH:

            "/health",



        STATUS:

            "/agent/status",



        EVALUATION:

            "/evaluation"


    }


};








// -----------------------------------------
// Sidebar Navigation
// -----------------------------------------


export const NAVIGATION_ITEMS=[


    {


        name:

            "Dashboard",


        path:

            "/",


        icon:

            "dashboard"


    },



    {


        name:

            "Chat",


        path:

            "/chat",


        icon:

            "chat"


    },



    {


        name:

            "Memory",


        path:

            "/memory",


        icon:

            "memory"


    },



    {


        name:

            "Evaluation",


        path:

            "/evaluation",


        icon:

            "evaluation"


    }


];








// -----------------------------------------
// Agent Modules
// -----------------------------------------


export const AGENT_MODULES=[


    "Task Manager",


    "Memory Pipeline",


    "Retrieval Pipeline",


    "Reasoning Engine",


    "Execution Engine",


    "Response Generator"


];








// -----------------------------------------
// Default Metrics
// -----------------------------------------


export const DEFAULT_METRICS={


    compressionRatio:

        "0%",



    tokenReduction:

        "0%",



    memories:

        0,



    latency:

        "0ms"



};








// -----------------------------------------
// Local Storage Keys
// -----------------------------------------


export const STORAGE_KEYS={


    TOKEN:

        "acie_token",



    SESSION:

        "acie_session",



    THEME:

        "acie_theme"


};