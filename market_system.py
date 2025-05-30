"""
Fragment Market System: Trading Identity Fragments and Memory Logs
Advanced resource trading with dynamic pricing and market forces
"""

import random
import json
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional, Tuple

class MarketItem:
    """Individual item available in the fragment market"""
    
    def __init__(self, item_id: str, item_type: str, name: str, base_price: int):
        self.item_id = item_id
        self.item_type = item_type
        self.name = name
        self.base_price = base_price
        
        # Market properties
        self.current_price = base_price
        self.demand = random.uniform(0.3, 0.8)
        self.supply = random.uniform(0.2, 0.9)
        self.volatility = random.uniform(0.1, 0.3)
        
        # Item properties
        self.quality = random.uniform(0.5, 1.0)
        self.rarity = self._calculate_rarity()
        self.properties = []
        self.history = []
        
    def _calculate_rarity(self) -> str:
        """Calculate item rarity based on quality"""
        if self.quality >= 0.9:
            return "legendary"
        elif self.quality >= 0.7:
            return "epic"
        elif self.quality >= 0.5:
            return "rare"
        else:
            return "common"

class FragmentMarket:
    """Main fragment market system"""
    
    def __init__(self):
        # Market state
        self.items = {}
        self.transaction_history = []
        self.market_volatility = 0.5
        self.supply_demand_factor = 1.0
        
        # Player resources
        self.player_fragments = 50
        self.player_time_salt = 100
        self.player_inventory = []
        
        # Initialize market
        self.initialize_market_items()
        
    def initialize_market_items(self):
        """Initialize basic market items"""
        basic_items = [
            ("memory_fragment_001", "memory_fragment", "Childhood Echo", 15),
            ("memory_fragment_002", "memory_fragment", "Lost Moment", 25),
            ("glyph_shard_001", "glyph_shard", "Void Shard", 20),
            ("glyph_shard_002", "glyph_shard", "Energy Shard", 18),
            ("loop_seed_001", "loop_seed", "Recursive Seed", 30),
            ("broken_fork_001", "broken_fork", "Shattered Timeline", 40),
            ("null_fragment_001", "null_fragment", "Emptiness Essence", 35),
            ("time_crystal_001", "time_crystal", "Temporal Residue", 50)
        ]
        
        for item_id, item_type, name, price in basic_items:
            item = MarketItem(item_id, item_type, name, price)
            self.items[item_id] = item
            
    def get_item_count(self) -> int:
        """Get total number of items in market"""
        return len(self.items)
        
    def buy_item(self, item_id: str, currency: str = "fragments") -> Dict[str, Any]:
        """Buy an item from the market"""
        if item_id not in self.items:
            return {
                "success": False,
                "error": f"Item {item_id} not found in market"
            }
            
        item = self.items[item_id]
        
        # Check if player has enough currency
        if currency == "fragments":
            if self.player_fragments < item.current_price:
                return {
                    "success": False,
                    "error": f"Insufficient fragments. Need {item.current_price}, have {self.player_fragments}"
                }
        elif currency == "time_salt":
            salt_price = int(item.current_price * 0.8)  # Time salt is more valuable
            if self.player_time_salt < salt_price:
                return {
                    "success": False,
                    "error": f"Insufficient time salt. Need {salt_price}, have {self.player_time_salt}"
                }
                
        # Process purchase
        if currency == "fragments":
            self.player_fragments -= item.current_price
            paid_amount = item.current_price
        else:
            salt_price = int(item.current_price * 0.8)
            self.player_time_salt -= salt_price
            paid_amount = salt_price
            
        # Add to player inventory
        self.player_inventory.append({
            "item": item.__dict__.copy(),
            "purchase_date": datetime.now(timezone.utc).isoformat(),
            "purchase_price": paid_amount,
            "currency_used": currency
        })
        
        # Update market dynamics
        item.demand = max(0.1, item.demand - 0.1)
        item.supply = max(0.1, item.supply - 0.1)
        item.current_price = int(item.base_price * (1.5 - item.supply + item.demand))
        
        # Record transaction
        transaction = {
            "type": "purchase",
            "item_id": item_id,
            "item_name": item.name,
            "price": paid_amount,
            "currency": currency,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
        self.transaction_history.append(transaction)
        
        return {
            "success": True,
            "item_purchased": item.name,
            "price_paid": paid_amount,
            "currency_used": currency,
            "remaining_fragments": self.player_fragments,
            "remaining_time_salt": self.player_time_salt,
            "item_properties": {
                "quality": round(item.quality, 2),
                "rarity": item.rarity,
                "type": item.item_type
            }
        }
        
    def sell_item(self, inventory_index: int) -> Dict[str, Any]:
        """Sell an item from player inventory"""
        if inventory_index < 0 or inventory_index >= len(self.player_inventory):
            return {
                "success": False,
                "error": "Invalid inventory index"
            }
            
        item_data = self.player_inventory[inventory_index]
        item = item_data["item"]
        
        # Calculate sell price (usually 60-80% of purchase price)
        sell_multiplier = random.uniform(0.6, 0.8)
        sell_price = int(item_data["purchase_price"] * sell_multiplier)
        
        # Add currency back to player
        if item_data["currency_used"] == "fragments":
            self.player_fragments += sell_price
        else:
            self.player_time_salt += sell_price
            
        # Remove from inventory
        sold_item = self.player_inventory.pop(inventory_index)
        
        # Record transaction
        transaction = {
            "type": "sale",
            "item_name": item["name"],
            "sell_price": sell_price,
            "currency": item_data["currency_used"],
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
        self.transaction_history.append(transaction)
        
        return {
            "success": True,
            "item_sold": item["name"],
            "price_received": sell_price,
            "currency_received": item_data["currency_used"],
            "remaining_fragments": self.player_fragments,
            "remaining_time_salt": self.player_time_salt
        }
        
    def get_market_status(self) -> Dict[str, Any]:
        """Get current market status"""
        available_items = []
        for item_id, item in self.items.items():
            available_items.append({
                "item_id": item_id,
                "name": item.name,
                "type": item.item_type,
                "current_price": item.current_price,
                "base_price": item.base_price,
                "quality": round(item.quality, 2),
                "rarity": item.rarity,
                "demand": round(item.demand, 2),
                "supply": round(item.supply, 2)
            })
            
        return {
            "market_volatility": round(self.market_volatility, 2),
            "supply_demand_factor": round(self.supply_demand_factor, 2),
            "available_items": available_items,
            "player_resources": {
                "fragments": self.player_fragments,
                "time_salt": self.player_time_salt,
                "inventory_count": len(self.player_inventory)
            },
            "recent_transactions": len(self.transaction_history)
        }
        
    def update_market_dynamics(self):
        """Update market prices and dynamics"""
        # Global market volatility
        volatility_change = random.uniform(-0.05, 0.05)
        self.market_volatility = max(0.1, min(0.9, self.market_volatility + volatility_change))
        
        # Update each item
        for item in self.items.values():
            # Supply and demand fluctuation
            supply_change = random.uniform(-0.1, 0.1) * self.market_volatility
            demand_change = random.uniform(-0.1, 0.1) * self.market_volatility
            
            item.supply = max(0.1, min(1.0, item.supply + supply_change))
            item.demand = max(0.1, min(1.0, item.demand + demand_change))
            
            # Price adjustment
            market_factor = (1.0 + item.demand - item.supply) * self.supply_demand_factor
            volatility_factor = 1.0 + (random.uniform(-0.1, 0.1) * item.volatility)
            
            new_price = int(item.base_price * market_factor * volatility_factor)
            item.current_price = max(1, new_price)  # Minimum price of 1
            
    def generate_special_offer(self) -> Dict[str, Any]:
        """Generate a special limited-time market offer"""
        offer_types = [
            "flash_sale",
            "rare_item_auction",
            "bulk_discount",
            "currency_exchange_bonus",
            "mystery_box"
        ]
        
        offer_type = random.choice(offer_types)
        
        if offer_type == "flash_sale":
            # Random item at 50% off
            item_id = random.choice(list(self.items.keys()))
            item = self.items[item_id]
            
            return {
                "type": "flash_sale",
                "item_id": item_id,
                "item_name": item.name,
                "original_price": item.current_price,
                "sale_price": int(item.current_price * 0.5),
                "duration_minutes": random.randint(5, 15),
                "description": f"Flash sale on {item.name}! 50% off for limited time!"
            }
            
        elif offer_type == "mystery_box":
            return {
                "type": "mystery_box",
                "price": random.randint(25, 75),
                "currency": random.choice(["fragments", "time_salt"]),
                "potential_rewards": [
                    "rare memory fragments",
                    "unique glyph shards", 
                    "temporal artifacts",
                    "void essences"
                ],
                "duration_minutes": random.randint(10, 30),
                "description": "Mystery box containing unknown treasures from the drift!"
            }
            
        return {
            "type": "no_offer",
            "description": "No special offers available at this time"
        }
        
    def export_state(self) -> Dict[str, Any]:
        """Export market system state"""
        return {
            "market_volatility": self.market_volatility,
            "supply_demand_factor": self.supply_demand_factor,
            "player_fragments": self.player_fragments,
            "player_time_salt": self.player_time_salt,
            "player_inventory": self.player_inventory.copy(),
            "transaction_history": self.transaction_history.copy(),
            "items_state": {
                item_id: {
                    "current_price": item.current_price,
                    "demand": item.demand,
                    "supply": item.supply,
                    "quality": item.quality
                }
                for item_id, item in self.items.items()
            }
        }
        
    def import_state(self, state_data: Dict[str, Any]):
        """Import market system state"""
        self.market_volatility = state_data.get("market_volatility", 0.5)
        self.supply_demand_factor = state_data.get("supply_demand_factor", 1.0)
        self.player_fragments = state_data.get("player_fragments", 50)
        self.player_time_salt = state_data.get("player_time_salt", 100)
        self.player_inventory = state_data.get("player_inventory", [])
        self.transaction_history = state_data.get("transaction_history", [])
        
        # Update item states
        items_state = state_data.get("items_state", {})
        for item_id, item_data in items_state.items():
            if item_id in self.items:
                item = self.items[item_id]
                item.current_price = item_data.get("current_price", item.base_price)
                item.demand = item_data.get("demand", 0.5)
                item.supply = item_data.get("supply", 0.5)
                item.quality = item_data.get("quality", item.quality)