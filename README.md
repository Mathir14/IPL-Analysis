# IPL Match Outcome Analysis: Understanding Pressure and Team Success
## Live Dashboard

[View Dashboard](https://iplanalysis-mathir14.streamlit.app/)
## Executive Summary

This project analyzes IPL matches from 2008–2024 to identify factors associated with team and match success.

The investigation begins with contextual factors (venue and toss), progresses through match-level pressure metrics (dot-ball dominance), and culminates in batting and bowling archetypes that describe how successful teams create and respond to pressure.

### Core Finding

Teams that consistently create pressure through dot balls while avoiding pressure in their own innings achieve substantially higher win rates. A weakness in either batting or bowling is survivable; weaknesses in both are not.

---

## Dataset

- IPL seasons: 2008–2024
- Ball-by-ball match data
- Match-level outcomes
- Team-season aggregations
- 146 team-seasons analyzed

---

## Research Questions & Findings

### 1. Do venue and toss influence match outcomes?

#### Findings

- Winning the toss provides a measurable but limited advantage.
- Teams that win the toss win more often than they lose.
- Venue effects are stronger than toss effects.
- Chasing advantage is venue-dependent rather than universal.

#### Validation

- Chi-Square Test of Independence
- Cramér's V

**Conclusion:** Toss advantage is real but weak. Venue characteristics have a stronger influence on match outcomes.

---

### 2. Does winning the dot-ball battle increase the probability of winning?

#### Findings

Teams winning the dot-ball battle won **69.6%** of IPL matches.

| Dot Ball Differential | Win Rate |
|----------------------|----------|
| 0–5% | 58.6% |
| 5–10% | 72.1% |
| 10–15% | 90.4% |
| 15%+ | 97.1% |

#### Conclusion

The relationship is not binary. Larger dot-ball advantages correspond to dramatically higher win rates.

---

### 3. Which innings phase matters most?

#### Findings

Two complementary perspectives emerged:

##### Separation Magnitude

Middle Overs and Powerplays create the largest winner-loser dot-ball separations.

##### Winner Advantage Frequency

Death Overs are where winners most consistently gain the dot-ball advantage.

#### Statistical Validation

- Friedman Test
- Wilcoxon Signed-Rank Test
- Cochran's Q Test
- McNemar Test

#### Conclusion

Different phases contribute differently to success. Middle Overs create separation, while Death Overs most consistently favor winners.

---

### 4. What batting profiles are associated with success?

#### Batting Archetypes

| Archetype | Avg Win % |
|------------|-----------:|
| Low Dot, High Boundary | 52.36 |
| Low Dot, Low Boundary | 50.82 |
| High Dot, High Boundary | 50.60 |
| High Dot, Low Boundary | 43.24 |

#### Findings

- Dot Ball % and Boundary % exhibit a strong inverse relationship.
- Boundary hitting can partially compensate for dot-ball pressure.
- High Dot + Low Boundary is the weakest batting profile.
- Batting quality alone does not fully explain team success.

#### Conclusion

Batting metrics describe successful offensive profiles but are insufficient to fully explain winning.

---

### 5. What bowling profiles are associated with success?

#### Bowling Archetypes

| Archetype | Avg Win % |
|------------|-----------:|
| High Dot, High Boundary Prevention | 53.10 |
| High Dot, Low Boundary Prevention | 52.06 |
| Low Dot, Low Boundary Prevention | 48.32 |
| Low Dot, High Boundary Conceded | 44.63 |

#### Findings

- Teams forcing dot balls consistently performed better.
- Dot-ball pressure emerged as the strongest recurring signal.
- The bowling perspective largely confirmed batting-side findings.

#### Conclusion

Pressure creation through dot balls is a more consistent indicator than boundary prevention alone.

---

### 6. Can batting compensate for poor bowling?

### 7. Can bowling compensate for poor batting?

#### Combined Archetype Analysis

| Quadrant | Avg Win % |
|-----------|-----------:|
| Good Batting, Good Bowling | 55.76 |
| Good Batting, Poor Bowling | 45.95 |
| Poor Batting, Good Bowling | 44.78 |
| Poor Batting, Poor Bowling | 23.81 |

#### Statistical Validation

##### Kruskal-Wallis Test

- H = 27.32
- p < 0.001

##### Dunn's Post-Hoc Test

Key Result:

- Good Batting + Poor Bowling vs Poor Batting + Good Bowling
- Adjusted p ≈ 0.95

#### Findings

- Teams strong in both disciplines perform best.
- Teams weak in both disciplines perform worst.
- Teams with one weakness remain competitive.
- Batting and bowling weaknesses are similarly damaging when considered independently.

#### Notable Observation

Only three team-seasons fell into the Poor Batting + Poor Bowling quadrant:

- Delhi Capitals (2014)
- Punjab Kings (2015)
- Delhi Capitals (2023)

---

## Key Findings

1. Dot-ball pressure is one of the strongest recurring indicators of success in IPL matches.
2. Venue effects are more influential than toss effects.
3. The impact of dot-ball pressure depends on innings phase.
4. Batting and bowling archetypes independently separate successful and unsuccessful teams.
5. Teams with one weakness remain competitive.
6. Teams with weaknesses in both batting and bowling perform dramatically worse.
7. Batting and bowling weaknesses are similarly damaging when only one weakness exists.

---

## Statistical Methods

- Chi-Square Test of Independence
- Cramér's V
- Friedman Test
- Wilcoxon Signed-Rank Test
- Cochran's Q Test
- McNemar Test
- Kruskal-Wallis Test
- Dunn's Post-Hoc Test

---

## Tools

- Python
- Polars
- SciPy
- Seaborn
- Matplotlib
- Jupyter Notebook
- Metabase

---

## Repository Structure

```text
1_venue_toss_effect.ipynb
2_dot_ball_impact.ipynb
3_dot_ball_advantage_by_phase.ipynb
4_batting_archetypes.ipynb
5_bowling_archetypes.ipynb
6_overall_archetypes_comparison.ipynb

plots/
README.md
```

## Final Conclusion

Across multiple independent analyses, the same theme repeatedly emerged:

**Pressure matters.**

Teams that consistently create pressure through dot balls while minimizing pressure in their own innings achieve superior long-term outcomes. While venue and toss influence results, team ability to create and manage pressure provides the strongest and most consistent explanation for success in the IPL dataset.
