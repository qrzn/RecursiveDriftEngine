"""
Recursive Oracle System: AI-Powered Paradox Prophecies
Advanced mystical prediction system with OpenAI integration
"""

import random
import json
import os
from datetime import datetime, timezone, timedelta
from typing import Dict, List, Any, Optional
import hashlib

# OpenAI integration for recursive oracle prophecies
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

class OracleEntity:
    """Individual oracle entity with unique personality and prediction style"""
    
    def __init__(self, oracle_id: str, name: str, oracle_type: str):
        self.oracle_id = oracle_id
        self.name = name
        self.oracle_type = oracle_type
        
        # Oracle properties
        self.prophecy_style = random.choice(["cryptic", "direct", "metaphorical", "mathematical", "poetic"])
        self.accuracy_rating = random.uniform(0.6, 0.9)
        self.paradox_affinity = random.uniform(0.3, 0.8)
        self.temporal_vision_range = random.uniform(1.0, 24.0)  # Hours into future
        
        # Oracle state
        self.total_prophecies = 0
        self.successful_predictions = 0
        self.energy_level = random.uniform(0.7, 1.0)
        self.last_prophecy_time = None
        self.consultation_count = 0
        
        # Personality traits
        self.personality_traits = random.sample([
            "wise", "mysterious", "eccentric", "analytical", "intuitive",
            "chaotic", "structured", "ancient", "progressive", "paradoxical"
        ], k=random.randint(2, 4))
        
    def generate_prophecy_prompt(self, query_context: Dict[str, Any]) -> str:
        """Generate a prompt for the oracle's prophecy style"""
        style_prompts = {
            "cryptic": "Speak in riddles and hidden meanings. Use symbolic language and metaphors.",
            "direct": "Provide clear, straightforward predictions with specific details.",
            "metaphorical": "Express insights through elaborate metaphors and analogies.",
            "mathematical": "Frame predictions in terms of patterns, probabilities, and equations.",
            "poetic": "Deliver prophecies in verse form with rhythmic, mystical language."
        }
        
        base_prompt = f"""You are {self.name}, a mystical oracle entity in the Recursive Drift Engine. 
        Your prophecy style is {self.prophecy_style}. {style_prompts.get(self.prophecy_style, '')}
        
        Your personality traits: {', '.join(self.personality_traits)}
        Your accuracy rating: {self.accuracy_rating:.2f}
        Your paradox affinity: {self.paradox_affinity:.2f}
        
        Current context:
        - Node ID: {query_context.get('node_id', 'Unknown')}
        - Entropy Level: {query_context.get('entropy_level', 0.5):.3f}
        - Active Enclave: {query_context.get('active_enclave', 'None')}
        - Time Salt: {query_context.get('time_salt', 0)}
        - Identity Fragments: {query_context.get('identity_fragments', 0)}
        
        Generate a mystical prophecy about the drift field's future. Focus on potential outcomes,
        warnings about entropy fluctuations, opportunities for discovery, or paradoxical insights.
        Keep the prophecy between 50-150 words. Return your response as JSON with this format:
        {{"prophecy": "your prophecy text", "confidence": 0.7, "timeframe": "near future", "type": "warning/opportunity/insight/paradox"}}
        """
        
        return base_prompt
        
    def get_consultation_cost(self) -> int:
        """Calculate cost for consulting this oracle"""
        base_cost = 5
        
        # More accurate oracles cost more
        accuracy_multiplier = 1 + (self.accuracy_rating - 0.5)
        
        # Energy level affects cost
        energy_multiplier = 2.0 - self.energy_level
        
        # Consultation count affects price (oracle gets tired)
        fatigue_multiplier = 1 + (self.consultation_count * 0.1)
        
        total_cost = int(base_cost * accuracy_multiplier * energy_multiplier * fatigue_multiplier)
        return max(1, total_cost)
        
    def update_energy(self, energy_change: float):
        """Update oracle's energy level"""
        self.energy_level = max(0.1, min(1.0, self.energy_level + energy_change))
        
    def record_prophecy_outcome(self, was_accurate: bool):
        """Record the outcome of a prophecy for accuracy tracking"""
        if was_accurate:
            self.successful_predictions += 1
            self.update_energy(0.1)  # Successful predictions boost energy
        else:
            self.update_energy(-0.05)  # Failed predictions drain energy
            
        # Update accuracy rating gradually
        current_accuracy = self.successful_predictions / max(1, self.total_prophecies)
        self.accuracy_rating = (self.accuracy_rating * 0.9) + (current_accuracy * 0.1)

class OracleSystem:
    """Main oracle system managing multiple oracle entities and AI integration"""
    
    def __init__(self):
        # OpenAI configuration
        self.openai_client = None
        self.ai_enabled = False
        self.initialize_ai()
        
        # Oracle entities
        self.oracles = {}
        self.active_prophecies = []
        self.prophecy_history = []
        self.background_prophecies = []
        
        # System state
        self.total_consultations = 0
        self.system_energy = 1.0
        self.paradox_resonance = 0.5
        self.temporal_clarity = 0.7
        
        # Initialize default oracles
        self.initialize_default_oracles()
        
    def initialize_ai(self):
        """Initialize OpenAI client for AI-powered prophecies"""
        if not OPENAI_AVAILABLE:
            return
            
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            try:
                self.openai_client = OpenAI(api_key=api_key)
                self.ai_enabled = True
            except Exception as e:
                print(f"Failed to initialize OpenAI client: {e}")
                
    def initialize_default_oracles(self):
        """Create default oracle entities"""
        default_oracles = [
            ("void_oracle", "The Void Whisperer", "entropy"),
            ("time_seer", "Chronos Vision", "temporal"),
            ("paradox_sage", "The Paradox Sage", "paradox"),
            ("crystal_prophet", "Crystal Mind", "structural"),
            ("chaos_oracle", "Entropy's Voice", "chaotic")
        ]
        
        for oracle_id, name, oracle_type in default_oracles:
            oracle = OracleEntity(oracle_id, name, oracle_type)
            self.oracles[oracle_id] = oracle
            
    def consult_oracle(self, oracle_id: str, query_context: Dict[str, Any], 
                      consultation_type: str = "general") -> Dict[str, Any]:
        """Consult a specific oracle for a prophecy"""
        if oracle_id not in self.oracles:
            return {
                "success": False,
                "error": f"Oracle {oracle_id} not found"
            }
            
        oracle = self.oracles[oracle_id]
        
        # Check if oracle has enough energy
        if oracle.energy_level < 0.3:
            return {
                "success": False,
                "error": f"{oracle.name} is too drained to provide prophecies",
                "energy_level": oracle.energy_level,
                "rest_time_needed": round((0.5 - oracle.energy_level) * 10, 1)
            }
            
        consultation_result = {
            "oracle_id": oracle_id,
            "oracle_name": oracle.name,
            "consultation_type": consultation_type,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "cost": oracle.get_consultation_cost()
        }
        
        # Generate prophecy
        if self.ai_enabled and random.random() < 0.7:  # 70% chance to use AI
            prophecy_result = self._generate_ai_prophecy(oracle, query_context)
        else:
            prophecy_result = self._generate_local_prophecy(oracle, query_context, consultation_type)
            
        consultation_result.update(prophecy_result)
        
        # Update oracle state
        oracle.total_prophecies += 1
        oracle.consultation_count += 1
        oracle.last_prophecy_time = datetime.now(timezone.utc).isoformat()
        oracle.update_energy(-0.1)  # Consulting drains energy
        
        # Update system state
        self.total_consultations += 1
        
        # Store prophecy
        prophecy_record = {
            "prophecy_id": f"prophecy_{len(self.prophecy_history)+1:04d}",
            "oracle_id": oracle_id,
            "consultation_result": consultation_result.copy(),
            "query_context": query_context.copy(),
            "created_time": datetime.now(timezone.utc).isoformat(),
            "verification_status": "pending"
        }
        
        self.prophecy_history.append(prophecy_record)
        self.active_prophecies.append(prophecy_record)
        
        consultation_result["prophecy_id"] = prophecy_record["prophecy_id"]
        consultation_result["success"] = True
        
        return consultation_result
        
    def _generate_ai_prophecy(self, oracle: OracleEntity, query_context: Dict[str, Any]) -> Dict[str, Any]:
        """Generate prophecy using OpenAI"""
        try:
            prompt = oracle.generate_prophecy_prompt(query_context)
            
            # the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
            # do not change this unless explicitly requested by the user
            response = self.openai_client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a mystical oracle entity. Respond only with valid JSON."
                    },
                    {
                        "role": "user", 
                        "content": prompt
                    }
                ],
                response_format={"type": "json_object"},
                max_tokens=300
            )
            
            prophecy_data = json.loads(response.choices[0].message.content)
            
            return {
                "prophecy_text": prophecy_data.get("prophecy", "The visions are unclear..."),
                "confidence": min(1.0, max(0.1, prophecy_data.get("confidence", 0.5))),
                "timeframe": prophecy_data.get("timeframe", "uncertain"),
                "prophecy_type": prophecy_data.get("type", "insight"),
                "generation_method": "ai_powered",
                "oracle_style": oracle.prophecy_style
            }
            
        except Exception as e:
            # Fallback to local generation
            return self._generate_local_prophecy(oracle, query_context, "general")
            
    def _generate_local_prophecy(self, oracle: OracleEntity, query_context: Dict[str, Any], 
                                consultation_type: str) -> Dict[str, Any]:
        """Generate prophecy using local algorithms"""
        # Base prophecy templates by oracle type and style
        prophecy_templates = {
            "entropy": {
                "cryptic": [
                    "The void whispers of {entropy_state} tides approaching the {node_location}...",
                    "In the dance of chaos and order, {glyph_symbol} shall {action_verb} when {condition}...",
                    "The entropy threads weave a pattern of {pattern_type} - beware the {warning_element}..."
                ],
                "direct": [
                    "Entropy levels will {trend_direction} to {entropy_prediction} within {timeframe}.",
                    "The drift field shows signs of {field_state} - expect {outcome_type}.",
                    "Resource fluctuations indicate {resource_prediction} in the {location_type}."
                ]
            },
            "temporal": {
                "cryptic": [
                    "Time flows backward through the {temporal_anomaly}, revealing {revelation}...",
                    "The chronos streams converge at the {convergence_point} - {temporal_warning}...",
                    "Past echoes {echo_action} in the {time_location}, creating {paradox_type}..."
                ],
                "mathematical": [
                    "Temporal probability matrices indicate {percentage}% chance of {event_type}.",
                    "Causal algorithms predict {calculation_result} within {time_range} cycles.",
                    "Time variance equals {variance_value}, suggesting {mathematical_conclusion}."
                ]
            },
            "paradox": {
                "paradoxical": [
                    "What is {statement} is not {opposite}, yet {contradiction} remains {truth_state}...",
                    "The answer you seek exists only when you stop {seeking_action}...",
                    "To {goal_verb} the {target}, one must first {opposite_action} the {paradox_element}..."
                ]
            }
        }
        
        # Generate prophecy components
        entropy_level = query_context.get("entropy_level", 0.5)
        
        prophecy_components = {
            "entropy_state": "turbulent" if entropy_level > 0.7 else "stable" if entropy_level < 0.3 else "shifting",
            "node_location": query_context.get("active_enclave", "drift nexus"),
            "glyph_symbol": random.choice(["▲", "⊗", "≈", "∇", "∆"]),
            "action_verb": random.choice(["manifest", "collapse", "transform", "resonate", "eclipse"]),
            "condition": random.choice(["the void aligns", "entropy peaks", "time fractures", "reality bends"]),
            "pattern_type": random.choice(["convergence", "divergence", "spiral", "cascade", "resonance"]),
            "warning_element": random.choice(["false harmony", "hidden chaos", "temporal trap", "void surge"]),
            "trend_direction": random.choice(["rise", "fall", "fluctuate", "stabilize"]),
            "entropy_prediction": f"{random.uniform(0.1, 0.9):.1f}",
            "timeframe": random.choice(["moments", "cycles", "phases", "eons"]),
            "temporal_anomaly": random.choice(["crystal caves", "void streams", "entropy gardens", "time wells"]),
            "revelation": random.choice(["forgotten truths", "future echoes", "past warnings", "hidden paths"]),
            "percentage": random.randint(15, 85),
            "event_type": random.choice(["cascade event", "stability breach", "resource discovery", "temporal shift"])
        }
        
        # Select appropriate template
        oracle_type = oracle.oracle_type
        prophecy_style = oracle.prophecy_style
        
        available_templates = prophecy_templates.get(oracle_type, prophecy_templates["entropy"])
        style_templates = available_templates.get(prophecy_style, available_templates.get("cryptic", []))
        
        if not style_templates:
            style_templates = ["The visions are unclear in these times of {entropy_state}..."]
            
        # Generate prophecy text
        template = random.choice(style_templates)
        prophecy_text = template.format(**prophecy_components)
        
        # Determine confidence based on oracle accuracy and energy
        base_confidence = oracle.accuracy_rating * oracle.energy_level
        confidence_variance = random.uniform(-0.2, 0.2)
        confidence = max(0.1, min(1.0, base_confidence + confidence_variance))
        
        # Determine timeframe based on oracle's temporal vision
        timeframe_options = ["immediate", "near future", "distant future", "beyond time"]
        if oracle.temporal_vision_range < 6:
            timeframe = random.choice(timeframe_options[:2])
        elif oracle.temporal_vision_range < 12:
            timeframe = random.choice(timeframe_options[1:3])
        else:
            timeframe = random.choice(timeframe_options[2:])
            
        # Determine prophecy type
        prophecy_types = ["warning", "opportunity", "insight", "paradox"]
        if oracle.paradox_affinity > 0.6:
            prophecy_type = random.choices(prophecy_types, weights=[20, 20, 30, 30])[0]
        else:
            prophecy_type = random.choices(prophecy_types, weights=[30, 30, 30, 10])[0]
            
        return {
            "prophecy_text": prophecy_text,
            "confidence": round(confidence, 2),
            "timeframe": timeframe,
            "prophecy_type": prophecy_type,
            "generation_method": "algorithmic",
            "oracle_style": oracle.prophecy_style
        }
        
    def request_paradox_query(self, paradox_statement: str, query_context: Dict[str, Any]) -> Dict[str, Any]:
        """Request a specific paradox query from the most suitable oracle"""
        # Find oracle with highest paradox affinity
        best_oracle = max(self.oracles.values(), key=lambda o: o.paradox_affinity)
        
        if best_oracle.energy_level < 0.4:
            return {
                "success": False,
                "error": "No oracle has sufficient energy for paradox queries",
                "recommendation": "Wait for oracle energy to regenerate"
            }
            
        # Enhanced context for paradox queries
        paradox_context = query_context.copy()
        paradox_context["paradox_statement"] = paradox_statement
        paradox_context["paradox_complexity"] = len(paradox_statement.split()) / 10.0
        
        # Use higher energy cost for paradox queries
        consultation_result = self.consult_oracle(best_oracle.oracle_id, paradox_context, "paradox")
        
        if consultation_result.get("success"):
            # Additional paradox-specific processing
            consultation_result["paradox_resolution"] = self._analyze_paradox(paradox_statement)
            consultation_result["logical_consistency"] = random.uniform(0.3, 0.8)
            
            # Extra energy drain for paradox queries
            best_oracle.update_energy(-0.05)
            
        return consultation_result
        
    def _analyze_paradox(self, paradox_statement: str) -> Dict[str, Any]:
        """Analyze paradox statement for logical patterns"""
        # Simple paradox analysis
        contradiction_keywords = ["not", "impossible", "never", "always", "cannot", "must"]
        temporal_keywords = ["before", "after", "when", "while", "during"]
        logical_keywords = ["if", "then", "because", "therefore", "thus"]
        
        statement_lower = paradox_statement.lower()
        
        analysis = {
            "contradiction_density": sum(1 for kw in contradiction_keywords if kw in statement_lower),
            "temporal_complexity": sum(1 for kw in temporal_keywords if kw in statement_lower),
            "logical_structure": sum(1 for kw in logical_keywords if kw in statement_lower),
            "statement_length": len(paradox_statement.split()),
            "paradox_type": "temporal" if any(kw in statement_lower for kw in temporal_keywords) else "logical"
        }
        
        # Calculate paradox strength
        paradox_strength = (
            analysis["contradiction_density"] * 0.4 +
            analysis["temporal_complexity"] * 0.3 +
            analysis["logical_structure"] * 0.2 +
            min(analysis["statement_length"] / 20.0, 1.0) * 0.1
        )
        
        analysis["paradox_strength"] = round(min(1.0, paradox_strength), 2)
        
        return analysis
        
    def generate_background_prophecy(self):
        """Generate background prophecies automatically"""
        if len(self.background_prophecies) >= 10:  # Limit background prophecies
            return
            
        # Select random oracle with sufficient energy
        available_oracles = [o for o in self.oracles.values() if o.energy_level > 0.5]
        if not available_oracles:
            return
            
        oracle = random.choice(available_oracles)
        
        # Generate minimal context for background prophecy
        background_context = {
            "node_id": "background_system",
            "entropy_level": random.uniform(0.3, 0.8),
            "active_enclave": "drift_field",
            "time_salt": 0,
            "identity_fragments": 0
        }
        
        # Generate local prophecy (don't use AI for background)
        prophecy_result = self._generate_local_prophecy(oracle, background_context, "background")
        
        background_prophecy = {
            "prophecy_id": f"bg_prophecy_{len(self.background_prophecies)+1:03d}",
            "oracle_id": oracle.oracle_id,
            "oracle_name": oracle.name,
            "prophecy_text": prophecy_result["prophecy_text"],
            "confidence": prophecy_result["confidence"],
            "timeframe": prophecy_result["timeframe"],
            "prophecy_type": prophecy_result["prophecy_type"],
            "creation_time": datetime.now(timezone.utc).isoformat(),
            "is_background": True
        }
        
        self.background_prophecies.append(background_prophecy)
        
        # Minimal energy drain for background prophecies
        oracle.update_energy(-0.02)
        
    def generate_initial_prophecy(self):
        """Generate initial prophecy for new game"""
        if not self.oracles:
            return
            
        # Use the void oracle for initial prophecy
        void_oracle = self.oracles.get("void_oracle")
        if not void_oracle:
            void_oracle = list(self.oracles.values())[0]
            
        initial_context = {
            "node_id": "Xi-Void-404",
            "entropy_level": 0.5,
            "active_enclave": "initialization",
            "time_salt": 100,
            "identity_fragments": 50
        }
        
        prophecy_result = self._generate_local_prophecy(void_oracle, initial_context, "initialization")
        
        initial_prophecy = {
            "prophecy_id": "initial_prophecy",
            "oracle_id": void_oracle.oracle_id,
            "oracle_name": void_oracle.name,
            "prophecy_text": prophecy_result["prophecy_text"],
            "confidence": prophecy_result["confidence"],
            "timeframe": "initialization",
            "prophecy_type": "guidance",
            "creation_time": datetime.now(timezone.utc).isoformat(),
            "is_initial": True
        }
        
        self.active_prophecies.append(initial_prophecy)
        
    def generate_micro_prophecy(self) -> str:
        """Generate a short micro-prophecy for sentient logs"""
        micro_templates = [
            "Change whispers in the void streams...",
            "The entropy tide turns {direction}...",
            "Patterns shift in the {location}...",
            "Time echoes carry {message}...",
            "The drift reveals {revelation}..."
        ]
        
        template = random.choice(micro_templates)
        components = {
            "direction": random.choice(["inward", "outward", "sideways", "upward"]),
            "location": random.choice(["crystal caves", "temporal streams", "void nexus"]),
            "message": random.choice(["warnings", "promises", "secrets", "truths"]),
            "revelation": random.choice(["hidden paths", "lost memories", "future fragments"])
        }
        
        return template.format(**components)
        
    def get_recent_prophecies(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Get recent prophecies"""
        return self.active_prophecies[-limit:]
        
    def get_oracle_status(self, oracle_id: str) -> Optional[Dict[str, Any]]:
        """Get status of specific oracle"""
        if oracle_id not in self.oracles:
            return None
            
        oracle = self.oracles[oracle_id]
        return {
            "oracle_id": oracle_id,
            "name": oracle.name,
            "type": oracle.oracle_type,
            "prophecy_style": oracle.prophecy_style,
            "accuracy_rating": round(oracle.accuracy_rating, 3),
            "energy_level": round(oracle.energy_level, 3),
            "total_prophecies": oracle.total_prophecies,
            "consultation_cost": oracle.get_consultation_cost(),
            "personality_traits": oracle.personality_traits,
            "last_prophecy": oracle.last_prophecy_time
        }
        
    def get_all_oracles_status(self) -> List[Dict[str, Any]]:
        """Get status of all oracles"""
        return [self.get_oracle_status(oid) for oid in self.oracles.keys()]
        
    def regenerate_oracle_energy(self):
        """Regenerate energy for all oracles (called periodically)"""
        for oracle in self.oracles.values():
            oracle.update_energy(0.05)  # Slow energy regeneration
            
    def export_state(self) -> Dict[str, Any]:
        """Export oracle system state"""
        return {
            "total_consultations": self.total_consultations,
            "system_energy": self.system_energy,
            "paradox_resonance": self.paradox_resonance,
            "temporal_clarity": self.temporal_clarity,
            "prophecy_history": self.prophecy_history.copy(),
            "active_prophecies": self.active_prophecies.copy(),
            "background_prophecies": self.background_prophecies.copy(),
            "oracle_states": {
                oid: {
                    "energy_level": oracle.energy_level,
                    "total_prophecies": oracle.total_prophecies,
                    "successful_predictions": oracle.successful_predictions,
                    "consultation_count": oracle.consultation_count,
                    "accuracy_rating": oracle.accuracy_rating
                }
                for oid, oracle in self.oracles.items()
            }
        }
        
    def import_state(self, state_data: Dict[str, Any]):
        """Import oracle system state"""
        self.total_consultations = state_data.get("total_consultations", 0)
        self.system_energy = state_data.get("system_energy", 1.0)
        self.paradox_resonance = state_data.get("paradox_resonance", 0.5)
        self.temporal_clarity = state_data.get("temporal_clarity", 0.7)
        self.prophecy_history = state_data.get("prophecy_history", [])
        self.active_prophecies = state_data.get("active_prophecies", [])
        self.background_prophecies = state_data.get("background_prophecies", [])
        
        # Restore oracle states
        oracle_states = state_data.get("oracle_states", {})
        for oracle_id, oracle_state in oracle_states.items():
            if oracle_id in self.oracles:
                oracle = self.oracles[oracle_id]
                oracle.energy_level = oracle_state.get("energy_level", 0.8)
                oracle.total_prophecies = oracle_state.get("total_prophecies", 0)
                oracle.successful_predictions = oracle_state.get("successful_predictions", 0)
                oracle.consultation_count = oracle_state.get("consultation_count", 0)
                oracle.accuracy_rating = oracle_state.get("accuracy_rating", oracle.accuracy_rating)
