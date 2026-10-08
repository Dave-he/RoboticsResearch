# 机器人研究每日摘要 · 2026-10-08

> 自动生成,共 45 篇命中论文。

## 🌐 具身智能 / 机器人基础模型 (4 篇)

### 1. Kinematic MeanFlow: One-Step Action Generation Policy for Robotic Foundation Models

- **arXiv**: [2610.00864v1](https://arxiv.org/abs/2610.00864v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.00864v1)
- **作者**: Jiawei Fan, Sifeng Wang, Yuqing Hou et al.
- **发表**: 2026-10-01  ·  **类别**: cs.RO, cs.AI, cs.CL
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: In this paper, we study how to achieve one-step action generation in Robotic Foundation Models (RFMs), aiming to overcome the high inference latency of multi-step flow matching. MeanFlow provides a promising framework for this goal, yet its direct application leads to performance collapse. We discover that this stems from two distinctive dynamics exhibited…

### 2. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 3. EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution

- **arXiv**: [2610.10498v1](https://arxiv.org/abs/2610.10498v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10498v1)
- **作者**: Python Song, Zhixuan Liang, Kelsey Fu et al.
- **发表**: 2026-10-07  ·  **类别**: cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Robot foundation models provide strong visuomotor control, yet their performance can degrade when object positions or task instructions change. Further improvements often require post-training on substantial robot data, which can be costly to collect through methods such as teleoperation. Agentic harnesses can adapt around the model, but current self-evolvi…

### 4. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

## 🦵 人形 / 足式机器人 (19 篇)

### 1. BiGym 2.0: Benchmarking Learned and Agent-Developed Policies for Humanoid Household Manipulation

- **arXiv**: [2610.07594v1](https://arxiv.org/abs/2610.07594v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.07594v1)
- **作者**: Zexi Zhang, Zecheng Zhu, Zidong Chen et al.
- **发表**: 2026-10-06  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: Humanoid household manipulation requires the arms to act while the body balances, steps and changes posture. We present BiGym 2.0, an adaptation of BiGym for the Unitree G1 across 20 household tasks using a unified whole-body controller for demonstration and evaluation. The suite provides 60 native human virtual-reality demonstrations per task with synchron…

### 2. LLA-MPPI: Rapidly Adaptive Whole-body Control of Legged Robots with GPU-Accelerated Parallel Simulations

- **arXiv**: [2610.10465v1](https://arxiv.org/abs/2610.10465v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10465v1)
- **作者**: Sebin Jung, Maitham F. AL-Sunni, Juan Alvarez-Padilla et al.
- **发表**: 2026-10-07  ·  **类别**: cs.RO, eess.SY
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Real-time whole-body controllers for legged robots typically plan through a fixed nominal model and degrade when the deployed dynamics change. Adaptive methods typically require a model structure that contact dynamics do not provide, or they need offline training for each anticipated condition. We present Look-back and Look-ahead Adaptive Model Predictive P…

### 3. OccluDex: Hierarchical 3D Visuo-Tactile Representation Learning for Egocentric Dexterous Manipulation under Self-Occlusion

- **arXiv**: [2609.39017v1](https://arxiv.org/abs/2609.39017v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39017v1)
- **作者**: Ziheng Xu, Yueyuan Chen, Xinyuan He et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Reliable dexterous manipulation requires continuous estimation of object geometry and hand-object contact throughout interaction. With egocentric sensing, however, the manipulating hand frequently occludes task-relevant object surfaces and contact regions, reducing the visual evidence available for state estimation and thereby making robust closed-loop cont…

### 4. Co${}^{2}$Skill: Whole-Body Control via Skill Composition for Long-Horizon Human-Environment Interaction

- **arXiv**: [2610.09291v1](https://arxiv.org/abs/2610.09291v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.09291v1)
- **作者**: Jeonghwan Kim, Hyeonwoo Kim, Hanbyul Joo
- **发表**: 2026-10-07  ·  **类别**: cs.RO, cs.GR
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Achieving human-level dexterity in complex, unstructured environments requires the seamless integration of whole-body scene interaction and dexterous object manipulation skills. While existing physics-based controllers generate physically plausible behaviors in each domain, they largely address these two capabilities independently. In this paper, we present…

### 5. Magnet-Aware Control of Legged Robots

- **arXiv**: [2610.08653v1](https://arxiv.org/abs/2610.08653v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.08653v1)
- **作者**: J. Playan Garai, S. B. Djuve, C. McGreavy et al.
- **发表**: 2026-10-06  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Autonomous robots can increase uptime and reduce human exposure in Big Science facilities, but strong magnetic fields needed for their operation corrupt sensors and induce pose-dependent mechanical wrenches that destabilize robots and challenge conventional reactive controllers. This paper presents a control framework for modeling, estimating, and dynamical…

### 6. Breaking speed scaling in quadrupedal robots via Huygens' coupled-pendulum dynamics

- **arXiv**: [2609.13290v1](https://arxiv.org/abs/2609.13290v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.13290v1)
- **作者**: Yucheng Tao, Yongbin Jin, Shaowen Cheng et al.
- **发表**: 2026-09-09  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Achieving biological-level running speeds has largely been pursued through advances in control algorithms, which improve the utilization of existing hardware. However, the ultimate speed limits remain governed by the underlying force and torque requirements of rapid locomotion, which are typically addressed through increased actuator capacity. Inspired by H…

### 7. HULK: Learning Whole-Body Forceful Loco-Manipulation for Humanoids

- **arXiv**: [2610.08970v1](https://arxiv.org/abs/2610.08970v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.08970v1)
- **作者**: An Dang, Arturo Flores Alvarez, Yu-Ming Chen et al.
- **发表**: 2026-10-06  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Humanoid loco-manipulation of large, heavy objects demands forceful interaction across the entire body. However, such payloads shift a humanoid's center of mass and impose sustained loads across the upper body, challenging balance and command tracking. We present HULK, a whole-body control framework for forceful loco-manipulation. Using model predictive con…

### 8. iGPC: Generative Motion Priors for Object-Aware Humanoid Interaction

- **arXiv**: [2610.08120v1](https://arxiv.org/abs/2610.08120v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.08120v1)
- **作者**: Anujith Muraleedharan, Abdul Ahad Butt, Nolan Fey et al.
- **发表**: 2026-10-06  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Humanoid robots operating in unstructured environments must combine robust whole-body control with the ability to perceive and physically interact with surrounding objects. While large-scale human motion data provides powerful priors for natural and versatile humanoid control, effectively transferring such priors to perception-driven object interaction rema…

### 9. EmbodiedSmith: Scaling Embodied Data through Recursive Self-Improvement Flywheel in Simulation

- **arXiv**: [2610.07969v1](https://arxiv.org/abs/2610.07969v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.07969v1)
- **作者**: Yikai Qin, Yifei Deng, Mingjian Liang et al.
- **发表**: 2026-10-06  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Scaling robotic foundation models requires diverse training data and reliable evaluation environments. Simulation offers a scalable solution, yet existing generation pipelines remain constrained by predefined assets and skills, a disconnect between scene generation and task generation, and limited support for complex embodiments and physics. We introduce Em…

### 10. Physics Residual Dynamics and Reduced Order Whole-Body Planning for Obstacle Aware Human Robot Cloth CoTransportation

- **arXiv**: [2610.06641v1](https://arxiv.org/abs/2610.06641v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.06641v1)
- **作者**: Moein Forouhar, Kosar Behnia, Anirvan Dutta et al.
- **发表**: 2026-10-05  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Human--robot co-transportation of deformable objects requires predicting object deformation during motion, since obstacle clearance depends on both the grasp points and the unactuated interior. We present a hierarchical planning framework that combines a learned cloth model with a reduced-order whole-body model of a dual-arm mobile manipulator. A physics-re…

## 🦾 操控 / 灵巧手 / 抓取 (9 篇)

### 1. NarrativeFlow: Flow-Based Vision-Language-Action Model Using Robot Velocity Fields

- **arXiv**: [2610.00981v1](https://arxiv.org/abs/2610.00981v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.00981v1)
- **作者**: Shota Kobayashi, Koki Seno, Daichi Yashima et al.
- **发表**: 2026-10-01  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: We focus on language-conditioned flow-based manipulation, where robot flows (robot velocity fields) serve as embodiment-agnostic, motion-centric representations for leveraging data collected from multiple robot platforms. This task is crucial because language-conditioned manipulation is essential for practical robotic systems, yet scaling robot foundation m…

### 2. TANDEM: Task and Motion Planning with As-Needed Demonstrations for Efficient Vision-Language-Action Model Fine-tuning

- **arXiv**: [2609.28314v1](https://arxiv.org/abs/2609.28314v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28314v1)
- **作者**: Samrat Sahoo, Liang Ji, Tom Silver et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Human teleoperators spend substantial time demonstrating behaviors that robots can already perform autonomously, limiting the scalability of data collection for robot foundation models. Task and motion planning (TAMP) can automate many of these behaviors, but a fixed planning domain may not support every stage of a long-horizon manipulation task. We present…

### 3. DeformSmith: Physics Harness-Guided Hierarchical Generation of Deformable Assets for Robot Manipulation

- **arXiv**: [2609.18620v2](https://arxiv.org/abs/2609.18620v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.18620v2)
- **作者**: Can Li, Jie Gu, Zishun Deng et al.
- **发表**: 2026-09-16  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Creating deformable assets for robot manipulation requires jointly specifying their geometry, appearance, and physical properties. This is especially challenging for deformable objects, since text and images provide limited evidence about how they deform and respond to contact, yet these responses directly affect their suitability for interaction. Automated…

### 4. FP2: Equipping Robotic Foundation Models with Force Control

- **arXiv**: [2609.37433v1](https://arxiv.org/abs/2609.37433v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.37433v1)
- **作者**: Hongjie Fang, Shirun Tang, Junjian Hu et al.
- **发表**: 2026-09-29  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Robotic foundation models (RFMs) are increasingly capable of general-purpose manipulation, yet reliable physical interaction remains challenging in contact-rich settings. We present FP2, a lightweight downstream interface that equips task-adapted RFMs with explicit force control while preserving their action-generation capability. FP2 adopts an action-regul…

### 5. LIFD: Anchored Diffusion for 3D-Aware Scene Memory in Robotic Manipulation

- **arXiv**: [2609.19796v2](https://arxiv.org/abs/2609.19796v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.19796v2)
- **作者**: Wenbo Li, Yiteng Chen, Wenhao Li et al.
- **发表**: 2026-09-17  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: During manipulation, robot and scene motion can move previously observed regions outside the camera's field of view. Geometry-aware RGB features encode visible structure, while control under partial observability requires scene memory that integrates observation history and grounds inferred content in current evidence. We introduce \lifd{} (Look, Imagine, F…

### 6. RopeFormer: Cross-Trial Adaptation from Interaction History for Dynamic Rope Manipulation

- **arXiv**: [2609.23432v1](https://arxiv.org/abs/2609.23432v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.23432v1)
- **作者**: Menglin Wu, Kaixiang Yao, Shangbo Luan et al.
- **发表**: 2026-09-20  ·  **类别**: cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Dynamic rope manipulation is highly sensitive to unknown object dynamics: the same robot motion can produce substantially different responses across ropes, while explicitly identifying the relevant physical properties is difficult. We present RopeFormer, a history-conditioned framework that uses prior task interaction as context for subsequent control. The…

### 7. VIA: Visual Interface Agent for Robot Control

- **arXiv**: [2607.11119v2](https://arxiv.org/abs/2607.11119v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.11119v2)
- **作者**: Hengyuan Hu, Jensen Gao, Priya Sundaresan et al.
- **发表**: 2026-07-13  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Robot manipulation is a complex task that requires visual perception, physical reasoning, planning, and closed-loop control. General-purpose foundation models (FMs) have grown remarkably capable of some of these, especially perception and reasoning. Inspired by the growing ability of FM-powered agents to operate software through visual interfaces, we ask wh…

### 8. LIBERO-VPro: Benchmarking Closed-Loop Visual Robustness of Robotic Foundation Models

- **arXiv**: [2609.24350v1](https://arxiv.org/abs/2609.24350v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.24350v1)
- **作者**: Huiqiong Li, Zhiting Mei, Anirudha Majumdar et al.
- **发表**: 2026-09-21  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Robotic foundation models achieve impressive performance on standard manipulation benchmarks, yet these evaluations typically assume clean, timely, and consistent visual observations throughout execution. We introduce LIBERO-VPro, a benchmark for systematically evaluating the closed-loop visual robustness of robotic foundation models by perturbing the visua…

### 9. A Perception-Manipulation Robotics System for Food Cutting

- **arXiv**: [2607.04367v1](https://arxiv.org/abs/2607.04367v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.04367v1)
- **作者**: Xinyuan Luo, Wenzhen Yuan
- **发表**: 2026-07-05  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: In the development of cooking robots, mastering the task of cutting is crucial. A significant challenge lies in the diverse properties of food, which necessitate distinct cutting policies and even different knives for optimal processing. This paper presents a perception-manipulation framework for food-cutting tasks. Our system features a knife selection mod…

## 🎓 模仿学习 / 强化学习 (7 篇)

### 1. HuMemSLAM: Efficient Human-Inspired Semantic Place Recognition for Robust Visual SLAM

- **arXiv**: [2609.17168v1](https://arxiv.org/abs/2609.17168v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.17168v1)
- **作者**: Mayowa Adebambo, Sebastian Donnelly, Armand Amaritei et al.
- **发表**: 2026-09-15  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Autonomous systems require reliable place recognition for efficient and effective simultaneous localisation and mapping (SLAM). Traditional geometric visual SLAM approaches rely on low-level features and geometric consistency, but remain vulnerable to perceptual aliasing, where different places appear similar, and perceptual variation, where the same place…

### 2. RawSLAM: Online HDR Gaussian SLAM from Linear Radiance

- **arXiv**: [2609.20589v1](https://arxiv.org/abs/2609.20589v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.20589v1)
- **作者**: Marina Orozco González, Luis Merino
- **发表**: 2026-09-17  ·  **类别**: cs.CV
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Current dense visual SLAM systems rely almost exclusively on 8-bit tonemapped Low Dynamic Range (LDR) inputs, limiting their robustness in extreme lighting where shadows and highlights trigger tracking drift and mapping collapse. Conversely, existing raw and High Dynamic Range (HDR) reconstruction pipelines operate strictly offline. They depend on Structure…

### 3. Unblur-SLAM: Dense Neural SLAM for Blurry Inputs

- **arXiv**: [2603.26810v1](https://arxiv.org/abs/2603.26810v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.26810v1)
- **作者**: Qi Zhang, Denis Rozumny, Francesco Girlanda et al.
- **发表**: 2026-03-26  ·  **类别**: cs.CV, eess.IV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We propose Unblur-SLAM, a novel RGB SLAM pipeline for sharp 3D reconstruction from blurred image inputs. In contrast to previous work, our approach is able to handle different types of blur and demonstrates state-of-the-art performance in the presence of both motion blur and defocus blur. Moreover, we adjust the computation effort with the amount of blur in…

### 4. Query Quantized Neural SLAM

- **arXiv**: [2412.16476v1](https://arxiv.org/abs/2412.16476v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2412.16476v1)
- **作者**: Sijia Jiang, Jing Hua, Zhizhong Han
- **发表**: 2024-12-21  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural implicit representations have shown remarkable abilities in jointly modeling geometry, color, and camera poses in simultaneous localization and mapping (SLAM). Current methods use coordinates, positional encodings, or other geometry features as input to query neural implicit functions for signed distances and color which produce rendering errors to d…

### 5. ACE-SLAM: Scene Coordinate Regression for Neural Implicit Real-Time SLAM

- **arXiv**: [2512.14032v1](https://arxiv.org/abs/2512.14032v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2512.14032v1)
- **作者**: Ignacio Alzugaray, Marwan Taher, Andrew J. Davison
- **发表**: 2025-12-16  ·  **类别**: cs.CV, cs.AI, eess.IV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: We present a novel neural RGB-D Simultaneous Localization And Mapping (SLAM) system that learns an implicit map of the scene in real time. For the first time, we explore the use of Scene Coordinate Regression (SCR) as the core implicit map representation in a neural SLAM pipeline, a paradigm that trains a lightweight network to directly map 2D image feature…

### 6. MISO: Multiresolution Submap Optimization for Efficient Globally Consistent Neural Implicit Reconstruction

- **arXiv**: [2504.19104v1](https://arxiv.org/abs/2504.19104v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2504.19104v1)
- **作者**: Yulun Tian, Hanwen Cao, Sunghwan Kim et al.
- **发表**: 2025-04-27  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Neural implicit representations have had a significant impact on simultaneous localization and mapping (SLAM) by enabling robots to build continuous, differentiable, and high-fidelity 3D maps from sensor data. However, as the scale and complexity of the environment increase, neural SLAM approaches face renewed challenges in the back-end optimization process…

### 7. NeRF and Gaussian Splatting SLAM in the Wild

- **arXiv**: [2412.03263v1](https://arxiv.org/abs/2412.03263v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2412.03263v1)
- **作者**: Fabian Schmidt, Markus Enzweiler, Abhinav Valada
- **发表**: 2024-12-04  ·  **类别**: cs.RO, cs.CV, cs.LG
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Navigating outdoor environments with visual Simultaneous Localization and Mapping (SLAM) systems poses significant challenges due to dynamic scenes, lighting variations, and seasonal changes, requiring robust solutions. While traditional SLAM methods struggle with adaptability, deep learning-based approaches and emerging neural radiance fields as well as Ga…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (6 篇)

### 1. Human-in-the-Loop Neuro-Symbolic Drift Anticipation for Reliable Visual SLAM

- **arXiv**: [2610.05757v1](https://arxiv.org/abs/2610.05757v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05757v1)
- **作者**: Junhyun Nam, Wonse Jo
- **发表**: 2026-10-05  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: This paper introduces Hybrid DeepSEE (HDS), a Human-in-the-Loop (HITL) neuro-symbolic framework for proactive drift anticipation in Visual SLAM (V-SLAM). While data-driven models offer predictive power, their "black-box" nature often yields physically inconsistent outputs in out-of-distribution (OOD) environments. To address this, HDS integrates neural drif…

### 2. Know-Your-Scene (KYS)-SLAM: Hierarchical Semantic-Motion Priors for Feature Matching in Stereo Visual SLAM

- **arXiv**: [2609.27509v1](https://arxiv.org/abs/2609.27509v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27509v1)
- **作者**: Preeti Chatterjee, Jin Lu, Jin Sun et al.
- **发表**: 2026-09-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Stereo visual SLAM systems built on local descriptors suffer from semantic ambiguity, instance-level confusion, and independently moving objects, each corrupting data association and accumulating as trajectory drift. Prevailing semantic and dynamic SLAM methods address this through binary feature rejection, sacrificing correspondence density for outlier sup…

### 3. BLASt3R: Bundle Adjustment of Any Image Set with Multi-View Matching and Monocular Priors

- **arXiv**: [2609.05210v1](https://arxiv.org/abs/2609.05210v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.05210v1)
- **作者**: Vincent Leroy, Philippe Weinzaepfel, Lojze Zust et al.
- **发表**: 2026-09-04  ·  **类别**: cs.CV
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Recent hybrid Structure-from-Motion (SfM) systems combine the robustness of feed-forward 3D reconstruction with the accuracy of traditional bundle adjustment (BA) with pixel matching. They are usually the best performing methods however their scalability and usability remains limited since estimating dense correspondences between views is prohibitively cost…

### 4. MVP-SLAM: Multi-Camera Visual-Inertial Floorplan-Prior SLAM

- **arXiv**: [2609.39596v1](https://arxiv.org/abs/2609.39596v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39596v1)
- **作者**: Asier Bikandi-Noya, Miguel Fernandez-Cortizas, Muhammad Shaheer et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Indoor building construction sites are demanding environments for visual SLAM, where variable lighting and repetitive, low-textured structures make the system drift over long trajectories, though structural elements such as walls remain distinguishable despite these conditions. These buildings are constructed according to their as-planned floor plans, avail…

### 5. Cube-Splat: High-Fidelity 360° Gaussian Splatting SLAM via Cubemap Factorization and Adjoint-Consistent Optimization

- **arXiv**: [2609.21347v1](https://arxiv.org/abs/2609.21347v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.21347v1)
- **作者**: Xiangfei Guo, Hao Shi, Yufan Zhang et al.
- **发表**: 2026-09-18  ·  **类别**: cs.CV
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Recent progress in 3D Gaussian Splatting (3DGS) has enabled dense visual SLAM with pinhole cameras, yet most pipelines are not designed for panoramic imagery. We present Cube-Splat, the first panoramic GS-SLAM framework that factorizes each 360° frame into a cubemap of four fixed-orientation virtual pinhole views sharing a single optical center. By designat…

### 6. Geodesic Flow Matching for Denoising High-Dimensional Structured Representations

- **arXiv**: [2606.00248v1](https://arxiv.org/abs/2606.00248v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.00248v1)
- **作者**: Karim Habashy, Chris Eliasmith
- **发表**: 2026-05-29  ·  **类别**: cs.AI
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Vector Symbolic Algebras (VSAs) enable robust neurosymbolic reasoning by encoding symbolic information into high-dimensional distributed representations. For continuous domains, Spatial Semantic Pointers (SSPs) extend this framework by mapping variables onto continuous toroidal manifolds. However, standard approaches like Flow Matching assume a flat Euclide…

---

## 📋 本日操作建议

**建议今日深读 (Top 3):**
1. [BiGym 2.0: Benchmarking Learned and Agent-Developed Policies for Humanoid Household Manipulation](https://arxiv.org/abs/2610.07594v1) — score 18
2. [NarrativeFlow: Flow-Based Vision-Language-Action Model Using Robot Velocity Fields](https://arxiv.org/abs/2610.00981v1) — score 16
3. [TANDEM: Task and Motion Planning with As-Needed Demonstrations for Efficient Vision-Language-Action Model Fine-tuning](https://arxiv.org/abs/2609.28314v1) — score 14

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
