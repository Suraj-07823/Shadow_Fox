#  Cricket Fielding Analysis - ShadowFox Internship
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load Dataset
df = pd.read_excel("IPL sample data.xlsx", skiprows=4)
df = df.dropna(subset=["Player Name"])
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

# Step 2: Clean Data
df = df[~df["Player Name"].str.contains("Catches|Runs|Pick|Throw", case=False, na=False)]
df["Pick"] = df["Pick"].astype(str).str.lower().str.strip()

# Step 3: Define Weights
weights = {
    "y": 2, "n": -1,
    "clean pick": 2,
    "good throw": 3,
    "catch": 10,
    "drop catch": -5,
    "stumping": 8,
    "run out": 12,
    "missed run out": -3,
    "direct hit": 6
}

# Step 4: Calculate Player Stats
player_stats = df.groupby("Player Name")["Pick"].value_counts().unstack(fill_value=0)

def calculate_score(row):
    score = 0
    for action, weight in weights.items():
        if action in row.index:
            score += row[action] * weight
    return score

player_stats["Performance Score"] = player_stats.apply(calculate_score, axis=1)

# Step 5: Top 5 Players
top_players = player_stats["Performance Score"].nlargest(5)
top_players.plot(kind="bar", color="skyblue", edgecolor="black", figsize=(8,5))
plt.title("Top 5 Fielders - Performance Score")
plt.ylabel("Performance Score")
plt.xlabel("Player")
plt.xticks(rotation=30, ha="right")
plt.show()

# Step 6: Save Results
player_stats.to_excel("fielding_scores.xlsx")
print(" Analysis complete. Results saved to fielding_scores.xlsx")
