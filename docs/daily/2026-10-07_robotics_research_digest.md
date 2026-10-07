# 机器人研究每日摘要 · 2026-10-07

> 自动生成,共 87 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (3 篇)

### 1. Adapting Vision-Language-Action Models to Unknown Visual Disruptions During Execution

- **arXiv**: [2610.07946v1](https://arxiv.org/abs/2610.07946v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.07946v1)
- **作者**: Ahin Lee, Jinwoo Seo, Youngsoo Jang et al.
- **发表**: 2026-10-06  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Visual disruptions can arise while a robot is executing a task, leaving a vision-language-action (VLA) policy to respond without knowing the disruption type or timing. We introduce Self-supervised Adaptation from Leftover Trajectories (SALT), which uses the leftover trajectory, the unexecuted part of the previous action chunk, as self-supervision for test-t…

### 2. StairVLA: Stage-Aware Hierarchical Action Generation for Vision-Language-Action Models

- **arXiv**: [2610.07756v1](https://arxiv.org/abs/2610.07756v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.07756v1)
- **作者**: Shangyuan Yuan, Xinda Qi, Yujiang Pu et al.
- **发表**: 2026-10-06  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Vision-language-action (VLA) models increasingly rely on diffusion- or flow-matching-based action heads to generate continuous robot actions. These action heads typically process the denoising trajectory in a largely uniform manner. However, we observe that the conditioning focus naturally shifts across denoising stages: early stages combine language instru…

### 3. Seeing the Invisible: Physics-Guided Visual Prompting for Temperature- and Radiation-Aware VLA Navigation

- **arXiv**: [2610.07558v1](https://arxiv.org/abs/2610.07558v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.07558v1)
- **作者**: Hojoon Son, Fan Zhang
- **发表**: 2026-10-06  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Vision-Language-Action (VLA) models have become a major paradigm for Vision-and-Language Navigation (VLN). However, in safety-critical facilities, invisible risks such as radiation or temperature spikes cannot be detected by an RGB camera, and handling each risk is expensive, requiring a new encoder, new data, and model retraining. We propose Physics-Guided…

## 🌐 具身智能 / 机器人基础模型 (10 篇)

### 1. Attacca: Goal-Directed Control under State Continuity for Long-Horizon Embodied Agents

- **arXiv**: [2610.07785v1](https://arxiv.org/abs/2610.07785v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.07785v1)
- **作者**: Gyusik Seo, Jaehong Yoon
- **发表**: 2026-10-06  ·  **类别**: cs.AI
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: A central capability of embodied agents is to accomplish complex objectives through sequences of interdependent tasks. Yet existing visual goal-conditioned policies underlying these agents are typically evaluated on isolated interactions where the target is already visible, and thus do not capture the conditions that arise during continuous long-horizon tas…

### 2. Inspect Robots: Evaluating the Capabilities and Safety of Embodied AI

- **arXiv**: [2610.06306v1](https://arxiv.org/abs/2610.06306v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.06306v1)
- **作者**: Christopher Leet, Achu Menon, Sravanthi Machcha et al.
- **发表**: 2026-10-05  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: General purpose language models are increasingly able to control robotic hardware. Understanding the capabilities and safety of these models when embodied is therefore increasingly important for understanding their societal impact and risks. To this end, we introduce Inspect Robots, a modular, open-source framework for developing and running evaluations of…

### 3. ArticuTable: Generating Instance-Level Interactive Rigid-Articulated 3D Tabletop Scenes from a Single Image

- **arXiv**: [2610.05249v1](https://arxiv.org/abs/2610.05249v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05249v1)
- **作者**: Kai Lv, Yibo Yin, Lijun Guo et al.
- **发表**: 2026-10-04  ·  **类别**: cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Embodied agents benefit from 3D environments that combine visual fidelity to real-world observations with physical interactivity. Existing single-image tabletop reconstruction methods recover plausible scene geometry but typically represent objects as monolithic rigid bodies, limiting interaction to whole-object rigid motion and precluding executable part-l…

### 4. PreAct-Nav: Agentic Reasoning Before Action for Urban Navigation

- **arXiv**: [2610.04916v1](https://arxiv.org/abs/2610.04916v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.04916v1)
- **作者**: Jing Xie, Shouwei Ruan, Yubin Wang et al.
- **发表**: 2026-10-04  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Urban navigation requires embodied agents to pursue long-horizon goals through local decisions based on egocentric observations. However, existing agentic navigation methods often struggle to translate distant goals into coherent local decisions in large-scale physical environments. Their reliance on linguistic reasoning over transient observations or limit…

### 5. OmniAct3D: Leveraging Foundation Geometry and Evidence-Grounded Reasoning for Panoramic 3D Detection

- **arXiv**: [2610.03015v1](https://arxiv.org/abs/2610.03015v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.03015v1)
- **作者**: Runtong Wu, Fei Teng, Di Wen et al.
- **发表**: 2026-10-02  ·  **类别**: cs.CV, cs.AI, cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Accurate 3D detection is essential for mobile embodied agents, while Vision Foundation Models (VFMs) offer transferable visual and geometric priors. Yet existing VFM-based 3D detectors rely on narrow-view monocular images or discrete perspective views, limiting coherent surround perception; equirectangular projection (ERP) instead encodes a continuous 360 s…

### 6. Benchmarking Jailbreak Guardrails for Embodied Agents

- **arXiv**: [2610.06122v1](https://arxiv.org/abs/2610.06122v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.06122v1)
- **作者**: Xunguang Wang, Qingyue Wang, Yuguang Zhou et al.
- **发表**: 2026-10-05  ·  **类别**: cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Embodied agents powered by large language models and vision-language models are increasingly deployed in physical environments, but jailbreak attacks can induce these agents to perform physically harmful actions. A growing number of guardrail methods have been proposed to intercept dangerous behavior before it is executed, yet existing safety benchmarks eva…

### 7. Kinematic MeanFlow: One-Step Action Generation Policy for Robotic Foundation Models

- **arXiv**: [2610.00864v1](https://arxiv.org/abs/2610.00864v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.00864v1)
- **作者**: Jiawei Fan, Sifeng Wang, Yuqing Hou et al.
- **发表**: 2026-10-01  ·  **类别**: cs.RO, cs.AI, cs.CL
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: In this paper, we study how to achieve one-step action generation in Robotic Foundation Models (RFMs), aiming to overcome the high inference latency of multi-step flow matching. MeanFlow provides a promising framework for this goal, yet its direct application leads to performance collapse. We discover that this stems from two distinctive dynamics exhibited…

### 8. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 9. EMBER-Bench: Benchmarking Cross-Event Causal Memory in Long-Horizon Embodied Tasks

- **arXiv**: [2610.05013v1](https://arxiv.org/abs/2610.05013v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05013v1)
- **作者**: Aoyang Cai, Boning Zhao, Shaoxuan Xie et al.
- **发表**: 2026-10-04  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Lifelong physical agents must reason over extended interactions where past events continue to shape the world long after they disappear from view. Beyond recalling what happened, agents must infer how history changes the current state and constrains future actions. Yet existing embodied and video-memory benchmarks largely focus on historical retrieval and s…

### 10. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

## 🦵 人形 / 足式机器人 (26 篇)

### 1. BiGym 2.0: Benchmarking Learned and Agent-Developed Policies for Humanoid Household Manipulation

- **arXiv**: [2610.07594v1](https://arxiv.org/abs/2610.07594v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.07594v1)
- **作者**: Zexi Zhang, Zecheng Zhu, Zidong Chen et al.
- **发表**: 2026-10-06  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Humanoid household manipulation requires the arms to act while the body balances, steps and changes posture. We present BiGym 2.0, an adaptation of BiGym for the Unitree G1 across 20 household tasks using a unified whole-body controller for demonstration and evaluation. The suite provides 60 native human virtual-reality demonstrations per task with synchron…

### 2. MobileVISTA: Generative Data Augmentation for Pose Generalization in Mobile Manipulation

- **arXiv**: [2610.07511v1](https://arxiv.org/abs/2610.07511v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.07511v1)
- **作者**: Suzannah Wistreich, Stephen Tian, Isabella Huang et al.
- **发表**: 2026-10-05  ·  **类别**: cs.RO, cs.CV, cs.LG
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Mobile manipulators such as humanoid robots are increasingly deployed in dynamic, unstructured environments to perform dexterous manipulation tasks. However, end-to-end manipulation policies trained to imitate demonstration data collected from a single robot pose are brittle: even centimeter-scale deviations in robot pose at deployment can drive ego-centric…

### 3. InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation

- **arXiv**: [2610.06850v1](https://arxiv.org/abs/2610.06850v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.06850v1)
- **作者**: Yucheng Zhang, Sirui Xu, Jinhong Li et al.
- **发表**: 2026-10-05  ·  **类别**: cs.RO, cs.CV, cs.GR
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Captured human-object interactions provide rich supervision for humanoid loco-manipulation, but they are sparse, heterogeneous, and not directly executable by robots. We introduce InterMimicGen, a self-evolving motion-imitation framework in which robot motion data and a tracking policy improve each other. First, we consolidate motion-captured human-object i…

### 4. OccluDex: Hierarchical 3D Visuo-Tactile Representation Learning for Egocentric Dexterous Manipulation under Self-Occlusion

- **arXiv**: [2609.39017v1](https://arxiv.org/abs/2609.39017v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39017v1)
- **作者**: Ziheng Xu, Yueyuan Chen, Xinyuan He et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Reliable dexterous manipulation requires continuous estimation of object geometry and hand-object contact throughout interaction. With egocentric sensing, however, the manipulating hand frequently occludes task-relevant object surfaces and contact regions, reducing the visual evidence available for state estimation and thereby making robust closed-loop cont…

### 5. DASH: A da Vinci Adapter for Serial-link and Humanoid Robots as an Accessible Platform for Surgical Robotics Research

- **arXiv**: [2610.05792v1](https://arxiv.org/abs/2610.05792v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05792v1)
- **作者**: Sara Wickenhiser, Junrong Zhou, Zekai Liang et al.
- **发表**: 2026-10-05  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Robotic minimally invasive surgery offers well-documented clinical benefits, but the cost and infrastructure requirements of purpose-built platforms limit access in rural and lower-resourced facilities. Recent work has teleoperated general-purpose robots for laparoscopic tasks and in vivo procedures, but relied on handheld instruments coupled through passiv…

### 6. Breaking speed scaling in quadrupedal robots via Huygens' coupled-pendulum dynamics

- **arXiv**: [2609.13290v1](https://arxiv.org/abs/2609.13290v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.13290v1)
- **作者**: Yucheng Tao, Yongbin Jin, Shaowen Cheng et al.
- **发表**: 2026-09-09  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Achieving biological-level running speeds has largely been pursued through advances in control algorithms, which improve the utilization of existing hardware. However, the ultimate speed limits remain governed by the underlying force and torque requirements of rapid locomotion, which are typically addressed through increased actuator capacity. Inspired by H…

### 7. iGPC: Generative Motion Priors for Object-Aware Humanoid Interaction

- **arXiv**: [2610.08120v1](https://arxiv.org/abs/2610.08120v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.08120v1)
- **作者**: Anujith Muraleedharan, Abdul Ahad Butt, Nolan Fey et al.
- **发表**: 2026-10-06  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Humanoid robots operating in unstructured environments must combine robust whole-body control with the ability to perceive and physically interact with surrounding objects. While large-scale human motion data provides powerful priors for natural and versatile humanoid control, effectively transferring such priors to perception-driven object interaction rema…

### 8. EmbodiedSmith: Scaling Embodied Data through Recursive Self-Improvement Flywheel in Simulation

- **arXiv**: [2610.07969v1](https://arxiv.org/abs/2610.07969v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.07969v1)
- **作者**: Yikai Qin, Yifei Deng, Mingjian Liang et al.
- **发表**: 2026-10-06  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Scaling robotic foundation models requires diverse training data and reliable evaluation environments. Simulation offers a scalable solution, yet existing generation pipelines remain constrained by predefined assets and skills, a disconnect between scene generation and task generation, and limited support for complex embodiments and physics. We introduce Em…

### 9. Exploiting Hierarchical Controller Structure in Contextual Parameter Learning for Humanoid Loco-Manipulation

- **arXiv**: [2610.04609v1](https://arxiv.org/abs/2610.04609v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.04609v1)
- **作者**: Sebastian Hirt, Lukas Theiner, Jan Peters et al.
- **发表**: 2026-10-03  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Hierarchical control architectures are widely used to decompose complex control problems into interacting control levels and are particularly important in robotics, where planning, whole-body motion, and lower-level control must be coordinated across different levels of abstraction and time scales. Their overall closed-loop performance, however, depends str…

### 10. Physics Residual Dynamics and Reduced Order Whole-Body Planning for Obstacle Aware Human Robot Cloth CoTransportation

- **arXiv**: [2610.06641v1](https://arxiv.org/abs/2610.06641v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.06641v1)
- **作者**: Moein Forouhar, Kosar Behnia, Anirvan Dutta et al.
- **发表**: 2026-10-05  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Human--robot co-transportation of deformable objects requires predicting object deformation during motion, since obstacle clearance depends on both the grasp points and the unactuated interior. We present a hierarchical planning framework that combines a learned cloth model with a reduced-order whole-body model of a dual-arm mobile manipulator. A physics-re…

## 🦾 操控 / 灵巧手 / 抓取 (26 篇)

### 1. SMART: Zero-Shot Sim-to-Real Articulated Object Manipulation via Large-Scale Synthetic Pretraining

- **arXiv**: [2610.07652v1](https://arxiv.org/abs/2610.07652v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.07652v1)
- **作者**: Jicong Ao, Shuhan Jiang, Yuling Zhong et al.
- **发表**: 2026-10-06  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 22  ·  **🔥 read_now**
- **摘要**: The ability to interact with articulated objects is essential for embodied intelligent systems, but collecting large-scale real-world demonstrations for these interactions remains challenging due to the precise contact and constraint-following motions involved. Although simulation provides a promising alternative, existing synthetic data efforts cover limit…

### 2. EigenDEXplore: Structured Exploration for Dexterous Manipulation with Human Priors

- **arXiv**: [2610.07681v1](https://arxiv.org/abs/2610.07681v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.07681v1)
- **作者**: Harsh Gupta, Tyler Ga Wei Lum, Changhao Wang et al.
- **发表**: 2026-10-06  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 21  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation poses a challenging high-dimensional optimization problem, as useful behaviors require coordinated motion across many hand joints. In reinforcement learning (RL) and sampling-based trajectory optimization, exploration commonly relies on independent robot joint perturbations, making coordinated behaviors difficult to discover. Prior wo…

### 3. GOTT: Object-centric Dexterous Manipulation with a Reusable Cross-Embodiment Primitive

- **arXiv**: [2610.03861v1](https://arxiv.org/abs/2610.03861v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.03861v1)
- **作者**: Yulin Liu, Lai Wei, Yen-Jen Wang et al.
- **发表**: 2026-10-02  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Foundation models and large-scale human data provide rich sources of manipulation intent, but translating this intent into multi-fingered robot behavior remains difficult. Dexterous hands still lack a reusable low-level primitive that reliably establishes contact across tasks and embodiments. We propose GOTT, a reach-acquire-move framework built around a si…

### 4. DITTO-X: Forward and Reverse Teleoperation for Dexterous Manipulation and Human Intervention

- **arXiv**: [2610.00781v2](https://arxiv.org/abs/2610.00781v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.00781v2)
- **作者**: Zhanpeng He, Joaquin Palacios, Zhangyu Wang et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Teleoperated demonstrations are a primary source of data for robot manipulation, and teleoperated interventions are a primary mechanism for correcting policies at deployment. Yet most teleoperation systems close the loop through vision alone and are built around parallel-jaw grippers, limiting both what the robot can execute and what the operator can expres…

### 5. Now You Feel It, Now You See Me: Digital-Twin-based Teleoperation Interface for Dexterous Manipulation

- **arXiv**: [2610.05081v1](https://arxiv.org/abs/2610.05081v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05081v1)
- **作者**: Youngchan Shim, Kyutae Lee, JooYun Kim et al.
- **发表**: 2026-10-04  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Teleoperation is becoming increasingly important for collecting high-quality demonstrations to teach robots dexterous manipulation skills. For dexterous manipulation, bare-hand tracking provides a practical way to control robotic hands and demonstrate coordinated finger movements without gloves or exoskeletons. However, this type of teleoperation faces two…

### 6. AgenticTactileVLA: Contact-Guided Execution-Time Supervision for Generalizable Dexterous Manipulation without VLA Retraining

- **arXiv**: [2610.04391v1](https://arxiv.org/abs/2610.04391v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.04391v1)
- **作者**: Elizaveta Semenyakina, Ivan Snegirev, Mikhail Kiselev et al.
- **发表**: 2026-10-03  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Vision-language-action policies may predict a transferable manipulation strategy yet fail to realize it reliably on the encountered object: objects compatible with the same grasp differ in geometry and compliance, and visual feedback degrades under closure occlusion. AgenticTactileVLA is presented as an execution-time supervisor that shifts part of object-s…

### 7. VLA-ACL: Action-Consistent Visual Token Pruning for Efficient Vision-Language-Action Models

- **arXiv**: [2610.08133v1](https://arxiv.org/abs/2610.08133v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.08133v1)
- **作者**: Owen Du, Yang Yue, Jie Zhang et al.
- **发表**: 2026-10-06  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models achieve strong robotic manipulation performance but incur high computational costs from processing long token sequences at every control step, limiting real-time deployment. Visual token pruning offers a direct solution, as visual patches dominate the input sequence and contain considerable redundancy. Existing approaches…

### 8. PatternDex: Learning Interaction Patterns to Guide Reinforcement Learning of Bimanual Dexterous Manipulation of Articulated Objects

- **arXiv**: [2610.04765v1](https://arxiv.org/abs/2610.04765v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.04765v1)
- **作者**: David Minkwan Kim, Runfa Blark Li, Beckham Po-Ju Lee et al.
- **发表**: 2026-10-03  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: In this paper, we develop a method that enables bimanual dexterous hands to manipulate articulated objects with a high success rate without suffering from an embodiment gap. We observe that the correlation between hand motions and object motions is dictated by the object rather than the hands and can be learned from human-object demonstrations. Based on thi…

### 9. NarrativeFlow: Flow-Based Vision-Language-Action Model Using Robot Velocity Fields

- **arXiv**: [2610.00981v1](https://arxiv.org/abs/2610.00981v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.00981v1)
- **作者**: Shota Kobayashi, Koki Seno, Daichi Yashima et al.
- **发表**: 2026-10-01  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: We focus on language-conditioned flow-based manipulation, where robot flows (robot velocity fields) serve as embodiment-agnostic, motion-centric representations for leveraging data collected from multiple robot platforms. This task is crucial because language-conditioned manipulation is essential for practical robotic systems, yet scaling robot foundation m…

### 10. ReDex: Repairing Sim-to-Real Dexterous Policies by Finger-Level Compliant Interaction

- **arXiv**: [2610.07525v1](https://arxiv.org/abs/2610.07525v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.07525v1)
- **作者**: Jinzhou Li, Hadi Tabatabaee, Kelin Yu et al.
- **发表**: 2026-10-05  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation policies trained in simulation often fail to transfer to the real world because of errors in contact timing and force regulation. Yet these policies can retain useful multi-finger coordination for task progression. We propose ReDex, a framework for adapting a simulation-trained base policy to the real world by correcting local contact…

## 🎓 模仿学习 / 强化学习 (15 篇)

### 1. Sim-to-Real Transfer of Vision-Language Navigation in Continuous Environments Using an Ackermann-Steered Mobile Robot

- **arXiv**: [2610.07192v1](https://arxiv.org/abs/2610.07192v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.07192v1)
- **作者**: Chalindu Abeywansa, Sahan Gunasekara, Devindi De Silva et al.
- **发表**: 2026-10-05  ·  **类别**: cs.AI, cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Vision-Language Navigation (VLN) enables robots to navigate through environments using natural language instructions, making human-robot interaction intuitive. Traditional VLN models often rely on navigation graphs, 360-degree views, and perfect localization which pose significant challenges when adapting these models to real-world settings. This work addre…

### 2. Dual Variational Autoencoders for Efficient Sim-to-Real Transfer in Low-Cost Robotic Navigation

- **arXiv**: [2610.06327v1](https://arxiv.org/abs/2610.06327v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.06327v1)
- **作者**: Álvaro Díez, Fidel Aznar
- **发表**: 2026-10-05  ·  **类别**: cs.RO, cs.CV, cs.LG
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Vision-based autonomous navigation for low-cost robots remains a fundamental challenge, primarily due to the significant gap between simulated training environments and real-world operational conditions. Direct policy transfer from simulation is often ineffective, while training exclusively on real data is impractical. We propose a hybrid transfer learning…

### 3. Robust Surgical Robotic Instrument Tracking via Sequential Multi-Cue Fusion and Sim-to-Real Self-Training

- **arXiv**: [2610.05491v1](https://arxiv.org/abs/2610.05491v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05491v1)
- **作者**: Hanyang Hu, Zekai Liang, Florian Richter et al.
- **发表**: 2026-10-04  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Efficient and robust tracking of surgical robotic instruments is important for robot-assisted minimally invasive surgery, yet remains challenging due to the complexity of surgical scenes and the unconventional geometry of surgical instruments. Keypoint-based approaches are efficient, but their performance depends on reliable feature detection. Improving the…

### 4. HuMemSLAM: Efficient Human-Inspired Semantic Place Recognition for Robust Visual SLAM

- **arXiv**: [2609.17168v1](https://arxiv.org/abs/2609.17168v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.17168v1)
- **作者**: Mayowa Adebambo, Sebastian Donnelly, Armand Amaritei et al.
- **发表**: 2026-09-15  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Autonomous systems require reliable place recognition for efficient and effective simultaneous localisation and mapping (SLAM). Traditional geometric visual SLAM approaches rely on low-level features and geometric consistency, but remain vulnerable to perceptual aliasing, where different places appear similar, and perceptual variation, where the same place…

### 5. Generative adversarial imitation learning for robot swarms: Learning from human demonstrations and trained policies

- **arXiv**: [2603.02783v1](https://arxiv.org/abs/2603.02783v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.02783v1)
- **作者**: Mattes Kraus, Jonas Kuckling
- **发表**: 2026-03-03  ·  **类别**: cs.RO, cs.LG, cs.MA
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, robots are supposed to learn from demonstrations of the desired behavior. Most of the work in imitation learning for swarm robotics provides the demonstrations as rollouts of an existing policy. In this work, we provide a framework based on generative adversarial imitation learning that aims to learn collective behaviors from human de…

### 6. End-to-End Deep Imitation Learning: Robot Soccer Case Study

- **arXiv**: [1807.09205v1](https://arxiv.org/abs/1807.09205v1)  ·  **PDF**: [link](https://arxiv.org/pdf/1807.09205v1)
- **作者**: Okan Aşık, Binnur Görer, H. Levent Akın
- **发表**: 2018-06-28  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, behavior learning is generally done using the features extracted from the demonstration data. Recent deep learning algorithms enable the development of machine learning methods that can get high dimensional data as an input. In this work, we use imitation learning to teach the robot to dribble the ball to the goal. We use B-Human robo…

### 7. TUCO: Curating Simulation Demonstrations for Sim-to-Real Robot Policy Co-Training

- **arXiv**: [2610.05407v1](https://arxiv.org/abs/2610.05407v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05407v1)
- **作者**: Ning Zhu, Mengfei Zhao, Yikai Tang et al.
- **发表**: 2026-10-04  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Simulation demonstrations can supplement scarce real-world data for robot policy co-training. However, the value of using data curation to actively select these demonstrations for sim-to-real co-training remains underexplored. Existing curation methods also lack a unified criterion for measuring trajectory-level utility and set-level coverage from closed-lo…

### 8. VideoResearchAgent: Grounded Task Synthesis and Sim-to-Real RL for Open-Web Video Research

- **arXiv**: [2610.04911v1](https://arxiv.org/abs/2610.04911v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.04911v1)
- **作者**: Yuhang Zhou, Fei Li, Yuxi Wu et al.
- **发表**: 2026-10-04  ·  **类别**: cs.AI, cs.CV
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Existing deep research agents are designed primarily for text- and image-based web sources, while video reasoning systems typically assume that relevant videos are provided in advance. We study open-web video research, where an agent must autonomously discover relevant videos, navigate their temporal content, and ground answers in visual evidence. Training…

### 9. RawSLAM: Online HDR Gaussian SLAM from Linear Radiance

- **arXiv**: [2609.20589v1](https://arxiv.org/abs/2609.20589v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.20589v1)
- **作者**: Marina Orozco González, Luis Merino
- **发表**: 2026-09-17  ·  **类别**: cs.CV
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Current dense visual SLAM systems rely almost exclusively on 8-bit tonemapped Low Dynamic Range (LDR) inputs, limiting their robustness in extreme lighting where shadows and highlights trigger tracking drift and mapping collapse. Conversely, existing raw and High Dynamic Range (HDR) reconstruction pipelines operate strictly offline. They depend on Structure…

### 10. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

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
1. [SMART: Zero-Shot Sim-to-Real Articulated Object Manipulation via Large-Scale Synthetic Pretraining](https://arxiv.org/abs/2610.07652v1) — score 22
2. [EigenDEXplore: Structured Exploration for Dexterous Manipulation with Human Priors](https://arxiv.org/abs/2610.07681v1) — score 21
3. [BiGym 2.0: Benchmarking Learned and Agent-Developed Policies for Humanoid Household Manipulation](https://arxiv.org/abs/2610.07594v1) — score 19

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
