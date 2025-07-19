# 🐶 Smart Dog Meal Planner (Research Reinforcement Learning)

**Optimizing dog nutrition using Reinforcement Learning (Proximal Policy Optimization)**  
A research-based intelligent system that generates personalized weekly meal plans for dogs based on breed, weight, age, emotional state, and more — continuously optimized using Reinforcement Learning.

Link to project thesis/report: https://drive.google.com/file/d/1JlD80QKPGG-kRRObAIDUvDGchm4g-ZVA/view?usp=sharing

Link to research paper: https://drive.google.com/file/d/1TX__wbJs4nwJruswwdhtpVpJwzgC1FJ2/view?usp=sharing

## 🧠 Project Overview

This system helps dog owners create optimal and adaptive meal plans tailored to each dog’s unique metabolism and health needs. It integrates:

- **Rule-Based Planning** for nutritional requirement estimation.
- **Reinforcement Learning (PPO)** for optimizing meal plans using user feedback.
- **Custom Meal Creation** with user-selected food items.
- **MongoDB** for managing nutritional datasets.
- **Docker & Flask API** for deployment and containerization.

---

## 📁 Project Structure

```
PPO-IMPL/               # PPO agent (PyTorch) and utilities
server/                 # MongoDB data insert + rule engine
plots/                  # Training curve visualizations
dockerfile              # Docker configuration
```

---

## 🔑 Key Features

### ✅ Rule-Based Engine

- Calculates dog's nutritional needs from breed, size, age, activity, pregnancy, and health.
- Uses real vet-approved datasets (vitamins, minerals, macros).
- Outputs: protein, fat, carb, energy, vitamin & mineral targets.

### 🤖 Reinforcement Learning

- **PPO-based agent** learns from weekly feedback.
- Adjusts nutrition targets using a custom reward system based on:
  - Weight trends
  - Emotional score
  - Body fat status

---

## 🚀 Getting Started

### 📦 Prerequisites

- Python 3.10+
- MongoDB (Atlas or Local)
- Docker (Optional)

### 🔧 Installation

```bash
git clone https://github.com/your-username/research-rl.git
cd research-rl
pip install -r PPO-IMPL/requirements.txt
```

### 📡 MongoDB Setup

Insert nutrition datasets:

```bash
python server/breed-size-dataInsert.py
python server/health-vitamin-dataInsert.py
python server/nutrition-protein-dataInsert.py
# ... and the rest
```

---

## 🧪 Running the System

### PPO Agent Training

```bash
python PPO-IMPL/main.py
```

### Or Using Docker

```bash
docker build -t research-rl .
docker run -it research-rl
```

### Rule Engine (Nutrition Calculation)

```bash
python server/meal-rule-engine.py
```

---

## 📊 Evaluation Summary

- **Rule-based planning**: 94% match to vet-recommended nutrition
- **RL Optimization (PPO)**: Converges in ~90 iterations (~1.5 years of weekly feedback)
- **Custom game environment**: Simulated PPO performance validation

---

## 📱 Technologies

- **PyTorch** (RL agents)
- **MongoDB** (nutrition data)
- **Flask API** (integration)
- **Docker** (containerization)
- **RuleEngine + NumPy** (rule-based logic + calculations)

---

## 📌 Notes

- Nutrition plans are dynamically adjusted every week.
- Feedback system tracks emotional state, weight, fat score.
- Environment designed using custom MDP (state-action-reward).

---

## 📃 License

This project is intended for academic and research use.
