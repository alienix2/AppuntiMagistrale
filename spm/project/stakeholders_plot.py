import matplotlib.pyplot as plt

adjusted_stakeholders = [
    {"name": "Investors/Funders", "power": 3, "influence": 3},
    {"name": "Project Team", "power": 2.9, "influence": 2.9},
    {"name": "Users (Physically Challenged Individuals)", "power": 2.1, "influence": 3},
    {"name": "Regulatory Authorities", "power": 3, "influence": 1.9},
    {"name": "Healthcare Professionals", "power": 2, "influence": 2},
    {"name": "Accessibility Advocates", "power": 1.1, "influence": 3},
    {"name": "Community Organizations", "power": 1, "influence": 2.1},
    {"name": "Marketing Team", "power": 1.2, "influence": 2},
    {"name": "Manufacturers/Suppliers", "power": 2, "influence": 1},
    {"name": "Technical Partners", "power": 2.1, "influence": 1.1},
    {"name": "Competitors", "power": 3, "influence": 2.85},  # Adjusted influence
    {"name": "Naysayers/Detractors", "power": 1.1, "influence": 1.9},  # Adjusted power
    {"name": "B2B Companies", "power": 2.8, "influence": 3},
]

# Extract the adjusted data points
adjusted_influences = [s["influence"] for s in adjusted_stakeholders]
adjusted_powers = [s["power"] for s in adjusted_stakeholders]
adjusted_names = [s["name"] for s in adjusted_stakeholders]

# Create the scatter plot with adjusted positions
plt.figure(figsize=(12, 8))

plt.scatter(
    adjusted_influences,
    adjusted_powers,
    color="dodgerblue",
    s=150,
    edgecolor="black",
    alpha=0.7,
    marker="o",
)


# Annotate each point with stakeholder names, adding offsets to avoid overlap
for i, name in enumerate(adjusted_names):
    plt.annotate(
        name,
        (adjusted_influences[i], adjusted_powers[i]),
        fontsize=9,
        ha="right"
        if adjusted_influences[i] > 1.5
        and (
            name != "Investors/Funders"
            and name != "Healthcare Professionals"
            and name != "B2B Companies"
        )
        else "left",
        va="bottom" if adjusted_powers[i] < 2 else "top",
        xytext=(3, 3),
        textcoords="offset points",
        bbox=dict(
            boxstyle="round,pad=0.3", edgecolor="gray", facecolor="white", alpha=0.6
        ),
    )

# Set plot labels and title with improved readability
plt.xlabel("Influence", fontsize=12, weight="bold")
plt.ylabel("Power", fontsize=12, weight="bold")
plt.title("Stakeholder Influence vs Power", fontsize=14, weight="bold")

# Set x and y axis limits and grid lines for readability
plt.xlim(0.5, 3.5)
plt.ylim(0.5, 3.5)
plt.grid(color="gray", linestyle="--", linewidth=0.5)

# Show the updated plot
plt.show()
