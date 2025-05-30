"""
Recursive Drift Engine: Core System Controller
Manages all game systems and their interactions
"""

import random
import json
from datetime import datetime, timezone
import threading
from typing import Dict, List, Any, Optional

# Import all subsystems
from alchemy_system import AlchemySystem
from enclave_system import EnclaveSystem
from time_mechanics import ChronoSystem
from oracle_system import OracleSystem
from mini_games import EntropyRitesSystem
from market_system import FragmentMarket
from glyphs import GlyphManager

class DriftEngine:
    """Main engine that coordinates all mystical systems"""
    
    def __init__(self):
        # Core state
        self.node_id = "Xi-Void-404"
        self.entropy_level = 0.5
        self.time_salt = 100
        self.identity_fragments = 50
        
        # System managers
        self.glyph_manager = GlyphManager()
        self.alchemy_system = AlchemySystem(self.glyph_manager)
        self.enclave_system = EnclaveSystem()
        self.chrono_system = ChronoSystem()
        self.oracle_system = OracleSystem()
        self.entropy_rites = EntropyRitesSystem()
        self.fragment_market = FragmentMarket()
        
        # Game state tracking
        self.fork_log = []
        self.feedback_log = []
        self.anomaly_echoes = []
        self.loop_chains = []
        self.sentient_logs = []
        
        # Real-time state
        self.active_enclave = None
        self.current_drift_map = None
        self.entropy_field = {}
        
        # Thread safety
        self.state_lock = threading.Lock()
        
        # Initialize systems
        self.initialize_entropy_field()
        
    def initialize_default_state(self):
        """Initialize the engine with default starting state"""
        with self.state_lock:
            # Generate initial drift map
            self.current_drift_map = self.generate_drift_map()
            
            # Set starting enclave
            self.active_enclave = self.enclave_system.get_enclave("void_nexus")
            
            # Create initial sentient log
            self.create_sentient_log("Genesis", "System initialization complete. Drift field stabilized.")
            
            # Generate starting prophecy
            self.oracle_system.generate_initial_prophecy()
            
    def initialize_entropy_field(self):
        """Initialize the entropy field across all systems"""
        self.entropy_field = {
            'global_flux': random.uniform(0.3, 0.7),
            'enclave_resonance': {},
            'glyph_harmonics': {},
            'temporal_distortion': 0.0,
            'market_volatility': random.uniform(0.1, 0.9)
        }
        
        # Initialize enclave resonances
        for enclave_id in self.enclave_system.get_all_enclave_ids():
            self.entropy_field['enclave_resonance'][enclave_id] = random.uniform(0.0, 1.0)
            
        # Initialize glyph harmonics
        for glyph in self.glyph_manager.get_all_glyphs():
            self.entropy_field['glyph_harmonics'][glyph] = random.uniform(0.0, 1.0)
            
    def update_entropy_field(self):
        """Update entropy field values - called by background thread"""
        with self.state_lock:
            # Global flux fluctuation
            flux_change = random.uniform(-0.05, 0.05)
            self.entropy_field['global_flux'] = max(0.0, min(1.0, 
                self.entropy_field['global_flux'] + flux_change))
            
            # Update enclave resonances
            for enclave_id in self.entropy_field['enclave_resonance']:
                resonance_change = random.uniform(-0.02, 0.02)
                current = self.entropy_field['enclave_resonance'][enclave_id]
                self.entropy_field['enclave_resonance'][enclave_id] = max(0.0, min(1.0, 
                    current + resonance_change))
            
            # Update glyph harmonics
            for glyph in self.entropy_field['glyph_harmonics']:
                harmonic_change = random.uniform(-0.03, 0.03)
                current = self.entropy_field['glyph_harmonics'][glyph]
                self.entropy_field['glyph_harmonics'][glyph] = max(0.0, min(1.0, 
                    current + harmonic_change))
            
            # Update temporal distortion
            temporal_change = random.uniform(-0.01, 0.01)
            self.entropy_field['temporal_distortion'] = max(-1.0, min(1.0,
                self.entropy_field['temporal_distortion'] + temporal_change))
            
            # Update market volatility
            volatility_change = random.uniform(-0.1, 0.1)
            self.entropy_field['market_volatility'] = max(0.0, min(1.0,
                self.entropy_field['market_volatility'] + volatility_change))
                
    def generate_drift_map(self, width: int = 5, height: int = 5) -> List[List[str]]:
        """Generate a new drift map with current entropy influence"""
        with self.state_lock:
            drift_map = []
            for y in range(height):
                row = []
                for x in range(width):
                    # Choose glyph based on entropy harmonics
                    weighted_glyphs = []
                    for glyph in self.glyph_manager.get_all_glyphs():
                        weight = self.entropy_field['glyph_harmonics'].get(glyph, 0.5)
                        weighted_glyphs.extend([glyph] * max(1, int(weight * 10)))
                    
                    chosen_glyph = random.choice(weighted_glyphs)
                    row.append(chosen_glyph)
                row.append(row)
            
            self.current_drift_map = drift_map
            return drift_map
            
    def fork_node(self, node_id: str = None) -> Dict[str, Any]:
        """Create a forked node with enhanced properties"""
        if node_id is None:
            node_id = self.node_id
            
        with self.state_lock:
            fork_id = f"{node_id}-{random.randint(1000, 9999)}"
            
            # Enhanced fork state with system integration
            fork_state = {
                "node_id": fork_id,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "parent_node": node_id,
                "glyph_state": random.sample(self.glyph_manager.get_all_glyphs(), k=3),
                "entropy_level": round(self.entropy_field['global_flux'], 3),
                "enclave_origin": self.active_enclave.name if self.active_enclave else "Unknown",
                "temporal_signature": self.chrono_system.get_current_signature(),
                "alchemy_potential": self.alchemy_system.calculate_fork_potential(fork_id),
                "sentience_probability": random.uniform(0.0, 0.3)
            }
            
            self.fork_log.append(fork_state)
            
            # Check for sentient log emergence
            if fork_state['sentience_probability'] > 0.2:
                self.create_sentient_log(fork_id, f"Emerged from fork operation: {fork_state['glyph_state']}")
            
            # Update entropy field
            self.entropy_field['global_flux'] *= 1.05  # Forking increases entropy
            
            return fork_state
            
    def collapse_node(self, node_id: str = None) -> Dict[str, Any]:
        """Collapse a node with system-wide effects"""
        if node_id is None:
            node_id = self.node_id
            
        with self.state_lock:
            collapse_result = {
                "node_id": node_id,
                "action": "collapse",
                "status": "erased",
                "sigil": random.choice(self.glyph_manager.get_all_glyphs()),
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "entropy_release": round(self.entropy_field['global_flux'] * 0.1, 3),
                "time_salt_generated": random.randint(1, 5),
                "fragments_released": random.randint(0, 3)
            }
            
            # Add resources from collapse
            self.time_salt += collapse_result['time_salt_generated']
            self.identity_fragments += collapse_result['fragments_released']
            
            # Reduce entropy
            self.entropy_field['global_flux'] *= 0.95
            
            # Add to anomaly echoes
            echo = self.create_anomaly_echo(collapse_result)
            self.anomaly_echoes.append(echo)
            
            return collapse_result
            
    def memory_wipe(self) -> str:
        """Perform memory wipe with enhanced effects"""
        with self.state_lock:
            # Store some data as anomaly echoes before wiping
            if self.fork_log:
                for i, fork in enumerate(random.sample(self.fork_log, min(3, len(self.fork_log)))):
                    echo = self.create_anomaly_echo(fork, fractured=True)
                    self.anomaly_echoes.append(echo)
            
            # Clear logs
            wiped_count = len(self.fork_log)
            self.fork_log = []
            
            # Generate time salt for the wipe
            salt_generated = wiped_count * 2
            self.time_salt += salt_generated
            
            # Reset some entropy
            self.entropy_field['global_flux'] = 0.5
            
            return f"Memory void complete. {wiped_count} fork histories erased. Generated {salt_generated} Time Salt."
            
    def create_anomaly_echo(self, source_data: Dict[str, Any], fractured: bool = False) -> Dict[str, Any]:
        """Create an anomaly echo from source data"""
        echo = {
            "echo_id": f"echo-{random.randint(10000, 99999)}",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "source_type": source_data.get('action', 'fork'),
            "fractured": fractured,
            "entropy_signature": round(random.uniform(0.0, 1.0), 3),
            "temporal_drift": random.uniform(-0.5, 0.5),
            "echo_strength": random.uniform(0.1, 0.9)
        }
        
        if fractured:
            # Corrupt some data for fractured echoes
            echo["corrupted_data"] = self._fracture_data(source_data)
        else:
            echo["source_data"] = source_data.copy()
            
        return echo
        
    def _fracture_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create fractured/corrupted version of data"""
        fractured = {}
        for key, value in data.items():
            if random.random() < 0.3:  # 30% chance to corrupt each field
                if isinstance(value, str):
                    # Corrupt string data
                    if len(value) > 3:
                        fractured[key] = value[:len(value)//2] + "█" * (len(value)//2)
                    else:
                        fractured[key] = "█" * len(value)
                elif isinstance(value, (int, float)):
                    # Corrupt numeric data
                    fractured[key] = "###"
                elif isinstance(value, list):
                    # Partially corrupt lists
                    fractured[key] = value[:len(value)//2] + ["█"] * (len(value)//2)
                else:
                    fractured[key] = "█" * 5
            else:
                fractured[key] = value
                
        return fractured
        
    def create_sentient_log(self, log_id: str, initial_content: str) -> Dict[str, Any]:
        """Create a new sentient log entity"""
        sentient_log = {
            "log_id": log_id,
            "creation_timestamp": datetime.now(timezone.utc).isoformat(),
            "content": initial_content,
            "sentience_level": random.uniform(0.1, 0.8),
            "autonomy_level": random.uniform(0.0, 0.5),
            "behavior_pattern": random.choice(["observer", "manipulator", "chronicler", "prophet"]),
            "interaction_count": 0,
            "last_activity": datetime.now(timezone.utc).isoformat(),
            "influence_radius": random.uniform(0.1, 0.3),
            "memory_fragments": []
        }
        
        self.sentient_logs.append(sentient_log)
        return sentient_log
        
    def update_sentient_logs(self):
        """Update behavior of all sentient logs"""
        with self.state_lock:
            for log in self.sentient_logs:
                if random.random() < log['autonomy_level']:
                    self._execute_sentient_behavior(log)
                    
    def _execute_sentient_behavior(self, log: Dict[str, Any]):
        """Execute autonomous behavior for a sentient log"""
        behavior = log['behavior_pattern']
        
        if behavior == "observer":
            # Observer logs watch and record
            log['memory_fragments'].append({
                "observation": f"Entropy flux: {self.entropy_field['global_flux']:.3f}",
                "timestamp": datetime.now(timezone.utc).isoformat()
            })
            
        elif behavior == "manipulator":
            # Manipulator logs try to influence entropy
            if len(log['memory_fragments']) < 10:  # Limit influence
                influence = log['influence_radius'] * random.uniform(-0.02, 0.02)
                self.entropy_field['global_flux'] = max(0.0, min(1.0, 
                    self.entropy_field['global_flux'] + influence))
                
                log['memory_fragments'].append({
                    "manipulation": f"Applied entropy influence: {influence:.4f}",
                    "timestamp": datetime.now(timezone.utc).isoformat()
                })
                
        elif behavior == "chronicler":
            # Chronicler logs preserve important events
            if self.fork_log:
                recent_fork = self.fork_log[-1]
                log['memory_fragments'].append({
                    "chronicle": f"Recorded fork: {recent_fork['node_id']}",
                    "timestamp": datetime.now(timezone.utc).isoformat()
                })
                
        elif behavior == "prophet":
            # Prophet logs generate predictions
            prediction = self.oracle_system.generate_micro_prophecy()
            log['memory_fragments'].append({
                "prophecy": prediction,
                "timestamp": datetime.now(timezone.utc).isoformat()
            })
            
        # Update activity timestamp and interaction count
        log['last_activity'] = datetime.now(timezone.utc).isoformat()
        log['interaction_count'] += 1
        
        # Evolve sentience over time
        if log['interaction_count'] % 10 == 0:
            log['sentience_level'] = min(1.0, log['sentience_level'] + 0.01)
            
    def get_system_status(self) -> Dict[str, Any]:
        """Get comprehensive status of all systems"""
        with self.state_lock:
            return {
                "node_id": self.node_id,
                "entropy_level": round(self.entropy_field['global_flux'], 3),
                "time_salt": self.time_salt,
                "identity_fragments": self.identity_fragments,
                "active_enclave": self.active_enclave.name if self.active_enclave else None,
                "fork_count": len(self.fork_log),
                "anomaly_count": len(self.anomaly_echoes),
                "sentient_logs": len(self.sentient_logs),
                "loop_chains": len(self.loop_chains),
                "entropy_field": self.entropy_field.copy(),
                "alchemy_combinations": self.alchemy_system.get_known_combinations_count(),
                "market_items": self.fragment_market.get_item_count(),
                "stasis_preservation": self.chrono_system.get_stasis_count()
            }
            
    def export_state(self) -> Dict[str, Any]:
        """Export complete engine state for persistence"""
        with self.state_lock:
            return {
                "node_id": self.node_id,
                "entropy_level": self.entropy_level,
                "time_salt": self.time_salt,
                "identity_fragments": self.identity_fragments,
                "fork_log": self.fork_log.copy(),
                "feedback_log": self.feedback_log.copy(),
                "anomaly_echoes": self.anomaly_echoes.copy(),
                "loop_chains": self.loop_chains.copy(),
                "sentient_logs": self.sentient_logs.copy(),
                "entropy_field": self.entropy_field.copy(),
                "active_enclave_id": self.active_enclave.enclave_id if self.active_enclave else None,
                "alchemy_state": self.alchemy_system.export_state(),
                "enclave_state": self.enclave_system.export_state(),
                "chrono_state": self.chrono_system.export_state(),
                "oracle_state": self.oracle_system.export_state(),
                "market_state": self.fragment_market.export_state(),
                "entropy_rites_state": self.entropy_rites.export_state()
            }
            
    def import_state(self, state_data: Dict[str, Any]):
        """Import complete engine state from persistence"""
        with self.state_lock:
            # Core properties
            self.node_id = state_data.get("node_id", "Xi-Void-404")
            self.entropy_level = state_data.get("entropy_level", 0.5)
            self.time_salt = state_data.get("time_salt", 100)
            self.identity_fragments = state_data.get("identity_fragments", 50)
            
            # Logs and tracking
            self.fork_log = state_data.get("fork_log", [])
            self.feedback_log = state_data.get("feedback_log", [])
            self.anomaly_echoes = state_data.get("anomaly_echoes", [])
            self.loop_chains = state_data.get("loop_chains", [])
            self.sentient_logs = state_data.get("sentient_logs", [])
            self.entropy_field = state_data.get("entropy_field", {})
            
            # Restore active enclave
            active_enclave_id = state_data.get("active_enclave_id")
            if active_enclave_id:
                self.active_enclave = self.enclave_system.get_enclave(active_enclave_id)
            
            # Import subsystem states
            if "alchemy_state" in state_data:
                self.alchemy_system.import_state(state_data["alchemy_state"])
            if "enclave_state" in state_data:
                self.enclave_system.import_state(state_data["enclave_state"])
            if "chrono_state" in state_data:
                self.chrono_system.import_state(state_data["chrono_state"])
            if "oracle_state" in state_data:
                self.oracle_system.import_state(state_data["oracle_state"])
            if "market_state" in state_data:
                self.fragment_market.import_state(state_data["market_state"])
            if "entropy_rites_state" in state_data:
                self.entropy_rites.import_state(state_data["entropy_rites_state"])
                
            # Ensure entropy field is properly initialized
            if not self.entropy_field:
                self.initialize_entropy_field()
