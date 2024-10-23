import streamlit as st

# Function to calculate ethanol mix
def calculate_ethanol_mix(current_fuel_level, current_ethanol_content, tank_size, target_ethanol_content, base_fuel_ethanol_content):
    current_fuel_volume = (current_fuel_level / 100) * tank_size
    current_fuel_ethanol = (current_ethanol_content / 100) * current_fuel_volume
    fuel_to_add = tank_size - current_fuel_volume
    
    # The total ethanol required for the target ethanol content
    total_ethanol_needed = (target_ethanol_content / 100) * tank_size
    
    # Ethanol to add (subtract the current ethanol in the tank from the total needed)
    ethanol_to_add = total_ethanol_needed - current_fuel_ethanol
    
    # Solve for the amount of E85 and base fuel needed
    # Let's denote: 
    # - V1 is the amount of E85 (ethanol content = 85%)
    # - V2 is the amount of base fuel (ethanol content varies, e.g., 10% for 93E10)
    
    # Formula: (V1 * 85%) + (V2 * base_fuel_ethanol_content%) = Ethanol needed
    # The total fuel added V1 + V2 = fuel_to_add
    # Thus, V2 = fuel_to_add - V1
    # Substitute V2 in the first equation and solve for V1
    
    V1 = ethanol_to_add / (0.85 - (base_fuel_ethanol_content / 100))
    V2 = fuel_to_add - V1
    
    # If V2 is negative, adjust to ensure no negative values
    if V2 < 0:
        V1 = fuel_to_add
        V2 = 0
    
    return V1, V2

# Streamlit UI
st.title("Ethanol Content Calculator")

# Input fields for the user
current_fuel_level = st.slider("Current Fuel Level (%)", 0, 100, 50)
current_ethanol_content = st.slider("Current Ethanol Content (%)", 10, 85, 10)
tank_size = st.number_input("Fuel Tank Size (gallons)", value=15.0)
target_ethanol_content = st.slider("Target Ethanol Content (%)", 10, 85, 30)
base_fuel_ethanol_content = st.slider("Ethanol % of Base Fuel (E.g., 93E10 = 10%)", 0, 15, 10)

# Calculate the fuel mix
if st.button("Calculate"):
    e85_needed, base_fuel_needed = calculate_ethanol_mix(current_fuel_level, current_ethanol_content, tank_size, target_ethanol_content, base_fuel_ethanol_content)
    
    # Display the results
    st.write(f"Add **{e85_needed:.2f} gallons** of E85.")
    st.write(f"Add **{base_fuel_needed:.2f} gallons** of 93E{base_fuel_ethanol_content}.")
