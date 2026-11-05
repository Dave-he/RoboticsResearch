# 机器人研究每日摘要 · 2026-11-06

> 自动生成,共 75 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (2 篇)

### 1. Where Is VLA Inference Time Spent? Bottlenecks and Optimization Interactions Across GPUs

- **arXiv**: [2611.06710v1](https://arxiv.org/abs/2611.06710v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.06710v1)
- **作者**: Muhammad Danish Waseem, Ahmed Ali-Eldin Hassan
- **发表**: 2026-11-04  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Vision-language-action (VLA) models map camera observations and language instructions to robot actions. However, their large backbones and repeated action generation can make inference take longer than the robot's real-time requirements for its next action. To reduce the load of VLA computations, researchers have proposed multiple optimization approaches, i…

### 2. PolicyIK: High-Precision Inverse Kinematics for Robot Arms with Reinforcement Learning

- **arXiv**: [2611.05372v1](https://arxiv.org/abs/2611.05372v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.05372v1)
- **作者**: Yuhan Liu, Xinqi Liu, Zixuan Dong et al.
- **发表**: 2026-11-03  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Inverse kinematics (IK) converts end-effector pose commands into joint motion, and many vision-language-action (VLA) policies rely on it to act on a given arm and to transfer across embodiments. Precise IK remains laborious: redundancy and singularities complicate the inverse mapping, execution depends on hand-tuned controllers, and training data on physica…

## 🌐 具身智能 / 机器人基础模型 (1 篇)

### 1. FoundationVIO: Enforcing Metric Scale in Feed-forward Visual-Inertial Odometry

- **arXiv**: [2610.14951v1](https://arxiv.org/abs/2610.14951v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.14951v1)
- **作者**: Jin Rhee, Yuhao Zhang, Frank Dellaert et al.
- **发表**: 2026-10-10  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Feed-forward geometric foundation models (GFMs) directly predict dense geometry and camera poses from batches of images. Emerging visual SLAM methods chain together consecutive GFM batches to form dense point cloud maps. A core challenge is how to address the ambiguous geometric scale of GFM predictions: independent predictions are locally consistent up-to-…

## 🦵 人形 / 足式机器人 (15 篇)

### 1. A fully articulated humanoid dexterous hand with human-level joint structure enabled by linkage-based actuation

- **arXiv**: [2610.36789v1](https://arxiv.org/abs/2610.36789v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.36789v1)
- **作者**: Jihao Li, Jianguo Wang, Haotian Guo et al.
- **发表**: 2026-10-27  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Humanoid dexterous hands are a core component of embodied intelligence, enabling robots to translate high-level intent into rich and adaptive physical interaction. However, existing designs remain constrained by a persistent trade-off among anthropomorphic kinematic complexity, mechanical robustness, load capacity and control simplicity, limiting dexterous…

### 2. GoalDex: Learning Image-Goal-Conditioned Policies for Dexterous In-Hand Manipulation

- **arXiv**: [2611.02171v1](https://arxiv.org/abs/2611.02171v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.02171v1)
- **作者**: Arjun Bhardwaj, Mayank Mittal, Maximum Wilder-Smith et al.
- **发表**: 2026-11-01  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Dexterous in-hand manipulation is commonly formulated around explicit object pose estimation, yet reliable pose tracking is challenging under severe hand-object occlusions and often requires object-specific supervision. This dependence creates a bottleneck between perception and control that can limit robustness and scalability. We present an end-to-end vis…

### 3. Catch It All!: Generalizable Dynamic Catching with a Dexterous Hand

- **arXiv**: [2610.39044v1](https://arxiv.org/abs/2610.39044v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.39044v1)
- **作者**: Arth Shukla, Kehlani Fay, Huaze Liu et al.
- **发表**: 2026-10-28  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Catching arbitrary objects requires generalization to novel projectiles and real-time adaptation to unpredictable contact dynamics under noisy visual observations. This paper presents Catch It All!, a sim-to-real catching framework for humanoid robots that generalizes and adapts to unseen objects with variable physical properties for underhand and overhand…

### 4. From Tabletop to Walking Bot: Deploying a VLA Model on a Legged Manipulator Robot

- **arXiv**: [2610.32271v1](https://arxiv.org/abs/2610.32271v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.32271v1)
- **作者**: Giovanni Minelli, Antonio Langella, Giovanni B. Dessy et al.
- **发表**: 2026-10-23  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models are typically pretrained on broad, diverse datasets and subsequently fine-tuned on a comparatively small dataset tailored to a specific target robot. Such adaptation recipe is now widely established, achieving its most mature results on fixed-base arms due to their static base dynamics and consistent reference frame. Moun…

### 5. Contact-Implicit Whole-Body Trajectory Optimization for Dynamic Humanoid Locomotion on Parameterizable Uneven Terrain

- **arXiv**: [2611.05585v1](https://arxiv.org/abs/2611.05585v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.05585v1)
- **作者**: Roberto Mauceri, Stefano Dafarra, Giulio Romualdi et al.
- **发表**: 2026-11-03  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: This letter presents a trajectory planner for humanoid robots to perform dynamic motions on complex, parameterizable terrains using a contact-implicit whole-body optimization framework. The planner generates feasible movements without predefined contact sequences, considering the robot's full dynamics and kinematics. To plan bipedal locomotion on steps, ram…

### 6. OccluDex: Hierarchical 3D Visuo-Tactile Representation Learning for Egocentric Dexterous Manipulation under Self-Occlusion

- **arXiv**: [2609.39017v1](https://arxiv.org/abs/2609.39017v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39017v1)
- **作者**: Ziheng Xu, Yueyuan Chen, Xinyuan He et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Reliable dexterous manipulation requires continuous estimation of object geometry and hand-object contact throughout interaction. With egocentric sensing, however, the manipulating hand frequently occludes task-relevant object surfaces and contact regions, reducing the visual evidence available for state estimation and thereby making robust closed-loop cont…

### 7. Playing Soccer Like Humans Do: Learning Versatile and Agile Humanoid Soccer via Latent Motion Priors

- **arXiv**: [2611.06564v1](https://arxiv.org/abs/2611.06564v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.06564v1)
- **作者**: Haoyu Shao, Yunshen Wang, Jingze Zhang et al.
- **发表**: 2026-11-04  ·  **类别**: cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Humanoid soccer requires a robot to seamlessly combine agile locomotion, ball manipulation, and impact-rich contact dynamics across a continuous, dynamic behavioral spectrum. Yet existing approaches either cover only a limited set of skills, or forego motion priors entirely and produce unnatural behaviors, leaving the combination of a unified skill set and…

### 8. ActOR: Ambient AI-Based Agentic Orchestration for Humanoid Autonomy in Operating Rooms

- **arXiv**: [2611.04255v1](https://arxiv.org/abs/2611.04255v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.04255v1)
- **作者**: Han Zhang, Sicheng Lu, Aleks Santari et al.
- **发表**: 2026-11-03  ·  **类别**: cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Operating rooms (ORs) increasingly contain ambient sensing infrastructure to enable AI-based optimization of workflows and utilization. We pursue an alternative path: using ambient AI to guide robot action and optimize utilization. Deploying humanoids in the OR without ambient AI is severely limited by cumbersome de novo orientation and planning due to part…

### 9. H^2MARL: Hierarchical Heterogeneous Multi-agent Reinforcement Learning for Humanoid Robot Control

- **arXiv**: [2611.06523v1](https://arxiv.org/abs/2611.06523v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.06523v1)
- **作者**: Xuemin Hu, Kaixin Li, Qingqing Xia et al.
- **发表**: 2026-11-04  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Coordinated whole-body control of humanoid robots remains challenging due to high-dimensional coupled dynamics and substantial physical heterogeneity across joint degrees of freedom (JDoFs). Existing multi-agent reinforcement learning methods either employ coarse agent partitions or directly apply generic heterogeneous-agent algorithms, while hierarchical c…

### 10. GRASP: Gradient-Guided Sampling for Contact-Rich Physics-Based Motion Retargeting

- **arXiv**: [2611.05754v1](https://arxiv.org/abs/2611.05754v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.05754v1)
- **作者**: Yang Liu, Tong Wang, Yiming Bao et al.
- **发表**: 2026-11-03  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: We study physics-based retargeting of human demonstrations for robot learning: finding robot controls that reproduce reference motions under contact dynamics. We propose GRASP (Gradient Recovery from Archived Samples for Proposals), which combines sampling-based exploration with gradient-guided refinement without requiring a differentiable simulator. GRASP-…

## 🦾 操控 / 灵巧手 / 抓取 (31 篇)

### 1. Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation

- **arXiv**: [2611.05979v1](https://arxiv.org/abs/2611.05979v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.05979v1)
- **作者**: Zhengdong Hong, Guofeng Zhang
- **发表**: 2026-11-04  ·  **类别**: cs.RO
- **相关性评分**: 20  ·  **🔥 read_now**
- **摘要**: Manipulating diverse objects with multi-fingered dexterous hands is challenging due to the high dimensionality and complex dynamics. Human-Object Interaction (HOI) datasets provide rich knowledge about task information and embodied interactions. Instead of solely imitating the human demonstrations, our method learns to holistically predict future hand-objec…

### 2. DexHOT: Learning Hand-Object Configuration Transfer for Dexterous Manipulation

- **arXiv**: [2611.05119v1](https://arxiv.org/abs/2611.05119v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.05119v1)
- **作者**: Zhewei Gui, Anthony Bolton, Jiyao Zhang et al.
- **发表**: 2026-11-03  ·  **类别**: cs.RO
- **相关性评分**: 20  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation involves not only moving objects, but also arranging the hand around them to maintain useful contacts and enable subsequent actions. Yet many learning-based systems specify goals primarily through object poses or trajectories, leaving hand-object configurations to emerge implicitly. We introduce DexHOT, which formulates dexterous mani…

### 3. EXE: Egocentric Cross-Embodiment Pretraining via Factorized Latent Actions for VLA Models

- **arXiv**: [2610.33685v1](https://arxiv.org/abs/2610.33685v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.33685v1)
- **作者**: Qingyuan Cai, Bo Zhang, Yongzhen Huang et al.
- **发表**: 2026-10-24  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models are bottlenecked by the scarcity of robot data. Egocentric human manipulation videos offer an abundant, diverse, and semantically-rich alternative that inherently captures manipulation intent. However, the embodiment gap makes it difficult to extract action-relevant representations from these videos. From the perspective…

### 4. DexArena: A Unified Benchmark for Long-Horizon Dexterous Manipulation

- **arXiv**: [2611.02629v2](https://arxiv.org/abs/2611.02629v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.02629v2)
- **作者**: Haonan Ping, Jianshu Hu, Yimin Wang et al.
- **发表**: 2026-11-02  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Long-horizon dexterous manipulation remains a fundamental challenge for robot learning, requiring the composition of multiple skills, precise bimanual coordination, generalizable visual understanding, and robust skill transitions. Yet existing manipulation benchmarks largely emphasize isolated skills or support only a limited range of end-effectors, making…

### 5. HandMimicX: Learning Human-Like Dexterous Manipulation via an Object-Centric Policy from Egocentric Videos

- **arXiv**: [2610.41336v1](https://arxiv.org/abs/2610.41336v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.41336v1)
- **作者**: Zihan Gao, Yufei Liu, Yuhong Zhang et al.
- **发表**: 2026-10-30  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Learning dexterous manipulation from human videos remains an open challenge, particularly in the context of transferring a single demonstration into a spatially generalizable robotic skill and maintaining physically plausible human-like interactions. Unlike prior works that emphasize hand-motion imitation, we introduce an object-centric framework for acquir…

### 6. Vortex-Induced Torque in Grasping Soft Objects: Influence of Geometry and Pneumatic Parameters

- **arXiv**: [2611.06359v1](https://arxiv.org/abs/2611.06359v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.06359v1)
- **作者**: Roman Mykhailyshyn, Tomohiro Motoda, Ivan Virgala et al.
- **发表**: 2026-11-04  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Vortex grippers are commonly integrated into automated systems for handling objects with complex geometries in packaging, sorting, and assembling. However, their interaction with compliant objects remains difficult to predict, particularly with respect to the vortex-induced torque transmitted during grasping. This study investigates vortex-induced torque du…

### 7. SoTa: Soft Tactile Skins for Dexterous Manipulation

- **arXiv**: [2610.02338v1](https://arxiv.org/abs/2610.02338v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.02338v1)
- **作者**: Jingyun Yang, Baiyu Shi, Timothy Yu et al.
- **发表**: 2026-10-01  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: A growing body of work suggests that tactile sensing gives robot policies contact information that complements vision in dexterous manipulation. However, visuo-tactile robot data remains scarce: dexterous demonstrations require teleoperating robots, which limits dataset scale. Human demonstrations are far cheaper to collect and offer a path to scale this da…

### 8. DexSuite: An All-in-One Framework for Dexterous Manipulation Across Arms, Hands, and Tasks

- **arXiv**: [2610.37799v1](https://arxiv.org/abs/2610.37799v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.37799v1)
- **作者**: Anas Houssaini, Hugo He, Junming Shi et al.
- **发表**: 2026-10-27  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Human-level dexterity remains a central open problem in robotics, yet few simulation frameworks cover the full workflow of dexterous manipulation, from setting up a robot to collecting dexterous demonstrations and evaluating policies. We present DexSuite, an all-in-one simulation framework for dexterous manipulation built on the Genesis simulator. DexSuite…

### 9. $A^3$-VLA: Automatic Perception-Guided Attention Alignment for Robot Manipulation

- **arXiv**: [2611.06447v1](https://arxiv.org/abs/2611.06447v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.06447v1)
- **作者**: Shengzhe Zhang, Qi Zhang, Dazhong Shen et al.
- **发表**: 2026-11-04  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action Models (VLAs) enable robots to perform manipulation tasks by leveraging Vision-Language Models (VLMs) to process visual observations and language instructions. However, the action prediction objective itself lacks fine-grained task-specific perceptual supervision, making it prone to relying on task-irrelevant visual shortcuts, leading…

### 10. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

## 🎓 模仿学习 / 强化学习 (10 篇)

### 1. KlaskTron-IL: A Contact-Rich Adversarial Imitation Learning Benchmark with a Validated Sim-to-Real Bridge

- **arXiv**: [2611.03091v1](https://arxiv.org/abs/2611.03091v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.03091v1)
- **作者**: Nicklas Sohm, Aswin Ramachandran, Raffaello D'Andrea
- **发表**: 2026-11-02  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: KlaskTron is an open-hardware physical platform for two-player adversarial reinforcement learning, with a learned actuator model that supports zero-shot sim-to-real transfer of trained policies. Building on this platform, we contribute KlaskTron-IL: a multi-tier imitation learning dataset (80k human demonstration timesteps collected directly on the physical…

### 2. Bracketing Shows the Way: Adaptive Multi-Exposure Policy as Input for Robust Visual SLAM

- **arXiv**: [2610.33174v1](https://arxiv.org/abs/2610.33174v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.33174v1)
- **作者**: Olivier Gamache, Anthony Lavertu, David-Alexandre Duclos et al.
- **发表**: 2026-10-23  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Rapid illumination transitions can disturb Visual SLAM (VSLAM) by saturating images before the Automatic Exposure (AE) policy adapts, removing the visual correspondences needed to maintain tracking. Our proposed methods mitigate this disturbance at two levels: B-Adapt acquires adaptive exposure brackets to cover the scene dynamic range while promoting photo…

### 3. A Practical Causal Framework for Autonomous Mobile Robots: From Simulation to Real-World Human Environments

- **arXiv**: [2611.04027v1](https://arxiv.org/abs/2611.04027v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.04027v1)
- **作者**: Luca Castri, Gloria Beraldo, Nicola Bellotto
- **发表**: 2026-11-02  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Causal inference has emerged as a powerful paradigm enabling robots to make safe, efficient decisions by reasoning about the ``why'' behind events. However, its real-world application is hindered by the difficulty of collecting causal data, especially in human-populated environments where training takes time, while users expect immediate operation. To this…

### 4. RingNav: Task-Shaped Circular Memory for Visual Heading

- **arXiv**: [2610.19044v1](https://arxiv.org/abs/2610.19044v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19044v1)
- **作者**: Naitri Rajyaguru, Aryan Tajne, Stephen Jardim et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Tiny robots have limited computation and memory, yet visual navigation systems often maintain more state than a task requires. We ask whether persistent memory can instead be shaped by the task. We present \textbf{RingNav}, a \(10.6\)k--parameter visual heading estimator that constrains its memory to the circular manifold \(S^1\). RingNav learns only the tu…

### 5. Degeneracy-Orthogonal Geometric Constraints for LiDAR SLAM

- **arXiv**: [2609.36753v1](https://arxiv.org/abs/2609.36753v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.36753v1)
- **作者**: Minseo Kim, Yina Kim, Jinhwa Hwang et al.
- **发表**: 2026-09-29  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Autonomous robot navigation relies on simultaneous localization and mapping (SLAM) to estimate motion and maintain an accurate pose within an environment. However, in axially uniform corridors such as long tunnels and pipelines, LiDAR odometry is fundamentally limited by unconstrained drift along the feature-weak travel direction. This structural degeneracy…

### 6. Chain-SLAM: Globally Consistent Backend for Multi-Session LiDAR SLAM via Chained Loop Closure

- **arXiv**: [2609.12221v1](https://arxiv.org/abs/2609.12221v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.12221v1)
- **作者**: Zhiheng Li, Xinhao Liu, Juexiao Zhang et al.
- **发表**: 2026-09-10  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Maintaining consistency over long spatial and temporal horizons remains a fundamental challenge in large-scale LiDAR SLAM, particularly when integrating maps collected across multiple sessions. We present Chain-SLAM, a LiDAR SLAM backend enabling online multi-session map alignment and reuse with global consistency at large scale. We implement a chained loop…

### 7. Generative adversarial imitation learning for robot swarms: Learning from human demonstrations and trained policies

- **arXiv**: [2603.02783v1](https://arxiv.org/abs/2603.02783v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.02783v1)
- **作者**: Mattes Kraus, Jonas Kuckling
- **发表**: 2026-03-03  ·  **类别**: cs.RO, cs.LG, cs.MA
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, robots are supposed to learn from demonstrations of the desired behavior. Most of the work in imitation learning for swarm robotics provides the demonstrations as rollouts of an existing policy. In this work, we provide a framework based on generative adversarial imitation learning that aims to learn collective behaviors from human de…

### 8. End-to-End Deep Imitation Learning: Robot Soccer Case Study

- **arXiv**: [1807.09205v1](https://arxiv.org/abs/1807.09205v1)  ·  **PDF**: [link](https://arxiv.org/pdf/1807.09205v1)
- **作者**: Okan Aşık, Binnur Görer, H. Levent Akın
- **发表**: 2018-06-28  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, behavior learning is generally done using the features extracted from the demonstration data. Recent deep learning algorithms enable the development of machine learning methods that can get high dimensional data as an input. In this work, we use imitation learning to teach the robot to dribble the ball to the goal. We use B-Human robo…

### 9. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 10. A Causal Approach to Predicting and Improving Human Perceptions of Social Navigation Robots

- **arXiv**: [2603.11290v1](https://arxiv.org/abs/2603.11290v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.11290v1)
- **作者**: Maximilian Diehl, Nathan Tsoi, Gustavo Chavez et al.
- **发表**: 2026-03-11  ·  **类别**: cs.RO
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: As mobile robots are increasingly deployed in human environments, enabling them to predict how people perceive them is critical for socially adaptable navigation. Predicting perceptions is challenging for two main reasons: (1) HRI prediction models must learn from limited data, and (2) the obtained models must be interpretable to enable safe and effective i…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (9 篇)

### 1. Spade-SLAM: Sparse Correspondence Anchors for Dense Self-Supervised Visual SLAM

- **arXiv**: [2611.01937v1](https://arxiv.org/abs/2611.01937v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.01937v1)
- **作者**: Julian Philipp Schmitt, Weirong Chen, Ganlin Zhang et al.
- **发表**: 2026-11-01  ·  **类别**: cs.CV
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: We introduce Spade-SLAM, a self-supervised dense visual SLAM framework that substantially narrows the long-standing performance gap to supervised methods in a zero-shot setting. By demonstrating that high-fidelity tracking can be achieved without explicit ground-truth pose and depth labels, our approach offers a highly effective and label-efficient alternat…

### 2. SKiD-SLAM: Resource-Aware Distributed Multi-Robot LiDAR SLAM for Planetary Missions with Field Deployments at Analog Sites

- **arXiv**: [2610.38141v1](https://arxiv.org/abs/2610.38141v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.38141v1)
- **作者**: Hogyun Kim, Juwon Kim, Dongjin Cho et al.
- **发表**: 2026-10-28  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **📚 综述(归档备查,按协议 §4 不深读)**
- **摘要**: Future planetary exploration missions require teams of robots to collaboratively map unknown environments under severe communication limits, constrained onboard computation, and no central infrastructure. In this field report, we present SKiD-SLAM, a distributed multi-robot LiDAR simultaneous localization and mapping (SLAM) system for such environments, and…

### 3. Evaluation of Front-End Feature Matching for Lunar Visual SLAM

- **arXiv**: [2610.30774v1](https://arxiv.org/abs/2610.30774v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30774v1)
- **作者**: Guillem Casadesus Vila, Grace Gao
- **发表**: 2026-10-22  ·  **类别**: cs.CV
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Lunar rovers will primarily rely on cameras for localization until navigation satellite services are deployed, and will continue to need them afterwards for relative navigation, hazard detection, and surface operations. Visual odometry (VO) and Simultaneous Localization and Mapping (SLAM) mostly estimate motion by matching features between frames. However,…

### 4. Line-Augmented cuVSLAM: Robust Visual Odometry in Low-Texture Environments

- **arXiv**: [2610.20958v1](https://arxiv.org/abs/2610.20958v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20958v1)
- **作者**: Dara Molloy, Terry Wu, Wonju Lee et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Autonomous mobile robots in warehouses and production facilities operate in precisely the environments that defeat point-feature visual odometry: featureless aisles, uniform walls, repetitive racking and specular floors. Such environments are, however, rich in straight-edge structure: rack uprights, door frames, wall junctions and cabinet outlines present h…

### 5. Smartphone Indoor Localization Enhanced by Hierarchical Multi-Sensor Context Recognition

- **arXiv**: [2610.39691v1](https://arxiv.org/abs/2610.39691v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.39691v1)
- **作者**: Wenhui Feng, Muhan Weng, Jianyu Liu et al.
- **发表**: 2026-10-29  ·  **类别**: cs.LG, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Smartphone indoor localization requires low-cost, robust positioning across scene transitions and phone-use variations. Pedestrian dead reckoning (PDR) enables infrastructure-free deployment but accumulates errors from heading drift, structural transitions, and carrying-mode changes. Existing methods often treat contextual cues as a single event stream or l…

### 6. Human-in-the-Loop Neuro-Symbolic Drift Anticipation for Reliable Visual SLAM

- **arXiv**: [2610.05757v1](https://arxiv.org/abs/2610.05757v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05757v1)
- **作者**: Junhyun Nam, Wonse Jo
- **发表**: 2026-10-05  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: This paper introduces Hybrid DeepSEE (HDS), a Human-in-the-Loop (HITL) neuro-symbolic framework for proactive drift anticipation in Visual SLAM (V-SLAM). While data-driven models offer predictive power, their "black-box" nature often yields physically inconsistent outputs in out-of-distribution (OOD) environments. To address this, HDS integrates neural drif…

### 7. RTISSLAM-3D: Full 6-DoF SLAM With an In-Air 3D Imaging Sonar

- **arXiv**: [2610.22552v1](https://arxiv.org/abs/2610.22552v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.22552v1)
- **作者**: Jan Steckel, Vincent Katter, Wouter Jansen
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Echolocating bats navigate dense forests using sonar alone, and in-air 3D imaging sonars now capture the entire frontal hemisphere with every pulse. Sonar SLAM, however, has so far been planar: current systems estimate a 2D trajectory and discard the elevation information in the sonar images, an assumption that does not hold on rough and sloped terrain such…

### 8. Does Dynamic-Point Filtering Help When Texture Is Scarce? A Controlled Study of ORB-SLAM2 Front-Ends in Synthetic Indoor Scenes

- **arXiv**: [2610.10564v1](https://arxiv.org/abs/2610.10564v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10564v1)
- **作者**: Zekui Xue
- **发表**: 2026-10-02  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Dynamic-point filters are routinely added to feature-based visual SLAM, and several recent systems argue that removing dynamic features can leave too few static features in low-texture regions. So far, these systems have been evaluated only on texture-rich benchmark sequences. We present a controlled study that isolates this interaction. We render synthetic…

### 9. Parameter Sensitivity Analysis for Aerial LiDAR-Inertial Odometries in low-altitude flights

- **arXiv**: [2609.12837v1](https://arxiv.org/abs/2609.12837v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.12837v1)
- **作者**: Robert Milijas, Jose Ramiro Martinez-de Dios, Stjepan Bogdan
- **发表**: 2026-09-11  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: LiDAR-based SLAM (Simultaneous Localization and Mapping) and LIO (LiDAR-inertial odometry) algorithms are often used for precise navigation of unmanned aerial vehicles, especially during interactions with the aerial robot's environment. However, the performance of these algorithms is greatly dependent on the scenario, LiDAR, and robot motion characteristics…

## 🧭 导航 / 路径规划 (1 篇)

### 1. Clinician-AI Collaboration in Endovascular Neurointerventions: In-Vitro User Study of Copilot Assistance Modes for Robotic Navigation Across the Autonomy Spectrum

- **arXiv**: [2611.03446v2](https://arxiv.org/abs/2611.03446v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.03446v2)
- **作者**: Nikola Fischer, Harry Robertshaw, S. M. Hadi Sadati et al.
- **发表**: 2026-11-02  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Mechanical thrombectomy (MT) is an effective treatment for acute ischemic stroke, yet access remains limited by the availability of neurointerventional expertise. Telerobotic and AI-assisted systems may help address this challenge, but it remains unclear how clinicians interact with different levels of autonomy and how autonomous navigation systems perform…

## 🧪 仿真 / Sim2Real (1 篇)

### 1. Training-Time Domain Transfer for Generator-Free Diagnostics on Novel Modalities in Computational Pathology

- **arXiv**: [2611.02931v1](https://arxiv.org/abs/2611.02931v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.02931v1)
- **作者**: Julia A. Mielcarz, Andrea Camilloni, Nita Mulliqi et al.
- **发表**: 2026-11-02  ·  **类别**: cs.CV, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Novel imaging modalities promise improved diagnostics, but AI development is constrained by scarce training data. Inference-time domain transfer can address this by mapping novel modalities to established ones, enabling reuse of existing diagnostic models. However, this introduces hallucination risks, computational overhead, and regulatory complexity. Inspi…

## 🤏 软体机器人 / 柔性控制 (4 篇)

### 1. SomaAlign: Reliability-Aware Multimodal Representation Learning for Soft Robotic Grasping

- **arXiv**: [2611.02794v1](https://arxiv.org/abs/2611.02794v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.02794v1)
- **作者**: Haoyuan Wang, Shuai Peng, Yongkai Liao et al.
- **发表**: 2026-11-02  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Robust multimodal perception for soft robotic grasping is challenged by modality-dependent noise, semantic ambiguity, and limited coordinated multisensory data. We introduce Soma, a dataset containing 100 objects, 1,000 continuous grasping trajectories, and 74,914 multimodal samples grouped by software acquisition cycle, spanning remote RGB, hand RGB, depth…

### 2. $\mathcal{C}^\infty$ Smooth Trajectory Planning with Application to Soft Robots

- **arXiv**: [2611.05615v1](https://arxiv.org/abs/2611.05615v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.05615v1)
- **作者**: Reinhard M. Grassmann, Abdulaziz Y. Alkayas, Lingyun Chen et al.
- **发表**: 2026-11-03  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: High motion performance and avoiding structural vibrations rely on smooth trajectory planning. The smoothness requirement depends on the robot's complexity in terms of the number of degrees of freedom and system order due to the flexibility of the joints and links. For industrial robots, the smoothness requirements have been determined and subsequently take…

### 3. Flap like a bat: Soft pneumatic wings for biomimetic ornithopters

- **arXiv**: [2611.00879v1](https://arxiv.org/abs/2611.00879v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.00879v1)
- **作者**: Besetty Satyanarayana, Sirivelu Akhilesh, Bammidi Abhilash et al.
- **发表**: 2026-10-31  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: This paper describes the development of a bio-inspired ornithopter wing mechanism that uses soft pneumatic actuators, such as PneuNet structures, in place of revolute joints, inspired by the complicated kinematics of bat flight. The proposed design employs pneumatically driven air pockets within a flexible wing skeleton to achieve smooth, lifelike flapping…

### 4. From Biological Curves to Soft Modular Robots: Learning-Based Inverse Design with Uncertainty-Guided Refinement

- **arXiv**: [2610.36681v2](https://arxiv.org/abs/2610.36681v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.36681v2)
- **作者**: Dixiang Wang, Minghao Zha, Arifur Rahman et al.
- **发表**: 2026-10-27  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Animals exhibit diverse shape-changing behaviors, from the undulatory swimming of eels to the arching movements of inchworms. Reproducing these biological shapes with modular soft robots offers a promising approach to developing versatile bioinspired robotic systems. However, translating a desired shape into a feasible robotic configuration remains challeng…

## 📦 其他机器人相关 (1 篇)

### 1. ReShoot: Generative Visual Domain Randomization of Recorded Robot Demonstrations for Visuomotor Policy Learning

- **arXiv**: [2609.19661v1](https://arxiv.org/abs/2609.19661v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.19661v1)
- **作者**: Chiyoung Kim, Min Sung Choi, Jinho Ju et al.
- **发表**: 2026-09-17  ·  **类别**: cs.RO
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Imitation-learned robot policies are frequently overfit to the visual conditions present in their training demonstrations. Consequently, variations in object color or background appearance often induce substantial performance degradation. A common mitigation strategy is to acquire additional demonstrations in each novel visual context; however, this approac…

---

## 📋 本日操作建议

**建议今日深读 (Top 3):**
1. [Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation](https://arxiv.org/abs/2611.05979v1) — score 20
2. [DexHOT: Learning Hand-Object Configuration Transfer for Dexterous Manipulation](https://arxiv.org/abs/2611.05119v1) — score 20
3. [EXE: Egocentric Cross-Embodiment Pretraining via Factorized Latent Actions for VLA Models](https://arxiv.org/abs/2610.33685v1) — score 18

> 筛选说明:本次 Top 3 已排除(综述跳过 1 篇)。

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
