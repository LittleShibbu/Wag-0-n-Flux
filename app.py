import gradio as gr
import pandas as pd

def calculate_wagonflux_deal(origin, destination):
    # Dummy Data: Real world mein ye SQL table se aayega
    data = [
        {"id": "WF-101", "from": "Mumbai", "to": "Pune", "base_price": 25000},
        {"id": "WF-102", "from": "Delhi", "to": "Jaipur", "base_price": 35000},
        {"id": "WF-103", "from": "Bangalore", "to": "Hyderabad", "base_price": 40000},
    ]
    
    df = pd.DataFrame(data)
    match = df[(df["from"] == origin) & (df["to"] == destination)]
    
    if match.empty:
        return "❌ No Return Trucks found for this route.", None
    
    # logic for 75% less price (Return Trip Optimization)
    original = match.iloc[0]["base_price"]
    wf_price = original * 0.25 # 75% Discount applied
    savings = original - wf_price
    
    summary = f"""
    ### 🚚 WagonFlux Optimized Route Found!
    **Truck ID:** {match.iloc[0]['id']}
    **Standard Market Rate:** ₹{original}
    **WagonFlux Return Rate:** ₹{wf_price} (75% OFF)
    **You Save:** ₹{savings}
    """
    return summary, match

# UI Layout
with gr.Blocks(title="WagonFlux") as demo:
    gr.Markdown("# 🚀 WagonFlux: Low-Cost Return Logistics")
    with gr.Row():
        source = gr.Textbox(label="Pickup City")
        dest = gr.Textbox(label="Drop City")
    
    btn = gr.Button("Find Return Deals", variant="primary")
    out_text = gr.Markdown()
    
    btn.click(calculate_wagonflux_deal, inputs=[source, dest], outputs=[out_text])

if __name__ == "__main__":
    demo.launch()
