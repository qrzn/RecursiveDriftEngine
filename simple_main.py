"""
Recursive Drift Engine: Terminal Interface
A mystical simulation system with comprehensive features
"""

import time
import json
import random
from datetime import datetime
from narrative_engine import NarrativeEngine

# Core glyphs for the drift field
GLYPHS = ["▲", "⊗", "≈", "∇", "∆"]

class SimpleDriftEngine:
    """Simplified drift engine for terminal interface"""
    
    def __init__(self):
        self.node_id = "Xi-Void-404"
        self.entropy_level = 0.5
        self.time_salt = 100
        self.identity_fragments = 50
        self.fork_count = 0
        self.total_operations = 0
        
        # System state
        self.current_drift_map = self.generate_drift_map()
        self.active_enclaves = ["Void Nexus", "Entropy Gardens", "Crystal Sanctum"]
        self.current_enclave = "Void Nexus"
        
        # Game history
        self.operation_log = []
        
        # Narrative engine for procedural storytelling
        self.narrative_engine = NarrativeEngine()
        
    def generate_drift_map(self, width=5, height=5):
        """Generate a mystical drift field map"""
        drift_map = []
        for y in range(height):
            row = []
            for x in range(width):
                # Add entropy influence to glyph selection
                if random.random() < self.entropy_level:
                    glyph = random.choice(GLYPHS)
                else:
                    glyph = random.choice(GLYPHS[:3])  # More stable glyphs
                row.append(glyph)
            drift_map.append(row)
        return drift_map
    
    def fork_node(self):
        """Create a forked node in the drift field"""
        fork_id = f"{self.node_id}-{random.randint(1000, 9999)}"
        
        # Calculate fork effects
        entropy_change = random.uniform(0.05, 0.15)
        self.entropy_level = min(1.0, self.entropy_level + entropy_change)
        
        # Generate rewards
        salt_reward = random.randint(2, 8)
        fragment_reward = random.randint(1, 5)
        
        self.time_salt += salt_reward
        self.identity_fragments += fragment_reward
        self.fork_count += 1
        self.total_operations += 1
        
        # Log the operation
        operation = {
            "type": "fork",
            "node_id": fork_id,
            "entropy_change": round(entropy_change, 3),
            "entropy_level": self.entropy_level,
            "rewards": {"time_salt": salt_reward, "fragments": fragment_reward},
            "timestamp": datetime.now().isoformat()
        }
        self.operation_log.append(operation)
        
        # Generate narrative
        narrative_result = self.narrative_engine.process_action(operation, self.get_status())
        operation["narrative"] = narrative_result
        
        return operation
    
    def collapse_node(self):
        """Collapse a node in the drift field"""
        # Calculate collapse effects
        entropy_reduction = random.uniform(0.1, 0.2)
        self.entropy_level = max(0.0, self.entropy_level - entropy_reduction)
        
        # Generate resources
        salt_reward = random.randint(3, 10)
        fragment_reward = random.randint(2, 6)
        
        self.time_salt += salt_reward
        self.identity_fragments += fragment_reward
        self.total_operations += 1
        
        # Log the operation
        operation = {
            "type": "collapse",
            "node_id": self.node_id,
            "entropy_reduction": round(entropy_reduction, 3),
            "entropy_level": self.entropy_level,
            "rewards": {"time_salt": salt_reward, "fragments": fragment_reward},
            "timestamp": datetime.now().isoformat()
        }
        self.operation_log.append(operation)
        
        # Generate narrative
        narrative_result = self.narrative_engine.process_action(operation, self.get_status())
        operation["narrative"] = narrative_result
        
        return operation
    
    def memory_wipe(self):
        """Perform a memory wipe operation"""
        # Clear some history but generate significant rewards
        wiped_operations = len(self.operation_log)
        self.operation_log = []
        
        # Reset entropy to neutral
        old_entropy = self.entropy_level
        self.entropy_level = 0.5
        
        # Generate major rewards
        salt_reward = wiped_operations * 3
        fragment_reward = wiped_operations * 2
        
        self.time_salt += salt_reward
        self.identity_fragments += fragment_reward
        self.total_operations += 1
        
        operation = {
            "type": "memory_wipe",
            "node_id": self.node_id,
            "operations_wiped": wiped_operations,
            "entropy_reset": round(old_entropy - 0.5, 3),
            "entropy_level": self.entropy_level,
            "rewards": {"time_salt": salt_reward, "fragments": fragment_reward},
            "timestamp": datetime.now().isoformat()
        }
        
        # Generate narrative (this will create a new timeline)
        narrative_result = self.narrative_engine.process_action(operation, self.get_status())
        operation["narrative"] = narrative_result
        
        return operation
    
    def scan_field(self):
        """Scan the current drift field"""
        self.current_drift_map = self.generate_drift_map()
        self.total_operations += 1
        
        # Small entropy fluctuation from scanning
        entropy_change = random.uniform(-0.02, 0.02)
        self.entropy_level = max(0.0, min(1.0, self.entropy_level + entropy_change))
        
        return {
            "type": "scan",
            "drift_map": self.current_drift_map,
            "entropy_change": round(entropy_change, 3),
            "timestamp": datetime.now().isoformat()
        }
    
    def change_enclave(self, enclave_name):
        """Change to a different enclave"""
        if enclave_name in self.active_enclaves:
            old_enclave = self.current_enclave
            self.current_enclave = enclave_name
            
            # Each enclave has different entropy effects
            enclave_effects = {
                "Void Nexus": random.uniform(-0.1, 0.1),
                "Entropy Gardens": random.uniform(0.0, 0.2),
                "Crystal Sanctum": random.uniform(-0.15, 0.05)
            }
            
            entropy_change = enclave_effects.get(enclave_name, 0.0)
            self.entropy_level = max(0.0, min(1.0, self.entropy_level + entropy_change))
            
            return {
                "type": "enclave_change",
                "from": old_enclave,
                "to": enclave_name,
                "entropy_effect": round(entropy_change, 3),
                "timestamp": datetime.now().isoformat()
            }
        else:
            return {"error": f"Enclave '{enclave_name}' not available"}
    
    def get_status(self):
        """Get current system status"""
        return {
            "node_id": self.node_id,
            "entropy_level": round(self.entropy_level, 3),
            "time_salt": self.time_salt,
            "identity_fragments": self.identity_fragments,
            "current_enclave": self.current_enclave,
            "fork_count": self.fork_count,
            "total_operations": self.total_operations,
            "operation_history": len(self.operation_log)
        }

def display_drift_map(drift_map):
    """Display the drift field map"""
    print("\n📍 Current Drift Field:")
    print("┌" + "─" * 15 + "┐")
    for row in drift_map:
        print("│ " + " ".join(row) + " │")
    print("└" + "─" * 15 + "┘")

def display_status(engine):
    """Display system status"""
    status = engine.get_status()
    print(f"""
🌌 Recursive Drift Engine Status
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Node ID: {status['node_id']}
Current Enclave: {status['current_enclave']}
Entropy Level: {status['entropy_level']} {'🔥' if status['entropy_level'] > 0.7 else '❄️' if status['entropy_level'] < 0.3 else '⚡'}
⧗ Time Salt: {status['time_salt']}
◊ Identity Fragments: {status['identity_fragments']}
Total Operations: {status['total_operations']}
Fork Count: {status['fork_count']}
""")

def show_help():
    """Display help information"""
    print("""
🔮 Recursive Drift Engine Commands
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
scan     - Scan the drift field for new patterns
fork     - Create a forked node (increases entropy)
collapse - Collapse a node (decreases entropy, more rewards)
wipe     - Memory wipe (resets entropy, major rewards)
enclave  - Change enclave (void/entropy/crystal)
status   - Show current system status
prophecy - Generate a mystical prophecy
story    - View recent narrative threads
timeline - Show timeline information
help     - Show this help message
quit     - Exit the drift field
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

def generate_prophecy(engine):
    """Generate a mystical prophecy based on current state"""
    status = engine.get_status()
    entropy = status['entropy_level']
    
    # Prophecy templates based on entropy level
    if entropy > 0.8:
        prophecies = [
            "The void whispers of chaotic tides approaching the nexus...",
            "Reality fractures at the edges - beware the entropy storm...",
            "The drift field pulses with unstable energy - collapse may bring peace...",
            f"In the {status['current_enclave']}, {random.choice(GLYPHS)} shall manifest when time fragments..."
        ]
    elif entropy < 0.2:
        prophecies = [
            "Crystalline silence spreads through the temporal streams...",
            "The void grows still - new mysteries await in the depths...",
            "Stability brings clarity, but growth requires gentle chaos...",
            f"Within the {status['current_enclave']}, {random.choice(GLYPHS)} holds the key to transformation..."
        ]
    else:
        prophecies = [
            "Balance dances between order and chaos in the drift...",
            "The entropy flows seek their destined pattern...",
            "Fork and collapse interweave the fabric of possibility...",
            f"The {status['current_enclave']} resonates with {random.choice(GLYPHS)} energy..."
        ]
    
    prophecy = random.choice(prophecies)
    confidence = random.uniform(0.6, 0.9)
    
    print(f"""
🔮 Oracle Prophecy
━━━━━━━━━━━━━━━━━━
"{prophecy}"

Confidence: {confidence:.1%}
Temporal Range: {random.choice(['immediate', 'near future', 'distant echoes'])}
━━━━━━━━━━━━━━━━━━
""")

def show_recent_story(engine):
    """Display recent narrative threads"""
    if not engine.narrative_engine.timelines:
        print("\n📖 No narrative threads yet. Perform some actions to begin your story.")
        return
        
    current_timeline = list(engine.narrative_engine.timelines.keys())[-1]
    timeline = engine.narrative_engine.timelines[current_timeline]
    
    print(f"""
📖 Recent Narrative Threads ({current_timeline})
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Narrative Tone: {timeline.narrative_tone}
Dominant Themes: {', '.join(timeline.dominant_themes)}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
    
    recent_threads = engine.narrative_engine.get_recent_narrative(current_timeline, 3)
    for i, thread in enumerate(recent_threads, 1):
        print(f"{i}. {thread['story_fragment']}")
        print(f"   Themes: {', '.join(thread['themes'])}")
        print()
        
    # Show character events if any
    if timeline.character_entities:
        print("🎭 Active Characters:")
        for char_id, char_data in list(timeline.character_entities.items())[-2:]:
            print(f"   • {char_data['character_type'].replace('_', ' ').title()}: {char_data['character_data']['description']}")
        print()

def show_timeline_info(engine):
    """Display timeline information"""
    if not engine.narrative_engine.timelines:
        print("\n⏳ No timelines created yet.")
        return
        
    print(f"""
⏳ Timeline Overview
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total Timelines: {len(engine.narrative_engine.timelines)}
Cross-Timeline Events: {len(engine.narrative_engine.cross_timeline_events)}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
    
    for timeline_id in engine.narrative_engine.timelines:
        summary = engine.narrative_engine.get_timeline_summary(timeline_id)
        print(f"""Timeline: {timeline_id}
   Tone: {summary['narrative_tone']}
   Themes: {', '.join(summary['dominant_themes'][:3])}
   Story Threads: {summary['thread_count']}
   Characters: {summary['character_count']}
""")
        
    # Show recent cross-timeline events
    if engine.narrative_engine.cross_timeline_events:
        recent_cross = engine.narrative_engine.cross_timeline_events[-1]
        print(f"🌀 Latest Cross-Timeline Event:")
        print(f"   {recent_cross['event_data']['description']}")
        print()

def display_narrative_result(result):
    """Display narrative results from actions"""
    if "narrative" not in result:
        return
        
    narrative = result["narrative"]
    
    print(f"""
📜 {narrative['narrative_fragment']}
   Timeline: {narrative['timeline_id']} ({narrative['narrative_tone']})""")
    
    if "character_event" in narrative:
        char_event = narrative["character_event"]
        print(f"""
🎭 Character Emergence!
   {char_event['character_type'].replace('_', ' ').title()}: {char_event['character_description']}
   
   {char_event['emergence_story']}""")
        
    if "cross_timeline_event" in narrative:
        cross_event = narrative["cross_timeline_event"]
        if cross_event["type"] != "no_cross_event":
            print(f"""
🌀 Cross-Timeline Event!
   {cross_event['description']}""")

def main():
    """Main application loop"""
    print("""
╔══════════════════════════════════════════════════════════════╗
║                    RECURSIVE DRIFT ENGINE                    ║
║                   Mystical Simulation v2.0                  ║
╚══════════════════════════════════════════════════════════════╝

🌌 Entering the drift field...
""")
    
    # Initialize the engine
    engine = SimpleDriftEngine()
    
    # Display initial status
    display_status(engine)
    display_drift_map(engine.current_drift_map)
    
    print("\nType 'help' for available commands")
    
    # Main interaction loop
    while True:
        try:
            command = input("\n🔮 drift> ").strip().lower()
            
            if command == "quit" or command == "exit":
                print("\n🌌 Exiting the drift field... Reality stabilizes.\n")
                break
                
            elif command == "help":
                show_help()
                
            elif command == "scan":
                result = engine.scan_field()
                print(f"\n⚡ Field scan complete! Entropy shift: {result['entropy_change']:+.3f}")
                display_drift_map(result['drift_map'])
                
            elif command == "fork":
                result = engine.fork_node()
                print(f"""
⚡ Node forked: {result.get('node_id', 'unknown')}
   Entropy increase: +{result['entropy_change']:.3f}
   Rewards: ⧗{result['rewards']['time_salt']} ◊{result['rewards']['fragments']}""")
                display_narrative_result(result)
                
            elif command == "collapse":
                result = engine.collapse_node()
                print(f"""
💥 Node collapsed successfully!
   Entropy reduction: -{result['entropy_reduction']:.3f}
   Rewards: ⧗{result['rewards']['time_salt']} ◊{result['rewards']['fragments']}""")
                display_narrative_result(result)
                
            elif command == "wipe":
                result = engine.memory_wipe()
                print(f"""
🌀 Memory wipe completed!
   Operations cleared: {result['operations_wiped']}
   Entropy reset: {result['entropy_reset']:+.3f}
   Major rewards: ⧗{result['rewards']['time_salt']} ◊{result['rewards']['fragments']}""")
                display_narrative_result(result)
                
            elif command == "status":
                display_status(engine)
                
            elif command == "prophecy":
                generate_prophecy(engine)
                
            elif command == "story":
                show_recent_story(engine)
                
            elif command == "timeline":
                show_timeline_info(engine)
                
            elif command.startswith("enclave"):
                parts = command.split()
                if len(parts) > 1:
                    enclave_map = {
                        "void": "Void Nexus",
                        "entropy": "Entropy Gardens", 
                        "crystal": "Crystal Sanctum"
                    }
                    enclave_choice = enclave_map.get(parts[1])
                    if enclave_choice:
                        result = engine.change_enclave(enclave_choice)
                        if "error" not in result:
                            print(f"""
🏛 Enclave transition complete!
   From: {result['from']} → To: {result['to']}
   Entropy effect: {result['entropy_effect']:+.3f}""")
                        else:
                            print(f"❌ {result['error']}")
                    else:
                        print("❌ Available enclaves: void, entropy, crystal")
                else:
                    print("❌ Usage: enclave <void|entropy|crystal>")
                    
            elif command == "":
                continue
                
            else:
                print(f"❌ Unknown command: {command}")
                print("   Type 'help' for available commands")
                
        except KeyboardInterrupt:
            print("\n\n🌌 Drift field interrupted. Exiting...\n")
            break
        except Exception as e:
            print(f"❌ Error in drift field: {e}")

if __name__ == "__main__":
    main()