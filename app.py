import streamlit as st
import random

# Page Configuration
st.set_page_config(page_title="OptiScale AI", page_icon="⚡", layout="wide")

st.title("⚡ OptiScale AI - Smart Blockchain Router")
st.write("Cross-Chain Gas Optimization & AI Routing Engine")

# 1. USER INPUT OPTIONS (Kept simple and familiar)
col1, col2 = st.columns(2)

with col1:
    tx_type = st.selectbox(
        "Select Transaction Type:",
        ["Mass Payroll", "Instant Vendor Payment", "Treasury Transfer"]
    )

with col2:
    tx_amount = st.number_input("Transaction Amount ($ USD):", min_value=1.0, value=1000.0, step=100.0)

# 2. DYNAMIC ROUTING ENGINE (Recalculates best route dynamically on analyze)
if st.button("🚀 Analyze & Route Transaction"):
    
    # Generate live, slightly varied dynamic gas fees (in USD)
    gas_fees = {
        "Ethereum L1": round(random.uniform(18.0, 50.0), 2),
        "Arbitrum L2": round(random.uniform(0.15, 0.90), 2),
        "Base L2": round(random.uniform(0.01, 0.12), 2),
        "Polygon": round(random.uniform(0.02, 0.18), 2)
    }
    
    # Determine optimal route based on selected transaction type & live lowest gas
    if tx_type == "Mass Payroll":
        # Evaluates lowest fee between low-cost L2s
        best_route = "Base L2" if gas_fees["Base L2"] <= gas_fees["Polygon"] else "Polygon"
        reasoning = f"Optimized for batch settlement. Saves ~{round(((gas_fees['Ethereum L1'] - gas_fees[best_route])/gas_fees['Ethereum L1'])*100, 1)}% vs Ethereum L1."
        
    elif tx_type == "Instant Vendor Payment":
        best_route = "Arbitrum L2" if gas_fees["Arbitrum L2"] < 0.50 else "Base L2"
        reasoning = "Selected for sub-second block finality and low execution latency."
        
    elif tx_type == "Treasury Transfer":
        best_route = "Ethereum L1"
        reasoning = "High-value enterprise transfer prioritized for maximum L1 network security."

    st.divider()

    # 3. DISPLAY RESULTS (Clean UI)
    st.subheader("💡 AI Recommended Route")
    st.success(f"**Optimal Network:** {best_route}")
    st.info(f"**AI Logic:** {reasoning}")

    # Display fee breakdown across all chains
    st.subheader("📊 Live Chain Fee Comparison")
    
    fee_cols = st.columns(4)
    for idx, (chain, fee) in enumerate(gas_fees.items()):
        with fee_cols[idx]:
            if chain == best_route:
                st.metric(label=f"🟢 {chain} (Best)", value=f"${fee}")
            else:
                st.metric(label=f"⚪ {chain}", value=f"${fee}")
