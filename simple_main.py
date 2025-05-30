"""
Recursive Drift Engine: Terminal Interface
A mystical simulation system with comprehensive features
"""

import time
import json
import random
from datetime import datetime

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
            "fork_id": fork_id,
            "entropy_change": round(entropy_change, 3),
            "rewards": {"time_salt": salt_reward, "fragments": fragment_reward},
            "timestamp": datetime.now().isoformat()
        }
        self.operation_log.append(operation)
        
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
            "entropy_reduction": round(entropy_reduction, 3),
            "rewards": {"time_salt": salt_reward, "fragments": fragment_reward},
            "timestamp": datetime.now().isoformat()
        }
        self.operation_log.append(operation)
        
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
        
        return {
            "type": "memory_wipe",
            "operations_wiped": wiped_operations,
            "entropy_reset": round(old_entropy - 0.5, 3),
            "rewards": {"time_salt": salt_reward, "fragments": fragment_reward},
            "timestamp": datetime.now().isoformat()
        }
    
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
⚡ Node forked: {result['fork_id']}
   Entropy increase: +{result['entropy_change']:.3f}
   Rewards: ⧗{result['rewards']['time_salt']} ◊{result['rewards']['fragments']}""")
                
            elif command == "collapse":
                result = engine.collapse_node()
                print(f"""
💥 Node collapsed successfully!
   Entropy reduction: -{result['entropy_reduction']:.3f}
   Rewards: ⧗{result['rewards']['time_salt']} ◊{result['rewards']['fragments']}""")
                
            elif command == "wipe":
                result = engine.memory_wipe()
                print(f"""
🌀 Memory wipe completed!
   Operations cleared: {result['operations_wiped']}
   Entropy reset: {result['entropy_reset']:+.3f}
   Major rewards: ⧗{result['rewards']['time_salt']} ◊{result['rewards']['fragments']}""")
                
            elif command == "status":
                display_status(engine)
                
            elif command == "prophecy":
                generate_prophecy(engine)
                
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