import streamlit as st

# Function to calculate the required volumes of E85 and base fuel (93E10)
def calculate_ethanol_mix(current_fuel_level, current_ethanol_content, tank_size, target_ethanol_content, base_fuel_ethanol_content):
    current_fuel_volume = (current_fuel_level / 100) * tank_size
    current_ethanol = current_fuel_volume * (current_ethanol_content / 100)
    total_ethanol_needed = (target_ethanol_content / 100) * tank_size
    ethanol_to_add = total_ethanol_needed - current_ethanol
    fuel_to_add = tank_size - current_fuel_volume

    # Solve for the volumes of E85 and base fuel
    # Using the ethanol balance equation and total fuel equation
    if fuel_to_add > 0:
        V1 = (ethanol_to_add - fuel_to_add * (base_fuel_ethanol_content / 100)) / (0.85 - (base_fuel_ethanol_content / 100))
        V2 = fuel_to_add - V1

        if V1 < 0:
            V1 = 0
            V2 = fuel_to_add
        elif V2 < 0:
            V2 = 0
            V1 = fuel_to_add
    else:
        V1, V2 = 0, 0

    return V1, V2

# Streamlit UI
st.title("Ethanol Content Calculator")

# Input fields for the user
current_fuel_level = st.slider("Current Fuel Level (%)", 0, 100, 50)
current_ethanol_content = st.slider("Current Ethanol Content (%)", 0, 100, 10)
tank_size = st.number_input("Fuel Tank Size (gallons)", value=15.0)
target_ethanol_content = st.slider("Target Ethanol Content (%)", 0, 100, 30)
base_fuel_ethanol_content = st.slider("Ethanol % of Base Fuel (E.g., 93E10 = 10%)", 0, 100, 10)

# Calculate the fuel mix
if st.button("Calculate"):
    e85_needed, base_fuel_needed = calculate_ethanol_mix(current_fuel_level, current_ethanol_content, tank_size, target_ethanol_content, base_fuel_ethanol_content)
    
    # Display the results
    st.write(f"Add **{e85_needed:.2f} gallons** of E85.")
    st.write(f"Add **{base_fuel_needed:.2f} gallons** of 93E{base_fuel_ethanol_content}.")
