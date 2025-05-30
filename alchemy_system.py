"""
Sigil Alchemy System: Glyph Combination Engine
Advanced mystical combination mechanics with pattern recognition
"""

import random
import json
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional, Tuple
import hashlib

class AlchemySystem:
    """Advanced alchemy system for combining glyphs into hybrid forms"""
    
    def __init__(self, glyph_manager):
        self.glyph_manager = glyph_manager
        
        # Alchemy state
        self.known_combinations = {}
        self.combination_history = []
        self.transmutation_count = 0
        self.mastery_level = 0
        
        # Pattern recognition data
        self.pattern_library = {}
        self.elemental_affinities = {}
        self.resonance_matrix = {}
        
        # Initialize base knowledge
        self.initialize_base_combinations()
        self.initialize_elemental_system()
        
    def initialize_base_combinations(self):
        """Initialize basic alchemical combinations"""
        base_glyphs = self.glyph_manager.get_all_glyphs()
        
        # Define fundamental combination patterns
        fundamental_patterns = {
            # Basic elemental combinations
            (base_glyphs[0], base_glyphs[1]): {
                "result_glyph": "⚡",
                "name": "Void Lightning",
                "properties": ["energy", "piercing", "unstable"],
                "potency": 0.7,
                "stability": 0.4,
                "entropy_cost": 0.1
            },
            (base_glyphs[1], base_glyphs[2]): {
                "result_glyph": "∾",
                "name": "Infinite Spiral",
                "properties": ["recursive", "growth", "time"],
                "potency": 0.6,
                "stability": 0.8,
                "entropy_cost": 0.15
            },
            (base_glyphs[2], base_glyphs[3]): {
                "result_glyph": "◊",
                "name": "Crystal Resonance",
                "properties": ["structure", "amplification", "memory"],
                "potency": 0.8,
                "stability": 0.9,
                "entropy_cost": 0.05
            },
            # Triple combinations
            (base_glyphs[0], base_glyphs[1], base_glyphs[2]): {
                "result_glyph": "⟐",
                "name": "Triadic Void",
                "properties": ["balance", "synthesis", "transcendence"],
                "potency": 0.9,
                "stability": 0.6,
                "entropy_cost": 0.25
            },
            (base_glyphs[1], base_glyphs[3], base_glyphs[4]): {
                "result_glyph": "⧨",
                "name": "Convergent Matrix",
                "properties": ["convergence", "power", "danger"],
                "potency": 1.0,
                "stability": 0.3,
                "entropy_cost": 0.4
            }
        }
        
        # Store combinations with pattern signatures
        for combination, result in fundamental_patterns.items():
            pattern_key = self._generate_pattern_key(list(combination))
            self.known_combinations[pattern_key] = result
            
    def initialize_elemental_system(self):
        """Initialize elemental affinities and resonance matrix"""
        base_glyphs = self.glyph_manager.get_all_glyphs()
        
        # Assign elemental affinities
        elemental_assignments = {
            base_glyphs[0]: "void",      # ▲
            base_glyphs[1]: "energy",    # ⊗
            base_glyphs[2]: "flow",      # ≈
            base_glyphs[3]: "stability", # ∇
            base_glyphs[4]: "change"     # ∆
        }
        
        self.elemental_affinities = elemental_assignments
        
        # Create resonance matrix
        elements = list(set(elemental_assignments.values()))
        for elem1 in elements:
            self.resonance_matrix[elem1] = {}
            for elem2 in elements:
                if elem1 == elem2:
                    self.resonance_matrix[elem1][elem2] = 1.0  # Perfect resonance
                else:
                    # Calculate resonance based on elemental relationships
                    resonance = self._calculate_elemental_resonance(elem1, elem2)
                    self.resonance_matrix[elem1][elem2] = resonance
                    
    def _calculate_elemental_resonance(self, elem1: str, elem2: str) -> float:
        """Calculate resonance between two elements"""
        resonance_rules = {
            ("void", "energy"): 0.8,
            ("void", "flow"): 0.3,
            ("void", "stability"): 0.1,
            ("void", "change"): 0.9,
            ("energy", "flow"): 0.7,
            ("energy", "stability"): 0.2,
            ("energy", "change"): 0.8,
            ("flow", "stability"): 0.4,
            ("flow", "change"): 0.6,
            ("stability", "change"): 0.1
        }
        
        # Check both directions
        key = (elem1, elem2)
        reverse_key = (elem2, elem1)
        
        return resonance_rules.get(key, resonance_rules.get(reverse_key, 0.5))
        
    def combine_glyphs(self, glyphs: List[str]) -> Dict[str, Any]:
        """Perform alchemical combination of glyphs"""
        if len(glyphs) < 2:
            raise ValueError("Need at least 2 glyphs for combination")
            
        if len(glyphs) > 5:
            raise ValueError("Cannot combine more than 5 glyphs at once")
            
        # Generate pattern key for this combination
        pattern_key = self._generate_pattern_key(glyphs)
        
        # Check if combination is known
        if pattern_key in self.known_combinations:
            result = self._execute_known_combination(pattern_key, glyphs)
        else:
            result = self._discover_new_combination(glyphs)
            
        # Record combination
        self._record_combination(glyphs, result)
        
        # Update mastery
        self._update_mastery()
        
        return result
        
    def _generate_pattern_key(self, glyphs: List[str]) -> str:
        """Generate a unique pattern key for glyph combination"""
        # Sort glyphs to ensure consistent pattern keys
        sorted_glyphs = sorted(glyphs)
        pattern_string = "".join(sorted_glyphs)
        
        # Create hash for pattern recognition
        pattern_hash = hashlib.md5(pattern_string.encode()).hexdigest()[:8]
        
        return f"pattern_{len(glyphs)}_{pattern_hash}"
        
    def _execute_known_combination(self, pattern_key: str, glyphs: List[str]) -> Dict[str, Any]:
        """Execute a known alchemical combination"""
        base_result = self.known_combinations[pattern_key].copy()
        
        # Apply mastery bonus
        mastery_bonus = self.mastery_level * 0.1
        base_result["potency"] = min(1.0, base_result["potency"] + mastery_bonus)
        
        # Apply entropy influence
        entropy_modifier = self._calculate_entropy_influence(glyphs)
        base_result["stability"] *= entropy_modifier
        
        # Calculate success
        success_chance = base_result["stability"] * (0.5 + mastery_bonus)
        success = random.random() < success_chance
        
        result = {
            "type": "known_combination",
            "success": success,
            "pattern_key": pattern_key,
            "input_glyphs": glyphs.copy(),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "mastery_bonus": mastery_bonus,
            "entropy_modifier": entropy_modifier
        }
        
        if success:
            result.update({
                "result_glyph": base_result["result_glyph"],
                "name": base_result["name"],
                "properties": base_result["properties"].copy(),
                "potency": base_result["potency"],
                "stability": base_result["stability"],
                "rarity": self._calculate_rarity(base_result["potency"])
            })
        else:
            result.update(self._generate_failure_result(glyphs))
            
        return result
        
    def _discover_new_combination(self, glyphs: List[str]) -> Dict[str, Any]:
        """Attempt to discover a new alchemical combination"""
        # Calculate discovery probability based on elemental resonance
        total_resonance = self._calculate_total_resonance(glyphs)
        discovery_chance = min(0.8, total_resonance * 0.3 + self.mastery_level * 0.1)
        
        success = random.random() < discovery_chance
        
        result = {
            "type": "new_discovery",
            "success": success,
            "input_glyphs": glyphs.copy(),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "discovery_chance": discovery_chance,
            "total_resonance": total_resonance
        }
        
        if success:
            new_combination = self._generate_new_combination(glyphs, total_resonance)
            
            # Store the new combination
            pattern_key = self._generate_pattern_key(glyphs)
            self.known_combinations[pattern_key] = {
                "result_glyph": new_combination["result_glyph"],
                "name": new_combination["name"],
                "properties": new_combination["properties"],
                "potency": new_combination["potency"],
                "stability": new_combination["stability"],
                "entropy_cost": new_combination["entropy_cost"]
            }
            
            result.update(new_combination)
            result["pattern_key"] = pattern_key
            result["discovery"] = True
        else:
            result.update(self._generate_failure_result(glyphs))
            
        return result
        
    def _calculate_total_resonance(self, glyphs: List[str]) -> float:
        """Calculate total resonance between all glyphs in combination"""
        if len(glyphs) < 2:
            return 0.0
            
        total_resonance = 0.0
        pair_count = 0
        
        for i in range(len(glyphs)):
            for j in range(i + 1, len(glyphs)):
                elem1 = self.elemental_affinities.get(glyphs[i], "unknown")
                elem2 = self.elemental_affinities.get(glyphs[j], "unknown")
                
                if elem1 in self.resonance_matrix and elem2 in self.resonance_matrix[elem1]:
                    total_resonance += self.resonance_matrix[elem1][elem2]
                    pair_count += 1
                    
        return total_resonance / max(1, pair_count)
        
    def _generate_new_combination(self, glyphs: List[str], resonance: float) -> Dict[str, Any]:
        """Generate a new combination result"""
        # Create hybrid glyph
        hybrid_glyphs = ["⟡", "⟢", "⟣", "⟤", "⟥", "⧆", "⧇", "⧈", "⧉", "⧊"]
        result_glyph = random.choice(hybrid_glyphs)
        
        # Generate name based on input elements
        elements = [self.elemental_affinities.get(g, "unknown") for g in glyphs]
        unique_elements = list(set(elements))
        
        name_parts = {
            "void": ["Void", "Shadow", "Null"],
            "energy": ["Lightning", "Flux", "Surge"],
            "flow": ["Stream", "Current", "Wave"],
            "stability": ["Crystal", "Anchor", "Foundation"],
            "change": ["Shift", "Mutation", "Evolution"],
            "unknown": ["Mystery", "Enigma", "Unknown"]
        }
        
        primary_element = max(unique_elements, key=lambda e: elements.count(e))
        secondary_element = None
        if len(unique_elements) > 1:
            secondary_element = [e for e in unique_elements if e != primary_element][0]
            
        name_components = name_parts[primary_element]
        if secondary_element:
            name_components.extend(name_parts[secondary_element])
            
        name = f"{random.choice(name_components)} {random.choice(['Synthesis', 'Fusion', 'Convergence', 'Amalgam'])}"
        
        # Generate properties based on input elements and resonance
        property_pool = {
            "void": ["nullification", "absorption", "emptiness"],
            "energy": ["amplification", "acceleration", "intensity"],
            "flow": ["fluidity", "adaptation", "continuity"],
            "stability": ["preservation", "structure", "endurance"],
            "change": ["transformation", "evolution", "chaos"]
        }
        
        properties = []
        for element in unique_elements:
            if element in property_pool:
                properties.extend(random.sample(property_pool[element], 
                                              min(2, len(property_pool[element]))))
                
        # Remove duplicates and limit
        properties = list(set(properties))[:4]
        
        # Calculate stats based on resonance and complexity
        complexity_factor = len(glyphs) / 5.0
        
        potency = min(1.0, resonance * 0.8 + complexity_factor * 0.3 + random.uniform(0.0, 0.2))
        stability = max(0.1, min(0.9, resonance * 0.9 - complexity_factor * 0.2))
        entropy_cost = complexity_factor * 0.2 + (1.0 - resonance) * 0.1
        
        return {
            "result_glyph": result_glyph,
            "name": name,
            "properties": properties,
            "potency": round(potency, 2),
            "stability": round(stability, 2),
            "entropy_cost": round(entropy_cost, 2),
            "rarity": self._calculate_rarity(potency)
        }
        
    def _generate_failure_result(self, glyphs: List[str]) -> Dict[str, Any]:
        """Generate result for failed combination"""
        failure_types = [
            "Resonance Collapse",
            "Elemental Rejection", 
            "Pattern Instability",
            "Entropy Overflow",
            "Harmonic Interference"
        ]
        
        failure_effects = [
            "glyph_scatter",
            "energy_discharge",
            "temporal_flux",
            "void_breach",
            "stability_loss"
        ]
        
        return {
            "result_glyph": "✗",
            "name": random.choice(failure_types),
            "properties": ["unstable", "dangerous"],
            "effect": random.choice(failure_effects),
            "potency": 0.0,
            "stability": 0.0,
            "entropy_cost": 0.05,
            "rarity": "failure"
        }
        
    def _calculate_entropy_influence(self, glyphs: List[str]) -> float:
        """Calculate how current entropy affects the combination"""
        # This would connect to the main engine's entropy field
        # For now, simulate entropy influence
        base_entropy = random.uniform(0.3, 0.8)
        
        # Higher entropy can either boost or destabilize
        if base_entropy > 0.7:
            return random.uniform(0.7, 1.3)  # Chaotic but potentially powerful
        elif base_entropy < 0.3:
            return random.uniform(0.9, 1.1)  # Stable but limited
        else:
            return random.uniform(0.8, 1.2)  # Balanced
            
    def _calculate_rarity(self, potency: float) -> str:
        """Calculate rarity based on potency"""
        if potency >= 0.9:
            return "legendary"
        elif potency >= 0.7:
            return "epic"
        elif potency >= 0.5:
            return "rare"
        elif potency >= 0.3:
            return "uncommon"
        else:
            return "common"
            
    def _record_combination(self, glyphs: List[str], result: Dict[str, Any]):
        """Record combination in history"""
        self.combination_history.append({
            "glyphs": glyphs.copy(),
            "result": result.copy(),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "mastery_at_time": self.mastery_level
        })
        
        self.transmutation_count += 1
        
        # Limit history size
        if len(self.combination_history) > 1000:
            self.combination_history = self.combination_history[-500:]
            
    def _update_mastery(self):
        """Update alchemy mastery level"""
        # Increase mastery based on successful combinations
        mastery_gain = 0.01
        
        # Bonus for discovering new combinations
        if self.combination_history and self.combination_history[-1]["result"].get("discovery"):
            mastery_gain *= 2
            
        self.mastery_level = min(10.0, self.mastery_level + mastery_gain)
        
    def calculate_fork_potential(self, fork_id: str) -> Dict[str, Any]:
        """Calculate alchemical potential for a fork"""
        # Analyze fork ID for hidden patterns
        id_chars = list(fork_id)
        pattern_strength = len(set(id_chars)) / len(id_chars)
        
        return {
            "pattern_strength": round(pattern_strength, 2),
            "resonance_potential": round(random.uniform(0.1, 0.9), 2),
            "stability_bias": round(random.uniform(-0.2, 0.2), 2),
            "elemental_inclination": random.choice(list(self.elemental_affinities.values()))
        }
        
    def get_known_combinations_count(self) -> int:
        """Get count of known combinations"""
        return len(self.known_combinations)
        
    def get_combination_by_pattern(self, pattern_key: str) -> Optional[Dict[str, Any]]:
        """Get combination data by pattern key"""
        return self.known_combinations.get(pattern_key)
        
    def get_recent_combinations(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent combination history"""
        return self.combination_history[-limit:]
        
    def get_mastery_info(self) -> Dict[str, Any]:
        """Get current mastery information"""
        return {
            "level": round(self.mastery_level, 2),
            "transmutations": self.transmutation_count,
            "known_patterns": len(self.known_combinations),
            "discovery_rate": self._calculate_discovery_rate(),
            "next_level_progress": round((self.mastery_level % 1.0) * 100, 1)
        }
        
    def _calculate_discovery_rate(self) -> float:
        """Calculate current discovery rate percentage"""
        if self.transmutation_count == 0:
            return 0.0
            
        discoveries = sum(1 for combo in self.combination_history 
                         if combo["result"].get("discovery", False))
        return round((discoveries / self.transmutation_count) * 100, 1)
        
    def export_state(self) -> Dict[str, Any]:
        """Export alchemy system state"""
        return {
            "known_combinations": self.known_combinations.copy(),
            "combination_history": self.combination_history.copy(),
            "transmutation_count": self.transmutation_count,
            "mastery_level": self.mastery_level,
            "elemental_affinities": self.elemental_affinities.copy(),
            "resonance_matrix": self.resonance_matrix.copy()
        }
        
    def import_state(self, state_data: Dict[str, Any]):
        """Import alchemy system state"""
        self.known_combinations = state_data.get("known_combinations", {})
        self.combination_history = state_data.get("combination_history", [])
        self.transmutation_count = state_data.get("transmutation_count", 0)
        self.mastery_level = state_data.get("mastery_level", 0)
        
        if "elemental_affinities" in state_data:
            self.elemental_affinities = state_data["elemental_affinities"]
        if "resonance_matrix" in state_data:
            self.resonance_matrix = state_data["resonance_matrix"]
