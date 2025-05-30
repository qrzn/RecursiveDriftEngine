"""
Entropy Rites System: Mini-Games for Mystical Manipulation
Interactive games that affect reality through skill and chance
"""

import random
import json
import math
import time
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional, Tuple, Callable

class SigilDrawGame:
    """Containment Sigil Draw mini-game"""
    
    def __init__(self):
        self.game_state = "inactive"
        self.current_pattern = []
        self.target_pattern = []
        self.accuracy_threshold = 0.7
        self.time_limit = 30.0  # seconds
        self.start_time = None
        self.score = 0
        self.combo_multiplier = 1.0
        
    def start_game(self, difficulty: str = "medium") -> Dict[str, Any]:
        """Start a new containment sigil draw game"""
        difficulty_settings = {
            "easy": {"pattern_length": 4, "time_limit": 45.0, "accuracy_threshold": 0.6},
            "medium": {"pattern_length": 6, "time_limit": 30.0, "accuracy_threshold": 0.7},
            "hard": {"pattern_length": 8, "time_limit": 20.0, "accuracy_threshold": 0.8},
            "nightmare": {"pattern_length": 10, "time_limit": 15.0, "accuracy_threshold": 0.9}
        }
        
        settings = difficulty_settings.get(difficulty, difficulty_settings["medium"])
        
        # Generate target pattern
        glyph_pool = ["▲", "⊗", "≈", "∇", "∆", "◊", "⟡", "⧆"]
        self.target_pattern = random.sample(glyph_pool, settings["pattern_length"])
        
        # Apply settings
        self.time_limit = settings["time_limit"]
        self.accuracy_threshold = settings["accuracy_threshold"]
        
        # Reset game state
        self.current_pattern = []
        self.game_state = "active"
        self.start_time = time.time()
        self.score = 0
        self.combo_multiplier = 1.0
        
        return {
            "success": True,
            "game_type": "containment_sigil_draw",
            "difficulty": difficulty,
            "target_pattern_length": len(self.target_pattern),
            "time_limit": self.time_limit,
            "accuracy_threshold": self.accuracy_threshold,
            "instructions": "Draw the containment sigil by selecting glyphs in the correct sequence"
        }
        
    def add_glyph(self, glyph: str) -> Dict[str, Any]:
        """Add a glyph to the current pattern"""
        if self.game_state != "active":
            return {
                "success": False,
                "error": "Game not active"
            }
            
        # Check time limit
        elapsed_time = time.time() - self.start_time
        if elapsed_time > self.time_limit:
            return self.end_game()
            
        self.current_pattern.append(glyph)
        
        # Check if pattern is complete
        if len(self.current_pattern) >= len(self.target_pattern):
            return self.end_game()
            
        # Calculate partial accuracy
        correct_positions = sum(1 for i, g in enumerate(self.current_pattern) 
                              if i < len(self.target_pattern) and g == self.target_pattern[i])
        partial_accuracy = correct_positions / len(self.current_pattern)
        
        # Update combo multiplier
        if len(self.current_pattern) > 0:
            if self.current_pattern[-1] == self.target_pattern[len(self.current_pattern)-1]:
                self.combo_multiplier = min(3.0, self.combo_multiplier + 0.2)
            else:
                self.combo_multiplier = max(1.0, self.combo_multiplier - 0.3)
                
        return {
            "success": True,
            "glyph_added": glyph,
            "current_pattern": self.current_pattern.copy(),
            "pattern_progress": f"{len(self.current_pattern)}/{len(self.target_pattern)}",
            "partial_accuracy": round(partial_accuracy, 2),
            "combo_multiplier": round(self.combo_multiplier, 1),
            "time_remaining": round(self.time_limit - elapsed_time, 1)
        }
        
    def end_game(self) -> Dict[str, Any]:
        """End the current game and calculate results"""
        if self.game_state != "active":
            return {
                "success": False,
                "error": "Game not active"
            }
            
        self.game_state = "completed"
        elapsed_time = time.time() - self.start_time
        
        # Calculate final accuracy
        correct_positions = sum(1 for i, g in enumerate(self.current_pattern) 
                              if i < len(self.target_pattern) and g == self.target_pattern[i])
        final_accuracy = correct_positions / len(self.target_pattern)
        
        # Calculate score
        base_score = correct_positions * 100
        time_bonus = max(0, (self.time_limit - elapsed_time) * 10)
        combo_bonus = (self.combo_multiplier - 1.0) * 200
        self.score = int(base_score + time_bonus + combo_bonus)
        
        # Determine success
        game_success = final_accuracy >= self.accuracy_threshold
        
        # Calculate rewards
        entropy_effect = 0.0
        time_salt_reward = 0
        fragment_reward = 0
        
        if game_success:
            entropy_effect = random.uniform(0.1, 0.3) * self.combo_multiplier
            time_salt_reward = random.randint(2, 8)
            fragment_reward = random.randint(1, 5)
            
            if final_accuracy >= 0.95:  # Perfect or near-perfect
                entropy_effect *= 1.5
                time_salt_reward *= 2
                fragment_reward += random.randint(2, 5)
                
        result = {
            "success": True,
            "game_success": game_success,
            "final_accuracy": round(final_accuracy, 3),
            "target_pattern": self.target_pattern.copy(),
            "drawn_pattern": self.current_pattern.copy(),
            "score": self.score,
            "time_taken": round(elapsed_time, 2),
            "combo_multiplier": round(self.combo_multiplier, 1),
            "rewards": {
                "entropy_effect": round(entropy_effect, 3),
                "time_salt": time_salt_reward,
                "identity_fragments": fragment_reward
            }
        }
        
        if game_success:
            result["containment_quality"] = self._calculate_containment_quality(final_accuracy)
            
        return result
        
    def _calculate_containment_quality(self, accuracy: float) -> Dict[str, Any]:
        """Calculate the quality of the containment sigil"""
        quality_levels = ["unstable", "weak", "stable", "strong", "perfect"]
        
        if accuracy >= 0.95:
            quality = "perfect"
            stability = random.uniform(0.9, 1.0)
        elif accuracy >= 0.85:
            quality = "strong"
            stability = random.uniform(0.8, 0.9)
        elif accuracy >= 0.75:
            quality = "stable"
            stability = random.uniform(0.7, 0.8)
        elif accuracy >= 0.65:
            quality = "weak"
            stability = random.uniform(0.5, 0.7)
        else:
            quality = "unstable"
            stability = random.uniform(0.2, 0.5)
            
        return {
            "quality": quality,
            "stability": round(stability, 2),
            "containment_power": round(accuracy * stability, 2),
            "duration": random.randint(5, 30)  # minutes
        }

class FeedbackChantGame:
    """Feedback Chant Match mini-game"""
    
    def __init__(self):
        self.game_state = "inactive"
        self.chant_sequence = []
        self.player_sequence = []
        self.current_phase = 0
        self.rhythm_accuracy = []
        self.tempo = 1.0
        self.phase_count = 5
        
    def start_game(self, difficulty: str = "medium") -> Dict[str, Any]:
        """Start a new feedback chant match game"""
        difficulty_settings = {
            "easy": {"phase_count": 3, "tempo": 0.8, "complexity": "simple"},
            "medium": {"phase_count": 5, "tempo": 1.0, "complexity": "moderate"},
            "hard": {"phase_count": 7, "tempo": 1.2, "complexity": "complex"},
            "nightmare": {"phase_count": 10, "tempo": 1.5, "complexity": "chaotic"}
        }
        
        settings = difficulty_settings.get(difficulty, difficulty_settings["medium"])
        
        self.phase_count = settings["phase_count"]
        self.tempo = settings["tempo"]
        
        # Generate chant sequence
        chant_elements = ["void", "echo", "surge", "pulse", "whisper", "roar", "silence"]
        
        if settings["complexity"] == "simple":
            self.chant_sequence = [random.choice(chant_elements[:4]) for _ in range(self.phase_count)]
        elif settings["complexity"] == "moderate":
            self.chant_sequence = [random.choice(chant_elements[:6]) for _ in range(self.phase_count)]
        elif settings["complexity"] == "complex":
            self.chant_sequence = [random.choice(chant_elements) for _ in range(self.phase_count)]
        else:  # chaotic
            # Add special chaotic elements
            chaotic_elements = chant_elements + ["paradox", "inversion", "recursion"]
            self.chant_sequence = [random.choice(chaotic_elements) for _ in range(self.phase_count)]
            
        # Reset game state
        self.player_sequence = []
        self.current_phase = 0
        self.rhythm_accuracy = []
        self.game_state = "active"
        
        return {
            "success": True,
            "game_type": "feedback_chant_match",
            "difficulty": difficulty,
            "phase_count": self.phase_count,
            "tempo": self.tempo,
            "complexity": settings["complexity"],
            "first_chant": self.chant_sequence[0] if self.chant_sequence else None,
            "instructions": "Listen to the chant and repeat it back with proper timing"
        }
        
    def submit_chant(self, chant_element: str, timing: float) -> Dict[str, Any]:
        """Submit a chant element with timing"""
        if self.game_state != "active":
            return {
                "success": False,
                "error": "Game not active"
            }
            
        if self.current_phase >= len(self.chant_sequence):
            return self.end_game()
            
        expected_chant = self.chant_sequence[self.current_phase]
        expected_timing = 1.0 / self.tempo  # Base timing interval
        
        # Check chant accuracy
        chant_correct = chant_element == expected_chant
        
        # Check timing accuracy (within 20% tolerance)
        timing_error = abs(timing - expected_timing) / expected_timing
        timing_correct = timing_error <= 0.2
        
        # Calculate rhythm accuracy for this phase
        rhythm_score = max(0.0, 1.0 - timing_error)
        self.rhythm_accuracy.append(rhythm_score)
        
        self.player_sequence.append({
            "chant": chant_element,
            "timing": timing,
            "expected_chant": expected_chant,
            "expected_timing": expected_timing,
            "chant_correct": chant_correct,
            "timing_correct": timing_correct,
            "rhythm_score": round(rhythm_score, 2)
        })
        
        self.current_phase += 1
        
        result = {
            "success": True,
            "phase": self.current_phase,
            "chant_element": chant_element,
            "chant_correct": chant_correct,
            "timing_correct": timing_correct,
            "rhythm_score": round(rhythm_score, 2),
            "phase_complete": True
        }
        
        # Check if game is complete
        if self.current_phase >= len(self.chant_sequence):
            return self.end_game()
        else:
            result["next_chant"] = self.chant_sequence[self.current_phase]
            
        return result
        
    def end_game(self) -> Dict[str, Any]:
        """End the chant game and calculate results"""
        if self.game_state != "active":
            return {
                "success": False,
                "error": "Game not active"
            }
            
        self.game_state = "completed"
        
        # Calculate overall accuracy
        chant_accuracy = sum(1 for phase in self.player_sequence if phase["chant_correct"]) / len(self.player_sequence)
        timing_accuracy = sum(1 for phase in self.player_sequence if phase["timing_correct"]) / len(self.player_sequence)
        rhythm_accuracy = sum(self.rhythm_accuracy) / len(self.rhythm_accuracy)
        
        overall_accuracy = (chant_accuracy * 0.5 + timing_accuracy * 0.3 + rhythm_accuracy * 0.2)
        
        # Calculate score
        base_score = int(overall_accuracy * 1000)
        tempo_bonus = int((self.tempo - 1.0) * 200) if self.tempo > 1.0 else 0
        perfect_bonus = 500 if chant_accuracy == 1.0 and timing_accuracy >= 0.8 else 0
        
        final_score = base_score + tempo_bonus + perfect_bonus
        
        # Determine success (70% threshold)
        game_success = overall_accuracy >= 0.7
        
        # Calculate rewards
        entropy_effect = 0.0
        time_salt_reward = 0
        fragment_reward = 0
        
        if game_success:
            entropy_effect = random.uniform(0.05, 0.2) * overall_accuracy
            time_salt_reward = random.randint(1, 6)
            fragment_reward = random.randint(1, 4)
            
            if overall_accuracy >= 0.9:  # Excellent performance
                entropy_effect *= 1.3
                time_salt_reward += random.randint(2, 4)
                fragment_reward += random.randint(1, 3)
                
        result = {
            "success": True,
            "game_success": game_success,
            "chant_accuracy": round(chant_accuracy, 3),
            "timing_accuracy": round(timing_accuracy, 3),
            "rhythm_accuracy": round(rhythm_accuracy, 3),
            "overall_accuracy": round(overall_accuracy, 3),
            "final_score": final_score,
            "chant_sequence": self.chant_sequence.copy(),
            "player_performance": self.player_sequence.copy(),
            "rewards": {
                "entropy_effect": round(entropy_effect, 3),
                "time_salt": time_salt_reward,
                "identity_fragments": fragment_reward
            }
        }
        
        if game_success:
            result["harmonic_resonance"] = self._calculate_harmonic_resonance(overall_accuracy, rhythm_accuracy)
            
        return result
        
    def _calculate_harmonic_resonance(self, overall_accuracy: float, rhythm_accuracy: float) -> Dict[str, Any]:
        """Calculate the harmonic resonance achieved"""
        resonance_strength = (overall_accuracy + rhythm_accuracy) / 2.0
        
        if resonance_strength >= 0.9:
            resonance_type = "perfect_harmony"
            effect_duration = random.randint(15, 30)
        elif resonance_strength >= 0.8:
            resonance_type = "strong_resonance"
            effect_duration = random.randint(10, 20)
        elif resonance_strength >= 0.7:
            resonance_type = "stable_harmony"
            effect_duration = random.randint(5, 15)
        else:
            resonance_type = "weak_resonance"
            effect_duration = random.randint(2, 8)
            
        return {
            "type": resonance_type,
            "strength": round(resonance_strength, 2),
            "effect_duration": effect_duration,  # minutes
            "harmonic_frequency": round(resonance_strength * self.tempo, 2)
        }

class NodePurgeGame:
    """Node Purge Pulse mini-game"""
    
    def __init__(self):
        self.game_state = "inactive"
        self.grid_size = 5
        self.corrupted_nodes = set()
        self.purged_nodes = set()
        self.pulse_energy = 100
        self.turns_taken = 0
        self.max_turns = 10
        
    def start_game(self, difficulty: str = "medium") -> Dict[str, Any]:
        """Start a new node purge pulse game"""
        difficulty_settings = {
            "easy": {"grid_size": 4, "corruption_rate": 0.3, "pulse_energy": 120, "max_turns": 12},
            "medium": {"grid_size": 5, "corruption_rate": 0.4, "pulse_energy": 100, "max_turns": 10},
            "hard": {"grid_size": 6, "corruption_rate": 0.5, "pulse_energy": 80, "max_turns": 8},
            "nightmare": {"grid_size": 7, "corruption_rate": 0.6, "pulse_energy": 60, "max_turns": 6}
        }
        
        settings = difficulty_settings.get(difficulty, difficulty_settings["medium"])
        
        self.grid_size = settings["grid_size"]
        self.pulse_energy = settings["pulse_energy"]
        self.max_turns = settings["max_turns"]
        
        # Generate corrupted nodes
        total_nodes = self.grid_size * self.grid_size
        corruption_count = int(total_nodes * settings["corruption_rate"])
        
        all_positions = [(x, y) for x in range(self.grid_size) for y in range(self.grid_size)]
        self.corrupted_nodes = set(random.sample(all_positions, corruption_count))
        
        # Reset game state
        self.purged_nodes = set()
        self.turns_taken = 0
        self.game_state = "active"
        
        return {
            "success": True,
            "game_type": "node_purge_pulse",
            "difficulty": difficulty,
            "grid_size": self.grid_size,
            "corruption_count": len(self.corrupted_nodes),
            "pulse_energy": self.pulse_energy,
            "max_turns": self.max_turns,
            "instructions": "Purge corrupted nodes by targeting pulse locations strategically"
        }
        
    def fire_pulse(self, target_x: int, target_y: int, pulse_type: str = "standard") -> Dict[str, Any]:
        """Fire a purge pulse at target coordinates"""
        if self.game_state != "active":
            return {
                "success": False,
                "error": "Game not active"
            }
            
        if target_x < 0 or target_x >= self.grid_size or target_y < 0 or target_y >= self.grid_size:
            return {
                "success": False,
                "error": "Target coordinates out of bounds"
            }
            
        # Calculate pulse cost
        pulse_costs = {
            "standard": 10,
            "wide": 15,    # Affects 3x3 area
            "piercing": 12, # Affects line
            "explosive": 20 # Affects 5x5 area but less precise
        }
        
        pulse_cost = pulse_costs.get(pulse_type, 10)
        
        if self.pulse_energy < pulse_cost:
            return {
                "success": False,
                "error": f"Insufficient pulse energy. Need {pulse_cost}, have {self.pulse_energy}"
            }
            
        # Apply pulse effect
        affected_nodes = self._calculate_pulse_effect(target_x, target_y, pulse_type)
        newly_purged = []
        
        for node_x, node_y in affected_nodes:
            if (node_x, node_y) in self.corrupted_nodes and (node_x, node_y) not in self.purged_nodes:
                self.purged_nodes.add((node_x, node_y))
                newly_purged.append((node_x, node_y))
                
        # Update game state
        self.pulse_energy -= pulse_cost
        self.turns_taken += 1
        
        # Check win/lose conditions
        remaining_corruption = len(self.corrupted_nodes - self.purged_nodes)
        
        result = {
            "success": True,
            "target": (target_x, target_y),
            "pulse_type": pulse_type,
            "pulse_cost": pulse_cost,
            "affected_nodes": affected_nodes,
            "newly_purged": newly_purged,
            "remaining_energy": self.pulse_energy,
            "remaining_corruption": remaining_corruption,
            "turns_taken": self.turns_taken,
            "turns_remaining": self.max_turns - self.turns_taken
        }
        
        # Check end conditions
        if remaining_corruption == 0:
            return self.end_game(victory=True)
        elif self.turns_taken >= self.max_turns or self.pulse_energy <= 0:
            return self.end_game(victory=False)
            
        return result
        
    def _calculate_pulse_effect(self, target_x: int, target_y: int, pulse_type: str) -> List[Tuple[int, int]]:
        """Calculate which nodes are affected by a pulse"""
        affected = []
        
        if pulse_type == "standard":
            # Single target
            affected = [(target_x, target_y)]
            
        elif pulse_type == "wide":
            # 3x3 area
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    x, y = target_x + dx, target_y + dy
                    if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
                        affected.append((x, y))
                        
        elif pulse_type == "piercing":
            # Line through grid
            for x in range(self.grid_size):
                affected.append((x, target_y))
            for y in range(self.grid_size):
                if (target_x, y) not in affected:
                    affected.append((target_x, y))
                    
        elif pulse_type == "explosive":
            # 5x5 area but with gaps
            for dx in range(-2, 3):
                for dy in range(-2, 3):
                    if abs(dx) + abs(dy) <= 3:  # Diamond pattern
                        x, y = target_x + dx, target_y + dy
                        if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
                            affected.append((x, y))
                            
        return affected
        
    def end_game(self, victory: bool = None) -> Dict[str, Any]:
        """End the purge game and calculate results"""
        if self.game_state != "active":
            return {
                "success": False,
                "error": "Game not active"
            }
            
        self.game_state = "completed"
        
        if victory is None:
            remaining_corruption = len(self.corrupted_nodes - self.purged_nodes)
            victory = remaining_corruption == 0
            
        # Calculate performance metrics
        purge_efficiency = len(self.purged_nodes) / len(self.corrupted_nodes)
        energy_efficiency = (100 - self.pulse_energy) / 100.0  # Energy used
        turn_efficiency = 1.0 - (self.turns_taken / self.max_turns)
        
        overall_performance = (purge_efficiency * 0.6 + energy_efficiency * 0.2 + turn_efficiency * 0.2)
        
        # Calculate score
        base_score = int(purge_efficiency * 1000)
        efficiency_bonus = int(energy_efficiency * 300)
        speed_bonus = int(turn_efficiency * 200)
        victory_bonus = 500 if victory else 0
        
        final_score = base_score + efficiency_bonus + speed_bonus + victory_bonus
        
        # Calculate rewards
        entropy_effect = 0.0
        time_salt_reward = 0
        fragment_reward = 0
        
        if victory:
            entropy_effect = random.uniform(0.2, 0.4) * overall_performance
            time_salt_reward = random.randint(3, 10)
            fragment_reward = random.randint(2, 8)
            
            if overall_performance >= 0.9:  # Exceptional performance
                entropy_effect *= 1.5
                time_salt_reward += random.randint(5, 10)
                fragment_reward += random.randint(3, 7)
                
        result = {
            "success": True,
            "victory": victory,
            "purge_efficiency": round(purge_efficiency, 3),
            "energy_efficiency": round(energy_efficiency, 3),
            "turn_efficiency": round(turn_efficiency, 3),
            "overall_performance": round(overall_performance, 3),
            "final_score": final_score,
            "corruption_map": list(self.corrupted_nodes),
            "purged_nodes": list(self.purged_nodes),
            "remaining_energy": self.pulse_energy,
            "turns_used": self.turns_taken,
            "rewards": {
                "entropy_effect": round(entropy_effect, 3),
                "time_salt": time_salt_reward,
                "identity_fragments": fragment_reward
            }
        }
        
        if victory:
            result["purification_quality"] = self._calculate_purification_quality(overall_performance)
            
        return result
        
    def _calculate_purification_quality(self, performance: float) -> Dict[str, Any]:
        """Calculate the quality of the purification"""
        if performance >= 0.9:
            quality = "perfect_purification"
            stability = random.uniform(0.95, 1.0)
        elif performance >= 0.8:
            quality = "excellent_purification"
            stability = random.uniform(0.85, 0.95)
        elif performance >= 0.7:
            quality = "good_purification"
            stability = random.uniform(0.75, 0.85)
        elif performance >= 0.6:
            quality = "adequate_purification"
            stability = random.uniform(0.65, 0.75)
        else:
            quality = "basic_purification"
            stability = random.uniform(0.5, 0.65)
            
        return {
            "quality": quality,
            "stability": round(stability, 2),
            "purification_power": round(performance * stability, 2),
            "corruption_resistance": round(stability * 0.8, 2)
        }

class EntropyRitesSystem:
    """Main system managing all entropy rites mini-games"""
    
    def __init__(self):
        # Game instances
        self.sigil_draw_game = SigilDrawGame()
        self.chant_game = FeedbackChantGame()
        self.purge_game = NodePurgeGame()
        
        # System statistics
        self.total_games_played = 0
        self.games_won = 0
        self.total_score = 0
        self.high_scores = {
            "containment_sigil_draw": 0,
            "feedback_chant_match": 0,
            "node_purge_pulse": 0
        }
        
        # Player progression
        self.mastery_levels = {
            "containment_sigil_draw": 0,
            "feedback_chant_match": 0,
            "node_purge_pulse": 0
        }
        
        self.ritual_energy = 100
        self.energy_regeneration_rate = 1.0  # per minute
        self.last_energy_update = time.time()
        
    def start_game(self, game_type: str, difficulty: str = "medium") -> Dict[str, Any]:
        """Start a specific mini-game"""
        # Check ritual energy
        energy_cost = self._get_energy_cost(game_type, difficulty)
        if self.ritual_energy < energy_cost:
            return {
                "success": False,
                "error": f"Insufficient ritual energy. Need {energy_cost}, have {self.ritual_energy}",
                "energy_regeneration_time": round((energy_cost - self.ritual_energy) / self.energy_regeneration_rate, 1)
            }
            
        # Start appropriate game
        if game_type == "containment_sigil_draw":
            result = self.sigil_draw_game.start_game(difficulty)
        elif game_type == "feedback_chant_match":
            result = self.chant_game.start_game(difficulty)
        elif game_type == "node_purge_pulse":
            result = self.purge_game.start_game(difficulty)
        else:
            return {
                "success": False,
                "error": f"Unknown game type: {game_type}"
            }
            
        if result.get("success"):
            self.ritual_energy -= energy_cost
            result["energy_cost"] = energy_cost
            result["remaining_energy"] = self.ritual_energy
            
        return result
        
    def _get_energy_cost(self, game_type: str, difficulty: str) -> int:
        """Calculate energy cost for starting a game"""
        base_costs = {
            "containment_sigil_draw": 15,
            "feedback_chant_match": 12,
            "node_purge_pulse": 20
        }
        
        difficulty_multipliers = {
            "easy": 0.8,
            "medium": 1.0,
            "hard": 1.3,
            "nightmare": 1.6
        }
        
        base_cost = base_costs.get(game_type, 15)
        multiplier = difficulty_multipliers.get(difficulty, 1.0)
        
        return int(base_cost * multiplier)
        
    def get_game_status(self, game_type: str) -> Dict[str, Any]:
        """Get status of a specific game"""
        if game_type == "containment_sigil_draw":
            return {
                "game_type": game_type,
                "state": self.sigil_draw_game.game_state,
                "progress": f"{len(self.sigil_draw_game.current_pattern)}/{len(self.sigil_draw_game.target_pattern)}" if self.sigil_draw_game.target_pattern else "0/0",
                "current_score": self.sigil_draw_game.score
            }
        elif game_type == "feedback_chant_match":
            return {
                "game_type": game_type,
                "state": self.chant_game.game_state,
                "progress": f"{self.chant_game.current_phase}/{self.chant_game.phase_count}",
                "tempo": self.chant_game.tempo
            }
        elif game_type == "node_purge_pulse":
            return {
                "game_type": game_type,
                "state": self.purge_game.game_state,
                "progress": f"{len(self.purge_game.purged_nodes)}/{len(self.purge_game.corrupted_nodes)}",
                "remaining_energy": self.purge_game.pulse_energy,
                "turns_remaining": self.purge_game.max_turns - self.purge_game.turns_taken
            }
        else:
            return {
                "success": False,
                "error": f"Unknown game type: {game_type}"
            }
            
    def process_game_completion(self, game_type: str, game_result: Dict[str, Any]) -> Dict[str, Any]:
        """Process completion of a mini-game"""
        if not game_result.get("success"):
            return game_result
            
        # Update statistics
        self.total_games_played += 1
        
        if game_result.get("game_success"):
            self.games_won += 1
            
        final_score = game_result.get("final_score", game_result.get("score", 0))
        self.total_score += final_score
        
        # Update high scores
        if final_score > self.high_scores.get(game_type, 0):
            self.high_scores[game_type] = final_score
            game_result["new_high_score"] = True
            
        # Update mastery
        self._update_mastery(game_type, game_result)
        
        # Apply game effects to broader system
        system_effects = self._calculate_system_effects(game_type, game_result)
        game_result["system_effects"] = system_effects
        
        return game_result
        
    def _update_mastery(self, game_type: str, game_result: Dict[str, Any]):
        """Update mastery level for a game type"""
        current_mastery = self.mastery_levels.get(game_type, 0)
        
        # Base mastery gain
        mastery_gain = 0.1
        
        # Bonus for success
        if game_result.get("game_success"):
            mastery_gain += 0.2
            
        # Bonus for high performance
        performance_metrics = {
            "containment_sigil_draw": game_result.get("final_accuracy", 0),
            "feedback_chant_match": game_result.get("overall_accuracy", 0),
            "node_purge_pulse": game_result.get("overall_performance", 0)
        }
        
        performance = performance_metrics.get(game_type, 0)
        if performance >= 0.9:
            mastery_gain += 0.3
        elif performance >= 0.8:
            mastery_gain += 0.2
        elif performance >= 0.7:
            mastery_gain += 0.1
            
        self.mastery_levels[game_type] = min(10.0, current_mastery + mastery_gain)
        
    def _calculate_system_effects(self, game_type: str, game_result: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate effects on the broader drift engine system"""
        effects = {
            "entropy_modifications": [],
            "temporal_effects": [],
            "market_influences": [],
            "enclave_resonances": []
        }
        
        if not game_result.get("game_success"):
            return effects
            
        # Entropy effects based on game type
        if game_type == "containment_sigil_draw":
            containment = game_result.get("containment_quality", {})
            if containment.get("quality") in ["strong", "perfect"]:
                effects["entropy_modifications"].append({
                    "type": "stabilization",
                    "strength": containment.get("stability", 0.5),
                    "duration": containment.get("duration", 10)
                })
                
        elif game_type == "feedback_chant_match":
            resonance = game_result.get("harmonic_resonance", {})
            if resonance.get("type") in ["strong_resonance", "perfect_harmony"]:
                effects["temporal_effects"].append({
                    "type": "harmonic_acceleration",
                    "frequency": resonance.get("harmonic_frequency", 1.0),
                    "duration": resonance.get("effect_duration", 10)
                })
                
        elif game_type == "node_purge_pulse":
            purification = game_result.get("purification_quality", {})
            if purification.get("quality") in ["excellent_purification", "perfect_purification"]:
                effects["market_influences"].append({
                    "type": "purification_bonus",
                    "power": purification.get("purification_power", 0.5),
                    "resistance": purification.get("corruption_resistance", 0.5)
                })
                
        return effects
        
    def update_energy(self):
        """Update ritual energy based on time passed"""
        current_time = time.time()
        time_elapsed = (current_time - self.last_energy_update) / 60.0  # Convert to minutes
        
        energy_gain = time_elapsed * self.energy_regeneration_rate
        self.ritual_energy = min(100, self.ritual_energy + energy_gain)
        
        self.last_energy_update = current_time
        
    def get_system_status(self) -> Dict[str, Any]:
        """Get comprehensive status of the entropy rites system"""
        self.update_energy()
        
        return {
            "ritual_energy": round(self.ritual_energy, 1),
            "total_games_played": self.total_games_played,
            "games_won": self.games_won,
            "win_rate": round(self.games_won / max(1, self.total_games_played), 3),
            "total_score": self.total_score,
            "average_score": round(self.total_score / max(1, self.total_games_played), 1),
            "high_scores": self.high_scores.copy(),
            "mastery_levels": {k: round(v, 2) for k, v in self.mastery_levels.items()},
            "available_games": ["containment_sigil_draw", "feedback_chant_match", "node_purge_pulse"]
        }
        
    def export_state(self) -> Dict[str, Any]:
        """Export entropy rites system state"""
        return {
            "total_games_played": self.total_games_played,
            "games_won": self.games_won,
            "total_score": self.total_score,
            "high_scores": self.high_scores.copy(),
            "mastery_levels": self.mastery_levels.copy(),
            "ritual_energy": self.ritual_energy,
            "last_energy_update": self.last_energy_update
        }
        
    def import_state(self, state_data: Dict[str, Any]):
        """Import entropy rites system state"""
        self.total_games_played = state_data.get("total_games_played", 0)
        self.games_won = state_data.get("games_won", 0)
        self.total_score = state_data.get("total_score", 0)
        self.high_scores = state_data.get("high_scores", {})
        self.mastery_levels = state_data.get("mastery_levels", {})
        self.ritual_energy = state_data.get("ritual_energy", 100)
        self.last_energy_update = state_data.get("last_energy_update", time.time())
