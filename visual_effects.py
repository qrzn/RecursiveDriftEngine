"""
Visual Effects Manager: Mystical Visual Enhancements
Handles particle effects and visual feedback for the interface
"""

import random
import tkinter as tk
from typing import Dict, Any, List, Optional

class VisualEffectsManager:
    """Manages visual effects and particle systems"""
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.effects_enabled = True
        self.particle_systems = []
        self.active_effects = []
        
    def update_particle_systems(self):
        """Update all active particle systems"""
        if not self.effects_enabled:
            return
            
        # Simulate particle system updates
        for system in self.particle_systems:
            system['lifetime'] -= 0.1
            if system['lifetime'] <= 0:
                self.particle_systems.remove(system)
                
    def create_entropy_effect(self, x: int, y: int) -> Dict[str, Any]:
        """Create entropy fluctuation visual effect"""
        effect = {
            'type': 'entropy_swirl',
            'x': x,
            'y': y,
            'lifetime': 3.0,
            'intensity': random.uniform(0.5, 1.0)
        }
        self.particle_systems.append(effect)
        return effect
        
    def create_glyph_resonance(self, glyph: str, x: int, y: int) -> Dict[str, Any]:
        """Create glyph resonance visual effect"""
        effect = {
            'type': 'glyph_resonance',
            'glyph': glyph,
            'x': x,
            'y': y,
            'lifetime': 2.0,
            'resonance': random.uniform(0.3, 0.8)
        }
        self.particle_systems.append(effect)
        return effect
        
    def flash_screen(self, color: str = "purple", duration: float = 0.2):
        """Create screen flash effect"""
        if self.effects_enabled:
            print(f"Screen flash: {color} for {duration}s")
            
    def set_effects_enabled(self, enabled: bool):
        """Enable or disable visual effects"""
        self.effects_enabled = enabled