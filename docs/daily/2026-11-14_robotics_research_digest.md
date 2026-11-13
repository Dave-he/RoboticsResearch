# 机器人研究每日摘要 · 2026-11-14

> 自动生成,共 114 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (7 篇)

### 1. VLA-MOPD: On-Policy Distillation for Multi-Task VLA Policy Consolidation

- **arXiv**: [2611.12286v1](https://arxiv.org/abs/2611.12286v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.12286v1)
- **作者**: Yongxuan Lv, Zhen Fang, Lichen Man et al.
- **发表**: 2026-11-09  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Physical intelligence requires embodied agents to ground language in observations and execute actions while retaining useful skills. Vision-language-action (VLA) policies offer a shared interface, but task-specific post-training often produces separate specialists. Consolidation is difficult: mixed-task reinforcement learning provides sparse trajectory-leve…

### 2. When Delay Meets Drift: Physical Safety of Robot Foundation Models Is a Cross-Layer Problem

- **arXiv**: [2611.02101v1](https://arxiv.org/abs/2611.02101v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.02101v1)
- **作者**: Liangkai Liu, Bimal Thapa Magar
- **发表**: 2026-11-01  ·  **类别**: cs.RO, cs.CV, cs.ET
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Robot foundation models now act in a closed loop, yet their safety is evaluated one variation at a time: robustness benchmarks perturb the scene while assuming instantaneous inference, and real-time execution methods study inference delay in nominal scenes. We argue that physical safety is not a property of the model alone, but emerges from how variations i…

### 3. ActionCodec2: A Streaming Action Tokenizer

- **arXiv**: [2611.15490v1](https://arxiv.org/abs/2611.15490v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.15490v1)
- **作者**: Zibin Dong, Yicheng Liu, Shiduo Zhang et al.
- **发表**: 2026-11-11  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Most action tokenizers for autoregressive vision language action (VLA) models compress motion into chunks that must be decoded in full before their actions become executable. We introduce ActionCodec2, a non-neural streaming tokenizer that releases actions incrementally while keeping trajectory reconstruction error within a prescribed tolerance. Its encoder…

### 4. Editing the Goal: Per-Token SAE Steering and Its Depth Limits in $π_{0.5}$

- **arXiv**: [2611.00602v1](https://arxiv.org/abs/2611.00602v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.00602v1)
- **作者**: Rocio Perales Valdes, Animesh Garg
- **发表**: 2026-10-31  ·  **类别**: cs.AI
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Sparse autoencoders (SAEs) have recovered interpretable, causally relevant features in robot foundation models (RFMs) such as $π_{0.5}$ (arXiv:2603.19183, arXiv:2603.19233). SAE features on individual instruction tokens are less interpretable than timestep-pooled ones (arXiv:2603.19183), and whether they can redirect a robot's goal remains untested. We show…

### 5. I See What You Want: Decoding Hierarchical Operator Intent from Visual Teleoperation History

- **arXiv**: [2611.16419v1](https://arxiv.org/abs/2611.16419v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.16419v1)
- **作者**: Xiangyi Jia, Kaixian Qu, Shengzhi Wang et al.
- **发表**: 2026-11-12  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-language models (VLMs) have become a powerful foundation for robotic scene understanding, task planning, and language-conditioned control. A natural question follows: can these models also decode what a human operator intends while teleoperating a robot, without any explicit instruction? We formulate this as hierarchical intent prediction, jointly in…

### 6. What Can a VLA Learn from the Agent That Calls It? Task-Level Experience Distillation for Embodied Navigation

- **arXiv**: [2611.16246v1](https://arxiv.org/abs/2611.16246v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.16246v1)
- **作者**: Jinze Tao, Yuxiao Han, Kangkang Dong et al.
- **发表**: 2026-11-12  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Navigation agents use a large language model (LLM) planner to call a vision-language-action (VLA) model. Each episode needs the LLM, adding cost and delay. We distill successful agent experience into the VLA instead of distilling the planner. The VLA then navigates alone at test time. Agent sessions are not VLA demonstrations. They include motions driven by…

### 7. La-JEPA: Compact Robot Policies with Latent World Modeling

- **arXiv**: [2611.08156v1](https://arxiv.org/abs/2611.08156v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.08156v1)
- **作者**: Mateo Clémente, George Z. Xue, Amin Abyaneh et al.
- **发表**: 2026-11-05  ·  **类别**: cs.RO, cs.CV, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: World-action models adapt pretrained video generators, and vision-language-action models build on pretrained vision-language backbones; both tie policy architecture and inference cost to large transformers designed for generation rather than control. It remains unclear how much these generation-oriented choices affect control. In this work, we introduce Lat…

## 🌐 具身智能 / 机器人基础模型 (12 篇)

### 1. IncR-3DSGG: Incremental Posed RGB Image Based 3D Scene Graph Generation via Privileged Depth Supervision

- **arXiv**: [2611.15429v1](https://arxiv.org/abs/2611.15429v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.15429v1)
- **作者**: Mrunmai Phatak, Daniel Kienzle, Roman Küble et al.
- **发表**: 2026-11-11  ·  **类别**: cs.CV
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Scene graphs provide a compact, structured representation of environments by capturing objects and their spatial or semantic relationships in a form suitable for embodied agents. Existing 3D scene graph generation methods often rely on depth sensing at inference, either to associate object instances across views via point cloud overlap or to compute inter-o…

### 2. HeMeR: Heterogeneous Memory Reconciliation for Embodied Agents via Structured KV Reuse

- **arXiv**: [2611.16487v1](https://arxiv.org/abs/2611.16487v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.16487v1)
- **作者**: Saehun Chun, Wonje Choi, Jinwoo Jang et al.
- **发表**: 2026-11-12  ·  **类别**: cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Embodied agents make decisions by combining information from heterogeneous memory modules, including declarative memory for explicit knowledge, procedural memory for learned routines, and working memory for current observations. During interaction, the memory contents required for decision making change with the agent's state, goal, and task progress, while…

### 3. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 4. From Concepts to Actual Causes: Toward Closing the Concept-Malfunction Gap in Robot Foundation Models

- **arXiv**: [2611.00155v1](https://arxiv.org/abs/2611.00155v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.00155v1)
- **作者**: Gihyuk Ko
- **发表**: 2026-10-30  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Post-incident analysis of a robot foundation model poses a singular causal question: which internal components caused this failure, and to what degree? Mechanistic interpretability (MI), however, establishes general causal claims by decoding the concepts a policy has learned, yet knowing which concepts are encoded is insufficient for identifying the actual…

### 5. XBot-Omni: An Omni-Modal Model for Embodied Understanding and Interaction

- **arXiv**: [2611.17160v1](https://arxiv.org/abs/2611.17160v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.17160v1)
- **作者**: Kerui Gu, Xing Fu, Shuoyang Sun et al.
- **发表**: 2026-11-12  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Embodied interaction requires an agent to integrate multimodal perception with verbal and nonverbal behaviors to effectively communicate its intentions, including speech, body motion, and facial expressions. We present XBot-Omni, a Thinker--Talker--Actor architecture that extends the Omni paradigm to robotic modalities, including body motion and facial expr…

### 6. AstroMemBench: A Benchmark for Memory Systems in Embodied Spacecraft Agents

- **arXiv**: [2611.16590v1](https://arxiv.org/abs/2611.16590v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.16590v1)
- **作者**: You Wu, Guhong Zhang, Hongwei Li et al.
- **发表**: 2026-11-12  ·  **类别**: cs.AI, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Long-term spacecraft autonomy requires embodied agents to use operational history under communication delays, time-critical operations, environmental uncertainty, complex physical interactions, power and computational constraints, and safety and reliability requirements. We introduce AstroMemBench and a Scenario-Challenge-Capability design method that maps…

### 7. What World Model Does Active Object Search Need? A Study under Imperfect Detection

- **arXiv**: [2611.15689v1](https://arxiv.org/abs/2611.15689v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.15689v1)
- **作者**: Kyeongryeol Go
- **发表**: 2026-11-11  ·  **类别**: cs.RO, eess.SY
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: In active object search, a robot must decide where to look and when to stop. Imperfect detection complicates both decisions: a non-detection may indicate occlusion, an out-of-view target, or a false negative, while a detection may be a false positive. This raises the question of which representations a world model needs to support reliable search under impe…

### 8. Softness is something you also need! Why compliance helps control: information metrics of a passive walker with compliant ankle

- **arXiv**: [2611.13779v1](https://arxiv.org/abs/2611.13779v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.13779v1)
- **作者**: Fabio Bonsignorio, Elisabetta Barletta, Sorin Dragomir et al.
- **发表**: 2026-11-10  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: A great gap in adaptivity, flexibility, and dexterity still exists between intelligent robots, whether they are made of rigid or (partially) compliant components, and their naturally evolved animal and vegetal counterparts. One reason could be of `paradigm' nature. On the one hand, most robots (both rigid and soft) are still designed by following a `Cartesi…

### 9. WanderBench: Can World Models Explore Dynamic Worlds from Video?

- **arXiv**: [2611.12557v1](https://arxiv.org/abs/2611.12557v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.12557v1)
- **作者**: Yuhang Chen, Jiheng Li, Jiale Wang et al.
- **发表**: 2026-11-09  ·  **类别**: cs.CV, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Video world models conditioned on an input video make it possible to explore real, recorded dynamic scenes, enabling re-shooting of footage, free-viewpoint replay, and real-to-sim environments for embodied agents. Such uses require the generated rollout to stay faithful to the recorded world, yet existing benchmarks start from a single image or a text promp…

### 10. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

## 🦵 人形 / 足式机器人 (30 篇)

### 1. PolyMorphWBC: Whole-Body Control from End-Effector Trajectories for Quadrupedal Mobile Manipulation across Arm Morphologies with Extended Reach

- **arXiv**: [2611.15117v1](https://arxiv.org/abs/2611.15117v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.15117v1)
- **作者**: Heng Li, Yang Li, Yifan Duan et al.
- **发表**: 2026-11-11  ·  **类别**: cs.RO
- **相关性评分**: 20  ·  **🔥 read_now**
- **摘要**: Quadrupedal mobile manipulators can extend their manipulation workspace by coordinating the mounted arm with the mobile base. At the task level, short-horizon end-effector (EE) trajectories provide an interface for specifying the desired manipulation motion without prescribing how it should be realized by the arm and base. However, executing such trajectori…

### 2. Decoupled Asynchronous System for Humanoids (DASH): Latency-Agnostic Scaling of Vision-Language-Action Models for Humanoid Manipulation

- **arXiv**: [2611.11854v2](https://arxiv.org/abs/2611.11854v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.11854v2)
- **作者**: Bingzhang Wang, Nathan Zhao, Jialeng Ni et al.
- **发表**: 2026-11-09  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models pair a vision-language backbone with an action head, but in closed-loop control the backbone sits on the control-critical path: while it computes, the robot keeps moving, so each executed action is conditioned on an increasingly stale observation. A larger backbone therefore directly blocks reactivity, especially in human…

### 3. PERA: Plug-in Experts for Robotic Actions in Continual Whole-Body Control

- **arXiv**: [2611.16188v1](https://arxiv.org/abs/2611.16188v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.16188v1)
- **作者**: Shangchao Hu, Yadan Sun, Xibo Yu et al.
- **发表**: 2026-11-12  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Motion imitation enables humanoid robots to acquire whole-body skills such as walking and dancing. However, fine-tuning an entire policy for a new skill can affect existing behaviors, while training a separate policy for each skill increases training and maintenance costs. We present PERA, a method for learning new skills by reusing existing motion capabili…

### 4. Embodied First Exam

- **arXiv**: [2611.12177v1](https://arxiv.org/abs/2611.12177v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.12177v1)
- **作者**: Kangrui Wang, Qineng Wang, Changhe Chen et al.
- **发表**: 2026-11-09  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Early successes on agentic robotics point to a potential paradigm shift toward using coding agents to control robots. Existing robotics benchmarks are built around visuomotor policy learning, leaving it open whether coding agents can reliably control diverse robots under physical-world constraints. We therefore introduce the Embodied First Exam, a unified,…

### 5. From Tabletop to Walking Bot: Deploying a VLA Model on a Legged Manipulator Robot

- **arXiv**: [2610.32271v1](https://arxiv.org/abs/2610.32271v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.32271v1)
- **作者**: Giovanni Minelli, Antonio Langella, Giovanni B. Dessy et al.
- **发表**: 2026-10-23  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models are typically pretrained on broad, diverse datasets and subsequently fine-tuned on a comparatively small dataset tailored to a specific target robot. Such adaptation recipe is now widely established, achieving its most mature results on fixed-base arms due to their static base dynamics and consistent reference frame. Moun…

### 6. Reading the Table: Sim-to-Real Game State Detection for the Chef's Hat Card Game

- **arXiv**: [2611.15524v1](https://arxiv.org/abs/2611.15524v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.15524v1)
- **作者**: Connor Gäde, Matthias Kerzel, Hauke Bünning et al.
- **发表**: 2026-11-11  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Tabletop games offer a compelling scenario to study the interaction between artificial and human agents, combining social interaction with game state tracking and physical manipulation. To assess the game state, a robot needs to precisely detect closely related game objects, such as different card designs, requiring dedicated training data that is costly to…

### 7. OccluDex: Hierarchical 3D Visuo-Tactile Representation Learning for Egocentric Dexterous Manipulation under Self-Occlusion

- **arXiv**: [2609.39017v1](https://arxiv.org/abs/2609.39017v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39017v1)
- **作者**: Ziheng Xu, Yueyuan Chen, Xinyuan He et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Reliable dexterous manipulation requires continuous estimation of object geometry and hand-object contact throughout interaction. With egocentric sensing, however, the manipulating hand frequently occludes task-relevant object surfaces and contact regions, reducing the visual evidence available for state estimation and thereby making robust closed-loop cont…

### 8. Runtime Safety and Emergency Stops on a Full-Size Humanoid: Deployment Lessons and a Case for Graduated Force Authority

- **arXiv**: [2611.15928v1](https://arxiv.org/abs/2611.15928v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.15928v1)
- **作者**: Max Conway, Yutong Zhang, Allen Devaraj et al.
- **发表**: 2026-11-11  ·  **类别**: cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Full-size humanoid robots are being considered for hazardous industrial work such as disassembling electric-vehicle batteries. We describe the safety mechanisms of an open-source autonomy stack for the Unitree H1-2 humanoid and what deploying them taught us. All joint commands pass through a safety layer that runs separately from the control software. It en…

### 9. CFGComposer: Compositional Audio-Text-to-Motion Generation via Copula Score Correction

- **arXiv**: [2611.15101v1](https://arxiv.org/abs/2611.15101v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.15101v1)
- **作者**: Pengyang Shi, Jinlu Zhang, Chunze Lin et al.
- **发表**: 2026-11-11  ·  **类别**: cs.SD, cs.AI
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Generating whole-body gestures that are simultaneously rhythmically synchronized with speech audio and semantically aligned with text descriptions is a fundamental challenge in embodied AI and social robotics. We tackle this Audio-Text-to-Motion (AT2M) problem by composing two independently-trained diffusion models at inference time and refine bias in joint…

### 10. E2DRL: End-to-End Differentiable Reinforcement Learning for 3D Obstacle Avoidance in Quadruped Robots

- **arXiv**: [2610.19627v1](https://arxiv.org/abs/2610.19627v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19627v1)
- **作者**: Cheng Fan, Bingyang Zhou, Gang Yang et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Differentiable reinforcement learning shows strong promise for robot policy learning, but its application to legged locomotion has remained limited to blind walking or simulated 2D tasks. Extending it to end-to-end visual obstacle avoidance is challenging because hard collision constraints and early termination upon contact corrupt first-order gradients, tr…

## 🦾 操控 / 灵巧手 / 抓取 (30 篇)

### 1. Learning Heterogeneous Tactile Representation for General Dexterous Manipulation

- **arXiv**: [2611.12806v1](https://arxiv.org/abs/2611.12806v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.12806v1)
- **作者**: Bing Han, Yichuan Peng, Haoyu Dong et al.
- **发表**: 2026-11-09  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Tactile sensing is an indispensable modality for contact-rich dexterous manipulation, a capability that hints at the ultimate frontiers of embodied intelligence. However, commercially available tactile sensors are still at a relatively early stage of development, with each type of sensor offering irreplaceable strengths alongside its own drawbacks. A key ch…

### 2. TactileLab: Sim-to-Real Dexterous Robot Manipulation with Efficient Shear-Sensitive Tactile Simulation

- **arXiv**: [2611.07881v1](https://arxiv.org/abs/2611.07881v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.07881v1)
- **作者**: Yijiong Lin, Wenhao He, Toby Jack et al.
- **发表**: 2026-11-05  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Robotic simulators that represent shear within tactile sensing are becoming increasingly important for contact-rich manipulation. However, simulating contact shear with high-fidelity deformable or soft-body simulation is computationally demanding, limiting scalability to large-scale reinforcement learning. Here we introduce \textit{TactileLab}, a scalable m…

### 3. Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation

- **arXiv**: [2611.05979v1](https://arxiv.org/abs/2611.05979v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.05979v1)
- **作者**: Zhengdong Hong, Guofeng Zhang
- **发表**: 2026-11-04  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Manipulating diverse objects with multi-fingered dexterous hands is challenging due to the high dimensionality and complex dynamics. Human-Object Interaction (HOI) datasets provide rich knowledge about task information and embodied interactions. Instead of solely imitating the human demonstrations, our method learns to holistically predict future hand-objec…

### 4. MOSAIC: Modular Obstacle and Spatial-Aware Framework for Manipulation In Cluttered Scenes

- **arXiv**: [2611.15937v1](https://arxiv.org/abs/2611.15937v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.15937v1)
- **作者**: Richard Shi, Mohammad Mahdavian, Mehrdad Momeni Zadeh et al.
- **发表**: 2026-11-11  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models have demonstrated strong performance in robotic manipulation, yet most rely primarily on 2D visual observations and language instructions, leaving scene geometry and obstacle relationships to be inferred implicitly. This limitation is particularly problematic in cluttered environments, where small spatial errors can lead…

### 5. SoTa: Soft Tactile Skins for Dexterous Manipulation

- **arXiv**: [2610.02338v1](https://arxiv.org/abs/2610.02338v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.02338v1)
- **作者**: Jingyun Yang, Baiyu Shi, Timothy Yu et al.
- **发表**: 2026-10-01  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: A growing body of work suggests that tactile sensing gives robot policies contact information that complements vision in dexterous manipulation. However, visuo-tactile robot data remains scarce: dexterous demonstrations require teleoperating robots, which limits dataset scale. Human demonstrations are far cheaper to collect and offer a path to scale this da…

### 6. ManiLadder: Benchmarking Robot Manipulation Through a Categorized and Multi-Difficulty Level Task Ladder

- **arXiv**: [2611.16374v1](https://arxiv.org/abs/2611.16374v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.16374v1)
- **作者**: Chongkai Gao, Jieao Shi, Zhaoyu Mu et al.
- **发表**: 2026-11-12  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Recent advances in robotic manipulation have enabled increasingly complex and dexterous behaviors, yet existing benchmarks still focus on simple pick-and-place tasks and lack a systematic framework for measuring progress in robot learning along the axis of task difficulty. We present ManiLadder, a large-scale and organized simulation benchmark for robotic m…

### 7. Low-Cost Mobile Bimanual Manipulation for Long-Horizon Toilet Cleaning

- **arXiv**: [2611.15381v1](https://arxiv.org/abs/2611.15381v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.15381v1)
- **作者**: Sven Schreiber, Bernard Burdiek, Lasse Huber-Saffer et al.
- **发表**: 2026-11-11  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models have shown promising capabilities for robot manipulation, but their performance on accessible mobile bimanual platforms remains underexplored. We present a low-cost and reproducible mobile bimanual platform integrating two LeRobot SO-101 manipulators with a TurtleBot 4 and a LeRobot-ROS 2 software stack. Using long-horizo…

### 8. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

### 9. PCTac: Mechanochromic Photonic-Crystal Tactile Sensor for Dexterous Manipulation

- **arXiv**: [2611.12383v1](https://arxiv.org/abs/2611.12383v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.12383v1)
- **作者**: Ruilin Zhang, Xuanshuo Liu, Junzhe Dai et al.
- **发表**: 2026-11-09  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Modern visuotactile sensors primarily sense contact by imaging the deformation of a compliant interface. Using techniques such as photometric stereo, they can recover detailed contact geometry, often represented as surface normals or depth. However, force-related information typically still needs to be inferred indirectly through calibration, geometric reco…

### 10. BAT-WAM: Bridging Action and Touch in World-Action Models for Dexterous Hands

- **arXiv**: [2611.10967v1](https://arxiv.org/abs/2611.10967v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.10967v1)
- **作者**: Dong Fang, Feixuan Huang, Yuanxin Zhong et al.
- **发表**: 2026-11-07  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation with world action models (WAMs) relies on hand configuration and contact information, yet joint-state and whole-hand tactile observations may be partially or entirely missing. RGB images provide scene context and hand-object geometry but are insufficient to reliably recover these missing modalities. We further observe a correlation be…

## 🎓 模仿学习 / 强化学习 (17 篇)

### 1. DeRep: Learning Depth Representations for End-to-End Navigation in Cluttered Environments

- **arXiv**: [2611.13499v1](https://arxiv.org/abs/2611.13499v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.13499v1)
- **作者**: Hanyu Jin, Kenji Shimada
- **发表**: 2026-11-10  ·  **类别**: cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: End-to-end navigation in cluttered environments relies on compact visual representations to support collision avoidance and goal-directed motion. Existing methods typically learn these representations jointly with the policy or through observation reconstruction, which does not explicitly specify what information the representation should preserve. Moreover…

### 2. Bracketing Shows the Way: Adaptive Multi-Exposure Policy as Input for Robust Visual SLAM

- **arXiv**: [2610.33174v1](https://arxiv.org/abs/2610.33174v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.33174v1)
- **作者**: Olivier Gamache, Anthony Lavertu, David-Alexandre Duclos et al.
- **发表**: 2026-10-23  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Rapid illumination transitions can disturb Visual SLAM (VSLAM) by saturating images before the Automatic Exposure (AE) policy adapts, removing the visual correspondences needed to maintain tracking. Our proposed methods mitigate this disturbance at two levels: B-Adapt acquires adaptive exposure brackets to cover the scene dynamic range while promoting photo…

### 3. DPGS-SLAM: Diffusion-Prior and Provenance-Aware Monocular Gaussian Splatting SLAM for Dynamic Visual Sensing

- **arXiv**: [2611.12038v2](https://arxiv.org/abs/2611.12038v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.12038v2)
- **作者**: Yifan Luo, Takafumi Matsumaru, Vibekananda Dutta et al.
- **发表**: 2026-11-09  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: This paper presents DPGS-SLAM (Diffusion-Prior and Provenance-Aware Monocular Gaussian Splatting SLAM) for dense mapping in environments containing dynamic objects. Objects in dynamic motion remain a significant challenge for dense visual SLAM since dynamic observations can contaminate camera tracking and scene reconstruction. Although 3DGS (3D Gaussian spl…

### 4. Degeneracy-Orthogonal Geometric Constraints for LiDAR SLAM

- **arXiv**: [2609.36753v1](https://arxiv.org/abs/2609.36753v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.36753v1)
- **作者**: Minseo Kim, Yina Kim, Jinhwa Hwang et al.
- **发表**: 2026-09-29  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Autonomous robot navigation relies on simultaneous localization and mapping (SLAM) to estimate motion and maintain an accurate pose within an environment. However, in axially uniform corridors such as long tunnels and pipelines, LiDAR odometry is fundamentally limited by unconstrained drift along the feature-weak travel direction. This structural degeneracy…

### 5. Chain-SLAM: Globally Consistent Backend for Multi-Session LiDAR SLAM via Chained Loop Closure

- **arXiv**: [2609.12221v1](https://arxiv.org/abs/2609.12221v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.12221v1)
- **作者**: Zhiheng Li, Xinhao Liu, Juexiao Zhang et al.
- **发表**: 2026-09-10  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Maintaining consistency over long spatial and temporal horizons remains a fundamental challenge in large-scale LiDAR SLAM, particularly when integrating maps collected across multiple sessions. We present Chain-SLAM, a LiDAR SLAM backend enabling online multi-session map alignment and reuse with global consistency at large scale. We implement a chained loop…

### 6. Generative adversarial imitation learning for robot swarms: Learning from human demonstrations and trained policies

- **arXiv**: [2603.02783v1](https://arxiv.org/abs/2603.02783v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.02783v1)
- **作者**: Mattes Kraus, Jonas Kuckling
- **发表**: 2026-03-03  ·  **类别**: cs.RO, cs.LG, cs.MA
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, robots are supposed to learn from demonstrations of the desired behavior. Most of the work in imitation learning for swarm robotics provides the demonstrations as rollouts of an existing policy. In this work, we provide a framework based on generative adversarial imitation learning that aims to learn collective behaviors from human de…

### 7. End-to-End Deep Imitation Learning: Robot Soccer Case Study

- **arXiv**: [1807.09205v1](https://arxiv.org/abs/1807.09205v1)  ·  **PDF**: [link](https://arxiv.org/pdf/1807.09205v1)
- **作者**: Okan Aşık, Binnur Görer, H. Levent Akın
- **发表**: 2018-06-28  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, behavior learning is generally done using the features extracted from the demonstration data. Recent deep learning algorithms enable the development of machine learning methods that can get high dimensional data as an input. In this work, we use imitation learning to teach the robot to dribble the ball to the goal. We use B-Human robo…

### 8. RingNav: Task-Shaped Circular Memory for Visual Heading

- **arXiv**: [2610.19044v1](https://arxiv.org/abs/2610.19044v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19044v1)
- **作者**: Naitri Rajyaguru, Aryan Tajne, Stephen Jardim et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Tiny robots have limited computation and memory, yet visual navigation systems often maintain more state than a task requires. We ask whether persistent memory can instead be shaped by the task. We present \textbf{RingNav}, a \(10.6\)k--parameter visual heading estimator that constrains its memory to the circular manifold \(S^1\). RingNav learns only the tu…

### 9. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 10. Fog-FWL: A Large-Scale Full-Waveform LiDAR Dataset for Recovering Fog-Hidden Objects

- **arXiv**: [2611.16742v1](https://arxiv.org/abs/2611.16742v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.16742v1)
- **作者**: Kazuma Ikeda, Kotaro Oishi, Ryosei Hara et al.
- **发表**: 2026-11-12  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: LiDAR is a core sensor for autonomous driving, yet it is highly vulnerable to fog. Fog scattering produces strong backscatter near the sensor and attenuates reflections from objects behind it, so weak object returns are often discarded by the peak detection that converts received signals into point clouds. Full-waveform LiDAR (FWL), which records the receiv…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (9 篇)

### 1. SKiD-SLAM: Resource-Aware Distributed Multi-Robot LiDAR SLAM for Planetary Missions with Field Deployments at Analog Sites

- **arXiv**: [2610.38141v1](https://arxiv.org/abs/2610.38141v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.38141v1)
- **作者**: Hogyun Kim, Juwon Kim, Dongjin Cho et al.
- **发表**: 2026-10-28  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **📚 综述(归档备查,按协议 §4 不深读)**
- **摘要**: Future planetary exploration missions require teams of robots to collaboratively map unknown environments under severe communication limits, constrained onboard computation, and no central infrastructure. In this field report, we present SKiD-SLAM, a distributed multi-robot LiDAR simultaneous localization and mapping (SLAM) system for such environments, and…

### 2. Spade-SLAM: Sparse Correspondence Anchors for Dense Self-Supervised Visual SLAM

- **arXiv**: [2611.01937v1](https://arxiv.org/abs/2611.01937v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.01937v1)
- **作者**: Julian Philipp Schmitt, Weirong Chen, Ganlin Zhang et al.
- **发表**: 2026-11-01  ·  **类别**: cs.CV
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: We introduce Spade-SLAM, a self-supervised dense visual SLAM framework that substantially narrows the long-standing performance gap to supervised methods in a zero-shot setting. By demonstrating that high-fidelity tracking can be achieved without explicit ground-truth pose and depth labels, our approach offers a highly effective and label-efficient alternat…

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

### 5. Smartphone Indoor Localization Enhanced by Hierarchical Multi-Sensor Context Recognition

- **arXiv**: [2610.39691v1](https://arxiv.org/abs/2610.39691v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.39691v1)
- **作者**: Wenhui Feng, Muhan Weng, Jianyu Liu et al.
- **发表**: 2026-10-29  ·  **类别**: cs.LG, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Smartphone indoor localization requires low-cost, robust positioning across scene transitions and phone-use variations. Pedestrian dead reckoning (PDR) enables infrastructure-free deployment but accumulates errors from heading drift, structural transitions, and carrying-mode changes. Existing methods often treat contextual cues as a single event stream or l…

### 6. Line-Augmented cuVSLAM: Robust Visual Odometry in Low-Texture Environments

- **arXiv**: [2610.20958v1](https://arxiv.org/abs/2610.20958v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20958v1)
- **作者**: Dara Molloy, Terry Wu, Wonju Lee et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Autonomous mobile robots in warehouses and production facilities operate in precisely the environments that defeat point-feature visual odometry: featureless aisles, uniform walls, repetitive racking and specular floors. Such environments are, however, rich in straight-edge structure: rack uprights, door frames, wall junctions and cabinet outlines present h…

### 7. RTISSLAM-3D: Full 6-DoF SLAM With an In-Air 3D Imaging Sonar

- **arXiv**: [2610.22552v1](https://arxiv.org/abs/2610.22552v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.22552v1)
- **作者**: Jan Steckel, Vincent Katter, Wouter Jansen
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Echolocating bats navigate dense forests using sonar alone, and in-air 3D imaging sonars now capture the entire frontal hemisphere with every pulse. Sonar SLAM, however, has so far been planar: current systems estimate a 2D trajectory and discard the elevation information in the sonar images, an assumption that does not hold on rough and sloped terrain such…

### 8. Parameter Sensitivity Analysis for Aerial LiDAR-Inertial Odometries in low-altitude flights

- **arXiv**: [2609.12837v1](https://arxiv.org/abs/2609.12837v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.12837v1)
- **作者**: Robert Milijas, Jose Ramiro Martinez-de Dios, Stjepan Bogdan
- **发表**: 2026-09-11  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: LiDAR-based SLAM (Simultaneous Localization and Mapping) and LIO (LiDAR-inertial odometry) algorithms are often used for precise navigation of unmanned aerial vehicles, especially during interactions with the aerial robot's environment. However, the performance of these algorithms is greatly dependent on the scenario, LiDAR, and robot motion characteristics…

### 9. Geodesic Flow Matching for Denoising High-Dimensional Structured Representations

- **arXiv**: [2606.00248v1](https://arxiv.org/abs/2606.00248v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.00248v1)
- **作者**: Karim Habashy, Chris Eliasmith
- **发表**: 2026-05-29  ·  **类别**: cs.AI
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Vector Symbolic Algebras (VSAs) enable robust neurosymbolic reasoning by encoding symbolic information into high-dimensional distributed representations. For continuous domains, Spatial Semantic Pointers (SSPs) extend this framework by mapping variables onto continuous toroidal manifolds. However, standard approaches like Flow Matching assume a flat Euclide…

## 🧭 导航 / 路径规划 (1 篇)

### 1. Accuracy potential of visual localization exploiting high-end street-level imagery

- **arXiv**: [2607.24409v2](https://arxiv.org/abs/2607.24409v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.24409v2)
- **作者**: Jonas Meyer, Stephan Nebiker, Pascal Theiler et al.
- **发表**: 2026-07-27  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Many applications, such as surveying, autonomous navigation, robotics and augmented reality, require accurate pose information with respect to a reference frame. Visual localization can complement GNSS positioning, whose availability and accuracy are often limited. However, the accuracy potential of visual localization has not yet been systematically invest…

## 🧪 仿真 / Sim2Real (1 篇)

### 1. Embedded Sim-to-Real Visual Servoing: Learned Reaching and Force-Guided Placement

- **arXiv**: [2611.15658v1](https://arxiv.org/abs/2611.15658v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.15658v1)
- **作者**: Dezhi Sun, Duy Khang Banh, Kenan Niu
- **发表**: 2026-11-11  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Embedded perception-to-control systems must combine visual targeting with reliable contact handling under tight computational constraints. We present a shared architecture on an NVIDIA Jetson AGX Orin controlling a Franka Research 3 through Cartesian impedance control. RealSense D435i observations, YOLO11-seg segmentation, depth back-projection, and hand--e…

## 🤏 软体机器人 / 柔性控制 (6 篇)

### 1. PneuGen: Task-Driven Agentic Co-Design of Soft Pneumatic Robots

- **arXiv**: [2611.13344v1](https://arxiv.org/abs/2611.13344v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.13344v1)
- **作者**: Shaohong Zhong, Marco Pontin, Perla Maiolino
- **发表**: 2026-11-09  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Task-driven design of soft robots requires the consideration of factors such as geometry, morphology, material properties, and actuation, resulting in a large and complex design space that is challenging to explore. Computational optimisation methods leverage signals from simulation to iteratively improve designs to achieve task objectives. However, these m…

### 2. Accelerated Reinforcement Learning for Soft Robotics: Hours Instead of Years

- **arXiv**: [2611.11718v1](https://arxiv.org/abs/2611.11718v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.11718v1)
- **作者**: Roshan S. Kaundinya, Hehui Zheng, Robert K. Katzschmann et al.
- **发表**: 2026-11-09  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Reinforcement learning (RL) requires large amounts of interaction data or a reliable simulator, both hard to obtain for nonlinear soft robotic hardware. Recent work shows that a time-scale separation inherent to soft robot dynamics justifies their reduction to low-dimensional invariant manifolds, known as adiabatic spectral submanifolds (aSSMs). We demonstr…

### 3. Actuation and Control of Passive Tendon-Driven Soft Extensions Through Rigid Manipulator Motion

- **arXiv**: [2611.15386v1](https://arxiv.org/abs/2611.15386v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.15386v1)
- **作者**: Ignacio Cuiral-Zueco, Gonzalo López-Nicolás, Youcef Mezouar
- **发表**: 2026-11-11  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Industrial manipulators offer reach and precision but can damage nearby structures in confined spaces. Soft robots provide compliant contact but typically have limited reach. Rigid-soft systems combine their advantages, although they often require dedicated actuation and control hardware. We propose actuating a passive tendon-driven soft extension through m…

### 4. SunLightBots: Turning sunlight into self-sustained, high-power motion in soft robots

- **arXiv**: [2611.14729v1](https://arxiv.org/abs/2611.14729v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.14729v1)
- **作者**: Yoo Jin Lee, Melanie Torres Crespo, Zhongxiao Deng et al.
- **发表**: 2026-11-10  ·  **类别**: cs.RO, cond-mat.soft, physics.app-ph
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Soft robots built from active materials can directly convert environmental stimuli into motion, offering a route to energy autonomy and embodied control. However, environmental energy is generally harvested at low power, whereas rapid, mechanically demanding actions require high mechanical output power. Reconciling this mismatch while sustaining self-regula…

### 5. DeepSoMo: Deformable Object Motion Estimation under Proprioceptive Partial Observability via Predictive Latent Dynamics

- **arXiv**: [2611.11242v1](https://arxiv.org/abs/2611.11242v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.11242v1)
- **作者**: Hanwen Zhao, Weicheng Dai, Luoyao Chen et al.
- **发表**: 2026-11-08  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Estimating the motion of deformable bodies in soft robotics from proprioceptive sensing is challenging due to partial observability, as internal observations provide only indirect access to global motion, contact, and shape evolution. In such settings, instantaneous observations are insufficient, and accurate estimation requires temporally consistent latent…

### 6. $\mathcal{C}^\infty$ Smooth Trajectory Planning with Application to Soft Robots

- **arXiv**: [2611.05615v1](https://arxiv.org/abs/2611.05615v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.05615v1)
- **作者**: Reinhard M. Grassmann, Abdulaziz Y. Alkayas, Lingyun Chen et al.
- **发表**: 2026-11-03  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: High motion performance and avoiding structural vibrations rely on smooth trajectory planning. The smoothness requirement depends on the robot's complexity in terms of the number of degrees of freedom and system order due to the flexibility of the joints and links. For industrial robots, the smoothness requirements have been determined and subsequently take…

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
1. [PolyMorphWBC: Whole-Body Control from End-Effector Trajectories for Quadrupedal Mobile Manipulation across Arm Morphologies with Extended Reach](https://arxiv.org/abs/2611.15117v1) — score 20
2. [Decoupled Asynchronous System for Humanoids (DASH): Latency-Agnostic Scaling of Vision-Language-Action Models for Humanoid Manipulation](https://arxiv.org/abs/2611.11854v2) — score 18
3. [Learning Heterogeneous Tactile Representation for General Dexterous Manipulation](https://arxiv.org/abs/2611.12806v1) — score 17

> 筛选说明:本次 Top 3 已排除(已研读跳过 1 篇、综述跳过 1 篇)。

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
