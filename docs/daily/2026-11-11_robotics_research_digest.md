# 机器人研究每日摘要 · 2026-11-11

> 自动生成,共 113 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (8 篇)

### 1. Where Should Models Run? A Collaborative Inference Framework for Embodied Intelligence in 6G

- **arXiv**: [2611.11023v1](https://arxiv.org/abs/2611.11023v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.11023v1)
- **作者**: Wanlu Sun, Zhenhui Yuan, Xiang Ji et al.
- **发表**: 2026-11-07  ·  **类别**: cs.LG, cs.AI
- **相关性评分**: 13  ·  **📚 综述(归档备查,按协议 §4 不深读)**
- **摘要**: Embodied intelligence systems rely on fast and reliable inference to enable real-time perception, reasoning, and control. Recent advances in large-scale artificial intelligence (AI) models, including Large Language Models (LLMs) and Vision-Language-Action (VLA) models, have significantly enhanced the capabilities of embodied agents in complex environments.…

### 2. VLA-MOPD: On-Policy Distillation for Multi-Task VLA Policy Consolidation

- **arXiv**: [2611.12286v1](https://arxiv.org/abs/2611.12286v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.12286v1)
- **作者**: Yongxuan Lv, Zhen Fang, Lichen Man et al.
- **发表**: 2026-11-09  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Physical intelligence requires embodied agents to ground language in observations and execute actions while retaining useful skills. Vision-language-action (VLA) policies offer a shared interface, but task-specific post-training often produces separate specialists. Consolidation is difficult: mixed-task reinforcement learning provides sparse trajectory-leve…

### 3. Motion Belief Action: From a Visual Scene Map to Physical Decisions

- **arXiv**: [2611.12113v1](https://arxiv.org/abs/2611.12113v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.12113v1)
- **作者**: Dibyendu Ghosh
- **发表**: 2026-11-09  ·  **类别**: cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: A robot that works among people must judge what it cannot see: whether an object is still where it was last seen, and whether a pull on a door or drawer is worth its risk. Maps that track object change hold nothing about force, maps of physical properties answer a risk question at a fixed risk level, and vision-language-action models keep no explicit estima…

### 4. Be My Eye: Learning to See Beyond a Robot's Own Perspective

- **arXiv**: [2611.12295v1](https://arxiv.org/abs/2611.12295v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.12295v1)
- **作者**: Baifu Huang, Shilin Fang, Jianan Wang
- **发表**: 2026-11-09  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 9  ·  **📚 综述(归档备查,按协议 §4 不深读)**
- **摘要**: Robots operating in the real world are inherently subject to partial observability, particularly in multi-robot collaboration, where individual observations may be insufficient for effective task execution. A key challenge is leveraging complementary observations from partner robots to support collaborative decision-making. We argue that information sharing…

### 5. When Delay Meets Drift: Physical Safety of Robot Foundation Models Is a Cross-Layer Problem

- **arXiv**: [2611.02101v1](https://arxiv.org/abs/2611.02101v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.02101v1)
- **作者**: Liangkai Liu, Bimal Thapa Magar
- **发表**: 2026-11-01  ·  **类别**: cs.RO, cs.CV, cs.ET
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Robot foundation models now act in a closed loop, yet their safety is evaluated one variation at a time: robustness benchmarks perturb the scene while assuming instantaneous inference, and real-time execution methods study inference delay in nominal scenes. We argue that physical safety is not a property of the model alone, but emerges from how variations i…

### 6. La-JEPA: Compact Robot Policies with Latent World Modeling

- **arXiv**: [2611.08156v1](https://arxiv.org/abs/2611.08156v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.08156v1)
- **作者**: Mateo Clémente, George Z. Xue, Amin Abyaneh et al.
- **发表**: 2026-11-05  ·  **类别**: cs.RO, cs.CV, cs.LG
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: World-action models adapt pretrained video generators, and vision-language-action models build on pretrained vision-language backbones; both tie policy architecture and inference cost to large transformers designed for generation rather than control. It remains unclear how much these generation-oriented choices affect control. In this work, we introduce Lat…

### 7. Editing the Goal: Per-Token SAE Steering and Its Depth Limits in $π_{0.5}$

- **arXiv**: [2611.00602v1](https://arxiv.org/abs/2611.00602v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.00602v1)
- **作者**: Rocio Perales Valdes, Animesh Garg
- **发表**: 2026-10-31  ·  **类别**: cs.AI
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Sparse autoencoders (SAEs) have recovered interpretable, causally relevant features in robot foundation models (RFMs) such as $π_{0.5}$ (arXiv:2603.19183, arXiv:2603.19233). SAE features on individual instruction tokens are less interpretable than timestep-pooled ones (arXiv:2603.19183), and whether they can redirect a robot's goal remains untested. We show…

### 8. DeltaForge: A Post-hoc Mixture-of-Experts VLA for Multi-Domain Autonomous Driving

- **arXiv**: [2611.11856v1](https://arxiv.org/abs/2611.11856v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.11856v1)
- **作者**: Bingzhang Wang, Mo Poorsartep, Yasaman Esfandiari
- **发表**: 2026-11-09  ·  **类别**: cs.LG, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Fleets of driving vision-language-action (VLA) models are developed one domain at a time: each operator finetunes a shared base model on private data, producing specialized experts that are costly to consolidate into a single model. Weight merging loses accuracy as heterogeneous domains accumulate, and dense mixture-of-experts routing is prohibitively expen…

## 🌐 具身智能 / 机器人基础模型 (9 篇)

### 1. Learning the Task or Learning the Verifier? Rethinking Criteria Exposure in Embodied Self-Improvement

- **arXiv**: [2611.08318v1](https://arxiv.org/abs/2611.08318v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.08318v1)
- **作者**: Wenbo Huang, Jianxin Bi, Shunyu Yang et al.
- **发表**: 2026-11-05  ·  **类别**: cs.AI, cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Self-improving embodied agents are increasingly being developed and compared on robot simulation benchmarks. Several recent works expose the benchmark's success criteria to the learning agent, a practice we call Criteria Exposure (CE). These criteria, originally written to verify policies trained by imitation learning, often demand more than the correspondi…

### 2. Review the Episodes, Refine the Lessons: Simple Memory Evolution for Embodied Agents

- **arXiv**: [2611.11509v1](https://arxiv.org/abs/2611.11509v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.11509v1)
- **作者**: Yifei Yao, Yude Zou, Xing Gao et al.
- **发表**: 2026-11-08  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 8  ·  **📚 综述(归档备查,按协议 §4 不深读)**
- **摘要**: Recent studies of embodied agents based on frontier multimodal large language models (MLLMs) develop harness engineering around the MLLM, such as harnesses with post-trained policies and recursive self-improvement loops. Yet whether these additions exceed the native capability of the MLLM remains unexplored. We introduce SimplEvo to explore how far an MLLM…

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

### 5. WanderBench: Can World Models Explore Dynamic Worlds from Video?

- **arXiv**: [2611.12557v1](https://arxiv.org/abs/2611.12557v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.12557v1)
- **作者**: Yuhang Chen, Jiheng Li, Jiale Wang et al.
- **发表**: 2026-11-09  ·  **类别**: cs.CV, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Video world models conditioned on an input video make it possible to explore real, recorded dynamic scenes, enabling re-shooting of footage, free-viewpoint replay, and real-to-sim environments for embodied agents. Such uses require the generated rollout to stay faithful to the recorded world, yet existing benchmarks start from a single image or a text promp…

### 6. Reinforcement Learning Enables Scaling Generalist Robot Policy Improvement

- **arXiv**: [2611.06905v1](https://arxiv.org/abs/2611.06905v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.06905v1)
- **作者**: Michal Korniak, Marco Bagatella, Ralf Römer et al.
- **发表**: 2026-11-04  ·  **类别**: cs.LG, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: The introduction of generalist robot policies has enabled a single, large model to learn to perform a variety of tasks from a vast pre-training corpus. While these models often exhibit powerful zero-shot generalization capabilities, they typically require an adaptation phase to achieve sufficient performance in deployment. Iterated self-improvement via rein…

### 7. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

### 8. Confidence-Modulated Safety Filtering for End-to-End Policies

- **arXiv**: [2610.40922v1](https://arxiv.org/abs/2610.40922v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.40922v1)
- **作者**: Javier Borquez, Jaime F. Fisac
- **发表**: 2026-10-29  ·  **类别**: cs.RO, eess.SY
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: End-to-end policies, from task-specific controllers to robot foundation models, learn complex behavior from raw observations but are not guaranteed to remain safe, so they are often wrapped in a safety filter. The resulting system operates under two domains: the filter's operational design domain (ODD), where its assumptions hold and safety is certified, an…

### 9. FoundationVIO: Enforcing Metric Scale in Feed-forward Visual-Inertial Odometry

- **arXiv**: [2610.14951v1](https://arxiv.org/abs/2610.14951v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.14951v1)
- **作者**: Jin Rhee, Yuhao Zhang, Frank Dellaert et al.
- **发表**: 2026-10-10  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Feed-forward geometric foundation models (GFMs) directly predict dense geometry and camera poses from batches of images. Emerging visual SLAM methods chain together consecutive GFM batches to form dense point cloud maps. A core challenge is how to address the ambiguous geometric scale of GFM predictions: independent predictions are locally consistent up-to-…

## 🦵 人形 / 足式机器人 (30 篇)

### 1. Decoupled Asynchronous System for Humanoids (DASH): Latency-Agnostic Scaling of Vision-Language-Action Models for Humanoid Manipulation

- **arXiv**: [2611.11854v1](https://arxiv.org/abs/2611.11854v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.11854v1)
- **作者**: Bingzhang Wang, Nathan Zhao, Jialeng Ni et al.
- **发表**: 2026-11-09  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models pair a vision-language backbone with an action head, but in closed-loop control the backbone sits on the control-critical path: while it computes, the robot keeps moving, so each executed action is conditioned on an increasingly stale observation. A larger backbone therefore directly blocks reactivity, especially in human…

### 2. SUGARv2: Learning Diverse Visual Humanoid Loco-Manipulation Skills from Synthesized Interaction References

- **arXiv**: [2611.09266v1](https://arxiv.org/abs/2611.09266v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.09266v1)
- **作者**: Tianshu Wu, Tianxiang Gui, Yue Chen et al.
- **发表**: 2026-11-06  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Scaling up visual humanoid loco-manipulation skill acquisition requires reducing the human effort needed as tasks and spatial configurations expand, particularly in demonstration collection and task-specific training design. We present SUGARv2, a unified framework for learning diverse visual humanoid loco-manipulation skills through interaction reference sy…

### 3. Embodied First Exam

- **arXiv**: [2611.12177v1](https://arxiv.org/abs/2611.12177v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.12177v1)
- **作者**: Kangrui Wang, Qineng Wang, Changhe Chen et al.
- **发表**: 2026-11-09  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Early successes on agentic robotics point to a potential paradigm shift toward using coding agents to control robots. Existing robotics benchmarks are built around visuomotor policy learning, leaving it open whether coding agents can reliably control diverse robots under physical-world constraints. We therefore introduce the Embodied First Exam, a unified,…

### 4. From Tabletop to Walking Bot: Deploying a VLA Model on a Legged Manipulator Robot

- **arXiv**: [2610.32271v1](https://arxiv.org/abs/2610.32271v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.32271v1)
- **作者**: Giovanni Minelli, Antonio Langella, Giovanni B. Dessy et al.
- **发表**: 2026-10-23  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models are typically pretrained on broad, diverse datasets and subsequently fine-tuned on a comparatively small dataset tailored to a specific target robot. Such adaptation recipe is now widely established, achieving its most mature results on fixed-base arms due to their static base dynamics and consistent reference frame. Moun…

### 5. Zero-Shot VLA Adaptation with Retrieved Guidance

- **arXiv**: [2611.10894v1](https://arxiv.org/abs/2611.10894v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.10894v1)
- **作者**: Subin Kim, Anh-Quan Pham, Dinesh Jayaraman
- **发表**: 2026-11-07  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Pre-training large parametric "Vision-Language-Action" (VLA) models on large demonstration datasets has recently yielded promising results for general-purpose manipulation. However, these models still struggle under even small domain shifts relative to the training data, such as changes in camera viewpoint, background, object identity, or robot morphology.…

### 6. STRIDE: Learning Humanoid Locomotion in Minutes with Acceleration-Based Rewards

- **arXiv**: [2611.08857v1](https://arxiv.org/abs/2611.08857v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.08857v1)
- **作者**: Nico Bohlinger, Jan Peters
- **发表**: 2026-11-06  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Learning locomotion directly on a humanoid robot is a promising direction to avoid the sim-to-real gap. However, locomotion rewards in Reinforcement Learning (RL) typically track the base velocity, which cannot be measured onboard without an external motion capture system or well-calibrated state estimator. This is why we introduce \method{}, which learns h…

### 7. DKWBC: Decoupling Motion Tracking and Balancing for Humanoid Whole-Body Control

- **arXiv**: [2611.09605v1](https://arxiv.org/abs/2611.09605v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.09605v1)
- **作者**: Dingkun Wei, Zehong Shen, Huaijin Pi et al.
- **发表**: 2026-11-06  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Humanoid whole-body control requires a robot to track diverse reference motions while maintaining balance under gravity, torque limits, contact switching, and external disturbances. Existing reinforcement-learning-based trackers typically learn control outputs that jointly address motion tracking and balance. However, similar reference poses can correspond…

### 8. HLO-AMP: Hierarchical Loco-Manipulation from Object-Aware Motion Priors

- **arXiv**: [2611.05113v1](https://arxiv.org/abs/2611.05113v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.05113v1)
- **作者**: Jean-Pierre Sleiman, Bilal Hammoud, He Li et al.
- **发表**: 2026-11-03  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Hierarchical pipelines for humanoid loco-manipulation typically pair a task-agnostic whole-body controller (WBC) with a downstream task policy. Such WBCs are often trained through manual reward shaping, which yields visibly machine-like motions; more consequentially, they are trained without the manipulated object in the scene. Object dynamics are instead a…

### 9. E2DRL: End-to-End Differentiable Reinforcement Learning for 3D Obstacle Avoidance in Quadruped Robots

- **arXiv**: [2610.19627v1](https://arxiv.org/abs/2610.19627v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19627v1)
- **作者**: Cheng Fan, Bingyang Zhou, Gang Yang et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Differentiable reinforcement learning shows strong promise for robot policy learning, but its application to legged locomotion has remained limited to blind walking or simulated 2D tasks. Extending it to end-to-end visual obstacle avoidance is challenging because hard collision constraints and early termination upon contact corrupt first-order gradients, tr…

### 10. OccluDex: Hierarchical 3D Visuo-Tactile Representation Learning for Egocentric Dexterous Manipulation under Self-Occlusion

- **arXiv**: [2609.39017v1](https://arxiv.org/abs/2609.39017v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39017v1)
- **作者**: Ziheng Xu, Yueyuan Chen, Xinyuan He et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Reliable dexterous manipulation requires continuous estimation of object geometry and hand-object contact throughout interaction. With egocentric sensing, however, the manipulating hand frequently occludes task-relevant object surfaces and contact regions, reducing the visual evidence available for state estimation and thereby making robust closed-loop cont…

## 🦾 操控 / 灵巧手 / 抓取 (35 篇)

### 1. GUARD: Anomaly-Informed Q-Steering for Generative Robot Policies in Dexterous Manipulation

- **arXiv**: [2611.10343v1](https://arxiv.org/abs/2611.10343v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.10343v1)
- **作者**: Aryaman Gupta, Xiaoyue Wu, Rana Soltani Zarrin et al.
- **发表**: 2026-11-07  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Generative robot policies based on diffusion and flow matching can model complex, multimodal behaviors, but remain susceptible to covariate shift during closed-loop execution. Existing approaches mitigate such failures through additional demonstrations, policy fine-tuning, or test-time guidance, but often require human intervention, engineered rewards, or o…

### 2. TactileLab: Sim-to-Real Dexterous Robot Manipulation with Efficient Shear-Sensitive Tactile Simulation

- **arXiv**: [2611.07881v1](https://arxiv.org/abs/2611.07881v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.07881v1)
- **作者**: Yijiong Lin, Wenhao He, Toby Jack et al.
- **发表**: 2026-11-05  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Robotic simulators that represent shear within tactile sensing are becoming increasingly important for contact-rich manipulation. However, simulating contact shear with high-fidelity deformable or soft-body simulation is computationally demanding, limiting scalability to large-scale reinforcement learning. Here we introduce \textit{TactileLab}, a scalable m…

### 3. Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation

- **arXiv**: [2611.05979v1](https://arxiv.org/abs/2611.05979v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.05979v1)
- **作者**: Zhengdong Hong, Guofeng Zhang
- **发表**: 2026-11-04  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Manipulating diverse objects with multi-fingered dexterous hands is challenging due to the high dimensionality and complex dynamics. Human-Object Interaction (HOI) datasets provide rich knowledge about task information and embodied interactions. Instead of solely imitating the human demonstrations, our method learns to holistically predict future hand-objec…

### 4. Learning Heterogeneous Tactile Representation for General Dexterous Manipulation

- **arXiv**: [2611.12806v1](https://arxiv.org/abs/2611.12806v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.12806v1)
- **作者**: Bing Han, Yichuan Peng, Haoyu Dong et al.
- **发表**: 2026-11-09  ·  **类别**: cs.RO
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: Tactile sensing is an indispensable modality for contact-rich dexterous manipulation, a capability that hints at the ultimate frontiers of embodied intelligence. However, commercially available tactile sensors are still at a relatively early stage of development, with each type of sensor offering irreplaceable strengths alongside its own drawbacks. A key ch…

### 5. Thermo-VLA: A Thermal-Aware Vision-Language-Action Model with Gated Residual Modulation for Robotic Manipulation

- **arXiv**: [2611.11981v1](https://arxiv.org/abs/2611.11981v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.11981v1)
- **作者**: Jingxuan Chen, Junshi Luo, Chencheng Dong et al.
- **发表**: 2026-11-09  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Recent Vision-Language-Action (VLA) models have begun incorporating thermal sensing, but existing approaches typically treat thermal images as ordinary visual inputs, providing limited support for temperature-aware relational reasoning in manipulation. To address this limitation, we propose Thermo-VLA with a ThermoRes Encoder, which decomposes thermal image…

### 6. RevoSim: Scalable Multimodal Tactile Simulation for Dexterous Manipulation

- **arXiv**: [2611.08939v1](https://arxiv.org/abs/2611.08939v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.08939v1)
- **作者**: Ke Zhang, Lixin Xu, Ziyi Wang et al.
- **发表**: 2026-11-06  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: We present RevoSim, a scalable and high-fidelity multimodal tactile simulator for the BrainCo Revo3 hand that jointly models 285 piezoresistive taxels and five visuotactile fingertips. RevoSim efficiently generates synchronized pressure, depth, RGB, and marker-displacement observations; on a single RTX 5090, its depth-conditioned marker-displacement configu…

### 7. DexHOT: Learning Hand-Object Configuration Transfer for Dexterous Manipulation

- **arXiv**: [2611.05119v2](https://arxiv.org/abs/2611.05119v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.05119v2)
- **作者**: Zhewei Gui, Anthony Bolton, Jiyao Zhang et al.
- **发表**: 2026-11-03  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation involves not only moving objects, but also arranging the hand around them to maintain useful contacts and enable subsequent actions. Yet many learning-based systems specify goals primarily through object poses or trajectories, leaving hand-object configurations to emerge implicitly. We introduce DexHOT, which formulates dexterous mani…

### 8. SoTa: Soft Tactile Skins for Dexterous Manipulation

- **arXiv**: [2610.02338v1](https://arxiv.org/abs/2610.02338v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.02338v1)
- **作者**: Jingyun Yang, Baiyu Shi, Timothy Yu et al.
- **发表**: 2026-10-01  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: A growing body of work suggests that tactile sensing gives robot policies contact information that complements vision in dexterous manipulation. However, visuo-tactile robot data remains scarce: dexterous demonstrations require teleoperating robots, which limits dataset scale. Human demonstrations are far cheaper to collect and offer a path to scale this da…

### 9. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

### 10. PCTac: Mechanochromic Photonic-Crystal Tactile Sensor for Dexterous Manipulation

- **arXiv**: [2611.12383v1](https://arxiv.org/abs/2611.12383v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.12383v1)
- **作者**: Ruilin Zhang, Xuanshuo Liu, Junzhe Dai et al.
- **发表**: 2026-11-09  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Modern visuotactile sensors primarily sense contact by imaging the deformation of a compliant interface. Using techniques such as photometric stereo, they can recover detailed contact geometry, often represented as surface normals or depth. However, force-related information typically still needs to be inferred indirectly through calibration, geometric reco…

## 🎓 模仿学习 / 强化学习 (14 篇)

### 1. Bracketing Shows the Way: Adaptive Multi-Exposure Policy as Input for Robust Visual SLAM

- **arXiv**: [2610.33174v1](https://arxiv.org/abs/2610.33174v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.33174v1)
- **作者**: Olivier Gamache, Anthony Lavertu, David-Alexandre Duclos et al.
- **发表**: 2026-10-23  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Rapid illumination transitions can disturb Visual SLAM (VSLAM) by saturating images before the Automatic Exposure (AE) policy adapts, removing the visual correspondences needed to maintain tracking. Our proposed methods mitigate this disturbance at two levels: B-Adapt acquires adaptive exposure brackets to cover the scene dynamic range while promoting photo…

### 2. DPGS-SLAM: Diffusion-Prior and Provenance-Aware Monocular Gaussian Splatting SLAM for Dynamic Visual Sensing

- **arXiv**: [2611.12038v1](https://arxiv.org/abs/2611.12038v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.12038v1)
- **作者**: Yifan Luo, Takafumi Matsumaru, Vibekananda Dutta et al.
- **发表**: 2026-11-09  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: This paper presents DPGS-SLAM (Diffusion-Prior and Provenance-Aware Monocular Gaussian Splatting SLAM) for dense mapping in environments containing dynamic objects. Dynamic observations can contaminate camera tracking and scene reconstruction in visual SLAM (simultaneous localization and mapping). Although 3DGS (3D Gaussian splatting) enables efficient dens…

### 3. RingNav: Task-Shaped Circular Memory for Visual Heading

- **arXiv**: [2610.19044v1](https://arxiv.org/abs/2610.19044v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19044v1)
- **作者**: Naitri Rajyaguru, Aryan Tajne, Stephen Jardim et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Tiny robots have limited computation and memory, yet visual navigation systems often maintain more state than a task requires. We ask whether persistent memory can instead be shaped by the task. We present \textbf{RingNav}, a \(10.6\)k--parameter visual heading estimator that constrains its memory to the circular manifold \(S^1\). RingNav learns only the tu…

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

### 8. Probably Safe Sim-to-Real Transfer with Lifetime Validity

- **arXiv**: [2611.09344v1](https://arxiv.org/abs/2611.09344v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.09344v1)
- **作者**: Rohan Tangri, Jan-Peter Calliess
- **发表**: 2026-11-06  ·  **类别**: cs.LG
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: We present Dejavu, a method that makes sim-to-real transfer of reinforcement learning policies in constrained Markov decision processes probably safe over an unbounded sequence of policy updates. An anytime valid test using per-decision importance sampling and a betting confidence sequence certifies each candidate trained in simulation before deployment usi…

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

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (10 篇)

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

### 9. Parameter Sensitivity Analysis for Aerial LiDAR-Inertial Odometries in low-altitude flights

- **arXiv**: [2609.12837v1](https://arxiv.org/abs/2609.12837v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.12837v1)
- **作者**: Robert Milijas, Jose Ramiro Martinez-de Dios, Stjepan Bogdan
- **发表**: 2026-09-11  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: LiDAR-based SLAM (Simultaneous Localization and Mapping) and LIO (LiDAR-inertial odometry) algorithms are often used for precise navigation of unmanned aerial vehicles, especially during interactions with the aerial robot's environment. However, the performance of these algorithms is greatly dependent on the scenario, LiDAR, and robot motion characteristics…

### 10. Geodesic Flow Matching for Denoising High-Dimensional Structured Representations

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

### 1. VeV: Video-Enhanced Vibration Data Augmentation For Structural Difference

- **arXiv**: [2611.10257v1](https://arxiv.org/abs/2611.10257v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.10257v1)
- **作者**: Joonhee Lee, Jiale Zhang, Sungmin Lee et al.
- **发表**: 2026-11-06  ·  **类别**: cs.HC, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Surface-mounted vibration sensing provides non-invasive structural monitoring with high temporal fidelity across diverse ubiquitous computing scenarios such as smart farms, yet structure-borne wave models remain fragile to physical relocation and structural shifts. However, addressing this spatial data discontinuity remains limited by costly manual recalibr…

## 🤏 软体机器人 / 柔性控制 (4 篇)

### 1. SomaAlign: Reliability-Aware Multimodal Representation Learning for Soft Robotic Grasping

- **arXiv**: [2611.02794v1](https://arxiv.org/abs/2611.02794v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.02794v1)
- **作者**: Haoyuan Wang, Shuai Peng, Yongkai Liao et al.
- **发表**: 2026-11-02  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Robust multimodal perception for soft robotic grasping is challenged by modality-dependent noise, semantic ambiguity, and limited coordinated multisensory data. We introduce Soma, a dataset containing 100 objects, 1,000 continuous grasping trajectories, and 74,914 multimodal samples grouped by software acquisition cycle, spanning remote RGB, hand RGB, depth…

### 2. Accelerated Reinforcement Learning for Soft Robotics: Hours Instead of Years

- **arXiv**: [2611.11718v1](https://arxiv.org/abs/2611.11718v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.11718v1)
- **作者**: Roshan S. Kaundinya, Hehui Zheng, Robert K. Katzschmann et al.
- **发表**: 2026-11-09  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Reinforcement learning (RL) requires large amounts of interaction data or a reliable simulator, both hard to obtain for nonlinear soft robotic hardware. Recent work shows that a time-scale separation inherent to soft robot dynamics justifies their reduction to low-dimensional invariant manifolds, known as adiabatic spectral submanifolds (aSSMs). We demonstr…

### 3. DeepSoMo: Deformable Object Motion Estimation under Proprioceptive Partial Observability via Predictive Latent Dynamics

- **arXiv**: [2611.11242v1](https://arxiv.org/abs/2611.11242v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.11242v1)
- **作者**: Hanwen Zhao, Weicheng Dai, Luoyao Chen et al.
- **发表**: 2026-11-08  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Estimating the motion of deformable bodies in soft robotics from proprioceptive sensing is challenging due to partial observability, as internal observations provide only indirect access to global motion, contact, and shape evolution. In such settings, instantaneous observations are insufficient, and accurate estimation requires temporally consistent latent…

### 4. $\mathcal{C}^\infty$ Smooth Trajectory Planning with Application to Soft Robots

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
1. [GUARD: Anomaly-Informed Q-Steering for Generative Robot Policies in Dexterous Manipulation](https://arxiv.org/abs/2611.10343v1) — score 19
2. [TactileLab: Sim-to-Real Dexterous Robot Manipulation with Efficient Shear-Sensitive Tactile Simulation](https://arxiv.org/abs/2611.07881v1) — score 19
3. [Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation](https://arxiv.org/abs/2611.05979v1) — score 19

> 筛选说明:本次 Top 3 已排除(已研读跳过 1 篇、综述跳过 4 篇)。

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
