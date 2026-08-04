"""
Adaptive Context Intelligence Engine (ACIE)
Constants
"""

# -------------------------------------------------
# Models
# -------------------------------------------------

DEFAULT_PROVIDER = "groq"

DEFAULT_MODEL = "llama-3.3-70b-versatile"

# -------------------------------------------------
# Cache
# -------------------------------------------------

CACHE_TTL = 300

EMBEDDING_CACHE_TTL = 3600

CACHE_MAX_ENTRIES = 1000

# -------------------------------------------------
# Memory
# -------------------------------------------------

WORKING_MEMORY_SIZE = 10

LONG_TERM_MEMORY_SIZE = 5000

# -------------------------------------------------
# Retrieval
# -------------------------------------------------

TOP_K = 5

SIMILARITY_THRESHOLD = 0.70

# -------------------------------------------------
# Token Budget
# -------------------------------------------------

MAX_CONTEXT_TOKENS = 32000

RESERVED_OUTPUT_TOKENS = 4000

# -------------------------------------------------
# Logging
# -------------------------------------------------

LOG_LEVEL = "DEBUG"

LOG_FILE = "logs/acie.log"

# -------------------------------------------------
# API
# -------------------------------------------------

API_VERSION = "2.0.0"

PROJECT_NAME = "Adaptive Context Intelligence Engine"