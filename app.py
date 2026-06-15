import streamlit as st

st.set_page_config(
    page_title="IPL Match Outcome Analysis", page_icon="🏏", layout="wide"
)

st.title("IPL Match Outcome Analysis (2008–2024)")
st.subheader("Understanding Pressure, Play Style, and Team Success")

st.markdown("""
This project investigates the factors associated with success in the Indian Premier League (IPL) using ball-by-ball and match-level data from 2008–2024.

### Key Findings

- Teams winning the dot-ball battle won 69.6% of matches.
- Venue effects were stronger than toss effects.
- Death overs most consistently favored winners.
- Teams strong in both batting and bowling achieved the highest win rates.
- Teams weak in both disciplines achieved the lowest win rates.
""")

st.divider()

st.header("1. Venue and Toss Effects")

st.markdown("""
### Research Question

Do venue conditions and toss outcomes influence IPL match results?

### Findings

- Winning the toss provides a measurable advantage.
- However, the effect size is relatively weak.
- Venue effects are stronger than toss effects.
- Chasing advantage is venue dependent rather than universal.

Examples observed during analysis:

- Some venues consistently favored chasing teams.
- Other venues showed stronger batting-first success rates.

### Statistical Validation

- Chi-Square Test of Independence
- Cramér's V

### Key Takeaway

While toss decisions matter, venue characteristics provide substantially more explanatory power when evaluating IPL match outcomes.
""")

st.divider()

st.header("2. Dot Ball Impact")

st.image("plots/dot_ball_win_rate.png", width="stretch")

st.markdown("""
### Finding

Teams winning the dot-ball battle won **69.6%** of IPL matches.

The relationship strengthened as dot-ball differential increased:

- 0–5% differential → 58.6% win rate
- 5–10% differential → 72.1% win rate
- 10–15% differential → 90.4% win rate
- 15%+ differential → 97.1% win rate

This suggests dot-ball pressure is strongly associated with match success.
""")

st.divider()

st.header("3. Dot Ball Impact by Phase")

st.image("plots/dot_ball_phase_seperation.png", width="stretch")

st.markdown("""
### Separation Analysis

Winner-loser dot-ball percentage separation was largest in:

- Middle Overs
- Powerplay

and smallest in:

- Death Overs

This suggests teams often establish performance gaps earlier in the innings.
""")

st.image("plots/winner_win%_by_phase.png", width="stretch")

st.markdown("""
### Winner Advantage Analysis

A second perspective examined where match winners most consistently gained the dot-ball advantage.

Results:

- Death Overs: 65.0%
- Powerplay: 60.2%
- Middle Overs: 56.1%

Middle overs create separation, while death overs most consistently favor winners.
""")

st.divider()

st.header("4. Batting Archetypes")

st.image("plots/dot_ball_boundary_tradeoff.png", width="stretch")

st.markdown("""
### Research Question

Can teams be grouped into meaningful batting styles associated with success?

### Findings

Teams were classified using:

- Dot Ball %
- Boundary %

The weakest batting archetype was:

**High Dot Ball % + Low Boundary %**

Average win rate:

**43.24%**

The strongest batting archetype was:

**Low Dot Ball % + High Boundary %**

Average win rate:

**52.36%**

Boundary hitting partially compensated for dot-ball pressure, but teams that frequently consumed deliveries without scoring and failed to hit boundaries consistently performed worst.
""")

st.divider()

st.header("5. Bowling Archetypes")

st.image("plots/dot_ball_boundary_tradeoff_bowlers_view.png", width="stretch")

st.markdown("""
### Research Question

Can the same framework explain success from the bowling perspective?

### Findings

Teams were classified using:

- Dot Balls Forced %
- Boundary Conceded %

The strongest bowling profiles consistently forced dot-ball pressure.

The weakest bowling profiles:

- Forced fewer dot balls
- Conceded more boundaries

Bowling archetypes showed a performance spread similar to batting archetypes, suggesting that batting and bowling contribute similarly to team success.

Most importantly, the recurring signal remained the same:

**Pressure creation through dot balls.**
""")

st.divider()

st.header("6. Combined Archetypes")

st.image("plots/batting_bowling_interaction_heatmap.png", width="stretch")

st.markdown("""
### Research Question

Can batting compensate for poor bowling?

Can bowling compensate for poor batting?

### Results

| Quadrant | Avg Win % |
|-----------|-----------:|
| Good Batting, Good Bowling | 55.76 |
| Good Batting, Poor Bowling | 45.95 |
| Poor Batting, Good Bowling | 44.78 |
| Poor Batting, Poor Bowling | 23.81 |

### Statistical Validation

- Kruskal-Wallis: H = 27.32
- p < 0.001

Post-hoc analysis showed:

Good Batting + Poor Bowling ≈ Poor Batting + Good Bowling

(adjusted p ≈ 0.95)

### Key Finding

A single weakness is survivable.

Two weaknesses are catastrophic.

Teams that were weak in both batting and bowling performed dramatically worse than every other group.
""")

st.divider()

st.header("Key Takeaways")

st.header("Key Takeaways")

st.markdown("""
1. Dot-ball pressure is one of the strongest recurring indicators of IPL success.

2. Venue effects are more influential than toss effects.

3. Different innings phases contribute differently to match outcomes.

4. Batting and bowling archetypes independently separate successful and unsuccessful teams.

5. Teams with one weakness remain competitive.

6. Teams with weaknesses in both batting and bowling perform dramatically worse.

### Final Conclusion

Across venue analysis, phase analysis, batting archetypes, bowling archetypes, and combined team archetypes, the same pattern repeatedly emerged:

**Successful IPL teams create pressure through dot balls while minimizing pressure in their own innings.**
""")
