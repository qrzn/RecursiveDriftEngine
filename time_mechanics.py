"""
Chrono-Glyph Stasis System: Time Manipulation Mechanics
Advanced temporal preservation and manipulation with Time Salt currency
"""

import random
import json
from datetime import datetime, timezone, timedelta
from typing import Dict, List, Any, Optional, Tuple
import hashlib

class ChronoStasisChamber:
    """Individual stasis chamber for preserving moments in time"""
    
    def __init__(self, chamber_id: str):
        self.chamber_id = chamber_id
        self.creation_time = datetime.now(timezone.utc)
        
        # Preservation state
        self.is_active = False
        self.preserved_moment = None
        self.time_salt_cost = 0
        self.preservation_quality = 0.0
        self.degradation_rate = random.uniform(0.001, 0.005)
        
        # Chamber properties
        self.capacity = random.uniform(0.5, 2.0)
        self.efficiency = random.uniform(0.7, 0.95)
        self.stability = random.uniform(0.8, 0.99)
        
    def preserve_moment(self, moment_data: Dict[str, Any], time_salt_amount: int) -> Dict[str, Any]:
        """Preserve a moment in time using Time Salt"""
        if self.is_active:
            return {
                "success": False,
                "error": "Chamber already contains a preserved moment"
            }
            
        # Calculate required Time Salt based on moment complexity
        complexity = self._calculate_moment_complexity(moment_data)
        required_salt = max(1, int(complexity * 10))
        
        if time_salt_amount < required_salt:
            return {
                "success": False,
                "error": f"Insufficient Time Salt. Required: {required_salt}, Provided: {time_salt_amount}"
            }
            
        # Preservation process
        preservation_result = {
            "success": True,
            "chamber_id": self.chamber_id,
            "preservation_timestamp": datetime.now(timezone.utc).isoformat(),
            "time_salt_used": required_salt,
            "time_salt_refunded": time_salt_amount - required_salt,
            "complexity": round(complexity, 3)
        }
        
        # Apply efficiency to preservation quality
        base_quality = min(1.0, time_salt_amount / required_salt)
        self.preservation_quality = base_quality * self.efficiency
        
        # Store preserved moment
        self.preserved_moment = {
            "data": moment_data.copy(),
            "preservation_time": datetime.now(timezone.utc).isoformat(),
            "original_timestamp": moment_data.get("timestamp", datetime.now(timezone.utc).isoformat()),
            "quality": self.preservation_quality,
            "integrity": 1.0
        }
        
        self.is_active = True
        self.time_salt_cost = required_salt
        
        preservation_result.update({
            "preservation_quality": round(self.preservation_quality, 3),
            "expected_degradation_rate": round(self.degradation_rate, 5),
            "estimated_lifespan_hours": round(1.0 / (self.degradation_rate * 24), 1)
        })
        
        return preservation_result
        
    def restore_moment(self) -> Dict[str, Any]:
        """Restore the preserved moment"""
        if not self.is_active or not self.preserved_moment:
            return {
                "success": False,
                "error": "No moment preserved in this chamber"
            }
            
        # Calculate current integrity
        self._update_integrity()
        
        restoration_result = {
            "success": True,
            "chamber_id": self.chamber_id,
            "restoration_timestamp": datetime.now(timezone.utc).isoformat(),
            "preserved_data": self.preserved_moment["data"].copy(),
            "preservation_quality": self.preserved_moment["quality"],
            "current_integrity": self.preserved_moment["integrity"],
            "time_salt_recovered": max(0, int(self.time_salt_cost * self.preserved_moment["integrity"]))
        }
        
        # Clear chamber
        self.preserved_moment = None
        self.is_active = False
        self.time_salt_cost = 0
        self.preservation_quality = 0.0
        
        return restoration_result
        
    def _calculate_moment_complexity(self, moment_data: Dict[str, Any]) -> float:
        """Calculate the complexity of a moment for Time Salt requirements"""
        complexity_factors = {
            "data_size": len(str(moment_data)) / 1000.0,
            "nested_structures": self._count_nested_structures(moment_data),
            "temporal_references": self._count_temporal_references(moment_data),
            "entropy_signatures": len([k for k in moment_data.keys() if "entropy" in k.lower()])
        }
        
        # Weight different factors
        base_complexity = (
            complexity_factors["data_size"] * 0.3 +
            complexity_factors["nested_structures"] * 0.4 +
            complexity_factors["temporal_references"] * 0.2 +
            complexity_factors["entropy_signatures"] * 0.1
        )
        
        return max(0.1, min(2.0, base_complexity))
        
    def _count_nested_structures(self, data: Any, depth: int = 0) -> int:
        """Count nested data structures"""
        if depth > 5:  # Prevent infinite recursion
            return 0
            
        count = 0
        if isinstance(data, dict):
            count += 1
            for value in data.values():
                count += self._count_nested_structures(value, depth + 1)
        elif isinstance(data, list):
            count += 1
            for item in data:
                count += self._count_nested_structures(item, depth + 1)
                
        return count
        
    def _count_temporal_references(self, data: Dict[str, Any]) -> int:
        """Count temporal references in the data"""
        temporal_keywords = ["timestamp", "time", "date", "temporal", "chrono", "moment"]
        
        count = 0
        data_str = str(data).lower()
        for keyword in temporal_keywords:
            count += data_str.count(keyword)
            
        return count
        
    def _update_integrity(self):
        """Update the integrity of the preserved moment"""
        if not self.preserved_moment:
            return
            
        # Calculate time elapsed since preservation
        preservation_time = datetime.fromisoformat(self.preserved_moment["preservation_time"].replace('Z', '+00:00'))
        time_elapsed = (datetime.now(timezone.utc) - preservation_time).total_seconds() / 3600  # Hours
        
        # Apply degradation
        degradation = self.degradation_rate * time_elapsed
        new_integrity = max(0.0, self.preserved_moment["integrity"] - degradation)
        
        self.preserved_moment["integrity"] = new_integrity
        
    def get_status(self) -> Dict[str, Any]:
        """Get current chamber status"""
        status = {
            "chamber_id": self.chamber_id,
            "is_active": self.is_active,
            "capacity": round(self.capacity, 2),
            "efficiency": round(self.efficiency, 3),
            "stability": round(self.stability, 3),
            "degradation_rate": round(self.degradation_rate, 5)
        }
        
        if self.is_active and self.preserved_moment:
            self._update_integrity()
            status.update({
                "preserved_since": self.preserved_moment["preservation_time"],
                "preservation_quality": round(self.preserved_moment["quality"], 3),
                "current_integrity": round(self.preserved_moment["integrity"], 3),
                "time_salt_invested": self.time_salt_cost
            })
            
        return status

class ChronoSystem:
    """Main temporal mechanics system"""
    
    def __init__(self):
        # Stasis chambers
        self.stasis_chambers = {}
        self.chamber_count = 3  # Start with 3 chambers
        
        # Time Salt economy
        self.time_salt_generation_rate = 0.1  # Per successful operation
        self.temporal_flux_level = 0.5
        self.causality_stability = 0.8
        
        # Temporal effects tracking
        self.active_temporal_effects = []
        self.temporal_anchors = []
        self.time_locks = {}
        
        # System state
        self.total_preservations = 0
        self.total_restorations = 0
        self.temporal_signature = self._generate_temporal_signature()
        
        # Initialize chambers
        self.initialize_chambers()
        
    def initialize_chambers(self):
        """Initialize starting stasis chambers"""
        for i in range(self.chamber_count):
            chamber_id = f"stasis_{i+1:03d}"
            self.stasis_chambers[chamber_id] = ChronoStasisChamber(chamber_id)
            
    def preserve_moment(self, moment_data: Dict[str, Any], time_salt_amount: int, 
                       chamber_id: Optional[str] = None) -> Dict[str, Any]:
        """Preserve a moment in time"""
        # Find available chamber
        if chamber_id:
            if chamber_id not in self.stasis_chambers:
                return {
                    "success": False,
                    "error": f"Chamber {chamber_id} not found"
                }
            target_chamber = self.stasis_chambers[chamber_id]
        else:
            # Find first available chamber
            target_chamber = None
            for chamber in self.stasis_chambers.values():
                if not chamber.is_active:
                    target_chamber = chamber
                    break
                    
            if not target_chamber:
                return {
                    "success": False,
                    "error": "No available stasis chambers"
                }
                
        # Attempt preservation
        result = target_chamber.preserve_moment(moment_data, time_salt_amount)
        
        if result["success"]:
            self.total_preservations += 1
            
            # Update temporal flux
            self.temporal_flux_level += random.uniform(0.01, 0.05)
            self.temporal_flux_level = min(1.0, self.temporal_flux_level)
            
            # Chance for temporal effect
            if random.random() < 0.1:
                temporal_effect = self._generate_temporal_effect("preservation")
                self.active_temporal_effects.append(temporal_effect)
                result["temporal_effect"] = temporal_effect
                
        return result
        
    def restore_moment(self, chamber_id: str) -> Dict[str, Any]:
        """Restore a preserved moment"""
        if chamber_id not in self.stasis_chambers:
            return {
                "success": False,
                "error": f"Chamber {chamber_id} not found"
            }
            
        chamber = self.stasis_chambers[chamber_id]
        result = chamber.restore_moment()
        
        if result["success"]:
            self.total_restorations += 1
            
            # Update temporal flux
            self.temporal_flux_level -= random.uniform(0.01, 0.03)
            self.temporal_flux_level = max(0.0, self.temporal_flux_level)
            
            # Check for causality effects
            if random.random() < 0.15:
                causality_effect = self._generate_causality_effect(result["preserved_data"])
                result["causality_effect"] = causality_effect
                
        return result
        
    def create_temporal_anchor(self, anchor_name: str, anchor_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a temporal anchor point"""
        anchor_id = f"anchor_{len(self.temporal_anchors)+1:03d}"
        
        temporal_anchor = {
            "anchor_id": anchor_id,
            "name": anchor_name,
            "creation_timestamp": datetime.now(timezone.utc).isoformat(),
            "anchor_data": anchor_data.copy(),
            "stability": random.uniform(0.7, 0.95),
            "temporal_weight": random.uniform(0.5, 1.2),
            "access_count": 0
        }
        
        self.temporal_anchors.append(temporal_anchor)
        
        return {
            "success": True,
            "anchor_id": anchor_id,
            "name": anchor_name,
            "stability": temporal_anchor["stability"],
            "temporal_weight": temporal_anchor["temporal_weight"]
        }
        
    def access_temporal_anchor(self, anchor_id: str) -> Dict[str, Any]:
        """Access a temporal anchor"""
        anchor = None
        for a in self.temporal_anchors:
            if a["anchor_id"] == anchor_id:
                anchor = a
                break
                
        if not anchor:
            return {
                "success": False,
                "error": f"Temporal anchor {anchor_id} not found"
            }
            
        # Check stability
        access_success = random.random() < anchor["stability"]
        
        result = {
            "anchor_id": anchor_id,
            "name": anchor["name"],
            "success": access_success,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
        
        if access_success:
            anchor["access_count"] += 1
            
            # Slight stability decrease with each access
            anchor["stability"] *= 0.98
            
            result.update({
                "anchor_data": anchor["anchor_data"].copy(),
                "temporal_weight": anchor["temporal_weight"],
                "access_count": anchor["access_count"],
                "remaining_stability": round(anchor["stability"], 3)
            })
        else:
            result.update({
                "failure_reason": "temporal_instability",
                "stability_loss": 0.05
            })
            anchor["stability"] -= 0.05
            
        return result
        
    def create_time_lock(self, lock_id: str, duration_hours: float, lock_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a time lock that preserves data for a specific duration"""
        if lock_id in self.time_locks:
            return {
                "success": False,
                "error": f"Time lock {lock_id} already exists"
            }
            
        unlock_time = datetime.now(timezone.utc) + timedelta(hours=duration_hours)
        
        time_lock = {
            "lock_id": lock_id,
            "creation_time": datetime.now(timezone.utc).isoformat(),
            "unlock_time": unlock_time.isoformat(),
            "duration_hours": duration_hours,
            "locked_data": lock_data.copy(),
            "attempts": 0,
            "max_attempts": random.randint(3, 7)
        }
        
        self.time_locks[lock_id] = time_lock
        
        return {
            "success": True,
            "lock_id": lock_id,
            "unlock_time": unlock_time.isoformat(),
            "duration_hours": duration_hours,
            "max_attempts": time_lock["max_attempts"]
        }
        
    def attempt_unlock_time_lock(self, lock_id: str, unlock_key: Optional[str] = None) -> Dict[str, Any]:
        """Attempt to unlock a time lock"""
        if lock_id not in self.time_locks:
            return {
                "success": False,
                "error": f"Time lock {lock_id} not found"
            }
            
        time_lock = self.time_locks[lock_id]
        current_time = datetime.now(timezone.utc)
        unlock_time = datetime.fromisoformat(time_lock["unlock_time"].replace('Z', '+00:00'))
        
        result = {
            "lock_id": lock_id,
            "attempt_timestamp": current_time.isoformat(),
            "attempts_made": time_lock["attempts"] + 1
        }
        
        # Check if time lock has expired naturally
        if current_time >= unlock_time:
            locked_data = time_lock["locked_data"].copy()
            del self.time_locks[lock_id]
            
            result.update({
                "success": True,
                "unlock_method": "natural_expiration",
                "locked_data": locked_data
            })
            return result
            
        # Check attempts limit
        time_lock["attempts"] += 1
        if time_lock["attempts"] > time_lock["max_attempts"]:
            # Lock destroyed by too many attempts
            del self.time_locks[lock_id]
            result.update({
                "success": False,
                "failure_reason": "max_attempts_exceeded",
                "lock_destroyed": True
            })
            return result
            
        # Early unlock attempt
        if unlock_key:
            # Generate a simple hash-based key check
            expected_key = hashlib.md5(f"{lock_id}_{time_lock['creation_time']}".encode()).hexdigest()[:8]
            
            if unlock_key == expected_key:
                locked_data = time_lock["locked_data"].copy()
                del self.time_locks[lock_id]
                
                result.update({
                    "success": True,
                    "unlock_method": "key_unlock",
                    "locked_data": locked_data
                })
                return result
                
        # Failed unlock attempt
        time_remaining = (unlock_time - current_time).total_seconds() / 3600
        
        result.update({
            "success": False,
            "failure_reason": "time_lock_active",
            "time_remaining_hours": round(time_remaining, 2),
            "attempts_remaining": time_lock["max_attempts"] - time_lock["attempts"]
        })
        
        return result
        
    def _generate_temporal_effect(self, trigger_type: str) -> Dict[str, Any]:
        """Generate a random temporal effect"""
        effect_types = {
            "preservation": [
                "temporal_echo", "causality_ripple", "time_dilation",
                "chronos_blessing", "temporal_resonance"
            ],
            "restoration": [
                "paradox_formation", "timeline_convergence", "temporal_backlash",
                "causality_loop", "time_storm"
            ]
        }
        
        available_effects = effect_types.get(trigger_type, effect_types["preservation"])
        effect_type = random.choice(available_effects)
        
        return {
            "type": effect_type,
            "trigger": trigger_type,
            "intensity": random.uniform(0.3, 0.8),
            "duration": random.uniform(5.0, 30.0),  # Minutes
            "creation_time": datetime.now(timezone.utc).isoformat(),
            "description": self._get_effect_description(effect_type)
        }
        
    def _get_effect_description(self, effect_type: str) -> str:
        """Get description for temporal effect"""
        descriptions = {
            "temporal_echo": "Faint echoes of the preserved moment ripple through time",
            "causality_ripple": "Small changes propagate through the timeline",
            "time_dilation": "Local time flow becomes slightly distorted",
            "chronos_blessing": "Temporal operations become more efficient",
            "temporal_resonance": "Harmonious vibrations strengthen time manipulation",
            "paradox_formation": "A small paradox threatens timeline stability",
            "timeline_convergence": "Multiple timeline branches begin to merge",
            "temporal_backlash": "The timeline resists manipulation",
            "causality_loop": "A causal loop forms, creating recursive effects",
            "time_storm": "Chaotic temporal energies disrupt the local area"
        }
        
        return descriptions.get(effect_type, "Unknown temporal phenomenon")
        
    def _generate_causality_effect(self, restored_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate causality effects from restoration"""
        effect_types = [
            "butterfly_effect", "temporal_displacement", "memory_alteration",
            "probability_shift", "reality_adjustment"
        ]
        
        return {
            "type": random.choice(effect_types),
            "magnitude": random.uniform(0.1, 0.6),
            "affected_systems": random.sample(["entropy", "market", "alchemy", "enclaves"], 
                                            random.randint(1, 3)),
            "description": "Restoration has altered the flow of causality"
        }
        
    def _generate_temporal_signature(self) -> str:
        """Generate unique temporal signature for current timeline"""
        timestamp = datetime.now(timezone.utc)
        signature_data = f"{timestamp.isoformat()}_{random.randint(1000, 9999)}"
        return hashlib.md5(signature_data.encode()).hexdigest()[:12]
        
    def get_current_signature(self) -> str:
        """Get current temporal signature"""
        return self.temporal_signature
        
    def get_available_chambers(self) -> List[str]:
        """Get list of available stasis chambers"""
        return [cid for cid, chamber in self.stasis_chambers.items() if not chamber.is_active]
        
    def get_active_chambers(self) -> List[str]:
        """Get list of active stasis chambers"""
        return [cid for cid, chamber in self.stasis_chambers.items() if chamber.is_active]
        
    def get_stasis_count(self) -> int:
        """Get count of active stasis preservations"""
        return len(self.get_active_chambers())
        
    def get_system_status(self) -> Dict[str, Any]:
        """Get comprehensive system status"""
        return {
            "total_chambers": len(self.stasis_chambers),
            "active_preservations": len(self.get_active_chambers()),
            "available_chambers": len(self.get_available_chambers()),
            "temporal_flux_level": round(self.temporal_flux_level, 3),
            "causality_stability": round(self.causality_stability, 3),
            "total_preservations": self.total_preservations,
            "total_restorations": self.total_restorations,
            "active_temporal_effects": len(self.active_temporal_effects),
            "temporal_anchors": len(self.temporal_anchors),
            "active_time_locks": len(self.time_locks),
            "temporal_signature": self.temporal_signature
        }
        
    def update_temporal_effects(self):
        """Update and clean up temporal effects"""
        current_time = datetime.now(timezone.utc)
        active_effects = []
        
        for effect in self.active_temporal_effects:
            creation_time = datetime.fromisoformat(effect["creation_time"].replace('Z', '+00:00'))
            elapsed_minutes = (current_time - creation_time).total_seconds() / 60
            
            if elapsed_minutes < effect["duration"]:
                active_effects.append(effect)
                
        self.active_temporal_effects = active_effects
        
    def export_state(self) -> Dict[str, Any]:
        """Export temporal system state"""
        return {
            "chamber_count": self.chamber_count,
            "temporal_flux_level": self.temporal_flux_level,
            "causality_stability": self.causality_stability,
            "total_preservations": self.total_preservations,
            "total_restorations": self.total_restorations,
            "temporal_signature": self.temporal_signature,
            "active_temporal_effects": self.active_temporal_effects.copy(),
            "temporal_anchors": self.temporal_anchors.copy(),
            "time_locks": self.time_locks.copy(),
            "chamber_states": {
                cid: chamber.get_status() 
                for cid, chamber in self.stasis_chambers.items()
            }
        }
        
    def import_state(self, state_data: Dict[str, Any]):
        """Import temporal system state"""
        self.chamber_count = state_data.get("chamber_count", 3)
        self.temporal_flux_level = state_data.get("temporal_flux_level", 0.5)
        self.causality_stability = state_data.get("causality_stability", 0.8)
        self.total_preservations = state_data.get("total_preservations", 0)
        self.total_restorations = state_data.get("total_restorations", 0)
        self.temporal_signature = state_data.get("temporal_signature", self._generate_temporal_signature())
        self.active_temporal_effects = state_data.get("active_temporal_effects", [])
        self.temporal_anchors = state_data.get("temporal_anchors", [])
        self.time_locks = state_data.get("time_locks", {})
        
        # Restore chamber states if available
        chamber_states = state_data.get("chamber_states", {})
        for chamber_id, chamber_state in chamber_states.items():
            if chamber_id in self.stasis_chambers and chamber_state.get("is_active"):
                # Restore chamber would need more complex state restoration
                # For now, just mark as active if it was active
                pass
