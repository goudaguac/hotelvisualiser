# app.py

import streamlit as st
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def calculate_max_rooms(site_area, room_area):
    return math.floor(site_area / room_area)

def calculate_site_dimensions(site_area):
    # Assume a simple rectangular site with width:length ratio ~1:2
    width = math.sqrt(site_area / 2)
    length = 2 * width
    return width, length

def generate_room_positions(site_width, site_length, room_width, room_length):
    rooms = []
    rows = int(site_width // room_width)
    cols = int(site_length // room_length)
    for i in range(rows):
        for j in range(cols):
            x = i * room_width
            y = j * room_length
            rooms.append((x, y))
    return rooms

# --- Streamlit App ---

st.title("Hotel Room Packing Prototype")
st.write(
    """
    🏨 **Goal:** Fit as many identical guest rooms as possible into a given site area.
    - Assumes rooms are rectangular and packed in rows along a corridor.
    - This is a super simple feasibility check — no cores, stairs, or code rules yet.
    """
)

site_area = st.number_input("Enter site area (sqm)", value=1000)
room_area = st.number_input("Enter single guest room area (sqm)", value=25)

max_rooms = calculate_max_rooms(site_area, room_area)
site_width, site_length = calculate_site_dimensions(site_area)

# Assume room dimensions for visual: 5m x 5m = 25 sqm
room_width = math.sqrt(room_area)
room_length = room_width

room_positions = generate_room_positions(site_width, site_length, room_width, room_length)

st.success(f"✅ Maximum rooms that fit: {max_rooms}")

# --- Plot ---
fig, ax = plt.subplots(figsize=(8, 4))
# Draw site boundary
ax.add_patch(patches.Rectangle((0, 0), site_width, site_length, fill=False, edgecolor='black', linewidth=2))

# Draw rooms
for (x, y) in room_positions:
    ax.add_patch(
        patches.Rectangle(
            (x, y),
            room_width,
            room_length,
            fill=True,
            edgecolor='blue',
            facecolor='lightblue'
        )
    )

ax.set_xlim(0, site_width)
ax.set_ylim(0, site_length)
ax.set_aspect('equal')
ax.set_title('Room Layout Visualization')
st.pyplot(fig)
