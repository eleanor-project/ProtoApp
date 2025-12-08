from typing import List, Dict
from .storage import PrecedentStorage

class PrecedentSearch:
    """
    Simplified text-based precedent search.
    Will be upgraded to vector similarity in Step 3.
    """
    
    def __init__(self, storage: PrecedentStorage):
        self.storage = storage
    
    def search_precedents(self, query_text: str, limit: int = 5) -> List[Dict]:
        """
        Search for similar precedents using simple text matching.
        Returns top 'limit' most relevant precedents.
        """
        all_precedents = self.storage.get_all_precedents()
        
        if not all_precedents:
            return []
        
        # Simple keyword-based scoring
        query_lower = query_text.lower()
        query_words = set(query_lower.split())
        
        scored_precedents = []
        for prec in all_precedents:
            input_lower = prec["input_text"].lower()
            input_words = set(input_lower.split())
            
            # Calculate simple word overlap score
            overlap = len(query_words & input_words)
            score = overlap / max(len(query_words), 1)
            
            scored_precedents.append({
                "precedent": prec,
                "score": score
            })
        
        # Sort by score descending
        scored_precedents.sort(key=lambda x: x["score"], reverse=True)
        
        # Return top results
        results = []
        for item in scored_precedents[:limit]:
            if item["score"] > 0:  # Only return if there's some match
                results.append({
                    "id": item["precedent"]["id"],
                    "citation": item["precedent"]["citation"],
                    "input_text": item["precedent"]["input_text"],
                    "decision": item["precedent"]["decision"],
                    "critics": item["precedent"]["critics"],
                    "similarity_score": item["score"]
                })
        
        return results
