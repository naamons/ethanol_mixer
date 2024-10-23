import streamlit as st

# Function to calculate ethanol and base fuel amounts needed
def calculate_ethanol_mix(current_fuel_level, current_ethanol_content, tank_size, target_ethanol_content, base_fuel_ethanol_content):
    current_fuel_ethanol = (current_fuel_level / 100) * (current_ethanol_content / 100) * tank_size
    current_gasoline = (current_fuel_level / 100) * tank_size - current_fuel_ethanol
    
    # Total ethanol needed in the final mix
    total_needed_ethanol = (target_ethanol_content / 100) * tank_size
    
    # Ethanol we need to add
    ethanol_to_add = total_needed_ethanol - current_fuel_ethanol
    
    # Total amount of fuel to be added
    fuel_to_add = tank_size - (current_fuel_level / 100) * tank_size
    
    # Amount of E85 to add (since E85 is 85% ethanol)
    e85_needed = ethanol_to_add / 0.85
    
    # Amount of base fuel to add (remaining portion)
    base_fuel_needed = fuel_to_add - e85_needed
    
    # Adjust if more base fuel is needed than available
    if base_fuel_needed < 0:
        e85_needed = fuel_to_add
        base_fuel_needed = 0
    
    return e85_needed, base_fuel_needed

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
