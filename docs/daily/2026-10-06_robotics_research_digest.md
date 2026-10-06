# 机器人研究每日摘要 · 2026-10-06

> 自动生成,共 91 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (5 篇)

### 1. Beyond LLM Serving: Characterizing Vision-Language-Action Workloads for Embodied AI System Design

- **arXiv**: [2610.05062v1](https://arxiv.org/abs/2610.05062v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05062v1)
- **作者**: Seonghun Jung, Sieun Moon, Jiyoung Jeong et al.
- **发表**: 2026-10-04  ·  **类别**: cs.AR, cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models translate multimodal observations into low-level robot actions. During robot operation, each control period sets an inference deadline, and overruns leave the robot acting on stale observations, reducing task success. Meeting this deadline motivates on-device or nearby edge execution, where a single robot requires batch-1…

### 2. When Does Retrieval Help? A Study of In-Context Adaptation in Vision-Language-Action Models

- **arXiv**: [2610.05492v1](https://arxiv.org/abs/2610.05492v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05492v1)
- **作者**: Zixuan Liu, Joris Köster, Zizhan Zheng et al.
- **发表**: 2026-10-04  ·  **类别**: cs.LG
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Vision-language-action (VLA) models have shown strong potential as generalist robot policies, but adapting them to unseen tasks often requires costly parameter updates. Recent work such as RICL introduces in-context adaptability by retrieving expert demonstrations based on the current VLA observation and providing them as additional context at test time. Th…

### 3. A Safe Action Is Not Enough: Feasible-Future Decoding for Vision-Language-Action Policies

- **arXiv**: [2610.05166v1](https://arxiv.org/abs/2610.05166v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05166v1)
- **作者**: Tu Nguyen, Matthieu Zimmer, Vu Anh Vu et al.
- **发表**: 2026-10-04  ·  **类别**: cs.AI, cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: A safe action is not necessarily a viable one. Under a frozen vision-language-action (VLA) policy, an action can be likely and locally admissible yet leave no policy-supported route to safe task completion. We call this the feasibility-likelihood gap: likelihood ranks the current action, whereas feasibility depends on the futures that remain after it. We de…

### 4. When and What to Prune? Stage-Aware Visual Token Pruning for Efficient VLA

- **arXiv**: [2610.05273v1](https://arxiv.org/abs/2610.05273v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05273v1)
- **作者**: Tianjun Shi, Haotian Xiong, Ziyu Gong et al.
- **发表**: 2026-10-04  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Visual token pruning is an effective way to accelerate vision-language models and is especially useful for vision-language-action (VLA) inference, where many visual tokens must be processed before predicting robot actions. Existing pruning methods usually estimate which tokens can be pruned based on attention scores or feature diversity, retaining tokens th…

### 5. What the Guard Misses, the Robot Executes: Implied Harm in VLA Instructions

- **arXiv**: [2610.05818v1](https://arxiv.org/abs/2610.05818v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05818v1)
- **作者**: Sripad Karne, Arjun Balaji
- **发表**: 2026-10-05  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-language-action models (VLAs) act on instructions without being able to refuse, so screening harmful requests falls to monitors. We test whether these monitors catch ordinary robot tasks requested for harmful reasons, holding the task fixed while varying only how explicitly the intent is stated. $π_{0.5}$ completes the task at every level of explicit…

## 🌐 具身智能 / 机器人基础模型 (9 篇)

### 1. Joint Movement and Compression Ratio Design for Mobile Embodied AI Networks (MEAN)

- **arXiv**: [2610.02334v1](https://arxiv.org/abs/2610.02334v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.02334v1)
- **作者**: Yahao Ding, Jiaxiang Wang, Zhouxiang Zhao et al.
- **发表**: 2026-10-01  ·  **类别**: cs.IT, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Mobile embodied AI networks (MEAN) enable embodied agents to perceive, reason, communicate, and act in wireless environments. In such networks, agent mobility can improve channel conditions, while semantic compression can reduce transmission payloads. However, movement consumes energy, and stronger compression incurs additional computational cost. This pape…

### 2. ArticuTable: Generating Instance-Level Interactive Rigid-Articulated 3D Tabletop Scenes from a Single Image

- **arXiv**: [2610.05249v1](https://arxiv.org/abs/2610.05249v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05249v1)
- **作者**: Kai Lv, Yibo Yin, Lijun Guo et al.
- **发表**: 2026-10-04  ·  **类别**: cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Embodied agents benefit from 3D environments that combine visual fidelity to real-world observations with physical interactivity. Existing single-image tabletop reconstruction methods recover plausible scene geometry but typically represent objects as monolithic rigid bodies, limiting interaction to whole-object rigid motion and precluding executable part-l…

### 3. PreAct-Nav: Agentic Reasoning Before Action for Urban Navigation

- **arXiv**: [2610.04916v1](https://arxiv.org/abs/2610.04916v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.04916v1)
- **作者**: Jing Xie, Shouwei Ruan, Yubin Wang et al.
- **发表**: 2026-10-04  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Urban navigation requires embodied agents to pursue long-horizon goals through local decisions based on egocentric observations. However, existing agentic navigation methods often struggle to translate distant goals into coherent local decisions in large-scale physical environments. Their reliance on linguistic reasoning over transient observations or limit…

### 4. OmniAct3D: Leveraging Foundation Geometry and Evidence-Grounded Reasoning for Panoramic 3D Detection

- **arXiv**: [2610.03015v1](https://arxiv.org/abs/2610.03015v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.03015v1)
- **作者**: Runtong Wu, Fei Teng, Di Wen et al.
- **发表**: 2026-10-02  ·  **类别**: cs.CV, cs.AI, cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Accurate 3D detection is essential for mobile embodied agents, while Vision Foundation Models (VFMs) offer transferable visual and geometric priors. Yet existing VFM-based 3D detectors rely on narrow-view monocular images or discrete perspective views, limiting coherent surround perception; equirectangular projection (ERP) instead encodes a continuous 360 s…

### 5. On Representational Alignment among Embodied Agents

- **arXiv**: [2610.02985v1](https://arxiv.org/abs/2610.02985v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.02985v1)
- **作者**: Fulvio Mastrogiovanni
- **发表**: 2026-10-02  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Embodied agents interacting with the same physical process may maintain heterogeneous, asynchronous, and observer-relative representations. Rather than assuming that such representations should always be globally aligned, we investigate which distinctions among them must actually be resolved for coherent interaction. We formalize this question through relat…

### 6. Kinematic MeanFlow: One-Step Action Generation Policy for Robotic Foundation Models

- **arXiv**: [2610.00864v1](https://arxiv.org/abs/2610.00864v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.00864v1)
- **作者**: Jiawei Fan, Sifeng Wang, Yuqing Hou et al.
- **发表**: 2026-10-01  ·  **类别**: cs.RO, cs.AI, cs.CL
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: In this paper, we study how to achieve one-step action generation in Robotic Foundation Models (RFMs), aiming to overcome the high inference latency of multi-step flow matching. MeanFlow provides a promising framework for this goal, yet its direct application leads to performance collapse. We discover that this stems from two distinctive dynamics exhibited…

### 7. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 8. EMBER-Bench: Benchmarking Cross-Event Causal Memory in Long-Horizon Embodied Tasks

- **arXiv**: [2610.05013v1](https://arxiv.org/abs/2610.05013v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05013v1)
- **作者**: Aoyang Cai, Boning Zhao, Shaoxuan Xie et al.
- **发表**: 2026-10-04  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Lifelong physical agents must reason over extended interactions where past events continue to shape the world long after they disappear from view. Beyond recalling what happened, agents must infer how history changes the current state and constrains future actions. Yet existing embodied and video-memory benchmarks largely focus on historical retrieval and s…

### 9. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

## 🦵 人形 / 足式机器人 (26 篇)

### 1. Towards a General Humanoid Loco-Manipulation Model via Egocentric Whole-Body Human Data Pretraining

- **arXiv**: [2610.00438v1](https://arxiv.org/abs/2610.00438v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.00438v1)
- **作者**: Chongyang Xu, Zhao Wu, Jin Chen et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Humanoid whole-body manipulation has advanced rapidly, enabling policies to coordinate locomotion, posture, bimanual interaction, and dexterous hand movements. Meanwhile, egocentric human videos provide diverse examples of everyday interactions across objects and scenes, offering scalable supervision without robot operation. However, existing supervision fr…

### 2. OccluDex: Hierarchical 3D Visuo-Tactile Representation Learning for Egocentric Dexterous Manipulation under Self-Occlusion

- **arXiv**: [2609.39017v1](https://arxiv.org/abs/2609.39017v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39017v1)
- **作者**: Ziheng Xu, Yueyuan Chen, Xinyuan He et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Reliable dexterous manipulation requires continuous estimation of object geometry and hand-object contact throughout interaction. With egocentric sensing, however, the manipulating hand frequently occludes task-relevant object surfaces and contact regions, reducing the visual evidence available for state estimation and thereby making robust closed-loop cont…

### 3. NEXUS: Perceptive Whole-Body Control for Terrain-Adaptive Teleoperation

- **arXiv**: [2609.39000v1](https://arxiv.org/abs/2609.39000v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39000v1)
- **作者**: Xiangyu Miao, Junsong Wu, Jiyuan Shi et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Whole-body teleoperation requires a humanoid robot to reproduce a human operator's behavior even when their terrains differ. This demands that the robot perceive local terrain and adapt its posture and contacts accordingly, rather than copy the operator's motion frame by frame. However, paired motion data linking the same behaviors across flat ground and di…

### 4. DASH: A da Vinci Adapter for Serial-link and Humanoid Robots as an Accessible Platform for Surgical Robotics Research

- **arXiv**: [2610.05792v1](https://arxiv.org/abs/2610.05792v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05792v1)
- **作者**: Sara Wickenhiser, Junrong Zhou, Zekai Liang et al.
- **发表**: 2026-10-05  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Robotic minimally invasive surgery offers well-documented clinical benefits, but the cost and infrastructure requirements of purpose-built platforms limit access in rural and lower-resourced facilities. Recent work has teleoperated general-purpose robots for laparoscopic tasks and in vivo procedures, but relied on handheld instruments coupled through passiv…

### 5. Breaking speed scaling in quadrupedal robots via Huygens' coupled-pendulum dynamics

- **arXiv**: [2609.13290v1](https://arxiv.org/abs/2609.13290v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.13290v1)
- **作者**: Yucheng Tao, Yongbin Jin, Shaowen Cheng et al.
- **发表**: 2026-09-09  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Achieving biological-level running speeds has largely been pursued through advances in control algorithms, which improve the utilization of existing hardware. However, the ultimate speed limits remain governed by the underlying force and torque requirements of rapid locomotion, which are typically addressed through increased actuator capacity. Inspired by H…

### 6. Real-Time Conformal-Seeded Hybrid Inverse Kinematics for Offset Redundant Manipulators

- **arXiv**: [2610.04266v1](https://arxiv.org/abs/2610.04266v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.04266v1)
- **作者**: Duc Cuong Vu, Van Tung Nguyen, Duc Hai Nguyen et al.
- **发表**: 2026-10-03  ·  **类别**: cs.RO, eess.SY
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: This paper presents a conformal-seeded hybrid strategy for solving inverse kinematics of offset, redundant 7-DoF robot arms of the humanoid class. Analytical inverse kinematics (AIK) provides closed-form solutions with very low computational cost. However, for offset kinematic structures, the exact closed-form solution is generally unavailable, and practica…

### 7. Exploiting Hierarchical Controller Structure in Contextual Parameter Learning for Humanoid Loco-Manipulation

- **arXiv**: [2610.04609v1](https://arxiv.org/abs/2610.04609v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.04609v1)
- **作者**: Sebastian Hirt, Lukas Theiner, Jan Peters et al.
- **发表**: 2026-10-03  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Hierarchical control architectures are widely used to decompose complex control problems into interacting control levels and are particularly important in robotics, where planning, whole-body motion, and lower-level control must be coordinated across different levels of abstraction and time scales. Their overall closed-loop performance, however, depends str…

### 8. MASkillBlender: Decentralized Whole-Body Coordination for Multi-Humanoid Loco-Manipulation via Skill Blending

- **arXiv**: [2610.01102v1](https://arxiv.org/abs/2610.01102v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.01102v1)
- **作者**: Yifan Hu, Luhang Hong, Mingkang Long et al.
- **发表**: 2026-10-01  ·  **类别**: cs.RO, cs.LG, cs.MA
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Coordinated multi-humanoid loco-manipulation is promising yet challenging due to high-dimensional whole-body control, decentralized decision making, and scalability. While recent reinforcement learning methods have improved single-humanoid whole-body control, extending them to the multi-humanoid setting remains nontrivial and often requires substantial rewa…

### 9. Toward Humanoid Robots in Construction: A Teleoperation Feasibility Study

- **arXiv**: [2610.00718v1](https://arxiv.org/abs/2610.00718v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.00718v1)
- **作者**: Parastoo Ali Pour, David R. Martin, Chang Min Hur et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO, cs.HC
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: We present a teleoperation system that enables a single operator to perform construction tasks on a Unitree G1 humanoid, combining extended reality (XR) based upper body control with pedal-based locomotion to enable simultaneous manipulation and locomotion. Motivated by persistent labor shortages, hazardous working conditions, and challenges in humanoid aut…

### 10. KungfuAthleteBot: learning high-dynamic humanoid motion from video with unified robust recovery

- **arXiv**: [2610.03388v1](https://arxiv.org/abs/2610.03388v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.03388v1)
- **作者**: Zhongxiang Lei, Lulu Cao, Xuyang Wang et al.
- **发表**: 2026-10-02  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Video is an abundant, inexpensive source of human motion data that is rich in extreme athletic behaviors. Making it usable for humanoid robots, however, is not a matter of simply retargeting a reconstructed trajectory: video-derived motion is physically inconsistent, devoid of actuation information, and says nothing about failure or recovery. We present Kun…

## 🦾 操控 / 灵巧手 / 抓取 (29 篇)

### 1. RoboBridge: A Self-Evolving Embodied Agent Framework for Sim-to-Real Transfer

- **arXiv**: [2610.02717v1](https://arxiv.org/abs/2610.02717v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.02717v1)
- **作者**: Chenxi Li, Zhangrui Zhao, Rui Li et al.
- **发表**: 2026-10-02  ·  **类别**: cs.RO
- **相关性评分**: 22  ·  **🔥 read_now**
- **摘要**: A key challenge in bringing embodied intelligence into the real world is transferring capabilities from simulation to reality and enabling agents to continually adapt after deployment. End-to-end vision-language-action policies provide strong manipulation capabilities, but their transfer to physical environments typically relies on calibrating simulated vis…

### 2. GOTT: Object-centric Dexterous Manipulation with a Reusable Cross-Embodiment Primitive

- **arXiv**: [2610.03861v1](https://arxiv.org/abs/2610.03861v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.03861v1)
- **作者**: Yulin Liu, Lai Wei, Yen-Jen Wang et al.
- **发表**: 2026-10-02  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 20  ·  **🔥 read_now**
- **摘要**: Foundation models and large-scale human data provide rich sources of manipulation intent, but translating this intent into multi-fingered robot behavior remains difficult. Dexterous hands still lack a reusable low-level primitive that reliably establishes contact across tasks and embodiments. We propose GOTT, a reach-acquire-move framework built around a si…

### 3. DITTO-X: Forward and Reverse Teleoperation for Dexterous Manipulation and Human Intervention

- **arXiv**: [2610.00781v1](https://arxiv.org/abs/2610.00781v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.00781v1)
- **作者**: Zhanpeng He, Joaquin Palacios, Zhangyu Wang et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Teleoperated demonstrations are a primary source of data for robot manipulation, and teleoperated interventions are a primary mechanism for correcting policies at deployment. Yet most teleoperation systems close the loop through vision alone and are built around parallel-jaw grippers, limiting both what the robot can execute and what the operator can expres…

### 4. Now You Feel It, Now You See Me: Digital-Twin-based Teleoperation Interface for Dexterous Manipulation

- **arXiv**: [2610.05081v1](https://arxiv.org/abs/2610.05081v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05081v1)
- **作者**: Youngchan Shim, Kyutae Lee, JooYun Kim et al.
- **发表**: 2026-10-04  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Teleoperation is becoming increasingly important for collecting high-quality demonstrations to teach robots dexterous manipulation skills. For dexterous manipulation, bare-hand tracking provides a practical way to control robotic hands and demonstrate coordinated finger movements without gloves or exoskeletons. However, this type of teleoperation faces two…

### 5. AgenticTactileVLA: Contact-Guided Execution-Time Supervision for Generalizable Dexterous Manipulation without VLA Retraining

- **arXiv**: [2610.04391v1](https://arxiv.org/abs/2610.04391v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.04391v1)
- **作者**: Elizaveta Semenyakina, Ivan Snegirev, Mikhail Kiselev et al.
- **发表**: 2026-10-03  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Vision-language-action policies may predict a transferable manipulation strategy yet fail to realize it reliably on the encountered object: objects compatible with the same grasp differ in geometry and compliance, and visual feedback degrades under closure occlusion. AgenticTactileVLA is presented as an execution-time supervisor that shifts part of object-s…

### 6. PatternDex: Learning Interaction Patterns to Guide Reinforcement Learning of Bimanual Dexterous Manipulation of Articulated Objects

- **arXiv**: [2610.04765v1](https://arxiv.org/abs/2610.04765v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.04765v1)
- **作者**: David Minkwan Kim, Runfa Blark Li, Beckham Po-Ju Lee et al.
- **发表**: 2026-10-03  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: In this paper, we develop a method that enables bimanual dexterous hands to manipulate articulated objects with a high success rate without suffering from an embodiment gap. We observe that the correlation between hand motions and object motions is dictated by the object rather than the hands and can be learned from human-object demonstrations. Based on thi…

### 7. DexJoCo-X: Benchmarking Action Representations for Multi-Hand Dexterous Manipulation

- **arXiv**: [2610.03278v1](https://arxiv.org/abs/2610.03278v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.03278v1)
- **作者**: Xiangwei Jiang, Yao Mu, Lixin Duan et al.
- **发表**: 2026-10-02  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: As dexterous hands proliferate, collecting data and training policies separately for every morphology becomes increasingly impractical. Scalable cross-embodiment learning therefore requires a unified representation that captures shared manipulation structure while preserving morphology-specific control. Differences in hands, tasks, datasets, and control int…

### 8. NarrativeFlow: Flow-Based Vision-Language-Action Model Using Robot Velocity Fields

- **arXiv**: [2610.00981v1](https://arxiv.org/abs/2610.00981v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.00981v1)
- **作者**: Shota Kobayashi, Koki Seno, Daichi Yashima et al.
- **发表**: 2026-10-01  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: We focus on language-conditioned flow-based manipulation, where robot flows (robot velocity fields) serve as embodiment-agnostic, motion-centric representations for leveraging data collected from multiple robot platforms. This task is crucial because language-conditioned manipulation is essential for practical robotic systems, yet scaling robot foundation m…

### 9. Kinematic Nonlinear Spatio-Temporal Trajectory Warping for Contact-Rich Dexterous Manipulation Demonstrations

- **arXiv**: [2609.36676v1](https://arxiv.org/abs/2609.36676v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.36676v1)
- **作者**: Hyojae Park, Arjun S. Lakshmipathy, Nancy S. Pollard
- **发表**: 2026-09-29  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: We present a straightforward but effective method for repurposing existing contact-rich dexterous manipulation demonstrations. Starting from inputs of hand and object trajectories, our method outputs high-quality nonlinear trajectory warps that account for intermediate waypoints, environmental barriers, temporal shifts, and varied start/end configurations.…

### 10. VICON: Visual-Inertial-Contact based Hand-Object Tracking for Manipulation Datasets

- **arXiv**: [2610.05180v1](https://arxiv.org/abs/2610.05180v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05180v1)
- **作者**: Yubin Jeon, Uiseong Shin, Hwanchul La et al.
- **发表**: 2026-10-04  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Learning dexterous manipulation benefits from human demonstration datasets that capture diverse and natural hand-object interactions. In particular, contact points and forces provide supervision on where and how strongly to interact, which cannot be fully captured by motion trajectories alone. However, methods for jointly capturing hand and object motion, c…

## 🎓 模仿学习 / 强化学习 (14 篇)

### 1. Robust Surgical Robotic Instrument Tracking via Sequential Multi-Cue Fusion and Sim-to-Real Self-Training

- **arXiv**: [2610.05491v1](https://arxiv.org/abs/2610.05491v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05491v1)
- **作者**: Hanyang Hu, Zekai Liang, Florian Richter et al.
- **发表**: 2026-10-04  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Efficient and robust tracking of surgical robotic instruments is important for robot-assisted minimally invasive surgery, yet remains challenging due to the complexity of surgical scenes and the unconventional geometry of surgical instruments. Keypoint-based approaches are efficient, but their performance depends on reliable feature detection. Improving the…

### 2. HuMemSLAM: Efficient Human-Inspired Semantic Place Recognition for Robust Visual SLAM

- **arXiv**: [2609.17168v1](https://arxiv.org/abs/2609.17168v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.17168v1)
- **作者**: Mayowa Adebambo, Sebastian Donnelly, Armand Amaritei et al.
- **发表**: 2026-09-15  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Autonomous systems require reliable place recognition for efficient and effective simultaneous localisation and mapping (SLAM). Traditional geometric visual SLAM approaches rely on low-level features and geometric consistency, but remain vulnerable to perceptual aliasing, where different places appear similar, and perceptual variation, where the same place…

### 3. Generative adversarial imitation learning for robot swarms: Learning from human demonstrations and trained policies

- **arXiv**: [2603.02783v1](https://arxiv.org/abs/2603.02783v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.02783v1)
- **作者**: Mattes Kraus, Jonas Kuckling
- **发表**: 2026-03-03  ·  **类别**: cs.RO, cs.LG, cs.MA
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, robots are supposed to learn from demonstrations of the desired behavior. Most of the work in imitation learning for swarm robotics provides the demonstrations as rollouts of an existing policy. In this work, we provide a framework based on generative adversarial imitation learning that aims to learn collective behaviors from human de…

### 4. End-to-End Deep Imitation Learning: Robot Soccer Case Study

- **arXiv**: [1807.09205v1](https://arxiv.org/abs/1807.09205v1)  ·  **PDF**: [link](https://arxiv.org/pdf/1807.09205v1)
- **作者**: Okan Aşık, Binnur Görer, H. Levent Akın
- **发表**: 2018-06-28  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, behavior learning is generally done using the features extracted from the demonstration data. Recent deep learning algorithms enable the development of machine learning methods that can get high dimensional data as an input. In this work, we use imitation learning to teach the robot to dribble the ball to the goal. We use B-Human robo…

### 5. TUCO: Curating Simulation Demonstrations for Sim-to-Real Robot Policy Co-Training

- **arXiv**: [2610.05407v1](https://arxiv.org/abs/2610.05407v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05407v1)
- **作者**: Ning Zhu, Mengfei Zhao, Yikai Tang et al.
- **发表**: 2026-10-04  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Simulation demonstrations can supplement scarce real-world data for robot policy co-training. However, the value of using data curation to actively select these demonstrations for sim-to-real co-training remains underexplored. Existing curation methods also lack a unified criterion for measuring trajectory-level utility and set-level coverage from closed-lo…

### 6. VideoResearchAgent: Grounded Task Synthesis and Sim-to-Real RL for Open-Web Video Research

- **arXiv**: [2610.04911v1](https://arxiv.org/abs/2610.04911v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.04911v1)
- **作者**: Yuhang Zhou, Fei Li, Yuxi Wu et al.
- **发表**: 2026-10-04  ·  **类别**: cs.AI, cs.CV
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Existing deep research agents are designed primarily for text- and image-based web sources, while video reasoning systems typically assume that relevant videos are provided in advance. We study open-web video research, where an agent must autonomously discover relevant videos, navigate their temporal content, and ground answers in visual evidence. Training…

### 7. Tackling Sim-to-Real Mismatch Through Sampling-Based Disturbance Observers: From Analytical Models to Learned World Models

- **arXiv**: [2610.04896v1](https://arxiv.org/abs/2610.04896v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.04896v1)
- **作者**: Tianqi Zhu, Jun Yang, Jianliang Mao et al.
- **发表**: 2026-10-04  ·  **类别**: cs.RO, eess.SY
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Robotic controllers increasingly rely on analytical models, simulators, cost-query interfaces, and learned world models. However, physical deployment can deviate from nominal assumptions, and additional disturbances may arise even when the model itself is accurate. In control systems, disturbance observers (DOB) are widely used to estimate such unmeasured e…

### 8. RawSLAM: Online HDR Gaussian SLAM from Linear Radiance

- **arXiv**: [2609.20589v1](https://arxiv.org/abs/2609.20589v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.20589v1)
- **作者**: Marina Orozco González, Luis Merino
- **发表**: 2026-09-17  ·  **类别**: cs.CV
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Current dense visual SLAM systems rely almost exclusively on 8-bit tonemapped Low Dynamic Range (LDR) inputs, limiting their robustness in extreme lighting where shadows and highlights trigger tracking drift and mapping collapse. Conversely, existing raw and High Dynamic Range (HDR) reconstruction pipelines operate strictly offline. They depend on Structure…

### 9. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 10. Unblur-SLAM: Dense Neural SLAM for Blurry Inputs

- **arXiv**: [2603.26810v1](https://arxiv.org/abs/2603.26810v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.26810v1)
- **作者**: Qi Zhang, Denis Rozumny, Francesco Girlanda et al.
- **发表**: 2026-03-26  ·  **类别**: cs.CV, eess.IV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We propose Unblur-SLAM, a novel RGB SLAM pipeline for sharp 3D reconstruction from blurred image inputs. In contrast to previous work, our approach is able to handle different types of blur and demonstrates state-of-the-art performance in the presence of both motion blur and defocus blur. Moreover, we adjust the computation effort with the amount of blur in…

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
- **相关性评分**: 5  ·  **📌 info**
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

## 🧭 导航 / 路径规划 (1 篇)

### 1. Autonomous Robotic Navigation for Endovascular Brain-Computer Interface Access

- **arXiv**: [2610.03537v1](https://arxiv.org/abs/2610.03537v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.03537v1)
- **作者**: Harry Robertshaw, Weijie Qi, Nikola Fischer et al.
- **发表**: 2026-10-02  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Endovascular brain-computer interfaces (BCIs) avoid craniotomy but require precise device delivery through anatomically variable cerebral veins. This work presents the first demonstration of in vitro autonomous robotic navigation for endovascular BCI access in the cerebral venous system. Soft Actor-Critic controllers were trained in silico for two sequentia…

## 📦 其他机器人相关 (1 篇)

### 1. ReShoot: Generative Visual Domain Randomization of Recorded Robot Demonstrations for Visuomotor Policy Learning

- **arXiv**: [2609.19661v1](https://arxiv.org/abs/2609.19661v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.19661v1)
- **作者**: Chiyoung Kim, Min Sung Choi, Jinho Ju et al.
- **发表**: 2026-09-17  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Imitation-learned robot policies are frequently overfit to the visual conditions present in their training demonstrations. Consequently, variations in object color or background appearance often induce substantial performance degradation. A common mitigation strategy is to acquire additional demonstrations in each novel visual context; however, this approac…

---

## 📋 本日操作建议

**建议今日深读 (Top 3):**
1. [RoboBridge: A Self-Evolving Embodied Agent Framework for Sim-to-Real Transfer](https://arxiv.org/abs/2610.02717v1) — score 22
2. [GOTT: Object-centric Dexterous Manipulation with a Reusable Cross-Embodiment Primitive](https://arxiv.org/abs/2610.03861v1) — score 20
3. [DITTO-X: Forward and Reverse Teleoperation for Dexterous Manipulation and Human Intervention](https://arxiv.org/abs/2610.00781v1) — score 19

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
