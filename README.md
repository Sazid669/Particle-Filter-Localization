
# 🧭 Particle Filter Localization – IFRoS Master's Project

This repository implements a **Monte Carlo Localization (MCL)** technique, also known as **Particle Filter Localization**, developed for the **IFRoS Master’s program**.

---

## 📘 Project Overview

**Monte Carlo Localization (MCL)** is a probabilistic localization algorithm for mobile robots that uses a set of weighted particles to represent the posterior belief of the robot’s state. This project simulates a differential drive robot performing localization using particle filters.

---

## 📂 Project Structure

- **Motion Model**: Differential drive robot simulation
- **Sensor Model**: Observation model for updating particle weights
- **Particle Filter Logic**: Resampling, prediction, and correction steps
- **Visualization**: Robot pose, particle cloud, and trajectory visualization

---

## 🧠 Algorithms & Techniques

- **Particle Filter / Monte Carlo Localization**
- **Differential Drive Kinematics**
- **Resampling Techniques**
- **Weighted Mean Pose Estimation**
- **Pose Uncertainty Visualization**

---

## 🗂️ Files & Modules

- `MCLocalization.py`: Main particle filter localization class
- `PF_3DOF_DR.py`, `PF_3DOF_MBL.py`: Particle filter using different drive and map-based localization models
- `ParticleFilter.py`: Core particle filtering algorithm
- `DifferentialDriveSimulatedRobot.py`: Robot movement simulation
- `SimulatedRobot.py`, `Pose3D.py`: Robot state representations
- `Particle Filter LAB.pdf`: Theory and lab instructions
- `README.md`: Project overview (this file)

---

## ▶️ How to Run

```bash
cd Particle-Filter-Localization-IFRoS-Master
python PF_3DOF_MBL.py
```

You may also explore `PF_3DOF_DR.py` for dead-reckoning based localization. Ensure required packages such as `numpy` and `matplotlib` are installed.

---

> If this helped you or your research, consider giving a ⭐ and spreading the word!
