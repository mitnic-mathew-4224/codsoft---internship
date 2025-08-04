import tkinter as tk
from recommender import recommend_items

# Create main window
root = tk.Tk()
root.title("Smart Recommender")
root.geometry("400x400")
root.config(bg="#f5f5f5")

# Header label
header = tk.Label(root, text="Smart Recommendation System", font=("Helvetica", 16, "bold"), bg="#f5f5f5")
header.pack(pady=20)

# Input label and entry
input_label = tk.Label(root, text="Enter a product you like:", font=("Helvetica", 12), bg="#f5f5f5")
input_label.pack(pady=5)

user_input = tk.Entry(root, font=("Helvetica", 12), width=30)
user_input.pack(pady=10)

# Output box
output_label = tk.Label(root, text="Recommendations:", font=("Helvetica", 12, "bold"), bg="#f5f5f5")
output_label.pack(pady=10)

output_box = tk.Text(root, height=8, width=40, font=("Helvetica", 11), wrap=tk.WORD, state=tk.DISABLED)
output_box.pack()

# Recommend button
def show_recommendations():
    item = user_input.get().strip()
    recommendations = recommend_items(item)
    
    output_box.config(state=tk.NORMAL)
    output_box.delete("1.0", tk.END)
    
    if recommendations:
        output_box.insert(tk.END, "\n".join(recommendations))
    else:
        output_box.insert(tk.END, "No recommendations found.")
    
    output_box.config(state=tk.DISABLED)

recommend_btn = tk.Button(root, text="Get Recommendations", command=show_recommendations, font=("Helvetica", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
recommend_btn.pack(pady=20)

root.mainloop()
a
