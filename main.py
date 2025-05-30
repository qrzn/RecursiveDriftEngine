"""
Recursive Drift Engine: Main Application Entry Point
Enhanced Mystical Simulation with Comprehensive Features
"""

import threading
import os
import sys
import time
import json
from datetime import datetime

# Import custom modules
from drift_engine import DriftEngine
from persistence import GameState

class RecursiveDriftApplication:
    """Main application class that orchestrates all systems"""
    
    def __init__(self):
        # Initialize core systems
        self.drift_engine = DriftEngine()
        self.game_state = GameState()
        self.running = True
        
        # Load saved state if exists
        self.load_game_state()
        
        # Start background systems
        self.start_background_threads()
        
    def setup_window(self):
        """Configure the main application window"""
        self.root.title("Recursive Drift Engine - Mystical Simulation")
        self.root.geometry("1200x800")
        self.root.configure(bg="#0a0a0a")
        
        # Set window icon and styling
        self.root.option_add("*TCombobox*Listbox.selectBackground", "#4a0e4e")
        
        # Configure styles
        style = ttk.Style()
        style.theme_use('clam')
        
        # Custom color scheme
        style.configure('Mystical.TFrame', background='#0a0a0a', borderwidth=1, relief='solid')
        style.configure('Mystical.TLabel', background='#0a0a0a', foreground='#ffd700')
        style.configure('Mystical.TButton', background='#2d1b69', foreground='#ffd700')
        style.map('Mystical.TButton', background=[('active', '#4a0e4e')])
        
    def setup_bindings(self):
        """Setup keyboard shortcuts and event bindings"""
        self.root.bind('<Control-s>', lambda e: self.save_game_state())
        self.root.bind('<Control-l>', lambda e: self.load_game_state())
        self.root.bind('<Control-q>', lambda e: self.quit_application())
        self.root.bind('<F1>', lambda e: self.show_help())
        
        # Protocol for window closing
        self.root.protocol("WM_DELETE_WINDOW", self.quit_application)
        
    def start_background_threads(self):
        """Start background threads for real-time updates"""
        # Entropy fluctuation thread
        entropy_thread = threading.Thread(target=self.entropy_update_loop, daemon=True)
        entropy_thread.start()
        
        # Oracle prophecy generation thread
        oracle_thread = threading.Thread(target=self.oracle_update_loop, daemon=True)
        oracle_thread.start()
        
        # Visual effects update thread
        effects_thread = threading.Thread(target=self.visual_effects_loop, daemon=True)
        effects_thread.start()
        
    def entropy_update_loop(self):
        """Background thread for entropy fluctuations"""
        import time
        while True:
            try:
                self.drift_engine.update_entropy_field()
                if self.ui:
                    self.root.after(0, self.ui.update_entropy_display)
                time.sleep(5)  # Update every 5 seconds
            except Exception as e:
                print(f"Entropy update error: {e}")
                time.sleep(10)
                
    def oracle_update_loop(self):
        """Background thread for oracle prophecy generation"""
        import time
        while True:
            try:
                self.drift_engine.oracle_system.generate_background_prophecy()
                time.sleep(30)  # Generate prophecy every 30 seconds
            except Exception as e:
                print(f"Oracle update error: {e}")
                time.sleep(60)
                
    def visual_effects_loop(self):
        """Background thread for visual effects updates"""
        import time
        while True:
            try:
                self.visual_effects.update_particle_systems()
                time.sleep(0.1)  # 10 FPS for smooth effects
            except Exception as e:
                print(f"Visual effects error: {e}")
                time.sleep(1)
                
    def save_game_state(self):
        """Save current game state to file"""
        try:
            state_data = {
                'drift_engine': self.drift_engine.export_state(),
                'timestamp': datetime.now().isoformat(),
                'version': '2.0.0'
            }
            
            if self.game_state.save_state(state_data):
                self.ui.show_status_message("Game state saved successfully", "success")
                self.audio_manager.play_sound('save_success')
            else:
                self.ui.show_status_message("Failed to save game state", "error")
                
        except Exception as e:
            messagebox.showerror("Save Error", f"Failed to save game state: {str(e)}")
            
    def load_game_state(self):
        """Load game state from file"""
        try:
            state_data = self.game_state.load_state()
            if state_data:
                self.drift_engine.import_state(state_data.get('drift_engine', {}))
                self.ui.refresh_all_displays()
                self.ui.show_status_message("Game state loaded successfully", "success")
                self.audio_manager.play_sound('load_success')
            else:
                # First time startup - initialize default state
                self.drift_engine.initialize_default_state()
                self.ui.show_status_message("Initialized new drift field", "info")
                
        except Exception as e:
            messagebox.showerror("Load Error", f"Failed to load game state: {str(e)}")
            self.drift_engine.initialize_default_state()
            
    def show_help(self):
        """Display help information"""
        help_text = """
Recursive Drift Engine - Controls & Features

KEYBOARD SHORTCUTS:
Ctrl+S - Save game state
Ctrl+L - Load game state  
Ctrl+Q - Quit application
F1 - Show this help

SYSTEMS:
• Drift Enclaves - Explore mystical zones with unique properties
• Sigil Alchemy - Combine glyphs to create hybrid forms
• Anomaly Echoes - View fractured logs from past timelines
• Loop-Chains - Build automated action sequences
• Entropy Rites - Play mini-games to manipulate reality
• Fragment Market - Trade identity fragments and memory logs
• Chrono-Glyph Stasis - Preserve moments in time with Time Salt
• Recursive Oracles - Receive AI-powered paradox prophecies
• Sentient Logs - Watch semi-autonomous behaviors unfold

Navigate through the tabs to access different systems.
Hover over elements for detailed tooltips.
        """
        
        messagebox.showinfo("Recursive Drift Engine - Help", help_text)
        
    def quit_application(self):
        """Safely quit the application"""
        try:
            # Save current state before quitting
            self.save_game_state()
            
            # Stop audio
            self.audio_manager.stop_all()
            
            # Clean up threads (they're daemon threads so they'll stop automatically)
            self.root.quit()
            self.root.destroy()
            
        except Exception as e:
            print(f"Error during shutdown: {e}")
        finally:
            sys.exit(0)
            
    def run(self):
        """Start the application main loop"""
        try:
            # Initialize audio ambience
            self.audio_manager.start_ambient_sound('void_drift')
            
            # Show startup message
            self.ui.show_status_message("Entering Recursive Drift Field...", "info")
            
            # Start main event loop
            self.root.mainloop()
            
        except KeyboardInterrupt:
            self.quit_application()
        except Exception as e:
            messagebox.showerror("Fatal Error", f"Application error: {str(e)}")
            self.quit_application()

def main():
    """Application entry point"""
    try:
        # Check for required dependencies
        required_modules = ['tkinter', 'json', 'threading', 'datetime', 'configparser']
        for module in required_modules:
            try:
                __import__(module)
            except ImportError:
                print(f"Error: Required module '{module}' not found")
                return
        
        # Create and run application
        app = RecursiveDriftApplication()
        app.run()
        
    except Exception as e:
        print(f"Failed to start Recursive Drift Engine: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
