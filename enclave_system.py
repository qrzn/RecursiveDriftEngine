"""
Drift Enclave System: Mystical Zone Management
Procedural generation and unique entropy rules for drift zones
"""

import random
import json
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional, Tuple
import configparser

class DriftEnclave:
    """Individual drift enclave with unique properties"""
    
    def __init__(self, enclave_id: str, name: str, enclave_type: str):
        self.enclave_id = enclave_id
        self.name = name
        self.enclave_type = enclave_type
        
        # Core properties
        self.entropy_modifier = random.uniform(0.5, 1.5)
        self.stability_factor = random.uniform(0.3, 0.9)
        self.resonance_frequency = random.uniform(0.1, 1.0)
        
        # Zone characteristics
        self.dominant_element = None
        self.secondary_elements = []
        self.special_properties = []
        self.hazards = []
        self.resources = {}
        
        # Exploration state
        self.exploration_level = 0
        self.discovered_secrets = []
        self.active_effects = []
        
        # Generate enclave properties
        self.generate_properties()
        
    def generate_properties(self):
        """Generate unique properties for this enclave"""
        enclave_configs = {
            "void_nexus": {
                "dominant_element": "void",
                "secondary_elements": ["energy", "change"],
                "base_properties": ["nullification", "absorption", "silence"],
                "possible_hazards": ["void_storms", "reality_tears", "memory_drain"],
                "resource_types": ["void_essence", "silence_crystals", "null_fragments"]
            },
            "entropy_gardens": {
                "dominant_element": "change",
                "secondary_elements": ["flow", "energy"],
                "base_properties": ["growth", "mutation", "chaos"],
                "possible_hazards": ["chaotic_surges", "mutation_fields", "time_loops"],
                "resource_types": ["chaos_seeds", "mutation_spores", "entropy_blooms"]
            },
            "crystal_sanctum": {
                "dominant_element": "stability",
                "secondary_elements": ["void", "flow"],
                "base_properties": ["preservation", "amplification", "memory"],
                "possible_hazards": ["crystal_resonance", "memory_echoes", "stasis_fields"],
                "resource_types": ["memory_crystals", "stability_cores", "resonance_shards"]
            },
            "temporal_streams": {
                "dominant_element": "flow",
                "secondary_elements": ["change", "stability"],
                "base_properties": ["time_flow", "causality", "prediction"],
                "possible_hazards": ["time_eddies", "causal_loops", "temporal_storms"],
                "resource_types": ["time_fragments", "causal_threads", "moment_pearls"]
            },
            "energy_maelstrom": {
                "dominant_element": "energy",
                "secondary_elements": ["void", "change"],
                "base_properties": ["amplification", "discharge", "intensity"],
                "possible_hazards": ["energy_overload", "electric_storms", "power_surges"],
                "resource_types": ["raw_energy", "lightning_essence", "power_cores"]
            }
        }
        
        config = enclave_configs.get(self.enclave_type, enclave_configs["void_nexus"])
        
        # Set elements
        self.dominant_element = config["dominant_element"]
        self.secondary_elements = config["secondary_elements"].copy()
        
        # Select properties
        base_props = config["base_properties"]
        self.special_properties = random.sample(base_props, min(3, len(base_props)))
        
        # Add random special properties
        additional_properties = [
            "phase_shifting", "dimensional_anchor", "reality_distortion",
            "consciousness_field", "probability_flux", "quantum_entanglement",
            "temporal_displacement", "memory_resonance", "soul_echo"
        ]
        
        if random.random() < 0.3:  # 30% chance for additional property
            self.special_properties.append(random.choice(additional_properties))
            
        # Select hazards
        possible_hazards = config["possible_hazards"]
        hazard_count = random.randint(1, min(3, len(possible_hazards)))
        self.hazards = random.sample(possible_hazards, hazard_count)
        
        # Generate resources
        resource_types = config["resource_types"]
        for resource_type in resource_types:
            self.resources[resource_type] = {
                "abundance": random.uniform(0.1, 0.8),
                "quality": random.uniform(0.3, 1.0),
                "extraction_difficulty": random.uniform(0.2, 0.9)
            }
            
    def enter_enclave(self, visitor_entropy: float) -> Dict[str, Any]:
        """Handle entity entering the enclave"""
        # Calculate entry effects
        resonance_match = abs(visitor_entropy - self.resonance_frequency)
        entry_success = resonance_match < 0.5
        
        entry_result = {
            "success": entry_success,
            "enclave_id": self.enclave_id,
            "name": self.name,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "visitor_entropy": visitor_entropy,
            "resonance_match": round(resonance_match, 3)
        }
        
        if entry_success:
            # Successful entry
            entry_effects = self._calculate_entry_effects(visitor_entropy)
            entry_result.update(entry_effects)
            
            # Update exploration
            self.exploration_level += 0.1
            
            # Check for secret discovery
            if random.random() < 0.1 + (self.exploration_level * 0.05):
                secret = self._discover_secret()
                if secret:
                    entry_result["secret_discovered"] = secret
                    
        else:
            # Entry failure
            entry_result.update({
                "failure_reason": "resonance_mismatch",
                "entropy_drain": round(visitor_entropy * 0.1, 2),
                "recommended_resonance": self.resonance_frequency
            })
            
        return entry_result
        
    def _calculate_entry_effects(self, visitor_entropy: float) -> Dict[str, Any]:
        """Calculate effects of entering the enclave"""
        effects = {
            "entropy_modification": self.entropy_modifier,
            "stability_influence": self.stability_factor,
            "active_properties": self.special_properties.copy(),
            "environmental_hazards": []
        }
        
        # Check for hazard activation
        for hazard in self.hazards:
            hazard_chance = 0.2 + (visitor_entropy * 0.3)
            if random.random() < hazard_chance:
                effects["environmental_hazards"].append({
                    "type": hazard,
                    "intensity": random.uniform(0.3, 0.8),
                    "duration": random.randint(5, 15)
                })
                
        # Resource discovery chance
        effects["visible_resources"] = []
        for resource_type, resource_data in self.resources.items():
            discovery_chance = resource_data["abundance"] * 0.5
            if random.random() < discovery_chance:
                effects["visible_resources"].append({
                    "type": resource_type,
                    "estimated_quantity": round(resource_data["abundance"] * 100, 1),
                    "quality": round(resource_data["quality"], 2)
                })
                
        return effects
        
    def _discover_secret(self) -> Optional[Dict[str, Any]]:
        """Attempt to discover an enclave secret"""
        possible_secrets = [
            {
                "type": "hidden_chamber",
                "name": "Forgotten Sanctum",
                "description": "A hidden chamber containing ancient artifacts",
                "benefit": "rare_resource_cache"
            },
            {
                "type": "resonance_node",
                "name": "Harmonic Convergence Point",
                "description": "A location where multiple energies converge",
                "benefit": "permanent_entropy_bonus"
            },
            {
                "type": "memory_crystal",
                "name": "Echo Crystal Formation",
                "description": "Crystals that store ancient memories",
                "benefit": "historical_knowledge"
            },
            {
                "type": "portal_nexus",
                "name": "Dimensional Gateway",
                "description": "A gateway to other enclaves or dimensions",
                "benefit": "enclave_connection"
            },
            {
                "type": "temporal_anchor",
                "name": "Time Lock Chamber",
                "description": "A room where time flows differently",
                "benefit": "temporal_manipulation"
            }
        ]
        
        # Check if already discovered
        existing_types = [s["type"] for s in self.discovered_secrets]
        available_secrets = [s for s in possible_secrets if s["type"] not in existing_types]
        
        if not available_secrets:
            return None
            
        secret = random.choice(available_secrets)
        secret["discovery_timestamp"] = datetime.now(timezone.utc).isoformat()
        secret["exploration_level_required"] = self.exploration_level
        
        self.discovered_secrets.append(secret)
        return secret
        
    def extract_resource(self, resource_type: str, extraction_method: str = "standard") -> Dict[str, Any]:
        """Extract resources from the enclave"""
        if resource_type not in self.resources:
            return {
                "success": False,
                "error": f"Resource type '{resource_type}' not available in this enclave"
            }
            
        resource_data = self.resources[resource_type]
        
        # Calculate extraction success
        base_chance = resource_data["abundance"]
        difficulty_penalty = resource_data["extraction_difficulty"]
        
        # Method modifiers
        method_modifiers = {
            "standard": 1.0,
            "careful": 0.8,    # Lower yield but safer
            "aggressive": 1.3,  # Higher yield but more dangerous
            "mystical": 1.1     # Balanced with special effects
        }
        
        method_modifier = method_modifiers.get(extraction_method, 1.0)
        success_chance = (base_chance * method_modifier) - difficulty_penalty
        
        extraction_result = {
            "resource_type": resource_type,
            "extraction_method": extraction_method,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "success": random.random() < success_chance
        }
        
        if extraction_result["success"]:
            # Successful extraction
            quantity = random.uniform(0.5, 2.0) * method_modifier
            quality_variance = random.uniform(0.8, 1.2)
            
            extraction_result.update({
                "quantity": round(quantity, 2),
                "quality": round(resource_data["quality"] * quality_variance, 2),
                "purity": round(random.uniform(0.7, 1.0), 2)
            })
            
            # Reduce resource abundance slightly
            self.resources[resource_type]["abundance"] *= 0.95
            
            # Check for side effects
            if extraction_method == "aggressive":
                extraction_result["side_effects"] = self._generate_extraction_side_effects()
                
        else:
            # Extraction failure
            failure_reasons = [
                "resource_depletion", "environmental_interference",
                "extraction_equipment_failure", "hazard_activation"
            ]
            
            extraction_result.update({
                "failure_reason": random.choice(failure_reasons),
                "resource_lost": round(random.uniform(0.1, 0.3), 2)
            })
            
        return extraction_result
        
    def _generate_extraction_side_effects(self) -> List[Dict[str, Any]]:
        """Generate side effects from aggressive extraction"""
        possible_effects = [
            {
                "type": "environmental_damage",
                "description": "Extraction process damaged the enclave environment",
                "impact": "reduced_resource_regeneration"
            },
            {
                "type": "hazard_activation",
                "description": "Extraction triggered environmental hazards",
                "impact": "temporary_danger_increase"
            },
            {
                "type": "resonance_disruption",
                "description": "Extraction disrupted enclave's natural resonance",
                "impact": "altered_entry_requirements"
            },
            {
                "type": "entity_attention",
                "description": "Extraction attracted unwanted attention",
                "impact": "potential_hostile_encounter"
            }
        ]
        
        effect_count = random.randint(1, 2)
        return random.sample(possible_effects, min(effect_count, len(possible_effects)))
        
    def get_status(self) -> Dict[str, Any]:
        """Get current enclave status"""
        return {
            "enclave_id": self.enclave_id,
            "name": self.name,
            "type": self.enclave_type,
            "dominant_element": self.dominant_element,
            "secondary_elements": self.secondary_elements,
            "entropy_modifier": round(self.entropy_modifier, 2),
            "stability_factor": round(self.stability_factor, 2),
            "resonance_frequency": round(self.resonance_frequency, 3),
            "exploration_level": round(self.exploration_level, 2),
            "special_properties": self.special_properties,
            "environmental_hazards": self.hazards,
            "available_resources": list(self.resources.keys()),
            "discovered_secrets": len(self.discovered_secrets),
            "active_effects": len(self.active_effects)
        }

class EnclaveSystem:
    """Manager for all drift enclaves"""
    
    def __init__(self):
        self.enclaves = {}
        self.discovered_enclaves = set()
        self.enclave_connections = {}
        self.exploration_history = []
        
        # Initialize default enclaves
        self.initialize_default_enclaves()
        
    def initialize_default_enclaves(self):
        """Create the initial set of drift enclaves"""
        default_enclaves = [
            ("void_nexus", "The Void Nexus", "void_nexus"),
            ("entropy_gardens", "Entropy Gardens", "entropy_gardens"),
            ("crystal_sanctum", "Crystal Sanctum", "crystal_sanctum"),
            ("temporal_streams", "Temporal Streams", "temporal_streams"),
            ("energy_maelstrom", "Energy Maelstrom", "energy_maelstrom")
        ]
        
        for enclave_id, name, enclave_type in default_enclaves:
            enclave = DriftEnclave(enclave_id, name, enclave_type)
            self.enclaves[enclave_id] = enclave
            
        # All default enclaves start discovered
        self.discovered_enclaves.update([e[0] for e in default_enclaves])
        
        # Create initial connections
        self.generate_enclave_connections()
        
    def generate_enclave_connections(self):
        """Generate connections between enclaves"""
        enclave_ids = list(self.enclaves.keys())
        
        for enclave_id in enclave_ids:
            # Each enclave connects to 1-3 others
            connection_count = random.randint(1, 3)
            possible_connections = [eid for eid in enclave_ids if eid != enclave_id]
            
            connections = random.sample(possible_connections, 
                                      min(connection_count, len(possible_connections)))
            
            self.enclave_connections[enclave_id] = []
            for connected_id in connections:
                connection_strength = random.uniform(0.3, 0.9)
                connection_stability = random.uniform(0.5, 1.0)
                
                self.enclave_connections[enclave_id].append({
                    "target_enclave": connected_id,
                    "strength": connection_strength,
                    "stability": connection_stability,
                    "bidirectional": random.choice([True, False])
                })
                
    def get_enclave(self, enclave_id: str) -> Optional[DriftEnclave]:
        """Get enclave by ID"""
        return self.enclaves.get(enclave_id)
        
    def get_all_enclave_ids(self) -> List[str]:
        """Get all enclave IDs"""
        return list(self.enclaves.keys())
        
    def get_discovered_enclaves(self) -> List[DriftEnclave]:
        """Get all discovered enclaves"""
        return [self.enclaves[eid] for eid in self.discovered_enclaves if eid in self.enclaves]
        
    def discover_new_enclave(self, discovery_method: str = "exploration") -> Optional[Dict[str, Any]]:
        """Attempt to discover a new enclave"""
        # Generate procedural enclave
        enclave_id = f"enclave_{random.randint(1000, 9999)}"
        
        # Generate name and type
        name_components = [
            ["Crimson", "Shadow", "Crystal", "Void", "Temporal", "Azure", "Golden"],
            ["Halls", "Sanctum", "Gardens", "Nexus", "Chambers", "Streams", "Citadel"]
        ]
        
        name = f"{random.choice(name_components[0])} {random.choice(name_components[1])}"
        
        enclave_types = ["void_nexus", "entropy_gardens", "crystal_sanctum", 
                        "temporal_streams", "energy_maelstrom"]
        enclave_type = random.choice(enclave_types)
        
        # Create enclave
        new_enclave = DriftEnclave(enclave_id, name, enclave_type)
        
        # Discovery success based on method
        discovery_chances = {
            "exploration": 0.3,
            "mystical_sensing": 0.5,
            "dimensional_scan": 0.7,
            "oracle_guidance": 0.8
        }
        
        discovery_chance = discovery_chances.get(discovery_method, 0.3)
        
        if random.random() < discovery_chance:
            # Successful discovery
            self.enclaves[enclave_id] = new_enclave
            self.discovered_enclaves.add(enclave_id)
            
            discovery_result = {
                "success": True,
                "enclave": new_enclave.get_status(),
                "discovery_method": discovery_method,
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
            
            self.exploration_history.append(discovery_result)
            return discovery_result
        else:
            return {
                "success": False,
                "discovery_method": discovery_method,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "hint": self._generate_discovery_hint()
            }
            
    def _generate_discovery_hint(self) -> str:
        """Generate a hint for enclave discovery"""
        hints = [
            "Strange resonance patterns detected in the void streams",
            "Temporal echoes suggest hidden chambers nearby",
            "Energy fluctuations indicate an undiscovered nexus",
            "Crystal formations point toward a concealed sanctuary",
            "Entropy disturbances reveal potential pathways"
        ]
        return random.choice(hints)
        
    def travel_between_enclaves(self, from_enclave_id: str, to_enclave_id: str, 
                              travel_method: str = "direct") -> Dict[str, Any]:
        """Travel between connected enclaves"""
        if from_enclave_id not in self.enclaves or to_enclave_id not in self.enclaves:
            return {
                "success": False,
                "error": "One or both enclaves not found"
            }
            
        # Check if enclaves are connected
        connections = self.enclave_connections.get(from_enclave_id, [])
        target_connection = None
        
        for connection in connections:
            if connection["target_enclave"] == to_enclave_id:
                target_connection = connection
                break
                
        travel_result = {
            "from_enclave": from_enclave_id,
            "to_enclave": to_enclave_id,
            "travel_method": travel_method,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
        
        if target_connection:
            # Direct connection exists
            success_chance = target_connection["stability"] * 0.8
            
            if travel_method == "careful":
                success_chance *= 1.2
            elif travel_method == "forced":
                success_chance *= 0.7
                
            travel_result["success"] = random.random() < success_chance
            travel_result["connection_strength"] = target_connection["strength"]
            
        else:
            # No direct connection - attempt dimensional hop
            if travel_method == "dimensional_hop":
                travel_result["success"] = random.random() < 0.4
                travel_result["requires_energy"] = True
            else:
                travel_result["success"] = False
                travel_result["error"] = "No direct connection available"
                
        if travel_result["success"]:
            travel_result["travel_time"] = random.uniform(1.0, 5.0)
            travel_result["entropy_cost"] = random.uniform(0.05, 0.15)
        else:
            travel_result["failure_consequence"] = random.choice([
                "temporal_displacement", "energy_drain", "dimensional_scatter"
            ])
            
        return travel_result
        
    def get_enclave_resonances(self) -> Dict[str, float]:
        """Get resonance levels for all discovered enclaves"""
        resonances = {}
        for enclave_id in self.discovered_enclaves:
            if enclave_id in self.enclaves:
                enclave = self.enclaves[enclave_id]
                # Add some random fluctuation to resonance
                fluctuation = random.uniform(-0.1, 0.1)
                resonances[enclave_id] = max(0.0, min(1.0, 
                    enclave.resonance_frequency + fluctuation))
        return resonances
        
    def export_state(self) -> Dict[str, Any]:
        """Export enclave system state"""
        return {
            "discovered_enclaves": list(self.discovered_enclaves),
            "enclave_connections": self.enclave_connections.copy(),
            "exploration_history": self.exploration_history.copy(),
            "enclave_states": {
                eid: {
                    "exploration_level": enclave.exploration_level,
                    "discovered_secrets": enclave.discovered_secrets.copy(),
                    "resources": enclave.resources.copy()
                }
                for eid, enclave in self.enclaves.items()
            }
        }
        
    def import_state(self, state_data: Dict[str, Any]):
        """Import enclave system state"""
        self.discovered_enclaves = set(state_data.get("discovered_enclaves", []))
        self.enclave_connections = state_data.get("enclave_connections", {})
        self.exploration_history = state_data.get("exploration_history", [])
        
        # Restore enclave states
        enclave_states = state_data.get("enclave_states", {})
        for enclave_id, enclave_state in enclave_states.items():
            if enclave_id in self.enclaves:
                enclave = self.enclaves[enclave_id]
                enclave.exploration_level = enclave_state.get("exploration_level", 0)
                enclave.discovered_secrets = enclave_state.get("discovered_secrets", [])
                enclave.resources = enclave_state.get("resources", enclave.resources)
