"""
Glyph Manager: Core Symbol System
Manages mystical glyphs and their properties
"""

import random
from typing import Dict, List, Any, Optional

class GlyphManager:
    """Central manager for all mystical glyphs"""
    
    def __init__(self):
        # Base glyph set
        self.base_glyphs = ["▲", "⊗", "≈", "∇", "∆"]
        
        # Extended glyph set for combinations
        self.extended_glyphs = [
            "◊", "⟡", "⟢", "⟣", "⟤", "⟥", 
            "⧆", "⧇", "⧈", "⧉", "⧊", "⧨", "⟐"
        ]
        
        # Special glyphs for failures and unique states
        self.special_glyphs = ["✗", "Ψ", "∾", "⚡"]
        
        # Glyph properties and meanings
        self.glyph_properties = {
            "▲": {"element": "void", "power": 0.7, "stability": 0.8},
            "⊗": {"element": "energy", "power": 0.9, "stability": 0.5},
            "≈": {"element": "flow", "power": 0.6, "stability": 0.9},
            "∇": {"element": "stability", "power": 0.8, "stability": 1.0},
            "∆": {"element": "change", "power": 0.8, "stability": 0.3},
            "◊": {"element": "crystal", "power": 0.8, "stability": 0.9},
            "⟡": {"element": "hybrid", "power": 0.7, "stability": 0.6},
            "⧆": {"element": "matrix", "power": 1.0, "stability": 0.4},
            "⧨": {"element": "convergence", "power": 1.0, "stability": 0.3},
            "⟐": {"element": "triadic", "power": 0.9, "stability": 0.6},
            "✗": {"element": "failure", "power": 0.0, "stability": 0.0},
            "Ψ": {"element": "transcendent", "power": 1.0, "stability": 0.7},
            "∾": {"element": "infinite", "power": 0.6, "stability": 0.8},
            "⚡": {"element": "lightning", "power": 0.7, "stability": 0.4}
        }
        
    def get_all_glyphs(self) -> List[str]:
        """Get all available glyphs"""
        return self.base_glyphs.copy()
        
    def get_extended_glyphs(self) -> List[str]:
        """Get extended glyph set for combinations"""
        return self.extended_glyphs.copy()
        
    def get_glyph_properties(self, glyph: str) -> Dict[str, Any]:
        """Get properties of a specific glyph"""
        return self.glyph_properties.get(glyph, {
            "element": "unknown",
            "power": 0.5,
            "stability": 0.5
        })
        
    def get_random_glyph(self, glyph_set: str = "base") -> str:
        """Get a random glyph from specified set"""
        if glyph_set == "extended":
            return random.choice(self.extended_glyphs)
        elif glyph_set == "special":
            return random.choice(self.special_glyphs)
        else:
            return random.choice(self.base_glyphs)
            
    def is_valid_glyph(self, glyph: str) -> bool:
        """Check if a glyph is valid"""
        all_glyphs = self.base_glyphs + self.extended_glyphs + self.special_glyphs
        return glyph in all_glyphs