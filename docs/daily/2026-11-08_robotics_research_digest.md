# 机器人研究每日摘要 · 2026-11-08

> 自动生成,共 111 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (5 篇)

### 1. Kinematic Hypothesis Context: Embodiment-Conditioned Learned Video Coding for Bandwidth-Limited Robot Policy Uplinks

- **arXiv**: [2611.07411v1](https://arxiv.org/abs/2611.07411v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.07411v1)
- **作者**: Yuze Lu
- **发表**: 2026-11-05  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Robots increasingly run large vision-language-action policies on remote servers, making the camera uplink the bottleneck. Existing video codecs spend bits on content the receiver could predict: the robot's own motion. We introduce the kinematic hypothesis context, a zero-rate conditioning signal that both ends build from joint states, the robot model and th…

### 2. T3R: Training-Free Two-Stage Token Refinement Towards Efficient and Robust VLA Models

- **arXiv**: [2611.08413v1](https://arxiv.org/abs/2611.08413v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.08413v1)
- **作者**: Mohammed Hassan, Zhenyang Chen, Zheng Wang et al.
- **发表**: 2026-11-05  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Vision-Language-Action (VLA) models enable end-to-end robot control, but inference is increasingly expensive. Each decision processes hundreds of visual tokens, often across multiple cameras, leading to substantial computation while allowing irrelevant background content to distract action prediction under distribution shift. We argue that these issues stem…

### 3. When Delay Meets Drift: Physical Safety of Robot Foundation Models Is a Cross-Layer Problem

- **arXiv**: [2611.02101v1](https://arxiv.org/abs/2611.02101v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.02101v1)
- **作者**: Liangkai Liu, Bimal Thapa Magar
- **发表**: 2026-11-01  ·  **类别**: cs.RO, cs.CV, cs.ET
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Robot foundation models now act in a closed loop, yet their safety is evaluated one variation at a time: robustness benchmarks perturb the scene while assuming instantaneous inference, and real-time execution methods study inference delay in nominal scenes. We argue that physical safety is not a property of the model alone, but emerges from how variations i…

### 4. La-JEPA: Compact Robot Policies with Latent World Modeling

- **arXiv**: [2611.08156v1](https://arxiv.org/abs/2611.08156v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.08156v1)
- **作者**: Mateo Clémente, George Z. Xue, Amin Abyaneh et al.
- **发表**: 2026-11-05  ·  **类别**: cs.RO, cs.CV, cs.LG
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: World-action models adapt pretrained video generators, and vision-language-action models build on pretrained vision-language backbones; both tie policy architecture and inference cost to large transformers designed for generation rather than control. It remains unclear how much these generation-oriented choices affect control. In this work, we introduce Lat…

### 5. Editing the Goal: Per-Token SAE Steering and Its Depth Limits in $π_{0.5}$

- **arXiv**: [2611.00602v1](https://arxiv.org/abs/2611.00602v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.00602v1)
- **作者**: Rocio Perales Valdes, Animesh Garg
- **发表**: 2026-10-31  ·  **类别**: cs.AI
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Sparse autoencoders (SAEs) have recovered interpretable, causally relevant features in robot foundation models (RFMs) such as $π_{0.5}$ (arXiv:2603.19183, arXiv:2603.19233). SAE features on individual instruction tokens are less interpretable than timestep-pooled ones (arXiv:2603.19183), and whether they can redirect a robot's goal remains untested. We show…

## 🌐 具身智能 / 机器人基础模型 (13 篇)

### 1. VagueBench: Benchmarking the Robustness of Embodied Agents on Ambient Context Illusions

- **arXiv**: [2611.03765v1](https://arxiv.org/abs/2611.03765v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.03765v1)
- **作者**: Yang Qu, Qiang Fu, Zonghao Ying et al.
- **发表**: 2026-11-02  ·  **类别**: cs.AI, cs.CV
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Embodied agents are increasingly deployed in open-world environments, yet current robustness evaluations remain biased toward hazardous instructions and jailbreak vulnerabilities. A more fundamental issue is largely overlooked: agents are rarely tested under semantically sufficient but contextually minimal instructions (i.e., common in real-world human comm…

### 2. TriPhysBench: Evaluating Physical Intelligence for Embodied Agents

- **arXiv**: [2611.01934v1](https://arxiv.org/abs/2611.01934v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.01934v1)
- **作者**: Zhongxiang Sun, Chenghao Yang, Haojie Ding et al.
- **发表**: 2026-11-01  ·  **类别**: cs.AI, cs.CV
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Embodied agents need physical intelligence to understand their surroundings through physical perception, physical knowledge retrieval, and physical reasoning. These capabilities must work together to interpret events and make quantitative judgments. Existing benchmarks advance physical understanding and general-purpose tool use, yet the coordination of thes…

### 3. Learning the Task or Learning the Verifier? Rethinking Criteria Exposure in Embodied Self-Improvement

- **arXiv**: [2611.08318v1](https://arxiv.org/abs/2611.08318v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.08318v1)
- **作者**: Wenbo Huang, Jianxin Bi, Shunyu Yang et al.
- **发表**: 2026-11-05  ·  **类别**: cs.AI, cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Self-improving embodied agents are increasingly being developed and compared on robot simulation benchmarks. Several recent works expose the benchmark's success criteria to the learning agent, a practice we call Criteria Exposure (CE). These criteria, originally written to verify policies trained by imitation learning, often demand more than the correspondi…

### 4. Physical Experience Builds Continual Spatial World Models

- **arXiv**: [2611.04016v1](https://arxiv.org/abs/2611.04016v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.04016v1)
- **作者**: Yuhang Sun
- **发表**: 2026-11-02  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: World models are increasingly used to support prediction and planning in embodied agents, but the knowledge is usually established before deployment and then carried into later encounters. Continual operation faces a different problem. A familiar environment may change, and the agent must use previous experience without allowing old expectations to override…

### 5. Generate-then-Rank: Learning Symbolic Goal Interpretation for Embodied Agents

- **arXiv**: [2611.07825v1](https://arxiv.org/abs/2611.07825v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.07825v1)
- **作者**: Jisen Lei, Huizhi Liang
- **发表**: 2026-11-05  ·  **类别**: cs.AI, cs.CL, cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Goal interpretation is to translate a natural language instruction into a formal symbolic goal that a planner can execute. It is critical for embodied agents because any error here propagates to every downstream planning and action step. Doing it well requires both generating suitable candidates and reliably selecting among them. We present a two-stage gene…

### 6. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 7. From Concepts to Actual Causes: Toward Closing the Concept-Malfunction Gap in Robot Foundation Models

- **arXiv**: [2611.00155v1](https://arxiv.org/abs/2611.00155v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.00155v1)
- **作者**: Gihyuk Ko
- **发表**: 2026-10-30  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Post-incident analysis of a robot foundation model poses a singular causal question: which internal components caused this failure, and to what degree? Mechanistic interpretability (MI), however, establishes general causal claims by decoding the concepts a policy has learned, yet knowing which concepts are encoded is insufficient for identifying the actual…

### 8. Reinforcement Learning Enables Scaling Generalist Robot Policy Improvement

- **arXiv**: [2611.06905v1](https://arxiv.org/abs/2611.06905v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.06905v1)
- **作者**: Michal Korniak, Marco Bagatella, Ralf Römer et al.
- **发表**: 2026-11-04  ·  **类别**: cs.LG, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: The introduction of generalist robot policies has enabled a single, large model to learn to perform a variety of tasks from a vast pre-training corpus. While these models often exhibit powerful zero-shot generalization capabilities, they typically require an adaptation phase to achieve sufficient performance in deployment. Iterated self-improvement via rein…

### 9. HTCE: Homeomorphism-inspired Topological Cross-Scene Experience Canonicalization and Reuse for Object Navigation

- **arXiv**: [2611.04836v1](https://arxiv.org/abs/2611.04836v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.04836v1)
- **作者**: Xiaoran Xu, Yupeng Wu, Tianyu Xue et al.
- **发表**: 2026-11-03  ·  **类别**: cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: As embodied agents perform object-goal navigation across residential environments, they accumulate successful experiences whose semantic structure recurs across scenes even when geometric trajectories do not. Reusing such experience is challenging because differences in region naming and observation granularity produce distinct graph representations of simi…

### 10. Do Embodied VLMs Actually Use Their Scene-Graph Memory?

- **arXiv**: [2611.02056v1](https://arxiv.org/abs/2611.02056v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.02056v1)
- **作者**: Shubh Garg, Divyansh Pandey, Vedant Khandelwal et al.
- **发表**: 2026-11-01  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Embodied agents that answer questions about their route need a memory of what they saw, and scene graphs are a natural form for it. A vision-language model (VLM) can receive such a graph as text or through a graph encoder, but accuracy alone cannot show whether the graph holds the episode's facts, reaches the model, or is actually relied on. In this diagnos…

## 🦵 人形 / 足式机器人 (28 篇)

### 1. A fully articulated humanoid dexterous hand with human-level joint structure enabled by linkage-based actuation

- **arXiv**: [2610.36789v1](https://arxiv.org/abs/2610.36789v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.36789v1)
- **作者**: Jihao Li, Jianguo Wang, Haotian Guo et al.
- **发表**: 2026-10-27  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Humanoid dexterous hands are a core component of embodied intelligence, enabling robots to translate high-level intent into rich and adaptive physical interaction. However, existing designs remain constrained by a persistent trade-off among anthropomorphic kinematic complexity, mechanical robustness, load capacity and control simplicity, limiting dexterous…

### 2. HLO-AMP: Hierarchical Loco-Manipulation from Object-Aware Motion Priors

- **arXiv**: [2611.05113v1](https://arxiv.org/abs/2611.05113v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.05113v1)
- **作者**: Jean-Pierre Sleiman, Bilal Hammoud, He Li et al.
- **发表**: 2026-11-03  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Hierarchical pipelines for humanoid loco-manipulation typically pair a task-agnostic whole-body controller (WBC) with a downstream task policy. Such WBCs are often trained through manual reward shaping, which yields visibly machine-like motions; more consequentially, they are trained without the manipulated object in the scene. Object dynamics are instead a…

### 3. Pixel: A Co-Designed Full-Stack Robot System for Learning General-Purpose Mobile Manipulation

- **arXiv**: [2611.03648v1](https://arxiv.org/abs/2611.03648v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.03648v1)
- **作者**: Tony Tao, Jason Jingzhou Liu, Ruslan Salakhutdinov et al.
- **发表**: 2026-11-02  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: General-purpose mobile manipulation requires a combination of capable robot hardware, scalable demonstration collection, expressive whole-body control, and effective policy learning. Yet these components are often developed independently, creating mismatches that limit the capabilities of the complete system. We present Pixel, a co-designed full-stack syste…

### 4. Catch It All!: Generalizable Dynamic Catching with a Dexterous Hand

- **arXiv**: [2610.39044v1](https://arxiv.org/abs/2610.39044v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.39044v1)
- **作者**: Arth Shukla, Kehlani Fay, Huaze Liu et al.
- **发表**: 2026-10-28  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Catching arbitrary objects requires generalization to novel projectiles and real-time adaptation to unpredictable contact dynamics under noisy visual observations. This paper presents Catch It All!, a sim-to-real catching framework for humanoid robots that generalizes and adapts to unseen objects with variable physical properties for underhand and overhand…

### 5. From Tabletop to Walking Bot: Deploying a VLA Model on a Legged Manipulator Robot

- **arXiv**: [2610.32271v1](https://arxiv.org/abs/2610.32271v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.32271v1)
- **作者**: Giovanni Minelli, Antonio Langella, Giovanni B. Dessy et al.
- **发表**: 2026-10-23  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models are typically pretrained on broad, diverse datasets and subsequently fine-tuned on a comparatively small dataset tailored to a specific target robot. Such adaptation recipe is now widely established, achieving its most mature results on fixed-base arms due to their static base dynamics and consistent reference frame. Moun…

### 6. AffectiveVLA: Safe and Intent-Aware VLA Control for Human-Humanoid Social Interaction

- **arXiv**: [2611.07712v1](https://arxiv.org/abs/2611.07712v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.07712v1)
- **作者**: Nikita Kuzmin, Georgii Demianchuk, Mariya Lezina et al.
- **发表**: 2026-11-05  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Social touch interactions, such as handshakes, fist bumps, and hugs, require humanoid robots to infer human intent, generate contact-rich motions, and maintain safe physical contact. We present AffectiveVLA, an intent-gated Vision-Language-Action (VLA) pipeline deployed on a Unitree G1 humanoid with dexterous hands. A lightweight RGB-based model recognizes…

### 7. Online iLQR-MPC with Whole-Body Control for Robust Humanoid Locomotion

- **arXiv**: [2611.04204v1](https://arxiv.org/abs/2611.04204v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.04204v1)
- **作者**: Xiang Li, Linlin Ou, Ruihan Wu et al.
- **发表**: 2026-11-03  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Humanoid locomotion requires deciding where to step and how to distribute contact forces. However, a disturbance can invalidate the nominal plan, requiring coordinated revision under constraints that switch with every footfall. To solve this online, the proposed approach employs the single-rigid-body model, which retains attitude dynamics and the full conta…

### 8. E2DRL: End-to-End Differentiable Reinforcement Learning for 3D Obstacle Avoidance in Quadruped Robots

- **arXiv**: [2610.19627v1](https://arxiv.org/abs/2610.19627v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19627v1)
- **作者**: Cheng Fan, Bingyang Zhou, Gang Yang et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Differentiable reinforcement learning shows strong promise for robot policy learning, but its application to legged locomotion has remained limited to blind walking or simulated 2D tasks. Extending it to end-to-end visual obstacle avoidance is challenging because hard collision constraints and early termination upon contact corrupt first-order gradients, tr…

### 9. OccluDex: Hierarchical 3D Visuo-Tactile Representation Learning for Egocentric Dexterous Manipulation under Self-Occlusion

- **arXiv**: [2609.39017v1](https://arxiv.org/abs/2609.39017v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39017v1)
- **作者**: Ziheng Xu, Yueyuan Chen, Xinyuan He et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Reliable dexterous manipulation requires continuous estimation of object geometry and hand-object contact throughout interaction. With egocentric sensing, however, the manipulating hand frequently occludes task-relevant object surfaces and contact regions, reducing the visual evidence available for state estimation and thereby making robust closed-loop cont…

### 10. CRISP: Constraint-Resolved Interactions between Subsystems for Predictive Whole-Body Cooperation

- **arXiv**: [2611.07268v1](https://arxiv.org/abs/2611.07268v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.07268v1)
- **作者**: Dario Valenzuela, Jeeseop Kim
- **发表**: 2026-11-05  ·  **类别**: cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: This paper presents a layered control framework that recasts high-dimensional system dynamics as a composition of dynamically interconnected subsystems, with dynamic dual-arm manipulation on the humanoid serving as a representative application. The humanoid is decomposed into a single rigid body (SRB) representing the torso and floating-base dynamic models…

## 🦾 操控 / 灵巧手 / 抓取 (33 篇)

### 1. TactileLab: Sim-to-Real Dexterous Robot Manipulation with Efficient Shear-Sensitive Tactile Simulation

- **arXiv**: [2611.07881v1](https://arxiv.org/abs/2611.07881v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.07881v1)
- **作者**: Yijiong Lin, Wenhao He, Toby Jack et al.
- **发表**: 2026-11-05  ·  **类别**: cs.RO
- **相关性评分**: 20  ·  **🔥 read_now**
- **摘要**: Robotic simulators that represent shear within tactile sensing are becoming increasingly important for contact-rich manipulation. However, simulating contact shear with high-fidelity deformable or soft-body simulation is computationally demanding, limiting scalability to large-scale reinforcement learning. Here we introduce \textit{TactileLab}, a scalable m…

### 2. Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation

- **arXiv**: [2611.05979v1](https://arxiv.org/abs/2611.05979v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.05979v1)
- **作者**: Zhengdong Hong, Guofeng Zhang
- **发表**: 2026-11-04  ·  **类别**: cs.RO
- **相关性评分**: 20  ·  **🔥 read_now**
- **摘要**: Manipulating diverse objects with multi-fingered dexterous hands is challenging due to the high dimensionality and complex dynamics. Human-Object Interaction (HOI) datasets provide rich knowledge about task information and embodied interactions. Instead of solely imitating the human demonstrations, our method learns to holistically predict future hand-objec…

### 3. DexHOT: Learning Hand-Object Configuration Transfer for Dexterous Manipulation

- **arXiv**: [2611.05119v1](https://arxiv.org/abs/2611.05119v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.05119v1)
- **作者**: Zhewei Gui, Anthony Bolton, Jiyao Zhang et al.
- **发表**: 2026-11-03  ·  **类别**: cs.RO
- **相关性评分**: 20  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation involves not only moving objects, but also arranging the hand around them to maintain useful contacts and enable subsequent actions. Yet many learning-based systems specify goals primarily through object poses or trajectories, leaving hand-object configurations to emerge implicitly. We introduce DexHOT, which formulates dexterous mani…

### 4. Latent RL Priors for Data-Efficient Dexterous Manipulation

- **arXiv**: [2611.08458v1](https://arxiv.org/abs/2611.08458v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.08458v1)
- **作者**: Yixiao Wang, Peiyi Chen, Mustafa Mukadam et al.
- **发表**: 2026-11-05  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Learning dexterous manipulation from limited visual demonstrations is challenging because policies must acquire both perceptual grounding and precise control, while reinforcement learning (RL) in simulation can acquire rich control behaviors from large-scale interaction with privileged information. We introduce \textbf{Latent RL Prior}, a two-stage framewor…

### 5. DexArena: A Unified Benchmark for Long-Horizon Dexterous Manipulation

- **arXiv**: [2611.02629v2](https://arxiv.org/abs/2611.02629v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.02629v2)
- **作者**: Haonan Ping, Jianshu Hu, Yimin Wang et al.
- **发表**: 2026-11-02  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Long-horizon dexterous manipulation remains a fundamental challenge for robot learning, requiring the composition of multiple skills, precise bimanual coordination, generalizable visual understanding, and robust skill transitions. Yet existing manipulation benchmarks largely emphasize isolated skills or support only a limited range of end-effectors, making…

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

### 8. HandMimicX: Learning Human-Like Dexterous Manipulation via an Object-Centric Policy from Egocentric Videos

- **arXiv**: [2610.41336v1](https://arxiv.org/abs/2610.41336v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.41336v1)
- **作者**: Zihan Gao, Yufei Liu, Yuhong Zhang et al.
- **发表**: 2026-10-30  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Learning dexterous manipulation from human videos remains an open challenge, particularly in the context of transferring a single demonstration into a spatially generalizable robotic skill and maintaining physically plausible human-like interactions. Unlike prior works that emphasize hand-motion imitation, we introduce an object-centric framework for acquir…

### 9. DexSuite: An All-in-One Framework for Dexterous Manipulation Across Arms, Hands, and Tasks

- **arXiv**: [2610.37799v1](https://arxiv.org/abs/2610.37799v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.37799v1)
- **作者**: Anas Houssaini, Hugo He, Junming Shi et al.
- **发表**: 2026-10-27  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Human-level dexterity remains a central open problem in robotics, yet few simulation frameworks cover the full workflow of dexterous manipulation, from setting up a robot to collecting dexterous demonstrations and evaluating policies. We present DexSuite, an all-in-one simulation framework for dexterous manipulation built on the Genesis simulator. DexSuite…

### 10. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

## 🎓 模仿学习 / 强化学习 (14 篇)

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

### 10. Unblur-SLAM: Dense Neural SLAM for Blurry Inputs

- **arXiv**: [2603.26810v1](https://arxiv.org/abs/2603.26810v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.26810v1)
- **作者**: Qi Zhang, Denis Rozumny, Francesco Girlanda et al.
- **发表**: 2026-03-26  ·  **类别**: cs.CV, eess.IV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We propose Unblur-SLAM, a novel RGB SLAM pipeline for sharp 3D reconstruction from blurred image inputs. In contrast to previous work, our approach is able to handle different types of blur and demonstrates state-of-the-art performance in the presence of both motion blur and defocus blur. Moreover, we adjust the computation effort with the amount of blur in…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (11 篇)

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

### 3. LIN-SLAM: Lightweight LiDAR--Inertial Neural SLAM for Real-Time Onboard Navigation

- **arXiv**: [2610.21199v1](https://arxiv.org/abs/2610.21199v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.21199v1)
- **作者**: Shiqi Che, Yijie Liu, Shuo Wang et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **✅ 已研读**
- **摘要**: Geometric light detection and ranging (LiDAR)--inertial simultaneous localization and mapping (SLAM) provides efficient state estimation but lacks the continuous map representation and global refinement capabilities of neural implicit SLAM, while neural implicit methods remain computationally expensive. We propose Lightweight LiDAR--Inertial Neural SLAM (LI…

### 4. Evaluation of Front-End Feature Matching for Lunar Visual SLAM

- **arXiv**: [2610.30774v1](https://arxiv.org/abs/2610.30774v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30774v1)
- **作者**: Guillem Casadesus Vila, Grace Gao
- **发表**: 2026-10-22  ·  **类别**: cs.CV
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Lunar rovers will primarily rely on cameras for localization until navigation satellite services are deployed, and will continue to need them afterwards for relative navigation, hazard detection, and surface operations. Visual odometry (VO) and Simultaneous Localization and Mapping (SLAM) mostly estimate motion by matching features between frames. However,…

### 5. Line-Augmented cuVSLAM: Robust Visual Odometry in Low-Texture Environments

- **arXiv**: [2610.20958v1](https://arxiv.org/abs/2610.20958v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20958v1)
- **作者**: Dara Molloy, Terry Wu, Wonju Lee et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Autonomous mobile robots in warehouses and production facilities operate in precisely the environments that defeat point-feature visual odometry: featureless aisles, uniform walls, repetitive racking and specular floors. Such environments are, however, rich in straight-edge structure: rack uprights, door frames, wall junctions and cabinet outlines present h…

### 6. Smartphone Indoor Localization Enhanced by Hierarchical Multi-Sensor Context Recognition

- **arXiv**: [2610.39691v1](https://arxiv.org/abs/2610.39691v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.39691v1)
- **作者**: Wenhui Feng, Muhan Weng, Jianyu Liu et al.
- **发表**: 2026-10-29  ·  **类别**: cs.LG, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Smartphone indoor localization requires low-cost, robust positioning across scene transitions and phone-use variations. Pedestrian dead reckoning (PDR) enables infrastructure-free deployment but accumulates errors from heading drift, structural transitions, and carrying-mode changes. Existing methods often treat contextual cues as a single event stream or l…

### 7. Human-in-the-Loop Neuro-Symbolic Drift Anticipation for Reliable Visual SLAM

- **arXiv**: [2610.05757v1](https://arxiv.org/abs/2610.05757v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05757v1)
- **作者**: Junhyun Nam, Wonse Jo
- **发表**: 2026-10-05  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: This paper introduces Hybrid DeepSEE (HDS), a Human-in-the-Loop (HITL) neuro-symbolic framework for proactive drift anticipation in Visual SLAM (V-SLAM). While data-driven models offer predictive power, their "black-box" nature often yields physically inconsistent outputs in out-of-distribution (OOD) environments. To address this, HDS integrates neural drif…

### 8. RTISSLAM-3D: Full 6-DoF SLAM With an In-Air 3D Imaging Sonar

- **arXiv**: [2610.22552v1](https://arxiv.org/abs/2610.22552v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.22552v1)
- **作者**: Jan Steckel, Vincent Katter, Wouter Jansen
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Echolocating bats navigate dense forests using sonar alone, and in-air 3D imaging sonars now capture the entire frontal hemisphere with every pulse. Sonar SLAM, however, has so far been planar: current systems estimate a 2D trajectory and discard the elevation information in the sonar images, an assumption that does not hold on rough and sloped terrain such…

### 9. Does Dynamic-Point Filtering Help When Texture Is Scarce? A Controlled Study of ORB-SLAM2 Front-Ends in Synthetic Indoor Scenes

- **arXiv**: [2610.10564v1](https://arxiv.org/abs/2610.10564v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10564v1)
- **作者**: Zekui Xue
- **发表**: 2026-10-02  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Dynamic-point filters are routinely added to feature-based visual SLAM, and several recent systems argue that removing dynamic features can leave too few static features in low-texture regions. So far, these systems have been evaluated only on texture-rich benchmark sequences. We present a controlled study that isolates this interaction. We render synthetic…

### 10. Parameter Sensitivity Analysis for Aerial LiDAR-Inertial Odometries in low-altitude flights

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
- **相关性评分**: 3  ·  **📌 info**
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
1. [TactileLab: Sim-to-Real Dexterous Robot Manipulation with Efficient Shear-Sensitive Tactile Simulation](https://arxiv.org/abs/2611.07881v1) — score 20
2. [Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation](https://arxiv.org/abs/2611.05979v1) — score 20
3. [DexHOT: Learning Hand-Object Configuration Transfer for Dexterous Manipulation](https://arxiv.org/abs/2611.05119v1) — score 20

> 筛选说明:本次 Top 3 已排除(已研读跳过 1 篇、综述跳过 1 篇)。

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
