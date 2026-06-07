# Robotics Seed Set

This file documents the **starting seed papers, repos, and industry players** for the RoboticsResearch project. Use it as a "must-watch" list when the automated crawler is missing items or when bootstrapping a new research cycle.

## 1. Foundational Papers (Read Once, Reference Forever)

### 1.1 VLA / Foundation Models

- **RT-2** (Brohan et al., Google DeepMind, 2023) — arXiv:2307.15818 — "vision-language-action models transferred from web knowledge"
- **RT-1** (Brohan et al., 2022) — arXiv:2212.06817 — first large-scale robot transformer
- **OpenVLA** (Kim et al., 2024) — arXiv:2406.09246 — 7B open-source VLA
- **Octo** (Team et al., 2024) — arXiv:2405.12213 — generalist robot policy
- **π0** (Physical Intelligence, 2024) — first generalist robot foundation model
- **π0-FAST / HiRT** — tokenization variants
- **GR-1** (Wu et al., ByteDance, 2024) — arXiv:2401.12916 — video generation → action
- **GR-2** (Cheang et al., ByteDance, 2024) — arXiv:2410.06180 — generative video-language-action
- **DreamerV3** (Hafner et al., 2023) — arXiv:2301.04104 — world model for RL
- **Gato** (Reed et al., DeepMind, 2022) — arXiv:2205.06175 — generalist agent
- **PaLM-E** (Driess et al., 2023) — arXiv:2303.03378 — embodied multimodal LLM
- **RoboFlamingo** (Li et al., 2023) — arXiv:2311.01378

### 1.2 Manipulation

- **3D Diffusion Policy (DP3)** (Ze et al., 2024) — arXiv:2403.03954
- **RDT-1B** (Liu et al., 2024) — Robotics Diffusion Transformer
- **Perceiver-Actor** (Shridhar et al., 2023) — multi-task manipulation
- **HPT** (Bharadhwaj et al., 2024) — heterogeneous pre-trained transformers
- **ManipLLM** (Li et al., 2023) — LLM for embodied manipulation
- **VoxPoser** (Huang et al., 2023) — LLM-driven affordance maps
- **SuSIE** (Black et al., 2024) — diffusion-based manipulation

### 1.3 Humanoid / Locomotion

- **ANYmal** papers (Hutter et al., ETH) — quadruped foundation
- **Atlas** control papers (Boston Dynamics, Boston Dynamics AI Institute)
- **Digit** papers (Agility Robotics)
- **H1** / **G1** technical reports (Unitree)
- **Learning quadrupedal locomotion over challenging terrain** (Lee et al., 2020) — Science
- **Walk These Ways** (Margolis et al., 2022) — multi-behavior RL
- **HOVER** (Cheng et al., 2024) — humanoid whole-body control

### 1.4 SLAM

- **ORB-SLAM2/3** — classical visual SLAM
- **LIO-SAM** — LiDAR-inertial odometry
- **NeRF-SLAM** (Sucar et al., 2021) — neural implicit SLAM
- **NICE-SLAM** (Zhu et al., 2022) — neural implicit SLAM
- **SplaTAM** (Keetha et al., 2024) — 3DGS SLAM
- **Photo-SLAM** (Huang et al., 2023) — 3DGS + visual SLAM
- **MASt3R-SLAM** (Asgharivaskasi et al., 2024)

### 1.5 Dexterous Hands

- **Dexterous Functional Grasping** (OpenAI et al., 2019)
- **LEAP Hand** (Shaw et al., 2023) — low-cost dexterous hand
- **Allegro Hand** documentation
- **Shadow Hand** documentation
- **DextrAH-G** (Roveda et al., 2024)
- **DexCap** (Wang et al., 2024) — wearable hand teleoperation

## 2. Foundational Repositories (Watch on GitHub)

### 2.1 VLA / Foundation Models

- openvla/openvla
- Physical-Intelligence/openpi
- octo-model/octo
- google-deepmind/open_x_embodiment (Open X-Embodiment dataset)
- nvidia/GR00T (Isaac GR00T)

### 2.2 Manipulation

- real-stanford/scale-ai-robo (Stanford)
- andrew-wei-droid/droid — DROID dataset
- bridge-data/bridge — Bridge dataset
- LLM-RGBD/ManipLLM
- real-stanford/sim-env-real-net

### 2.3 Simulation

- google-deepmind/mujoco
- NVIDIA/Isaac-Sim
- NVIDIA/Isaac-GR00T
- haosulab/MuJoCo-XLA
- Genesis-Embodied-AI/Genesis
- ManiSkill
- RoboSuite

### 2.4 Humanoid

- unitreerobotics/unitree_sdk2
- unitreerobotics/unitree_legged_sdk
- BostonDynamics/orb3 (if open)
- ANYbotics/legged_gym
- isaac-sim/IsaacLab
- lecar-lab/hovertra (HOVER)

### 2.5 SLAM

- UZ-SLAMLab/ORB_SLAM3
- TixiaoShan/LIO-SAM
- MIT-SPARK/NICE-SLAM
- nerfstudio-project/nerfstudio
- graphdeco-inria/gaussian-splatting

## 3. Industry Players (Track Their Blogs, GitHub, Press)

### 3.1 Humanoid OEMs

- **Figure AI** (USA) — Figure 01/02
- **Tesla** (USA) — Optimus
- **1X Technologies** (Norway) — Neo
- **Apptronik** (USA) — Apollo
- **Agility Robotics** (USA) — Digit
- **Unitree** (China) — H1/G1
- **AgiBot 智元** (China) — A2
- **Fourier Intelligence 傅利叶** (China) — GR-1/GR-2
- **UBTech 优必选** (China) — Walker S
- **XPeng 鹏行** (China) — Iron
- **Xiaomi 小米** (China) — CyberOne
- **Leju Robot 乐聚** (China) — Kuavo
- **Robotera 加速进化** (China) — 星动STAR1
- **Booster Robotics 机器人** (China) — T1
- **LimX Dynamics 逐际动力** (China) — CL-1

### 3.2 Robot Foundation Model Companies

- **Physical Intelligence** (USA) — π0
- **Skild AI** (USA) — Skild Brain
- **Covariant** (USA, acquired by Amazon 2024)
- **Google DeepMind** — RT series
- **Meta FAIR** — Habitat, Aria
- **NVIDIA** — GR00T, Isaac

### 3.3 Dexterous Hand Companies

- **Shadow Robot** (UK) — Shadow Hand
- **Wonik Robotics** (Korea) — Allegro Hand
- **LEAP Hand** (Stanford spinoff)
- **因时机器人** (China) — RH series
- **傲意 OYMotion** (China)
- **灵巧智能 DexRobot** (China)

### 3.4 SLAM / Perception Companies

- **Nuro** (USA) — autonomous driving
- **Wayve** (UK) — autonomous driving (end-to-end)
- **Waymo** (USA) — autonomous driving
- **小马智行** (China) — Pony.ai
- **禾多科技** (China) — autonomous driving

## 4. RSS / Blog Sources

- https://www.figure.ai/
- https://www.tesla.com/AI (Optimus updates)
- https://www.1x.tech/
- https://www.physicalintelligence.company/blog
- https://bostondynamics.com/blog/
- https://www.unitree.com/
- https://www.agilityrobotics.com/
- https://www.apptronik.com/news
- https://agibot.com/
- https://www.fourierintelligence.com/
- https://news.deepmind.google/
- https://research.nvidia.com/labs/dvl/
- https://ai.meta.com/blog/

## 5. Conferences / Venues (Submission Deadlines)

- **ICRA** (May)
- **IROS** (October)
- **CoRL** (November)
- **RSS** (July)
- **NeurIPS**, **ICML**, **CVPR**, **ECCV**, **ICCV** (general AI/ML/CV)

## 6. Standards Bodies

- **ISO/TC 299** — Robotics
- **ASTM F45** — Robotics and automation
- **IEEE Robotics and Automation Society**

## 7. Industry Analysts

- **IFR** (International Federation of Robotics) — annual World Robotics Report
- **IDC** — service robotics market reports
- **Goldman Sachs** — humanoid robot research notes
- **Morgan Stanley** — humanoid robot market projections
