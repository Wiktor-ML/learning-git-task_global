import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont

class ShoppingListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping List")
        self.root.geometry("600x500")  # Set window size
        self.root.configure(bg="#f0f0f0")  # Light gray background
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Use 'clam' theme for modern look
        self.style.configure("Treeview",
                           background="#ffffff",
                           fieldbackground="#ffffff",
                           foreground="#333333",
                           rowheight=30,
                           font=('Helvetica', 10))
        self.style.configure("Treeview.Heading",
                           font=('Helvetica', 11, 'bold'),
                           padding=5)
        
        # Shopping dictionary
        self.shopping_list = {
            "bakery": ["bread", "rolls", "donuts"],
            "greengrocer": ["carrot", "celery", "arugula"]
        }
        
        # Create main frame with padding
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Add title label
        title_font = tkfont.Font(family="Helvetica", size=16, weight="bold")
        self.title_label = ttk.Label(
            self.main_frame,
            text="Shopping List",
            font=title_font,
            padding="0 0 20 0"
        )
        self.title_label.grid(row=0, column=0, columnspan=2)
        
        # Create and configure the treeview
        self.tree = ttk.Treeview(self.main_frame, columns=("Items",), height=8)
        self.tree.heading("#0", text="Store")
        self.tree.heading("Items", text="Products")
        self.tree.column("#0", width=150, minwidth=150)
        self.tree.column("Items", width=400, minwidth=300)
        self.tree.grid(row=1, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=self.tree.yview)
        scrollbar.grid(row=1, column=2, sticky=(tk.N, tk.S))
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Populate treeview
        for shop, items in self.shopping_list.items():
            capitalized_items = [item.capitalize() for item in items]
            self.tree.insert("", tk.END, text=shop.capitalize(), 
                           values=(", ".join(capitalized_items),))
        
        # Modify the controls frame to include delete functionality
        self.controls_frame = ttk.Frame(self.main_frame, padding="10")
        self.controls_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        # Add buttons frame
        self.buttons_frame = ttk.Frame(self.main_frame, padding="10")
        self.buttons_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        # Add delete button
        self.delete_button = ttk.Button(
            self.buttons_frame,
            text="Delete Store",
            command=self.delete_selected_shop,
            style="Accent.TButton"
        )
        self.delete_button.grid(row=0, column=0, padx=5)
        
        # Style for the delete button
        self.style.configure(
            "Accent.TButton",
            background="#ff4444",
            foreground="white",
            padding=5
        )
        
        # Move add controls to a new row
        self.add_controls_frame = ttk.Frame(self.main_frame, padding="10")
        self.add_controls_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        # Add entry fields for new items (moved to new frame)
        self.shop_var = tk.StringVar()
        self.item_var = tk.StringVar()
        
        ttk.Label(self.add_controls_frame, text="New Store:").grid(row=0, column=0, padx=5)
        self.shop_entry = ttk.Entry(self.add_controls_frame, textvariable=self.shop_var)
        self.shop_entry.grid(row=0, column=1, padx=5)
        
        ttk.Label(self.add_controls_frame, text="New Product:").grid(row=0, column=2, padx=5)
        self.item_entry = ttk.Entry(self.add_controls_frame, textvariable=self.item_var)
        self.item_entry.grid(row=0, column=3, padx=5)
        
        # Add button (moved to new frame)
        self.add_button = ttk.Button(self.add_controls_frame, text="Add", command=self.add_item)
        self.add_button.grid(row=0, column=4, padx=5)
        
        # Move total label to last row
        self.total_label = ttk.Label(
            self.main_frame,
            text=f"Total products: {sum(len(items) for items in self.shopping_list.values())}",
            font=tkfont.Font(family="Helvetica", size=12),
            padding="20 10"
        )
        self.total_label.grid(row=4, column=0, columnspan=2)
        
        # Configure grid weights
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)

    def add_item(self):
        shop = self.shop_var.get().strip()
        item = self.item_var.get().strip()
        
        if shop and item:
            # Update dictionary
            if shop.lower() in self.shopping_list:
                self.shopping_list[shop.lower()].append(item.lower())
            else:
                self.shopping_list[shop.lower()] = [item.lower()]
            
            # Clear tree
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            # Repopulate tree
            for shop, items in self.shopping_list.items():
                capitalized_items = [item.capitalize() for item in items]
                self.tree.insert("", tk.END, text=shop.capitalize(), 
                               values=(", ".join(capitalized_items),))
            
            # Update total count
            total_items = sum(len(items) for items in self.shopping_list.values())
            self.total_label.configure(text=f"Total products: {total_items}")
            
            # Clear entry fields
            self.shop_var.set("")
            self.item_var.set("")

    def delete_selected_shop(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return
            
        # Get the shop name from the selected item
        shop_name = self.tree.item(selected_item[0])['text'].lower()
        
        # Remove from dictionary
        if shop_name in self.shopping_list:
            del self.shopping_list[shop_name]
            
        # Remove from treeview
        self.tree.delete(selected_item)
        
        # Update total count
        total_items = sum(len(items) for items in self.shopping_list.values())
        self.total_label.configure(text=f"Total products: {total_items}")

def main():
    root = tk.Tk()
    app = ShoppingListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
