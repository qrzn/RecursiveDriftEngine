"""
Procedural Narrative Engine: Timeline Story Generation
Creates evolving stories based on player actions across multiple timelines
"""

import random
import json
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional

class TimelineNarrative:
    """Individual timeline with its own narrative thread"""
    
    def __init__(self, timeline_id: str, origin_event: Dict[str, Any]):
        self.timeline_id = timeline_id
        self.origin_event = origin_event
        self.narrative_threads = []
        self.character_entities = {}
        self.location_memories = {}
        self.entropy_history = []
        self.major_events = []
        
        # Narrative properties
        self.narrative_tone = random.choice(["mystical", "ominous", "hopeful", "chaotic", "ancient"])
        self.dominant_themes = random.sample([
            "identity_fragmentation", "temporal_recursion", "void_emergence", 
            "crystal_resonance", "entropy_cascade", "memory_echo"
        ], k=random.randint(2, 4))
        
        # Generate initial narrative
        self.generate_origin_story()
        
    def generate_origin_story(self):
        """Generate the origin story for this timeline"""
        event_type = self.origin_event.get("type", "unknown")
        
        origin_templates = {
            "fork": [
                "In the moment of forking, reality split like crystal under pressure. A new thread of existence emerged from the quantum foam, carrying echoes of what was and whispers of what might be.",
                "The void trembled as consciousness divided itself. Where once there was one path, now two timelines stretched into infinity, each bearing the weight of different choices.",
                "A fork in the river of time created ripples that would reshape the very fabric of the drift field. The {node_id} became a nexus point between parallel possibilities."
            ],
            "collapse": [
                "As the node collapsed, time folded inward like a dying star. The implosion created a gravitational well in the timeline, drawing fragments of scattered realities into its core.",
                "The collapse sent shockwaves through the temporal substrate. What was destroyed in one moment became the foundation for entirely new forms of existence.",
                "In the aftermath of the great collapse, silence descended upon the drift field. But within that silence, new stories began to write themselves."
            ],
            "memory_wipe": [
                "The great forgetting began not with violence, but with a whisper. Memories dissolved like salt in an infinite ocean, leaving only the faint taste of what once was.",
                "When the memory wipe completed its work, the timeline found itself reborn. Past and future became fluid concepts, reality a canvas waiting for new experiences to paint upon it.",
                "The erasure created a void that nature abhors. Into this emptiness flowed new possibilities, each more strange and wonderful than the last."
            ]
        }
        
        templates = origin_templates.get(event_type, origin_templates["fork"])
        template = random.choice(templates)
        
        origin_story = template.format(
            node_id=self.origin_event.get("node_id", "the nexus"),
            entropy=self.origin_event.get("entropy_level", 0.5)
        )
        
        self.narrative_threads.append({
            "thread_id": "origin",
            "story_fragment": origin_story,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "themes": ["origin", "beginning"],
            "entropy_level": self.origin_event.get("entropy_level", 0.5)
        })

class NarrativeEngine:
    """Main engine for procedural narrative generation"""
    
    def __init__(self):
        self.timelines = {}
        self.narrative_history = []
        self.recurring_characters = {}
        self.cross_timeline_events = []
        
        # Narrative configuration
        self.story_complexity = 0.7
        self.character_emergence_chance = 0.15
        self.cross_timeline_chance = 0.1
        self.memory_persistence = 0.8
        
        # Story elements library
        self.character_archetypes = {
            "void_walker": {
                "description": "A figure that moves between emptiness and form",
                "themes": ["void", "identity", "transformation"],
                "personality": ["enigmatic", "patient", "profound"]
            },
            "entropy_sage": {
                "description": "An ancient consciousness that understands chaos",
                "themes": ["chaos", "wisdom", "prediction"],
                "personality": ["wise", "cryptic", "knowing"]
            },
            "crystal_guardian": {
                "description": "A crystalline entity that preserves memories",
                "themes": ["memory", "preservation", "structure"],
                "personality": ["protective", "methodical", "eternal"]
            },
            "time_weaver": {
                "description": "A being that manipulates temporal threads",
                "themes": ["time", "causality", "connection"],
                "personality": ["complex", "manipulative", "caring"]
            },
            "fragment_collector": {
                "description": "An entity that gathers scattered pieces of identity",
                "themes": ["identity", "collection", "completion"],
                "personality": ["obsessive", "helpful", "mysterious"]
            }
        }
        
    def process_action(self, action_data: Dict[str, Any], current_state: Dict[str, Any]) -> Dict[str, Any]:
        """Process a player action and generate narrative content"""
        action_type = action_data.get("type", "unknown")
        timeline_id = self.get_or_create_timeline(action_data, current_state)
        
        # Generate narrative for this action
        narrative_fragment = self.generate_action_narrative(action_data, current_state, timeline_id)
        
        # Check for character emergence
        character_event = None
        if random.random() < self.character_emergence_chance:
            character_event = self.trigger_character_emergence(action_data, current_state, timeline_id)
            
        # Check for cross-timeline events
        cross_event = None
        if len(self.timelines) > 1 and random.random() < self.cross_timeline_chance:
            cross_event = self.trigger_cross_timeline_event(action_data, timeline_id)
            
        # Update timeline
        timeline = self.timelines[timeline_id]
        timeline.narrative_threads.append({
            "thread_id": f"action_{len(timeline.narrative_threads)}",
            "story_fragment": narrative_fragment,
            "action_data": action_data.copy(),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "themes": self.extract_themes_from_action(action_data),
            "entropy_level": current_state.get("entropy_level", 0.5)
        })
        
        # Record entropy history
        timeline.entropy_history.append({
            "level": current_state.get("entropy_level", 0.5),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "action": action_type
        })
        
        result = {
            "timeline_id": timeline_id,
            "narrative_fragment": narrative_fragment,
            "narrative_tone": timeline.narrative_tone,
            "active_themes": timeline.dominant_themes
        }
        
        if character_event:
            result["character_event"] = character_event
            
        if cross_event:
            result["cross_timeline_event"] = cross_event
            
        return result
        
    def get_or_create_timeline(self, action_data: Dict[str, Any], current_state: Dict[str, Any]) -> str:
        """Get existing timeline or create new one based on action"""
        
        # For memory wipes, always create new timeline
        if action_data.get("type") == "memory_wipe":
            timeline_id = f"timeline_{len(self.timelines) + 1:03d}"
            self.timelines[timeline_id] = TimelineNarrative(timeline_id, action_data)
            return timeline_id
            
        # For major entropy shifts, chance to create new timeline
        entropy_level = current_state.get("entropy_level", 0.5)
        if (entropy_level > 0.9 or entropy_level < 0.1) and random.random() < 0.3:
            timeline_id = f"timeline_{len(self.timelines) + 1:03d}"
            self.timelines[timeline_id] = TimelineNarrative(timeline_id, action_data)
            return timeline_id
            
        # Otherwise, use most recent timeline or create first one
        if not self.timelines:
            timeline_id = "timeline_001"
            self.timelines[timeline_id] = TimelineNarrative(timeline_id, action_data)
            return timeline_id
        else:
            return list(self.timelines.keys())[-1]
            
    def generate_action_narrative(self, action_data: Dict[str, Any], current_state: Dict[str, Any], timeline_id: str) -> str:
        """Generate narrative text for a specific action"""
        action_type = action_data.get("type", "unknown")
        entropy_level = current_state.get("entropy_level", 0.5)
        timeline = self.timelines[timeline_id]
        
        # Base narrative templates
        narrative_templates = {
            "fork": {
                "low_entropy": [
                    "In the crystalline silence of the {enclave}, a gentle bifurcation occurred. Reality quietly split along predetermined lines, creating new possibilities without disturbing the cosmic order.",
                    "The forking manifested as a whisper in the void. Where stability reigned, a new branch of existence grew like a crystal formation, precise and inevitable."
                ],
                "high_entropy": [
                    "Chaos erupted as the node violently split apart! The {enclave} trembled with the force of uncontrolled forking, reality fracturing into jagged, unpredictable shards.",
                    "The fork tore through the fabric of space-time like lightning through storm clouds. Wild energies cascaded across the {enclave}, leaving reality scarred but transformed."
                ],
                "balanced": [
                    "At the nexus point in {enclave}, existence chose its path. The fork created a harmonious divergence, neither chaotic nor rigid, but perfectly balanced between order and possibility.",
                    "The bifurcation unfolded like a flower blooming in reverse time. In {enclave}, one became two, and the universe held its breath at the beauty of the transformation."
                ]
            },
            "collapse": {
                "low_entropy": [
                    "The collapse was a meditation on impermanence. In the {enclave}, matter folded inward with serene inevitability, leaving behind only pure potential and crystallized memory.",
                    "Like a tide returning to the ocean, the node dissolved back into the fundamental substrate. The {enclave} witnessed this peaceful return to the source."
                ],
                "high_entropy": [
                    "The collapse was violent and spectacular! Reality imploded with tremendous force, sending shockwaves through {enclave} as raw chaos consumed ordered matter.",
                    "In a cataclysmic display, the node destroyed itself in magnificent fury. The {enclave} shook as matter and energy returned to the primal chaos from whence they came."
                ],
                "balanced": [
                    "The collapse proceeded with dignified grace. In {enclave}, the node chose its moment of dissolution, neither resisting nor rushing toward its transformation.",
                    "Balance guided the collapse, each moment perfectly orchestrated. The {enclave} bore witness to matter choosing its own path back to the void."
                ]
            },
            "scan": {
                "low_entropy": [
                    "The scanning revealed intricate patterns of crystalline perfection across the {enclave}. Each glyph held its position with mathematical precision, creating a mandala of ordered beauty.",
                    "Consciousness swept across the {enclave} like morning light over still water. The drift field responded with gentle luminescence, revealing its hidden geometries."
                ],
                "high_entropy": [
                    "The scan pierced through swirling chaos in the {enclave}! Glyphs flickered and danced in wild patterns, each moment bringing new configurations of beautiful disorder.",
                    "Awareness struggled to map the turbulent energies of {enclave}. The drift field writhed and shifted, a living tapestry of ever-changing possibilities."
                ],
                "balanced": [
                    "The scan revealed the {enclave} in a state of dynamic equilibrium. Glyphs pulsed with gentle rhythms, neither static nor chaotic, but alive with purposeful motion.",
                    "Perception flowed across {enclave} like a gentle breeze. The drift field responded with subtle shifts, revealing both structure and spontaneity in perfect harmony."
                ]
            },
            "memory_wipe": [
                "The great forgetting began... In {enclave}, time itself seemed to hold its breath as countless stories dissolved into the quantum foam. What remained was not emptiness, but infinite potential.",
                "Memory fragments scattered like stars going supernova across {enclave}. Each forgotten moment became a seed for new realities, new stories waiting to be born.",
                "The erasure was complete yet gentle, like snow covering an ancient landscape. In {enclave}, the past became a blank canvas upon which the future could paint its dreams."
            ]
        }
        
        # Select appropriate template based on entropy level
        if action_type in narrative_templates:
            if action_type == "memory_wipe":
                template = random.choice(narrative_templates[action_type])
            else:
                if entropy_level < 0.3:
                    template = random.choice(narrative_templates[action_type]["low_entropy"])
                elif entropy_level > 0.7:
                    template = random.choice(narrative_templates[action_type]["high_entropy"])
                else:
                    template = random.choice(narrative_templates[action_type]["balanced"])
        else:
            template = "In the {enclave}, something profound occurred. The very fabric of reality shifted in response to forces beyond comprehension."
            
        # Fill in template variables
        enclave = current_state.get("current_enclave", "drift nexus")
        narrative = template.format(enclave=enclave)
        
        # Add theme-specific embellishments
        if "void" in timeline.dominant_themes:
            narrative += " The void whispered approval of this transformation."
        elif "crystal" in timeline.dominant_themes:
            narrative += " Crystalline resonances sang in harmony with the change."
        elif "chaos" in timeline.dominant_themes:
            narrative += " Chaotic energies danced in celebration of the disruption."
            
        return narrative
        
    def trigger_character_emergence(self, action_data: Dict[str, Any], current_state: Dict[str, Any], timeline_id: str) -> Dict[str, Any]:
        """Trigger the emergence of a narrative character"""
        timeline = self.timelines[timeline_id]
        
        # Select character archetype based on action and entropy
        action_type = action_data.get("type", "unknown")
        entropy_level = current_state.get("entropy_level", 0.5)
        
        character_selection_weights = {
            "void_walker": 0.2 + (0.3 if "void" in timeline.dominant_themes else 0),
            "entropy_sage": 0.1 + (0.4 if entropy_level > 0.7 else 0),
            "crystal_guardian": 0.2 + (0.3 if entropy_level < 0.3 else 0),
            "time_weaver": 0.15 + (0.3 if action_type in ["fork", "memory_wipe"] else 0),
            "fragment_collector": 0.1 + (0.3 if action_type == "collapse" else 0)
        }
        
        # Select character weighted by preferences
        character_type = random.choices(
            list(character_selection_weights.keys()),
            weights=list(character_selection_weights.values())
        )[0]
        
        character_data = self.character_archetypes[character_type].copy()
        character_id = f"{character_type}_{timeline_id}_{len(timeline.character_entities):02d}"
        
        # Generate character emergence story
        emergence_stories = {
            "void_walker": [
                "From the emptiness between thoughts, a figure materialized. The Void Walker stepped through dimensions as easily as walking through mist.",
                "Reality parted like curtains as the Void Walker emerged from the spaces that exist between existence."
            ],
            "entropy_sage": [
                "Ancient eyes opened in the swirling chaos. The Entropy Sage had been watching, waiting for this moment of perfect disorder.",
                "From the heart of the storm came wisdom incarnate. The Entropy Sage spoke in languages older than time itself."
            ],
            "crystal_guardian": [
                "Light refracted through crystalline form as the Guardian awakened. Memories of countless ages glittered in its faceted consciousness.",
                "The Crystal Guardian rose from the geometric depths, each surface reflecting different moments in time."
            ],
            "time_weaver": [
                "Temporal threads gathered and twisted into the shape of consciousness. The Time Weaver materialized from the very fabric of causality.",
                "Past and future converged to birth the Time Weaver, whose very presence made time itself more malleable."
            ],
            "fragment_collector": [
                "Scattered pieces of identity swirled together, forming the Fragment Collector. Each gathered piece made the entity more complete.",
                "The Collector emerged from the accumulation of lost memories, drawn to this moment by an irresistible compulsion."
            ]
        }
        
        emergence_story = random.choice(emergence_stories[character_type])
        
        # Store character in timeline
        timeline.character_entities[character_id] = {
            "character_type": character_type,
            "character_data": character_data,
            "emergence_story": emergence_story,
            "emergence_action": action_data.copy(),
            "timeline_id": timeline_id,
            "interaction_count": 0,
            "last_seen": datetime.now(timezone.utc).isoformat()
        }
        
        return {
            "character_id": character_id,
            "character_type": character_type,
            "emergence_story": emergence_story,
            "character_description": character_data["description"],
            "character_themes": character_data["themes"]
        }
        
    def trigger_cross_timeline_event(self, action_data: Dict[str, Any], current_timeline_id: str) -> Dict[str, Any]:
        """Trigger an event that affects multiple timelines"""
        other_timelines = [tid for tid in self.timelines.keys() if tid != current_timeline_id]
        if not other_timelines:
            return {
                "type": "no_cross_event",
                "description": "No other timelines available for cross-dimensional effects.",
                "effect": "isolation"
            }
            
        affected_timeline = random.choice(other_timelines)
        
        cross_events = [
            {
                "type": "memory_bleed",
                "description": f"Memories from {affected_timeline} began bleeding through into {current_timeline_id}. Past and present intermingled like colors in water.",
                "effect": "temporal_confusion"
            },
            {
                "type": "echo_resonance", 
                "description": f"An echo of actions in {current_timeline_id} resonated across dimensional barriers, causing ripples in {affected_timeline}.",
                "effect": "cross_dimensional_influence"
            },
            {
                "type": "character_migration",
                "description": f"A consciousness from {affected_timeline} sensed the disturbance and began moving toward {current_timeline_id}.",
                "effect": "entity_transfer"
            },
            {
                "type": "convergence_point",
                "description": f"The actions in {current_timeline_id} created a convergence point where {affected_timeline} briefly touched this reality.",
                "effect": "temporary_merger"
            }
        ]
        
        cross_event = random.choice(cross_events)
        
        # Record the cross-timeline event
        self.cross_timeline_events.append({
            "event_data": cross_event,
            "source_timeline": current_timeline_id,
            "affected_timeline": affected_timeline,
            "trigger_action": action_data.copy(),
            "timestamp": datetime.now(timezone.utc).isoformat()
        })
        
        return cross_event
        
    def extract_themes_from_action(self, action_data: Dict[str, Any]) -> List[str]:
        """Extract narrative themes from an action"""
        action_type = action_data.get("type", "unknown")
        
        theme_mappings = {
            "fork": ["divergence", "choice", "multiplication"],
            "collapse": ["convergence", "destruction", "transformation"],
            "scan": ["observation", "revelation", "awareness"],
            "memory_wipe": ["forgetting", "renewal", "erasure"],
            "enclave_change": ["travel", "transition", "exploration"]
        }
        
        return theme_mappings.get(action_type, ["mystery"])
        
    def get_timeline_summary(self, timeline_id: str) -> Dict[str, Any]:
        """Get a summary of a specific timeline's narrative"""
        if timeline_id not in self.timelines:
            return {"error": "Timeline not found"}
            
        timeline = self.timelines[timeline_id]
        
        return {
            "timeline_id": timeline_id,
            "narrative_tone": timeline.narrative_tone,
            "dominant_themes": timeline.dominant_themes,
            "thread_count": len(timeline.narrative_threads),
            "character_count": len(timeline.character_entities),
            "major_events": len(timeline.major_events),
            "entropy_progression": [
                {"level": h["level"], "action": h["action"]} 
                for h in timeline.entropy_history[-5:]  # Last 5 events
            ]
        }
        
    def get_recent_narrative(self, timeline_id: str, count: int = 3) -> List[Dict[str, Any]]:
        """Get recent narrative fragments from a timeline"""
        if timeline_id not in self.timelines:
            return []
            
        timeline = self.timelines[timeline_id]
        recent_threads = timeline.narrative_threads[-count:]
        
        return [
            {
                "story_fragment": thread["story_fragment"],
                "themes": thread["themes"],
                "timestamp": thread["timestamp"]
            }
            for thread in recent_threads
        ]
        
    def export_narrative_state(self) -> Dict[str, Any]:
        """Export the complete narrative state"""
        return {
            "timelines": {
                tid: {
                    "narrative_tone": timeline.narrative_tone,
                    "dominant_themes": timeline.dominant_themes,
                    "thread_count": len(timeline.narrative_threads),
                    "character_count": len(timeline.character_entities),
                    "entropy_history": timeline.entropy_history
                }
                for tid, timeline in self.timelines.items()
            },
            "cross_timeline_events": self.cross_timeline_events,
            "total_narrative_threads": sum(len(t.narrative_threads) for t in self.timelines.values())
        }