"""
Eleanor Precedent System - Simplified Local Version
This will be upgraded to PostgreSQL + pgvector in Step 3
"""

from .storage import PrecedentStorage
from .search import PrecedentSearch

__all__ = ['PrecedentStorage', 'PrecedentSearch']
