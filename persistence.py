"""
Game State Persistence System
Handles saving and loading of game state data
"""

import json
import os
from datetime import datetime
from typing import Dict, Any, Optional

class GameState:
    """Handles game state persistence"""
    
    def __init__(self, save_file: str = "drift_save.json"):
        self.save_file = save_file
        
    def save_state(self, state_data: Dict[str, Any]) -> bool:
        """Save game state to file"""
        try:
            with open(self.save_file, 'w') as f:
                json.dump(state_data, f, indent=2)
            return True
        except Exception as e:
            print(f"Failed to save state: {e}")
            return False
            
    def load_state(self) -> Optional[Dict[str, Any]]:
        """Load game state from file"""
        try:
            if os.path.exists(self.save_file):
                with open(self.save_file, 'r') as f:
                    return json.load(f)
            return None
        except Exception as e:
            print(f"Failed to load state: {e}")
            return None