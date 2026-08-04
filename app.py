import streamlit as st
import random

# 1. AI ROUTING LOGIC FUNCTION
def get_recommended_route(tx_type):
    # Simulated gas fees in USD
    gas_fees = {
        "Ethereum L1": round(random.uniform(15.0, 45.0), 2),
        "Arbitrum L2": round(random.uniform(0.10, 0.80), 2),
        "Base L2": round(random.uniform(0.01, 0.15), 2),
        "Polygon": round(random.uniform(0.02, 0.20), 2)
    }
    
    # Dynamic logic based on selected transaction type
    if tx_type == "Mass Payroll":
        best_route = "Base L2" if gas_fees["Base L2"] <= gas_fees["Polygon"] else "Polygon"
        reasoning = "Selected for maximum gas efficiency on bulk batch transactions."
        
    elif tx_type == "Instant Vendor Payment":
        best_route = "Arbitrum L2"
        reasoning = "Selected for ultra-low latency and instant block finality."
        
    elif tx_type == "Treasury Transfer":
        best_route = "Ethereum L1"
        reasoning = "Selected for maximum decentralization and protocol-level security."
        
    else:
        best_route = min(gas_fees, key=gas_fees.get)
        reasoning = "Selected as the absolute lowest cost network at this moment."
        
    return best_route, gas_fees, reasoning

# 2. STREAMLIT USER INTERFACE (UI)
st.title("OptiScale AI - Smart Routing Engine")

# User selects transaction type
tx_type = st.selectbox(
    "Select Transaction Type:",
    ["Mass Payroll", "Instant Vendor Payment", "Treasury Transfer"]
)

# Trigger dynamic AI route recommendation
if st.button("Find Optimal Route"):
    best_route, fees, reason = get_recommended_route(tx_type)
    
    # Display dynamic results
    st.success(f"**Recommended Route:** {best_route}")
    st.info(f"**AI Decision Logic:** {reason}")
    
    # Display gas fee comparisons
    st.subheader("Current Gas Fee Estimates:")
    for chain, fee in fees.items():
        st.write(f"- **{chain}:** ${fee}")
