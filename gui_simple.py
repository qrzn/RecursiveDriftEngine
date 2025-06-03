import tkinter as tk
from tkinter import scrolledtext, messagebox
import random
from datetime import datetime

from simple_main import SimpleDriftEngine
from persistence import GameState


def drift_map_to_string(drift_map):
    return "\n".join(" ".join(row) for row in drift_map)


def status_to_string(engine):
    status = engine.get_status()
    return (
        f"Node: {status['node_id']}\n"
        f"Enclave: {status['current_enclave']}\n"
        f"Entropy: {status['entropy_level']:.3f}\n"
        f"Time Salt: {status['time_salt']}\n"
        f"Fragments: {status['identity_fragments']}\n"
        f"Forks: {status['fork_count']}\n"
        f"Operations: {status['total_operations']}\n"
    )


def prophecy_text(engine):
    status = engine.get_status()
    entropy = status['entropy_level']
    if entropy > 0.8:
        prophecies = [
            "The void whispers of chaotic tides approaching the nexus...",
            "Reality fractures at the edges - beware the entropy storm...",
            "The drift field pulses with unstable energy - collapse may bring peace...",
            f"In the {status['current_enclave']}, {random.choice(['▲','⊗','≈','∇','∆'])} shall manifest when time fragments...",
        ]
    elif entropy < 0.2:
        prophecies = [
            "Crystalline silence spreads through the temporal streams...",
            "The void grows still - new mysteries await in the depths...",
            "Stability brings clarity, but growth requires gentle chaos...",
            f"Within the {status['current_enclave']}, {random.choice(['▲','⊗','≈','∇','∆'])} holds the key to transformation...",
        ]
    else:
        prophecies = [
            "Balance dances between order and chaos in the drift...",
            "The entropy flows seek their destined pattern...",
            "Fork and collapse interweave the fabric of possibility...",
            f"The {status['current_enclave']} resonates with {random.choice(['▲','⊗','≈','∇','∆'])} energy...",
        ]
    prophecy = random.choice(prophecies)
    confidence = random.uniform(0.6, 0.9)
    return (
        "🔮 Oracle Prophecy\n"
        f"{prophecy}\n"
        f"Confidence: {confidence:.1%}\n"
        f"Temporal Range: {random.choice(['immediate','near future','distant echoes'])}"
    )


class DriftGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Recursive Drift Engine")
        self.engine = SimpleDriftEngine()
        self.game_state = GameState()

        self.create_widgets()
        self.update_display()

    def create_widgets(self):
        top_frame = tk.Frame(self.root)
        top_frame.pack(fill=tk.BOTH, expand=True)

        self.map_text = tk.Text(top_frame, height=6, width=24, font=("Courier", 12))
        self.map_text.pack(side=tk.LEFT, padx=5, pady=5)

        self.log = scrolledtext.ScrolledText(top_frame, width=60, height=20, state="disabled", font=("Courier", 10))
        self.log.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill=tk.X)

        actions = [
            ("Scan", self.action_scan),
            ("Fork", self.action_fork),
            ("Collapse", self.action_collapse),
            ("Wipe", self.action_wipe),
            ("Prophecy", self.action_prophecy),
            ("Status", self.action_status),
            ("Save", self.action_save),
            ("Load", self.action_load),
            ("Quit", self.root.quit),
        ]
        for text, cmd in actions:
            tk.Button(btn_frame, text=text, command=cmd, width=8).pack(side=tk.LEFT, padx=2, pady=2)

    def log_message(self, msg):
        self.log.configure(state="normal")
        self.log.insert(tk.END, msg + "\n")
        self.log.configure(state="disabled")
        self.log.see(tk.END)

    def update_display(self):
        self.map_text.delete("1.0", tk.END)
        self.map_text.insert(tk.END, drift_map_to_string(self.engine.current_drift_map))

    def action_scan(self):
        result = self.engine.scan_field()
        self.update_display()
        self.log_message(f"Scanned field: entropy change {result['entropy_change']:+.3f}")

    def action_fork(self):
        result = self.engine.fork_node()
        self.update_display()
        self.log_message(f"Forked node {result['node_id']} entropy +{result['entropy_change']:.3f}")

    def action_collapse(self):
        result = self.engine.collapse_node()
        self.update_display()
        self.log_message(f"Collapsed node entropy -{result['entropy_reduction']:.3f}")

    def action_wipe(self):
        result = self.engine.memory_wipe()
        self.update_display()
        self.log_message(f"Memory wipe: {result['operations_wiped']} operations cleared")

    def action_prophecy(self):
        self.log_message(prophecy_text(self.engine))

    def action_status(self):
        self.log_message(status_to_string(self.engine))

    def action_save(self):
        state_data = {
            "engine_state": self.engine.export_state(),
            "timestamp": datetime.now().isoformat(),
        }
        if self.game_state.save_state(state_data):
            self.log_message("Game state saved")
        else:
            messagebox.showerror("Save Error", "Failed to save game state")

    def action_load(self):
        data = self.game_state.load_state()
        if data and "engine_state" in data:
            self.engine.import_state(data["engine_state"])
            self.update_display()
            self.log_message("Game state loaded")
        else:
            messagebox.showwarning("Load", "No saved state found")


def main():
    root = tk.Tk()
    app = DriftGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
