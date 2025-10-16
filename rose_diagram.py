# ===============================
# 1️⃣ Import Required Libraries
# ===============================
import numpy as np
import matplotlib.pyplot as plt

# ===============================
# 2️⃣ User Inputs
# ===============================

# Joint dip directions (in degrees)
# Example: three joint sets centered at 255°, 105°, and 210°
dip_directions = [255, 105, 210]

# Corresponding frequencies or counts
frequencies = [10, 8, 7]

# Width of each bar (in degrees)
bar_width_deg = 10

# Title for the plot
plot_title = "Joint Rose Diagram - Location 1"

# ===============================
# 3️⃣ Prepare Data
# ===============================

# Extend directions to include opposite sides (180° apart)
extended_directions = dip_directions + [(d + 180) % 360 for d in dip_directions]
extended_frequencies = frequencies + frequencies  # duplicate frequencies for symmetry

# Convert degrees to radians
extended_angles = np.radians(extended_directions)
bar_width = np.radians(bar_width_deg)

# ===============================
# 4️⃣ Compute Mean and Perpendicular Angles
# ===============================

# Compute circular mean for first two sets
mean_angle_rad = np.arctan2(
    np.sin(np.radians(dip_directions[:2])).sum(),
    np.cos(np.radians(dip_directions[:2])).sum()
)
mean_angle_deg = np.degrees(mean_angle_rad) % 360

# Bisecting and perpendicular directions
bisecting_angles = [mean_angle_deg, (mean_angle_deg + 180) % 360]
perpendicular_angles = [(mean_angle_deg + 90) % 360, (mean_angle_deg + 270) % 360]

# Print computed angles for clarity
print("Bisecting Angles (°):", [round(a, 2) for a in bisecting_angles])
print("Perpendicular Angles (°):", [round(a, 2) for a in perpendicular_angles])

# ===============================
# 5️⃣ Create Polar Plot
# ===============================
fig, ax = plt.subplots(figsize=(7, 7), subplot_kw={'projection': 'polar'})

# Plot bars
colors = ['#0077b6', '#ff6b6b', '#2ecc71'] * 2  # repeated for symmetry
bars = ax.bar(extended_angles, extended_frequencies, width=bar_width,
              color=colors, alpha=0.7, edgecolor='black', linewidth=1.2)

# Plot bisecting lines
for angle in bisecting_angles:
    ax.plot([np.radians(angle), np.radians(angle)],
            [0, max(frequencies) + 2],
            linestyle="--", linewidth=2, color="black", label="Bisecting Line")

# Plot perpendicular lines
for angle in perpendicular_angles:
    ax.plot([np.radians(angle), np.radians(angle)],
            [0, max(frequencies) + 2],
            linestyle=":", linewidth=2, color="purple", label="Perpendicular Line")

# ===============================
# 6️⃣ Customize the Plot
# ===============================
ax.set_theta_zero_location('N')     # 0° at North
ax.set_theta_direction(-1)          # Clockwise angles
ax.set_xticks(np.radians(np.arange(0, 360, 30)))
ax.set_rlabel_position(0)
ax.set_title(plot_title, va='bottom', fontsize=14, weight='bold')

# Avoid duplicate legend entries
handles, labels = ax.get_legend_handles_labels()
unique = dict(zip(labels, handles))
ax.legend(unique.values(), unique.keys(),
          loc='upper right', bbox_to_anchor=(1.2, 1.1))

# ===============================
# 7️⃣ Display
# ===============================
plt.tight_layout()
plt.show()
