# 机器人研究每日摘要 · 2026-10-20

> 自动生成,共 89 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (10 篇)

### 1. From Sliding Windows to Self-evolving Lifelong Memory: A Dual-perspective Survey of Memory Paradigms for Long-Horizon Robotics VLA Models

- **arXiv**: [2610.23319v1](https://arxiv.org/abs/2610.23319v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.23319v1)
- **作者**: Yong Wang, Boyu Shen, Xinwei Zhang et al.
- **发表**: 2026-10-16  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Long-horizon robotic tasks expose a fundamental limitation of current Vision-Language-Action (VLA) models because their restricted temporal context pre-vents effective accumulation and reuse of past experiences. As a result, memory has become a fundamental component for enabling embodied agents to perform long-horizon reasoning and adaptive decision-making.…

### 2. NestedVLA: Learning to Consolidate and Generate Skills for Vision-Language-Action Models

- **arXiv**: [2610.23271v1](https://arxiv.org/abs/2610.23271v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.23271v1)
- **作者**: Guodong Du, Wanyu Lin
- **发表**: 2026-10-16  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Vision--Language--Action (VLA) models promise generalist robotic agents, yet consolidating skills learned across heterogeneous tasks and environments remains difficult: training data is fragmented across platforms, joint multi-task training suffers from interference, and model merging tends to introduce parameter conflicts or require architectural changes.…

### 3. ACCRUE: Continual Off-Policy Reinforcement Learning for Robot Foundation Models

- **arXiv**: [2610.18596v1](https://arxiv.org/abs/2610.18596v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.18596v1)
- **作者**: Changyeon Kim, Kimin Lee, Yashraj Narang et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Reinforcement learning (RL) post-training improves robot foundation models (RFMs) beyond their demonstrations, but real-world deployment demands more: learning new tasks efficiently while retaining previously acquired behaviors. Existing continual RL methods on top of VLAs mitigate forgetting but rely on on-policy updates with limited forward transfer, wher…

### 4. AdaRSI: On-Demand Recursive Self-Improvement for Embodied Agents

- **arXiv**: [2610.20474v1](https://arxiv.org/abs/2610.20474v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20474v1)
- **作者**: Peidong Wang, Ying Chang, Zhiming Ma et al.
- **发表**: 2026-10-14  ·  **类别**: cs.CL, cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Pretrained vision-language-action models (VLAs) often fail midway through unseen long-horizon tasks. Recursive self-improvement (RSI) offers a remedy, but embodied RSI methods either refine the harness around a frozen executor and so cannot add a missing motion, or train the executor on persistent failures without asking whether a failure lies in how the ex…

### 5. Multi-Dimensional Featurizers Yield Fine-Grained Steering and Data Shaping in Robot Foundation Models

- **arXiv**: [2610.20767v1](https://arxiv.org/abs/2610.20767v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20767v1)
- **作者**: Aiden Swann, Mozes Jacobs, Mathilde Papillon et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Can better feature discovery improve control over robot behavior through internal interventions and training data? Recent work in vision and language models reveals multidimensional features, motivating block-sparse featurizers (BSFs), which represent each feature in a low-dimensional subspace. We investigate whether recovering this structure provides an in…

### 6. Beyond Success Rate: Interventional Evaluation of Memory in Vision-Language-Action Systems

- **arXiv**: [2610.23372v1](https://arxiv.org/abs/2610.23372v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.23372v1)
- **作者**: Keyuan Luo, Yi Xie, Wanyun Ling et al.
- **发表**: 2026-10-16  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: When we say that a robot uses memory, does that memory actually play a role? Success-rate ablations alone cannot establish the use of task-relevant facts: they change information and computation together, while aggregate rates can hide offsetting gains and losses. We propose an Interventional Memory Evaluation Protocol (IMEP) for vision-language-action (VLA…

### 7. $Δ$ Flow Matching for Robot Foundation Models

- **arXiv**: [2610.15794v1](https://arxiv.org/abs/2610.15794v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.15794v1)
- **作者**: Kuangji Zuo, Tuo An, Xinying Guo et al.
- **发表**: 2026-10-11  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Flow matching is a common generative recipe for robot foundation models. Vision-language-action models (VLAs) generate action chunks, while world-action models (WAMs) additionally generate future visual states. Both start generation from a fixed Gaussian prior, despite temporal continuity between past and future states and actions. This requires costly trai…

### 8. Unifying Embodied Foundation Models via a Model-to-Policy Formulation

- **arXiv**: [2610.23053v1](https://arxiv.org/abs/2610.23053v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.23053v1)
- **作者**: Xinyi Hong, Mingyang Ren
- **发表**: 2026-10-16  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Vision-language-action (VLA) models and world-action models (WAMs) have emerged as promising approaches to robot learning and control. These models integrate multimodal perception and action generation, but differ in their architectures, output representations, and learning objectives. In this paper, we present a unified, architecture-agnostic probabilistic…

### 9. ARC: A Reasoning Recipe for Robot Foundation Models

- **arXiv**: [2610.12386v1](https://arxiv.org/abs/2610.12386v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12386v1)
- **作者**: Gokul Puthumanaillam, Tao Sun, Elie Aljalbout et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The prevailing approach to improving robot foundation models (RFMs) relies on larger models, more robot demonstrations, and costly training at scale. We show that there exists an effective and efficient complementary approach: the right reasoning recipe can substantially improve the zero-shot task performance of existing state-of-the-art RFMs. We refer to t…

### 10. Embodiment-Classifier Guidance: Transferring Frozen VLAs Across Robot Dynamics without Demonstrations

- **arXiv**: [2610.22576v1](https://arxiv.org/abs/2610.22576v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.22576v1)
- **作者**: Devin Han, Hershraj Niranjani
- **发表**: 2026-10-15  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Flow-based policies such as $π_0$ are trained on a fixed set of embodiments, and transferring them to new ones is an open problem. To adapt a frozen $π_0$ to a new embodiment without additional demonstrations or parameter updates, we train a lightweight embodiment classifier to distinguish successful action chunks on the source body from those on the target…

## 🌐 具身智能 / 机器人基础模型 (9 篇)

### 1. SimpleVLN: Towards Simple and Frontier Vision-Language Navigation

- **arXiv**: [2610.23203v1](https://arxiv.org/abs/2610.23203v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.23203v1)
- **作者**: Lingyi Hong, Weiren Cai, Jiayu Chen et al.
- **发表**: 2026-10-16  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Vision-and-Language Navigation (VLN) requires embodied agents to ground language in visual observations and make long-horizon decisions. Existing methods often address these demands through task-specific architectures. As multimodal large language models (MLLMs) become increasingly capable, an important question remains: Have we truly unlocked the potential…

### 2. Towards a Data-Centric Understanding of Spatial Reasoning in Multimodal Large Language Models

- **arXiv**: [2610.19108v1](https://arxiv.org/abs/2610.19108v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19108v1)
- **作者**: Mahdieh Mallahnezhad, Masoud Jafaripour, Mohamadali Tofigh et al.
- **发表**: 2026-10-13  ·  **类别**: cs.CV, cs.AI, cs.CL
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Multimodal Large Language Models (MLLMs) have been widely applied in embodied agents and robotics for vision tasks. However, MLLMs suffer from limitations in spatial reasoning and perception. Post-training techniques have shown promise for improving these capabilities; yet, there are limited data-driven surveys of such approaches. In this survey, we conside…

### 3. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 4. Thinking from Above: Efficient Spatial Reasoning with Bird's-Eye-View Visual Tokens

- **arXiv**: [2610.22700v1](https://arxiv.org/abs/2610.22700v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.22700v1)
- **作者**: Faizan Siddiqui, Nirav Savaliya, Sahith Reddy Chada et al.
- **发表**: 2026-10-15  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Existing video multimodal large language models (MLLMs) organize observations primarily in time, but embodied spatial reasoning requires organizing them in space. Consequently, their visual representations can remain locally consistent across nearby frames while lacking a persistent spatial context that is stable across viewpoints and time. We exploit depth…

### 5. F2A-ObjectNav: An Adaptive Agentic Architecture for Object-Goal Navigation

- **arXiv**: [2610.19618v1](https://arxiv.org/abs/2610.19618v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19618v1)
- **作者**: Seyed Ali Mirghasemi, Alireza Taheri
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Object-goal navigation requires an embodied agent to explore an unfamiliar environment, identify a target object, navigate toward candidate instances, and reliably determine whether the observed object satisfies the mission goal. This work investigates this problem through a two-stage development process. In Stage I, a fixed modular framework is used to exa…

### 6. From Failures to Learnable Worlds: Policy-Conditioned Environment Generation for Navigation Agents

- **arXiv**: [2610.19420v1](https://arxiv.org/abs/2610.19420v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19420v1)
- **作者**: Yue Zhang, Han Lin, Zun Wang et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Simulated environments enable scalable training data generation for embodied agents, but more data does not necessarily provide what a particular agent needs to learn. Existing environment-generation pipelines largely optimize generic properties such as realism, diversity, or task coverage, while different pretrained policies can fail for different environm…

### 7. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

### 8. FoundationVIO: Enforcing Metric Scale in Feed-forward Visual-Inertial Odometry

- **arXiv**: [2610.14951v1](https://arxiv.org/abs/2610.14951v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.14951v1)
- **作者**: Jin Rhee, Yuhao Zhang, Frank Dellaert et al.
- **发表**: 2026-10-10  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Feed-forward geometric foundation models (GFMs) directly predict dense geometry and camera poses from batches of images. Emerging visual SLAM methods chain together consecutive GFM batches to form dense point cloud maps. A core challenge is how to address the ambiguous geometric scale of GFM predictions: independent predictions are locally consistent up-to-…

### 9. EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution

- **arXiv**: [2610.10498v1](https://arxiv.org/abs/2610.10498v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10498v1)
- **作者**: Python Song, Zhixuan Liang, Kelsey Fu et al.
- **发表**: 2026-10-07  ·  **类别**: cs.AI
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Robot foundation models provide strong visuomotor control, yet their performance can degrade when object positions or task instructions change. Further improvements often require post-training on substantial robot data, which can be costly to collect through methods such as teleoperation. Agentic harnesses can adapt around the model, but current self-evolvi…

## 🦵 人形 / 足式机器人 (27 篇)

### 1. CoEvolve: Self-Evolving Code Policies from Skills to Strategies for Humanoid Robots

- **arXiv**: [2610.23288v1](https://arxiv.org/abs/2610.23288v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.23288v1)
- **作者**: Zicheng Liu, Haochen Wu, Jiawei He et al.
- **发表**: 2026-10-16  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Recent advances in Vision-Language-Action (VLA) models and World Action Models (WAMs) have expanded the manipulation and whole body capabilities of individual robots. Yet a single robot remains limited by its embodiment, and many real world tasks require capabilities that can only emerge through cooperation. Existing multi robot frameworks largely emphasize…

### 2. Reinforcement Learning Based Multi-Terrain Adaptive Whole-Body Control for a Quadruped Manipulator

- **arXiv**: [2610.23548v1](https://arxiv.org/abs/2610.23548v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.23548v1)
- **作者**: Yanzhou Jin, Fei Suo, Chang Liu et al.
- **发表**: 2026-10-16  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Legged robots equipped with manipulators offer promising capabilities for loco-manipulation tasks in unstructured environments. However, achieving task-consistent end-effector behavior during locomotion remains challenging due to terrain-induced disturbances and the strong coupling between locomotion and manipulation, particularly for small-scale quadruped…

### 3. Beyond Kinematic Tracking: Preserving Expressive Characteristics in Humanoid Whole-Body Control

- **arXiv**: [2610.19393v1](https://arxiv.org/abs/2610.19393v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19393v1)
- **作者**: Lingfan Bao, Hanshang Zhu, Yan Pan et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Whole-body control plays a crucial role in enabling humanoid robots to execute expressive motions. Faithful execution requires preserving both the intended action and its expressive characteristics. Existing whole-body trackers typically balance joint and keypoint tracking with physical stability across diverse motions, but these objectives do not necessari…

### 4. CQDC-Warp: GPU-Accelerated Differentiable Quasi-Dynamic Simulation for Contact-Rich Manipulation

- **arXiv**: [2610.21349v1](https://arxiv.org/abs/2610.21349v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.21349v1)
- **作者**: Yanchen Ding, Jiayi Chen, Jianfeng Xu et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Efficient synthesis of contact-rich manipulation trajectories is essential for downstream robot learning. Gradient-based planning offers a promising approach, but jointly optimizing motion and contact decisions remains challenging. Meanwhile, many existing planners run on CPUs with limited throughput. We present CQDC-Warp, a GPU-accelerated differentiable q…

### 5. E2DRL: End-to-End Differentiable Reinforcement Learning for 3D Obstacle Avoidance in Quadruped Robots

- **arXiv**: [2610.19627v1](https://arxiv.org/abs/2610.19627v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19627v1)
- **作者**: Cheng Fan, Bingyang Zhou, Gang Yang et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Differentiable reinforcement learning shows strong promise for robot policy learning, but its application to legged locomotion has remained limited to blind walking or simulated 2D tasks. Extending it to end-to-end visual obstacle avoidance is challenging because hard collision constraints and early termination upon contact corrupt first-order gradients, tr…

### 6. Spark-0: Scaling Spatially Aligned Tactile Pretraining for Robot Dexterous Manipulation

- **arXiv**: [2610.22342v1](https://arxiv.org/abs/2610.22342v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.22342v1)
- **作者**: Tianxing Chen, Wenwei Lin, Chuqiao Lyu et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Generalist robot policies benefit from large-scale visual pretraining but often struggle with contact-rich dexterous manipulation, where force, compliance, and incipient slip are hard to observe from images. We present Spark-0, a spatially aligned vision-tactile-language-action (VTLA) model that uses touch in two complementary ways. During pretraining, imag…

### 7. Whole-Body Dexterity

- **arXiv**: [2610.22184v1](https://arxiv.org/abs/2610.22184v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.22184v1)
- **作者**: Conor Mc Gartoll, An Dang, Pranay Thangeda et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Current humanoid dexterous manipulation remains largely confined to end-effectors and simple grasps, falling short of humans' ability to engage the entire body by bracing and sliding bulky objects against the arms and torso. We introduce Whole-Body Dexterity (WBD), a general framework that uses the robot's body and appendages as contact surfaces to grasp an…

### 8. KODA: Kinematics--Observation Data Alignment for Humanoid Learning from Human Egocentric Demonstration

- **arXiv**: [2610.21152v1](https://arxiv.org/abs/2610.21152v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.21152v1)
- **作者**: Zibo Zhou, Yueru Chen, Junsong Wu et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Training humanoid whole-body vision-language-action (VLA) policies requires costly robot demonstrations with aligned robot-view observations and controller-compatible whole-body state-action labels. Egocentric human demonstrations offer scalable supervision but have misaligned views and sparse motion cues. Existing approaches either pretrain policies that s…

### 9. OccluDex: Hierarchical 3D Visuo-Tactile Representation Learning for Egocentric Dexterous Manipulation under Self-Occlusion

- **arXiv**: [2609.39017v1](https://arxiv.org/abs/2609.39017v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39017v1)
- **作者**: Ziheng Xu, Yueyuan Chen, Xinyuan He et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Reliable dexterous manipulation requires continuous estimation of object geometry and hand-object contact throughout interaction. With egocentric sensing, however, the manipulating hand frequently occludes task-relevant object surfaces and contact regions, reducing the visual evidence available for state estimation and thereby making robust closed-loop cont…

### 10. Blind Precise Assembly: Proprioceptive Sim-to-Real Peg-in-Hole for Diverse Parts

- **arXiv**: [2610.23849v1](https://arxiv.org/abs/2610.23849v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.23849v1)
- **作者**: Antonia Bronars, Younghyo Park, Kushal Kedia et al.
- **发表**: 2026-10-16  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Every robot already carries high-resolution contact sensors: its own joints. Legged robots and humanoids exploit them to walk, run, and track whole-body motions without vision, but there the contacts are large and forceful. Is joint sensing also enough for precise, contact-rich assembly, where the robot must find a millimeter-scale opening, mesh gear teeth,…

## 🦾 操控 / 灵巧手 / 抓取 (24 篇)

### 1. No Eyes, No Problem: What Does Touch Contribute to Blind Baoding Ball Manipulation?

- **arXiv**: [2610.23438v1](https://arxiv.org/abs/2610.23438v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.23438v1)
- **作者**: Ayush Deshmukh, Nalin Agarwal, Elle Miller et al.
- **发表**: 2026-10-16  ·  **类别**: cs.RO
- **相关性评分**: 22  ·  **🔥 read_now**
- **摘要**: Humans manipulate objects within their hands through touch alone with remarkable ease, but for robots, achieving sustained real-world manipulation without vision remains an open challenge. Although reinforcement learning (RL) can generate sophisticated blind manipulation policies in simulation, transferring them to a real dexterous hand remains hindered by…

### 2. HiFun: a Hierarchical Framework for Efficient Functional Dexterous Manipulation Learning

- **arXiv**: [2610.19518v1](https://arxiv.org/abs/2610.19518v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19518v1)
- **作者**: Linyi Huang, Guowei Huai, Weibin Liu et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: While multi-fingered dexterous robot hands have the potential to provide human-level dexterity, using them for functional manipulation remains difficult because task success depends on precise contact, coordinated arm-hand motion, and reactive recovery from execution errors. Precise contact depends on complex contact dynamics that are difficult to model acc…

### 3. Enhancing Visual Task-Redirection Attacks on Vision-Language-Action Models via Closed-Loop Optimization

- **arXiv**: [2610.23566v1](https://arxiv.org/abs/2610.23566v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.23566v1)
- **作者**: Chunjin Ye, Guanying Chen, Jianjie Huang et al.
- **发表**: 2026-10-16  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models enable language-guided robot manipulation, but remain vulnerable to visual attacks that undermine user control over robot behavior. Prior studies optimize visual perturbations using fixed target supervision. However, the perturbation can change earlier actions and, in turn, the physical states reached later. As the attack…

### 4. DexMimic: A Generalist Dexterous Hand-Object Tracking Policy via Value-Guided Reset Allocation

- **arXiv**: [2610.19089v2](https://arxiv.org/abs/2610.19089v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19089v2)
- **作者**: Zhexi Luo, Zhixuan Xu, Rui Yang et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Achieving human-like dexterous manipulation remains a central challenge in robotics. Learning from human hand-object interaction (HOI) datasets offers a promising pathway to diverse dexterous skills, yet existing physics-based approaches train specialist policies for individual trajectories, thereby limiting skill reuse at scale. We introduce DexMimic, a ge…

### 5. EgoCPT: Learning Dexterous Manipulation from a Single Ego-Centric Video with Contact-Aware Optimization

- **arXiv**: [2610.17572v1](https://arxiv.org/abs/2610.17572v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.17572v1)
- **作者**: Zhixin Sun, Kairui Shi, Tianao Ren et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: While expert demonstrations on real robots are difficult to collect, human ego-centric videos are easy to collect and abundant on the internet. However, learning dexterous manipulation policies from human videos remains challenging---one of the most important challenges being the difficulty of reconstructing physically grounded robot trajectories due to the…

### 6. Causal Analysis of Robot Foundation Models Enables Efficiency Gains

- **arXiv**: [2610.20750v1](https://arxiv.org/abs/2610.20750v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20750v1)
- **作者**: Aiden Swann, Mathilde Papillon, Mozes Jacobs et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models are a promising approach to general purpose robot manipulation. While the internal computation of vision-language models, which compose the backbone of VLAs, has been studied extensively, less is known about how their perceptual and semantic representations are transformed into action in VLA models. We study this question…

### 7. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

### 8. Perceive, Predict, and Plan: a Unified World Action Model for Egocentric Dexterous Manipulation

- **arXiv**: [2610.22363v1](https://arxiv.org/abs/2610.22363v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.22363v1)
- **作者**: Zirui Wu, Chen Guo, Tianjian Jiang et al.
- **发表**: 2026-10-15  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: We introduce P$^{3}$-WAM, a unified world action model for egocentric dexterous manipulation that learns 3D perception, action-conditioned prediction, and goal-directed planning through three complementary modes: Perceive, which reconstructs articulated hand motion and camera trajectories from video; Predict, which generates visual futures under prescribed…

### 9. Evo-DexBench: Benchmarking Generalization across Related Tasks for Dexterous Manipulation

- **arXiv**: [2610.21180v1](https://arxiv.org/abs/2610.21180v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.21180v1)
- **作者**: Bing Cheng, Yiran Mao, Zewei Ye et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: General-purpose dexterous manipulation requires policies to transfer knowledge from related tasks to new tasks with only a few target demonstrations. Existing benchmarks often provide too many target demonstrations. They also leave the differences between source and target tasks uncontrolled. As a result, they cannot clearly distinguish knowledge transfer f…

### 10. EgoJEPA: Beyond Retargeting for Dexterous Manipulation from Egocentric Videos

- **arXiv**: [2610.20904v1](https://arxiv.org/abs/2610.20904v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20904v1)
- **作者**: Meng Cao, Can Zhao, Jinjie Wei et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Egocentric human videos offer a scalable alternative to costly robot demonstra- tions, yet transferring their manipulation priors to robot control remains chal- lenging. The commonly adopted retargeting-based approaches convert human wrist and finger poses into embodiment-specific action commands through hand- crafted geometric mappings. However, such mappi…

## 🎓 模仿学习 / 强化学习 (8 篇)

### 1. RingNav: Task-Shaped Circular Memory for Visual Heading

- **arXiv**: [2610.19044v1](https://arxiv.org/abs/2610.19044v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19044v1)
- **作者**: Naitri Rajyaguru, Aryan Tajne, Stephen Jardim et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Tiny robots have limited computation and memory, yet visual navigation systems often maintain more state than a task requires. We ask whether persistent memory can instead be shaped by the task. We present \textbf{RingNav}, a \(10.6\)k--parameter visual heading estimator that constrains its memory to the circular manifold \(S^1\). RingNav learns only the tu…

### 2. Generative adversarial imitation learning for robot swarms: Learning from human demonstrations and trained policies

- **arXiv**: [2603.02783v1](https://arxiv.org/abs/2603.02783v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.02783v1)
- **作者**: Mattes Kraus, Jonas Kuckling
- **发表**: 2026-03-03  ·  **类别**: cs.RO, cs.LG, cs.MA
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, robots are supposed to learn from demonstrations of the desired behavior. Most of the work in imitation learning for swarm robotics provides the demonstrations as rollouts of an existing policy. In this work, we provide a framework based on generative adversarial imitation learning that aims to learn collective behaviors from human de…

### 3. End-to-End Deep Imitation Learning: Robot Soccer Case Study

- **arXiv**: [1807.09205v1](https://arxiv.org/abs/1807.09205v1)  ·  **PDF**: [link](https://arxiv.org/pdf/1807.09205v1)
- **作者**: Okan Aşık, Binnur Görer, H. Levent Akın
- **发表**: 2018-06-28  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, behavior learning is generally done using the features extracted from the demonstration data. Recent deep learning algorithms enable the development of machine learning methods that can get high dimensional data as an input. In this work, we use imitation learning to teach the robot to dribble the ball to the goal. We use B-Human robo…

### 4. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 5. Unblur-SLAM: Dense Neural SLAM for Blurry Inputs

- **arXiv**: [2603.26810v1](https://arxiv.org/abs/2603.26810v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.26810v1)
- **作者**: Qi Zhang, Denis Rozumny, Francesco Girlanda et al.
- **发表**: 2026-03-26  ·  **类别**: cs.CV, eess.IV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We propose Unblur-SLAM, a novel RGB SLAM pipeline for sharp 3D reconstruction from blurred image inputs. In contrast to previous work, our approach is able to handle different types of blur and demonstrates state-of-the-art performance in the presence of both motion blur and defocus blur. Moreover, we adjust the computation effort with the amount of blur in…

### 6. Query Quantized Neural SLAM

- **arXiv**: [2412.16476v1](https://arxiv.org/abs/2412.16476v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2412.16476v1)
- **作者**: Sijia Jiang, Jing Hua, Zhizhong Han
- **发表**: 2024-12-21  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural implicit representations have shown remarkable abilities in jointly modeling geometry, color, and camera poses in simultaneous localization and mapping (SLAM). Current methods use coordinates, positional encodings, or other geometry features as input to query neural implicit functions for signed distances and color which produce rendering errors to d…

### 7. ACE-SLAM: Scene Coordinate Regression for Neural Implicit Real-Time SLAM

- **arXiv**: [2512.14032v1](https://arxiv.org/abs/2512.14032v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2512.14032v1)
- **作者**: Ignacio Alzugaray, Marwan Taher, Andrew J. Davison
- **发表**: 2025-12-16  ·  **类别**: cs.CV, cs.AI, eess.IV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: We present a novel neural RGB-D Simultaneous Localization And Mapping (SLAM) system that learns an implicit map of the scene in real time. For the first time, we explore the use of Scene Coordinate Regression (SCR) as the core implicit map representation in a neural SLAM pipeline, a paradigm that trains a lightweight network to directly map 2D image feature…

### 8. MISO: Multiresolution Submap Optimization for Efficient Globally Consistent Neural Implicit Reconstruction

- **arXiv**: [2504.19104v1](https://arxiv.org/abs/2504.19104v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2504.19104v1)
- **作者**: Yulun Tian, Hanwen Cao, Sunghwan Kim et al.
- **发表**: 2025-04-27  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Neural implicit representations have had a significant impact on simultaneous localization and mapping (SLAM) by enabling robots to build continuous, differentiable, and high-fidelity 3D maps from sensor data. However, as the scale and complexity of the environment increase, neural SLAM approaches face renewed challenges in the back-end optimization process…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (8 篇)

### 1. LIN-SLAM: Lightweight LiDAR--Inertial Neural SLAM for Real-Time Onboard Navigation

- **arXiv**: [2610.21199v1](https://arxiv.org/abs/2610.21199v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.21199v1)
- **作者**: Shiqi Che, Yijie Liu, Shuo Wang et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Geometric light detection and ranging (LiDAR)--inertial simultaneous localization and mapping (SLAM) provides efficient state estimation but lacks the continuous map representation and global refinement capabilities of neural implicit SLAM, while neural implicit methods remain computationally expensive. We propose Lightweight LiDAR--Inertial Neural SLAM (LI…

### 2. Line-Augmented cuVSLAM: Robust Visual Odometry in Low-Texture Environments

- **arXiv**: [2610.20958v1](https://arxiv.org/abs/2610.20958v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20958v1)
- **作者**: Dara Molloy, Terry Wu, Wonju Lee et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Autonomous mobile robots in warehouses and production facilities operate in precisely the environments that defeat point-feature visual odometry: featureless aisles, uniform walls, repetitive racking and specular floors. Such environments are, however, rich in straight-edge structure: rack uprights, door frames, wall junctions and cabinet outlines present h…

### 3. Human-in-the-Loop Neuro-Symbolic Drift Anticipation for Reliable Visual SLAM

- **arXiv**: [2610.05757v1](https://arxiv.org/abs/2610.05757v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05757v1)
- **作者**: Junhyun Nam, Wonse Jo
- **发表**: 2026-10-05  ·  **类别**: cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: This paper introduces Hybrid DeepSEE (HDS), a Human-in-the-Loop (HITL) neuro-symbolic framework for proactive drift anticipation in Visual SLAM (V-SLAM). While data-driven models offer predictive power, their "black-box" nature often yields physically inconsistent outputs in out-of-distribution (OOD) environments. To address this, HDS integrates neural drif…

### 4. Know-Your-Scene (KYS)-SLAM: Hierarchical Semantic-Motion Priors for Feature Matching in Stereo Visual SLAM

- **arXiv**: [2609.27509v1](https://arxiv.org/abs/2609.27509v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27509v1)
- **作者**: Preeti Chatterjee, Jin Lu, Jin Sun et al.
- **发表**: 2026-09-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Stereo visual SLAM systems built on local descriptors suffer from semantic ambiguity, instance-level confusion, and independently moving objects, each corrupting data association and accumulating as trajectory drift. Prevailing semantic and dynamic SLAM methods address this through binary feature rejection, sacrificing correspondence density for outlier sup…

### 5. Does Dynamic-Point Filtering Help When Texture Is Scarce? A Controlled Study of ORB-SLAM2 Front-Ends in Synthetic Indoor Scenes

- **arXiv**: [2610.10564v1](https://arxiv.org/abs/2610.10564v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10564v1)
- **作者**: Zekui Xue
- **发表**: 2026-10-02  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Dynamic-point filters are routinely added to feature-based visual SLAM, and several recent systems argue that removing dynamic features can leave too few static features in low-texture regions. So far, these systems have been evaluated only on texture-rich benchmark sequences. We present a controlled study that isolates this interaction. We render synthetic…

### 6. MVP-SLAM: Multi-Camera Visual-Inertial Floorplan-Prior SLAM

- **arXiv**: [2609.39596v1](https://arxiv.org/abs/2609.39596v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39596v1)
- **作者**: Asier Bikandi-Noya, Miguel Fernandez-Cortizas, Muhammad Shaheer et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Indoor building construction sites are demanding environments for visual SLAM, where variable lighting and repetitive, low-textured structures make the system drift over long trajectories, though structural elements such as walls remain distinguishable despite these conditions. These buildings are constructed according to their as-planned floor plans, avail…

### 7. Cube-Splat: High-Fidelity 360° Gaussian Splatting SLAM via Cubemap Factorization and Adjoint-Consistent Optimization

- **arXiv**: [2609.21347v1](https://arxiv.org/abs/2609.21347v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.21347v1)
- **作者**: Xiangfei Guo, Hao Shi, Yufan Zhang et al.
- **发表**: 2026-09-18  ·  **类别**: cs.CV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Recent progress in 3D Gaussian Splatting (3DGS) has enabled dense visual SLAM with pinhole cameras, yet most pipelines are not designed for panoramic imagery. We present Cube-Splat, the first panoramic GS-SLAM framework that factorizes each 360° frame into a cubemap of four fixed-orientation virtual pinhole views sharing a single optical center. By designat…

### 8. Geodesic Flow Matching for Denoising High-Dimensional Structured Representations

- **arXiv**: [2606.00248v1](https://arxiv.org/abs/2606.00248v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.00248v1)
- **作者**: Karim Habashy, Chris Eliasmith
- **发表**: 2026-05-29  ·  **类别**: cs.AI
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Vector Symbolic Algebras (VSAs) enable robust neurosymbolic reasoning by encoding symbolic information into high-dimensional distributed representations. For continuous domains, Spatial Semantic Pointers (SSPs) extend this framework by mapping variables onto continuous toroidal manifolds. However, standard approaches like Flow Matching assume a flat Euclide…

## 🧭 导航 / 路径规划 (1 篇)

### 1. PASS: A Trustworthy Precision Approach Simulation System for CAT III Integrity Algorithm Development

- **arXiv**: [2610.23019v1](https://arxiv.org/abs/2610.23019v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.23019v1)
- **作者**: Lang Zhu, Xin Zhang, Yulong Sun et al.
- **发表**: 2026-10-16  ·  **类别**: cs.RO, eess.SP
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: For fixed-wing aircraft, reliable localization during approach and landing is critical to flight safety. Visual--inertial navigation is promising, but aircraft navigation also requires integrity: trustworthy outputs and timely warnings when they should not be used. Real approach data are costly to collect, while many visual errors and failures required for…

## 🧪 仿真 / Sim2Real (1 篇)

### 1. Quality-of-Transmission Estimation in Quantum Networks: Compute, Simulate, or Learn?

- **arXiv**: [2610.23827v1](https://arxiv.org/abs/2610.23827v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.23827v1)
- **作者**: Anis Bekri, Amar Abane, Van Sy Mai et al.
- **发表**: 2026-10-16  ·  **类别**: quant-ph, cs.LG, cs.NI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Future quantum networks will rely on control-plane decisions such as routing, scheduling, entanglement provisioning, purification, and memory allocation. Each decision depends on a timely and reliable estimate of the quality of the entanglement that a candidate path can deliver, with end-to-end fidelity as a central metric. Inspired by the optical-networkin…

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
1. [No Eyes, No Problem: What Does Touch Contribute to Blind Baoding Ball Manipulation?](https://arxiv.org/abs/2610.23438v1) — score 22
2. [HiFun: a Hierarchical Framework for Efficient Functional Dexterous Manipulation Learning](https://arxiv.org/abs/2610.19518v1) — score 19
3. [CoEvolve: Self-Evolving Code Policies from Skills to Strategies for Humanoid Robots](https://arxiv.org/abs/2610.23288v1) — score 17

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
