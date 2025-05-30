"""
Mystical UI Components: Enhanced Interface Elements
Custom themed components for the Recursive Drift Engine
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, simpledialog
import math
import time
from typing import Dict, List, Any, Optional, Callable

class MysticalUI:
    """Main UI controller with mystical theming"""
    
    def __init__(self, root: tk.Tk, drift_engine, audio_manager, visual_effects):
        self.root = root
        self.drift_engine = drift_engine
        self.audio_manager = audio_manager
        self.visual_effects = visual_effects
        
        # Color scheme
        self.colors = {
            'void_black': '#0a0a0a',
            'entropy_purple': '#4a0e4e',
            'glyph_gold': '#ffd700',
            'drift_silver': '#c0c0c0',
            'anomaly_red': '#8b0000',
            'time_blue': '#191970',
            'success_green': '#228b22',
            'warning_orange': '#ff8c00'
        }
        
        # UI state
        self.status_message = ""
        self.status_color = self.colors['glyph_gold']
        self.floating_widgets = []
        
        # Create main interface
        self.create_main_interface()
        
    def create_main_interface(self):
        """Create the main tabbed interface"""
        # Main container
        self.main_frame = tk.Frame(self.root, bg=self.colors['void_black'])
        self.main_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Status bar at top
        self.create_status_bar()
        
        # Main notebook for tabs
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill='both', expand=True, pady=(10, 0))
        
        # Create all tabs
        self.create_drift_control_tab()
        self.create_alchemy_tab()
        self.create_enclave_tab()
        self.create_oracle_tab()
        self.create_market_tab()
        self.create_temporal_tab()
        self.create_entropy_rites_tab()
        self.create_anomaly_echoes_tab()
        self.create_sentient_logs_tab()
        
        # Setup tab styling
        self.setup_notebook_styling()
        
    def create_status_bar(self):
        """Create the top status bar"""
        status_frame = tk.Frame(self.main_frame, bg=self.colors['entropy_purple'], height=40)
        status_frame.pack(fill='x', pady=(0, 5))
        status_frame.pack_propagate(False)
        
        # Node ID display
        self.node_label = tk.Label(status_frame, text=f"Node: {self.drift_engine.node_id}", 
                                  bg=self.colors['entropy_purple'], fg=self.colors['glyph_gold'],
                                  font=('Courier', 10, 'bold'))
        self.node_label.pack(side='left', padx=10, pady=8)
        
        # Resources display
        self.resources_frame = tk.Frame(status_frame, bg=self.colors['entropy_purple'])
        self.resources_frame.pack(side='right', padx=10, pady=5)
        
        self.time_salt_label = tk.Label(self.resources_frame, text=f"⧗ {self.drift_engine.time_salt}",
                                       bg=self.colors['entropy_purple'], fg=self.colors['time_blue'],
                                       font=('Courier', 9, 'bold'))
        self.time_salt_label.pack(side='right', padx=5)
        
        self.fragments_label = tk.Label(self.resources_frame, text=f"◊ {self.drift_engine.identity_fragments}",
                                       bg=self.colors['entropy_purple'], fg=self.colors['drift_silver'],
                                       font=('Courier', 9, 'bold'))
        self.fragments_label.pack(side='right', padx=5)
        
        # Entropy level with animated bar
        self.entropy_frame = tk.Frame(status_frame, bg=self.colors['entropy_purple'])
        self.entropy_frame.pack(side='left', padx=20, pady=5)
        
        self.entropy_canvas = tk.Canvas(self.entropy_frame, width=100, height=20, 
                                       bg=self.colors['void_black'], highlightthickness=0)
        self.entropy_canvas.pack(side='left')
        
        self.entropy_text_label = tk.Label(self.entropy_frame, text="Entropy",
                                          bg=self.colors['entropy_purple'], fg=self.colors['glyph_gold'],
                                          font=('Courier', 8))
        self.entropy_text_label.pack(side='left', padx=(5, 0))
        
        # Status message area
        self.status_label = tk.Label(status_frame, text="Drift field stabilized",
                                    bg=self.colors['entropy_purple'], fg=self.colors['glyph_gold'],
                                    font=('Courier', 9))
        self.status_label.pack(side='left', padx=20, pady=8)
        
    def create_drift_control_tab(self):
        """Create the main drift control interface"""
        drift_frame = tk.Frame(self.notebook, bg=self.colors['void_black'])
        self.notebook.add(drift_frame, text="◈ Drift Control")
        
        # Left panel - Drift map and controls
        left_panel = tk.Frame(drift_frame, bg=self.colors['void_black'])
        left_panel.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        
        # Drift map display
        map_frame = tk.LabelFrame(left_panel, text="Current Drift Field", 
                                 bg=self.colors['void_black'], fg=self.colors['glyph_gold'],
                                 font=('Courier', 10, 'bold'))
        map_frame.pack(fill='x', pady=(0, 10))
        
        self.drift_map_canvas = tk.Canvas(map_frame, width=300, height=200, 
                                         bg=self.colors['void_black'], highlightthickness=1,
                                         highlightbackground=self.colors['entropy_purple'])
        self.drift_map_canvas.pack(padx=10, pady=10)
        
        # Control buttons
        controls_frame = tk.LabelFrame(left_panel, text="Node Operations",
                                      bg=self.colors['void_black'], fg=self.colors['glyph_gold'],
                                      font=('Courier', 10, 'bold'))
        controls_frame.pack(fill='x', pady=(0, 10))
        
        button_configs = [
            ("🔍 Scan Field", self.action_scan, self.colors['time_blue']),
            ("⚡ Fork Node", self.action_fork, self.colors['entropy_purple']),
            ("💥 Collapse Node", self.action_collapse, self.colors['anomaly_red']),
            ("🌀 Memory Wipe", self.action_memory_wipe, self.colors['warning_orange'])
        ]
        
        buttons_frame = tk.Frame(controls_frame, bg=self.colors['void_black'])
        buttons_frame.pack(fill='x', padx=10, pady=10)
        
        for i, (text, command, color) in enumerate(button_configs):
            btn = tk.Button(buttons_frame, text=text, command=command,
                           bg=color, fg=self.colors['glyph_gold'],
                           font=('Courier', 9, 'bold'),
                           relief='raised', borderwidth=2,
                           activebackground=self.lighten_color(color),
                           activeforeground=self.colors['void_black'])
            btn.pack(side='left', fill='x', expand=True, padx=2)
            
        # Right panel - Logs and information
        right_panel = tk.Frame(drift_frame, bg=self.colors['void_black'])
        right_panel.pack(side='right', fill='both', expand=True, padx=5, pady=5)
        
        # Activity log
        log_frame = tk.LabelFrame(right_panel, text="Activity Log",
                                 bg=self.colors['void_black'], fg=self.colors['glyph_gold'],
                                 font=('Courier', 10, 'bold'))
        log_frame.pack(fill='both', expand=True)
        
        self.activity_log = scrolledtext.ScrolledText(log_frame, 
                                                     bg=self.colors['void_black'],
                                                     fg=self.colors['drift_silver'],
                                                     font=('Courier', 9),
                                                     insertbackground=self.colors['glyph_gold'],
                                                     wrap=tk.WORD)
        self.activity_log.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Quick info panel
        info_frame = tk.LabelFrame(right_panel, text="System Status",
                                  bg=self.colors['void_black'], fg=self.colors['glyph_gold'],
                                  font=('Courier', 10, 'bold'))
        info_frame.pack(fill='x', pady=(10, 0))
        
        self.info_text = tk.Text(info_frame, height=6, 
                                bg=self.colors['void_black'], fg=self.colors['glyph_gold'],
                                font=('Courier', 8),
                                state='disabled')
        self.info_text.pack(fill='x', padx=10, pady=10)
        
    def create_alchemy_tab(self):
        """Create the sigil alchemy interface"""
        alchemy_frame = tk.Frame(self.notebook, bg=self.colors['void_black'])
        self.notebook.add(alchemy_frame, text="⚗ Sigil Alchemy")
        
        # Left side - Glyph selection and combination
        left_alchemy = tk.Frame(alchemy_frame, bg=self.colors['void_black'])
        left_alchemy.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        
        # Glyph palette
        glyph_frame = tk.LabelFrame(left_alchemy, text="Glyph Palette",
                                   bg=self.colors['void_black'], fg=self.colors['glyph_gold'],
                                   font=('Courier', 10, 'bold'))
        glyph_frame.pack(fill='x', pady=(0, 10))
        
        self.glyph_palette = tk.Frame(glyph_frame, bg=self.colors['void_black'])
        self.glyph_palette.pack(fill='x', padx=10, pady=10)
        
        # Create glyph buttons
        self.selected_glyphs = []
        for i, glyph in enumerate(self.drift_engine.glyph_manager.get_all_glyphs()):
            btn = tk.Button(self.glyph_palette, text=glyph, 
                           font=('Courier', 16, 'bold'),
                           width=3, height=2,
                           bg=self.colors['entropy_purple'],
                           fg=self.colors['glyph_gold'],
                           command=lambda g=glyph: self.select_glyph(g))
            btn.grid(row=i//5, column=i%5, padx=2, pady=2)
            
        # Combination area
        combo_frame = tk.LabelFrame(left_alchemy, text="Alchemy Crucible",
                                   bg=self.colors['void_black'], fg=self.colors['glyph_gold'],
                                   font=('Courier', 10, 'bold'))
        combo_frame.pack(fill='both', expand=True)
        
        self.combination_canvas = tk.Canvas(combo_frame, height=200,
                                           bg=self.colors['void_black'],
                                           highlightthickness=1,
                                           highlightbackground=self.colors['entropy_purple'])
        self.combination_canvas.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Alchemy controls
        alchemy_controls = tk.Frame(combo_frame, bg=self.colors['void_black'])
        alchemy_controls.pack(fill='x', padx=10, pady=(0, 10))
        
        tk.Button(alchemy_controls, text="🔥 Transmute", 
                 command=self.perform_alchemy,
                 bg=self.colors['warning_orange'], fg=self.colors['void_black'],
                 font=('Courier', 10, 'bold')).pack(side='left', padx=5)
        
        tk.Button(alchemy_controls, text="🧹 Clear", 
                 command=self.clear_combination,
                 bg=self.colors['anomaly_red'], fg=self.colors['glyph_gold'],
                 font=('Courier', 10, 'bold')).pack(side='left', padx=5)
        
        # Right side - Results and known combinations
        right_alchemy = tk.Frame(alchemy_frame, bg=self.colors['void_black'])
        right_alchemy.pack(side='right', fill='both', expand=True, padx=5, pady=5)
        
        # Results display
        results_frame = tk.LabelFrame(right_alchemy, text="Transmutation Results",
                                     bg=self.colors['void_black'], fg=self.colors['glyph_gold'],
                                     font=('Courier', 10, 'bold'))
        results_frame.pack(fill='x', pady=(0, 10))
        
        self.alchemy_results = scrolledtext.ScrolledText(results_frame, height=8,
                                                        bg=self.colors['void_black'],
                                                        fg=self.colors['drift_silver'],
                                                        font=('Courier', 9))
        self.alchemy_results.pack(fill='x', padx=10, pady=10)
        
        # Known combinations
        known_frame = tk.LabelFrame(right_alchemy, text="Known Combinations",
                                   bg=self.colors['void_black'], fg=self.colors['glyph_gold'],
                                   font=('Courier', 10, 'bold'))
        known_frame.pack(fill='both', expand=True)
        
        self.known_combinations = scrolledtext.ScrolledText(known_frame,
                                                           bg=self.colors['void_black'],
                                                           fg=self.colors['glyph_gold'],
                                                           font=('Courier', 8))
        self.known_combinations.pack(fill='both', expand=True, padx=10, pady=10)
        
    def create_enclave_tab(self):
        """Create the drift enclaves interface"""
        enclave_frame = tk.Frame(self.notebook, bg=self.colors['void_black'])
        self.notebook.add(enclave_frame, text="🏛 Drift Enclaves")
        
        # Top panel - Current enclave info
        current_enclave_frame = tk.LabelFrame(enclave_frame, text="Current Enclave",
                                             bg=self.colors['void_black'], fg=self.colors['glyph_gold'],
                                             font=('Courier', 10, 'bold'))
        current_enclave_frame.pack(fill='x', padx=5, pady=5)
        
        self.current_enclave_info = tk.Text(current_enclave_frame, height=4,
                                           bg=self.colors['void_black'], fg=self.colors['drift_silver'],
                                           font=('Courier', 9),
                                           state='disabled')
        self.current_enclave_info.pack(fill='x', padx=10, pady=10)
        
        # Middle panel - Available enclaves
        enclaves_list_frame = tk.LabelFrame(enclave_frame, text="Available Enclaves",
                                           bg=self.colors['void_black'], fg=self.colors['glyph_gold'],
                                           font=('Courier', 10, 'bold'))
        enclaves_list_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Create scrollable list of enclaves
        enclaves_container = tk.Frame(enclaves_list_frame, bg=self.colors['void_black'])
        enclaves_container.pack(fill='both', expand=True, padx=10, pady=10)
        
        enclave_scroll = tk.Scrollbar(enclaves_container)
        enclave_scroll.pack(side='right', fill='y')
        
        self.enclaves_listbox = tk.Listbox(enclaves_container,
                                          bg=self.colors['void_black'],
                                          fg=self.colors['glyph_gold'],
                                          font=('Courier', 10),
                                          selectbackground=self.colors['entropy_purple'],
                                          yscrollcommand=enclave_scroll.set)
        self.enclaves_listbox.pack(side='left', fill='both', expand=True)
        enclave_scroll.config(command=self.enclaves_listbox.yview)
        
        # Enclave controls
        enclave_controls = tk.Frame(enclave_frame, bg=self.colors['void_black'])
        enclave_controls.pack(fill='x', padx=5, pady=5)
        
        tk.Button(enclave_controls, text="🚪 Enter Enclave",
                 command=self.enter_selected_enclave,
                 bg=self.colors['time_blue'], fg=self.colors['glyph_gold'],
                 font=('Courier', 10, 'bold')).pack(side='left', padx=5)
        
        tk.Button(enclave_controls, text="🔮 Scan Resonance",
                 command=self.scan_enclave_resonance,
                 bg=self.colors['entropy_purple'], fg=self.colors['glyph_gold'],
                 font=('Courier', 10, 'bold')).pack(side='left', padx=5)
        
    def create_oracle_tab(self):
        """Create the recursive oracles interface"""
        oracle_frame = tk.Frame(self.notebook, bg=self.colors['void_black'])
        self.notebook.add(oracle_frame, text="🔮 Recursive Oracles")
        
        # Prophecy display
        prophecy_frame = tk.LabelFrame(oracle_frame, text="Current Prophecies",
                                      bg=self.colors['void_black'], fg=self.colors['glyph_gold'],
                                      font=('Courier', 10, 'bold'))
        prophecy_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        self.prophecy_display = scrolledtext.ScrolledText(prophecy_frame,
                                                         bg=self.colors['void_black'],
                                                         fg=self.colors['time_blue'],
                                                         font=('Courier', 10),
                                                         wrap=tk.WORD)
        self.prophecy_display.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Oracle controls
        oracle_controls = tk.Frame(oracle_frame, bg=self.colors['void_black'])
        oracle_controls.pack(fill='x', padx=5, pady=5)
        
        tk.Button(oracle_controls, text="🌌 Request Prophecy",
                 command=self.request_prophecy,
                 bg=self.colors['time_blue'], fg=self.colors['glyph_gold'],
                 font=('Courier', 10, 'bold')).pack(side='left', padx=5)
        
        tk.Button(oracle_controls, text="⚡ Paradox Query",
                 command=self.request_paradox_query,
                 bg=self.colors['entropy_purple'], fg=self.colors['glyph_gold'],
                 font=('Courier', 10, 'bold')).pack(side='left', padx=5)
        
    def create_market_tab(self):
        """Create the fragment market interface"""
        market_frame = tk.Frame(self.notebook, bg=self.colors['void_black'])
        self.notebook.add(market_frame, text="💎 Fragment Market")
        
        # Market listings
        listings_frame = tk.LabelFrame(market_frame, text="Available Fragments",
                                      bg=self.colors['void_black'], fg=self.colors['glyph_gold'],
                                      font=('Courier', 10, 'bold'))
        listings_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Create treeview for market items
        market_tree_frame = tk.Frame(listings_frame, bg=self.colors['void_black'])
        market_tree_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.market_tree = ttk.Treeview(market_tree_frame, 
                                       columns=('Type', 'Price', 'Rarity'),
                                       show='tree headings')
        self.market_tree.heading('#0', text='Item')
        self.market_tree.heading('Type', text='Type')
        self.market_tree.heading('Price', text='Price')
        self.market_tree.heading('Rarity', text='Rarity')
        self.market_tree.pack(fill='both', expand=True)
        
        # Market controls
        market_controls = tk.Frame(market_frame, bg=self.colors['void_black'])
        market_controls.pack(fill='x', padx=5, pady=5)
        
        tk.Button(market_controls, text="💰 Purchase",
                 command=self.purchase_fragment,
                 bg=self.colors['success_green'], fg=self.colors['void_black'],
                 font=('Courier', 10, 'bold')).pack(side='left', padx=5)
        
        tk.Button(market_controls, text="📊 Refresh Market",
                 command=self.refresh_market,
                 bg=self.colors['time_blue'], fg=self.colors['glyph_gold'],
                 font=('Courier', 10, 'bold')).pack(side='left', padx=5)
        
    def create_temporal_tab(self):
        """Create the chrono-glyph stasis interface"""
        temporal_frame = tk.Frame(self.notebook, bg=self.colors['void_black'])
        self.notebook.add(temporal_frame, text="⧗ Temporal Mechanics")
        
        # Stasis preservation area
        stasis_frame = tk.LabelFrame(temporal_frame, text="Chrono-Glyph Stasis",
                                    bg=self.colors['void_black'], fg=self.colors['glyph_gold'],
                                    font=('Courier', 10, 'bold'))
        stasis_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        self.stasis_display = scrolledtext.ScrolledText(stasis_frame,
                                                       bg=self.colors['void_black'],
                                                       fg=self.colors['time_blue'],
                                                       font=('Courier', 9))
        self.stasis_display.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Temporal controls
        temporal_controls = tk.Frame(temporal_frame, bg=self.colors['void_black'])
        temporal_controls.pack(fill='x', padx=5, pady=5)
        
        tk.Button(temporal_controls, text="⏸ Preserve Moment",
                 command=self.preserve_moment,
                 bg=self.colors['time_blue'], fg=self.colors['glyph_gold'],
                 font=('Courier', 10, 'bold')).pack(side='left', padx=5)
        
        tk.Button(temporal_controls, text="⏮ Restore Moment",
                 command=self.restore_moment,
                 bg=self.colors['entropy_purple'], fg=self.colors['glyph_gold'],
                 font=('Courier', 10, 'bold')).pack(side='left', padx=5)
        
    def create_entropy_rites_tab(self):
        """Create the entropy rites mini-games interface"""
        rites_frame = tk.Frame(self.notebook, bg=self.colors['void_black'])
        self.notebook.add(rites_frame, text="🎮 Entropy Rites")
        
        # Mini-games selection
        games_frame = tk.LabelFrame(rites_frame, text="Available Rites",
                                   bg=self.colors['void_black'], fg=self.colors['glyph_gold'],
                                   font=('Courier', 10, 'bold'))
        games_frame.pack(fill='x', padx=5, pady=5)
        
        games_buttons = tk.Frame(games_frame, bg=self.colors['void_black'])
        games_buttons.pack(fill='x', padx=10, pady=10)
        
        tk.Button(games_buttons, text="🎯 Containment Sigil Draw",
                 command=self.start_sigil_draw,
                 bg=self.colors['entropy_purple'], fg=self.colors['glyph_gold'],
                 font=('Courier', 9, 'bold')).pack(side='left', fill='x', expand=True, padx=2)
        
        tk.Button(games_buttons, text="🎵 Feedback Chant Match",
                 command=self.start_chant_match,
                 bg=self.colors['time_blue'], fg=self.colors['glyph_gold'],
                 font=('Courier', 9, 'bold')).pack(side='left', fill='x', expand=True, padx=2)
        
        tk.Button(games_buttons, text="💥 Node Purge Pulse",
                 command=self.start_purge_pulse,
                 bg=self.colors['anomaly_red'], fg=self.colors['glyph_gold'],
                 font=('Courier', 9, 'bold')).pack(side='left', fill='x', expand=True, padx=2)
        
        # Game area
        game_area_frame = tk.LabelFrame(rites_frame, text="Rite Chamber",
                                       bg=self.colors['void_black'], fg=self.colors['glyph_gold'],
                                       font=('Courier', 10, 'bold'))
        game_area_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        self.game_canvas = tk.Canvas(game_area_frame,
                                    bg=self.colors['void_black'],
                                    highlightthickness=1,
                                    highlightbackground=self.colors['entropy_purple'])
        self.game_canvas.pack(fill='both', expand=True, padx=10, pady=10)
        
    def create_anomaly_echoes_tab(self):
        """Create the anomaly echoes interface"""
        echoes_frame = tk.Frame(self.notebook, bg=self.colors['void_black'])
        self.notebook.add(echoes_frame, text="👻 Anomaly Echoes")
        
        # Echoes display
        echoes_display_frame = tk.LabelFrame(echoes_frame, text="Fractured Timeline Echoes",
                                            bg=self.colors['void_black'], fg=self.colors['glyph_gold'],
                                            font=('Courier', 10, 'bold'))
        echoes_display_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        self.echoes_display = scrolledtext.ScrolledText(echoes_display_frame,
                                                       bg=self.colors['void_black'],
                                                       fg=self.colors['anomaly_red'],
                                                       font=('Courier', 9),
                                                       wrap=tk.WORD)
        self.echoes_display.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Echo controls
        echo_controls = tk.Frame(echoes_frame, bg=self.colors['void_black'])
        echo_controls.pack(fill='x', padx=5, pady=5)
        
        tk.Button(echo_controls, text="🔍 Scan for Echoes",
                 command=self.scan_for_echoes,
                 bg=self.colors['anomaly_red'], fg=self.colors['glyph_gold'],
                 font=('Courier', 10, 'bold')).pack(side='left', padx=5)
        
        tk.Button(echo_controls, text="🧹 Purge Echoes",
                 command=self.purge_echoes,
                 bg=self.colors['warning_orange'], fg=self.colors['void_black'],
                 font=('Courier', 10, 'bold')).pack(side='left', padx=5)
        
    def create_sentient_logs_tab(self):
        """Create the sentient logs interface"""
        logs_frame = tk.Frame(self.notebook, bg=self.colors['void_black'])
        self.notebook.add(logs_frame, text="🤖 Sentient Logs")
        
        # Sentient logs list
        logs_list_frame = tk.LabelFrame(logs_frame, text="Active Sentient Entities",
                                       bg=self.colors['void_black'], fg=self.colors['glyph_gold'],
                                       font=('Courier', 10, 'bold'))
        logs_list_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Create treeview for sentient logs
        logs_tree_frame = tk.Frame(logs_list_frame, bg=self.colors['void_black'])
        logs_tree_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.sentient_tree = ttk.Treeview(logs_tree_frame,
                                         columns=('Sentience', 'Behavior', 'Activity'),
                                         show='tree headings')
        self.sentient_tree.heading('#0', text='Log ID')
        self.sentient_tree.heading('Sentience', text='Sentience Level')
        self.sentient_tree.heading('Behavior', text='Behavior Pattern')
        self.sentient_tree.heading('Activity', text='Last Activity')
        self.sentient_tree.pack(fill='both', expand=True)
        
        # Interaction controls
        interaction_controls = tk.Frame(logs_frame, bg=self.colors['void_black'])
        interaction_controls.pack(fill='x', padx=5, pady=5)
        
        tk.Button(interaction_controls, text="💬 Interact",
                 command=self.interact_with_log,
                 bg=self.colors['success_green'], fg=self.colors['void_black'],
                 font=('Courier', 10, 'bold')).pack(side='left', padx=5)
        
        tk.Button(interaction_controls, text="🔄 Refresh Status",
                 command=self.refresh_sentient_logs,
                 bg=self.colors['time_blue'], fg=self.colors['glyph_gold'],
                 font=('Courier', 10, 'bold')).pack(side='left', padx=5)
        
    def setup_notebook_styling(self):
        """Setup custom styling for the notebook tabs"""
        style = ttk.Style()
        
        style.configure('TNotebook', background=self.colors['void_black'])
        style.configure('TNotebook.Tab', 
                       background=self.colors['entropy_purple'],
                       foreground=self.colors['glyph_gold'],
                       padding=[10, 5])
        style.map('TNotebook.Tab',
                 background=[('selected', self.colors['glyph_gold'])],
                 foreground=[('selected', self.colors['void_black'])])
        
    # UI Action Methods
    def action_scan(self):
        """Perform drift field scan"""
        try:
            new_map = self.drift_engine.generate_drift_map()
            self.update_drift_map_display(new_map)
            self.log_activity("🔍 Drift field scan completed")
            self.audio_manager.play_sound('scan')
            self.visual_effects.trigger_scan_effect()
        except Exception as e:
            self.show_status_message(f"Scan failed: {e}", "error")
            
    def action_fork(self):
        """Perform node fork operation"""
        try:
            result = self.drift_engine.fork_node()
            self.log_activity(f"⚡ Node forked: {result['node_id']}")
            self.log_activity(f"   Entropy: {result['entropy_level']}")
            self.log_activity(f"   Glyphs: {', '.join(result['glyph_state'])}")
            self.audio_manager.play_sound('fork')
            self.visual_effects.trigger_fork_effect()
            self.update_resources_display()
        except Exception as e:
            self.show_status_message(f"Fork failed: {e}", "error")
            
    def action_collapse(self):
        """Perform node collapse operation"""
        try:
            result = self.drift_engine.collapse_node()
            self.log_activity(f"💥 Node collapsed: {result['node_id']}")
            self.log_activity(f"   Sigil: {result['sigil']}")
            self.log_activity(f"   Time Salt: +{result['time_salt_generated']}")
            self.log_activity(f"   Fragments: +{result['fragments_released']}")
            self.audio_manager.play_sound('collapse')
            self.visual_effects.trigger_collapse_effect()
            self.update_resources_display()
        except Exception as e:
            self.show_status_message(f"Collapse failed: {e}", "error")
            
    def action_memory_wipe(self):
        """Perform memory wipe operation"""
        try:
            result = messagebox.askyesno("Memory Wipe", 
                                       "Are you sure you want to wipe all fork memories? This cannot be undone.")
            if result:
                message = self.drift_engine.memory_wipe()
                self.log_activity(f"🌀 {message}")
                self.audio_manager.play_sound('memory_wipe')
                self.visual_effects.trigger_wipe_effect()
                self.update_resources_display()
        except Exception as e:
            self.show_status_message(f"Memory wipe failed: {e}", "error")
            
    # Glyph Selection and Alchemy
    def select_glyph(self, glyph: str):
        """Select a glyph for alchemy combination"""
        if len(self.selected_glyphs) < 5:  # Maximum 5 glyphs per combination
            self.selected_glyphs.append(glyph)
            self.update_combination_display()
            self.audio_manager.play_sound('glyph_select')
            
    def clear_combination(self):
        """Clear current glyph combination"""
        self.selected_glyphs = []
        self.update_combination_display()
        
    def perform_alchemy(self):
        """Perform sigil alchemy with selected glyphs"""
        if len(self.selected_glyphs) >= 2:
            try:
                result = self.drift_engine.alchemy_system.combine_glyphs(self.selected_glyphs)
                self.display_alchemy_result(result)
                self.audio_manager.play_sound('alchemy_success')
                self.visual_effects.trigger_alchemy_effect(self.selected_glyphs)
                self.clear_combination()
                self.update_known_combinations_display()
            except Exception as e:
                self.show_status_message(f"Alchemy failed: {e}", "error")
        else:
            self.show_status_message("Need at least 2 glyphs for alchemy", "warning")
            
    # Display Update Methods
    def update_drift_map_display(self, drift_map: List[List[str]]):
        """Update the drift map canvas display"""
        self.drift_map_canvas.delete("all")
        
        cell_width = 40
        cell_height = 30
        
        for y, row in enumerate(drift_map):
            for x, glyph in enumerate(row):
                # Calculate position
                canvas_x = x * cell_width + 20
                canvas_y = y * cell_height + 20
                
                # Get glyph color based on entropy
                glyph_color = self.get_glyph_color(glyph)
                
                # Draw cell background
                self.drift_map_canvas.create_rectangle(
                    canvas_x - 15, canvas_y - 10,
                    canvas_x + 15, canvas_y + 10,
                    fill=self.colors['entropy_purple'],
                    outline=self.colors['glyph_gold']
                )
                
                # Draw glyph
                self.drift_map_canvas.create_text(
                    canvas_x, canvas_y,
                    text=glyph,
                    font=('Courier', 16, 'bold'),
                    fill=glyph_color
                )
                
    def update_combination_display(self):
        """Update the alchemy combination canvas"""
        self.combination_canvas.delete("all")
        
        if not self.selected_glyphs:
            self.combination_canvas.create_text(
                150, 100,
                text="Select glyphs to combine",
                font=('Courier', 12),
                fill=self.colors['drift_silver']
            )
            return
            
        # Draw selected glyphs in circle formation
        center_x, center_y = 150, 100
        radius = 60
        
        for i, glyph in enumerate(self.selected_glyphs):
            angle = (2 * math.pi * i) / len(self.selected_glyphs)
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            
            # Draw glyph circle
            self.combination_canvas.create_oval(
                x - 20, y - 20, x + 20, y + 20,
                fill=self.colors['entropy_purple'],
                outline=self.colors['glyph_gold'],
                width=2
            )
            
            # Draw glyph
            self.combination_canvas.create_text(
                x, y,
                text=glyph,
                font=('Courier', 14, 'bold'),
                fill=self.colors['glyph_gold']
            )
            
        # Draw connecting lines
        if len(self.selected_glyphs) > 1:
            for i in range(len(self.selected_glyphs)):
                angle1 = (2 * math.pi * i) / len(self.selected_glyphs)
                angle2 = (2 * math.pi * ((i + 1) % len(self.selected_glyphs))) / len(self.selected_glyphs)
                
                x1 = center_x + radius * math.cos(angle1)
                y1 = center_y + radius * math.sin(angle1)
                x2 = center_x + radius * math.cos(angle2)
                y2 = center_y + radius * math.sin(angle2)
                
                self.combination_canvas.create_line(
                    x1, y1, x2, y2,
                    fill=self.colors['time_blue'],
                    width=2
                )
                
    def update_entropy_display(self):
        """Update the entropy level display"""
        self.entropy_canvas.delete("all")
        
        # Draw entropy bar
        entropy_level = self.drift_engine.entropy_field.get('global_flux', 0.5)
        bar_width = int(90 * entropy_level)
        
        # Background bar
        self.entropy_canvas.create_rectangle(5, 5, 95, 15, 
                                           fill=self.colors['void_black'],
                                           outline=self.colors['drift_silver'])
        
        # Entropy level bar with color based on level
        if entropy_level < 0.3:
            bar_color = self.colors['time_blue']
        elif entropy_level < 0.7:
            bar_color = self.colors['entropy_purple']
        else:
            bar_color = self.colors['anomaly_red']
            
        self.entropy_canvas.create_rectangle(5, 5, 5 + bar_width, 15,
                                           fill=bar_color,
                                           outline="")
        
    def update_resources_display(self):
        """Update the resources display in status bar"""
        self.time_salt_label.config(text=f"⧗ {self.drift_engine.time_salt}")
        self.fragments_label.config(text=f"◊ {self.drift_engine.identity_fragments}")
        
    def refresh_all_displays(self):
        """Refresh all UI displays after state change"""
        try:
            if self.drift_engine.current_drift_map:
                self.update_drift_map_display(self.drift_engine.current_drift_map)
            self.update_entropy_display()
            self.update_resources_display()
            self.update_system_info()
            self.update_known_combinations_display()
            self.refresh_market()
            self.refresh_sentient_logs()
            self.update_enclaves_list()
            self.update_echoes_display()
        except Exception as e:
            print(f"Error refreshing displays: {e}")
            
    def log_activity(self, message: str):
        """Log activity to the activity log"""
        timestamp = time.strftime("%H:%M:%S")
        self.activity_log.insert(tk.END, f"[{timestamp}] {message}\n")
        self.activity_log.see(tk.END)
        
    def show_status_message(self, message: str, message_type: str = "info"):
        """Show status message in status bar"""
        color_map = {
            "info": self.colors['glyph_gold'],
            "success": self.colors['success_green'],
            "warning": self.colors['warning_orange'],
            "error": self.colors['anomaly_red']
        }
        
        self.status_label.config(text=message, fg=color_map.get(message_type, self.colors['glyph_gold']))
        
        # Auto-clear after 5 seconds
        self.root.after(5000, lambda: self.status_label.config(text="Drift field stabilized", 
                                                              fg=self.colors['glyph_gold']))
        
    # Utility Methods
    def get_glyph_color(self, glyph: str) -> str:
        """Get color for glyph based on its entropy harmonic"""
        harmonic = self.drift_engine.entropy_field.get('glyph_harmonics', {}).get(glyph, 0.5)
        
        if harmonic < 0.3:
            return self.colors['time_blue']
        elif harmonic < 0.7:
            return self.colors['glyph_gold']
        else:
            return self.colors['anomaly_red']
            
    def lighten_color(self, color: str) -> str:
        """Create a lighter version of a color"""
        # Simple color lightening - in production would use proper color manipulation
        color_map = {
            self.colors['entropy_purple']: '#6a2e6e',
            self.colors['time_blue']: '#3939a0',
            self.colors['anomaly_red']: '#ab2020',
            self.colors['warning_orange']: '#ffac30'
        }
        return color_map.get(color, color)
        
    # Placeholder methods for features to be implemented by subsystems
    def display_alchemy_result(self, result): pass
    def update_known_combinations_display(self): pass
    def update_system_info(self): pass
    def enter_selected_enclave(self): pass
    def scan_enclave_resonance(self): pass
    def update_enclaves_list(self): pass
    def request_prophecy(self): pass
    def request_paradox_query(self): pass
    def purchase_fragment(self): pass
    def refresh_market(self): pass
    def preserve_moment(self): pass
    def restore_moment(self): pass
    def start_sigil_draw(self): pass
    def start_chant_match(self): pass
    def start_purge_pulse(self): pass
    def scan_for_echoes(self): pass
    def purge_echoes(self): pass
    def update_echoes_display(self): pass
    def interact_with_log(self): pass
    def refresh_sentient_logs(self): pass
