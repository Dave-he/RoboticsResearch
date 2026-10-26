# 机器人研究每日摘要 · 2026-10-27

> 自动生成,共 105 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (7 篇)

### 1. HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games

- **arXiv**: [2610.31162v1](https://arxiv.org/abs/2610.31162v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.31162v1)
- **作者**: Zecong Tang, Zian Guan, Yuncheng Guo et al.
- **发表**: 2026-10-22  ·  **类别**: cs.CV
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Building virtual embodied agents that operate in open-ended games like human players is a long-standing goal requiring both long-horizon autonomy and reliable native-interface control. As a procedurally generated open world, Minecraft provides a natural testbed for studying the integration of these capabilities. Existing agents typically provide either nati…

### 2. Multi-Dimensional Featurizers Yield Fine-Grained Steering and Data Shaping in Robot Foundation Models

- **arXiv**: [2610.20767v1](https://arxiv.org/abs/2610.20767v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20767v1)
- **作者**: Aiden Swann, Mozes Jacobs, Mathilde Papillon et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Can better feature discovery improve control over robot behavior through internal interventions and training data? Recent work in vision and language models reveals multidimensional features, motivating block-sparse featurizers (BSFs), which represent each feature in a low-dimensional subspace. We investigate whether recovering this structure provides an in…

### 3. When to Stop Penalizing Actions? Martingale GRPO for VLA Reinforcement Learning

- **arXiv**: [2610.32431v1](https://arxiv.org/abs/2610.32431v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.32431v1)
- **作者**: Zongyao Zhao, Cheng-Jie Zhao, Ruihang Jiang et al.
- **发表**: 2026-10-23  ·  **类别**: cs.AI
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: A failed vision-language-action (VLA) rollout does not imply that every action contributed to failure. Yet in group-relative policy optimization (GRPO), a single trajectory-level advantage is assigned to all actions in a rollout. Potentially useful recovery attempts can thus be penalized alongside the errors they aim to correct. Ideal stopping conditions fo…

### 4. Do VLAs Know They Will Fail? Interpretable Success and Failure Patterns in Physical AI Systems

- **arXiv**: [2610.32208v1](https://arxiv.org/abs/2610.32208v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.32208v1)
- **作者**: Christian A. Rogers, Qian Lin, Daniel S. Brown
- **发表**: 2026-10-23  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Vision-Language-Action (VLA) models have emerged as powerful general-purpose robot policies, but their successes and failures remain difficult to diagnose and understand. In this work, we show that sparse autoencoder (SAE) representations of OpenVLA activations contain outcome-predictive information and can be used to predict task failure before the robot r…

### 5. Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success

- **arXiv**: [2610.31670v2](https://arxiv.org/abs/2610.31670v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.31670v2)
- **作者**: Yunfei Xie, Howard H. Qian, Shiyi Lan et al.
- **发表**: 2026-10-22  ·  **类别**: cs.CV, cs.LG, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Robot foundation models are typically evaluated through costly closed-loop rollouts, motivating low-cost offline proxies for model capability. The Platonic Representation Hypothesis (PRH) suggests that as representations improve, modalities such as vision and language converge toward a shared statistical model of reality. We ask whether motion trajectories…

### 6. When Human Corrections Travel: Safety in Federated VLA Adaptation

- **arXiv**: [2610.32888v1](https://arxiv.org/abs/2610.32888v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.32888v1)
- **作者**: Vigneshwaran Subbaraju, Obaidullah Zaland, Monowar Bhuyan
- **发表**: 2026-10-23  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-language-action (VLA) policies can adapt to local human intervention, while federated learning can combine distributed robot experience without pooling raw records. We examine their prospective intersection: sharing adaptations derived from diverse human corrections across tasks, environments, people, and robot embodiments. Corrections differ in moda…

### 7. Retiming Robot Demonstrations with a Learned Speed Prior

- **arXiv**: [2610.32676v1](https://arxiv.org/abs/2610.32676v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.32676v1)
- **作者**: Seungyong Moon, Deokjae Lee, Hansang Lee et al.
- **发表**: 2026-10-23  ·  **类别**: cs.AI, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: The pace of a robot demonstration is often determined by the teleoperator rather than by the task itself. As a result, the same motion can appear at widely different speeds across demonstrations, and policies trained on such data may inherit operator-specific timing along with task behavior. We propose to learn a speed prior directly from large-scale demons…

## 🌐 具身智能 / 机器人基础模型 (11 篇)

### 1. TARSphere: A Robot-Oriented Full-Stack Framework for Long-Horizon Embodied Agents in Evolving Physical and Social Environments

- **arXiv**: [2610.30043v1](https://arxiv.org/abs/2610.30043v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30043v1)
- **作者**: Yicheng Xu, Zhikai Xu, Ziyuan Chen et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Robots must act under physical and social constraints while adapting to changes in their environment and human needs. Existing embodied-agent systems often focus on specified goals or abstract execution into symbolic actions, limiting evaluation in an evolving world. We introduce TARSphere, a robot-oriented full-stack framework for physically and socially g…

### 2. A Sparse Topometric Graph for Scalable Cross-Session Indoor Navigation

- **arXiv**: [2610.31432v1](https://arxiv.org/abs/2610.31432v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.31432v1)
- **作者**: Eun Sun Lee, Minkyun Seo, Gwangtak Bae et al.
- **发表**: 2026-10-22  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: A conventional embodied agent in an indoor environment builds a map by accumulating noisy real-world measurements and results from heavy inference to guide navigation. While the detailed measurements may differ due to scene changes or sensor settings, the unique topological structure of navigable passages or the connectivity between rooms may provide traini…

### 3. Know When to Escalate: Critic-Guided Adaptive Execution for Cloud-Local Embodied Agents

- **arXiv**: [2610.30587v1](https://arxiv.org/abs/2610.30587v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30587v1)
- **作者**: Wei Zhang, Lirong Xiang, Charles Fleming
- **发表**: 2026-10-22  ·  **类别**: cs.RO, cs.DC
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Recent advances in foundation-model agents have enabled increasingly capable embodied systems for long-horizon planning and interaction. However, embodied agents require fast, closed-loop decisions as they continuously perceive and act on a changing environment. Deploying strong cloud agents leaves the platform idle for seconds between consecutive actions,…

### 4. Externalise the Memory: A Pre-Registered Study of Where an Embodied Agent's Experience Should Live

- **arXiv**: [2610.30478v1](https://arxiv.org/abs/2610.30478v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30478v1)
- **作者**: Cheng-Yin Tu
- **发表**: 2026-10-21  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Should an embodied agent's experience be baked into its policy weights, or kept external and retrieved at inference? A memory-augmented teacher (a VLM that retrieves lessons, with their episode images, from its own past attempts) produces trajectories on a vision-conditioned reach task; from the same trajectories we distil LoRA student policies and evaluate…

### 5. Multimodal Embodied Agents: A Unified Capability-centric Perspective from Computer-Use to Robot-Use

- **arXiv**: [2610.30108v1](https://arxiv.org/abs/2610.30108v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30108v1)
- **作者**: Yanzhe Chen, Ziyi Yang, Jifeng Zhu et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 8  ·  **📚 综述(归档备查,按协议 §4 不深读)**
- **摘要**: Multimodal agents (MMAs) sustain interaction through reasoning, memory, tools, and feedback, most visibly as computer-use agents, while robotic systems (RSs) couple sensing and actuation under physical dynamics. We define multimodal embodied agents (MMEAs) as goal-directed systems that couple multimodal task reasoning with physical action and revise decisio…

### 6. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 7. SceneBloom: Agentic Indoor Environment Generation with Realistic and Diverse Layouts for Embodied Learning

- **arXiv**: [2610.32978v1](https://arxiv.org/abs/2610.32978v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.32978v1)
- **作者**: Yuhan Liu, Lianhui Qin, Shenji Wan
- **发表**: 2026-10-23  ·  **类别**: cs.CV, cs.AI, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Training generalizable embodied agents requires realistic, varied, and simulation-ready indoor environments. Language-guided methods support semantic planning and object-level reasoning, but precise spatial grounding remains difficult. Visual generative models offer rich priors over plausible arrangements, yet their outputs require geometric reasoning to be…

### 8. HGWM: Hierarchical Graph-Guided World Model for Zero-Shot Object Navigation via Graph Matching

- **arXiv**: [2610.32554v1](https://arxiv.org/abs/2610.32554v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.32554v1)
- **作者**: I-tak Ieong, Hao Tang
- **发表**: 2026-10-23  ·  **类别**: cs.RO, cs.MA
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Zero-shot object navigation requires an embodied agent to choose where to search while retaining evidence from previous observations. HGWM couples an LLM-generated room-anchor prior with persistent spatial-semantic memory. A coarse stage assigns visual-semantic scores to candidate headings on a 0-10 scale; a fine stage measures symbolic compatibility betwee…

### 9. PRISM: Learning Realistic Depth via Physics-Grounded Noise Disentanglement with Semantic-Geometric Collaboration

- **arXiv**: [2610.29432v1](https://arxiv.org/abs/2610.29432v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.29432v1)
- **作者**: Xiujian Liang, Jiacheng Liu, Mingyang Sun et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Real-world physical sensing exhibits complex, heterogeneous noise patterns that deviate significantly from idealized simulation, posing a fundamental bottleneck for sim-to-real transfer. Existing sensor modelings typically treat depth noise as a monolithic black-box process, overlooking the distinct physical mechanisms that govern different error modalities…

### 10. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

## 🦵 人形 / 足式机器人 (28 篇)

### 1. COWBOY: A Scalable Sim-to-Real Framework for Learning Contextual Whole-Body Manipulation

- **arXiv**: [2610.28948v1](https://arxiv.org/abs/2610.28948v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.28948v1)
- **作者**: Jiahui Yang, Jason Jingzhou Liu, Ray Muxin Liu et al.
- **发表**: 2026-10-20  ·  **类别**: cs.RO
- **相关性评分**: 21  ·  **✅ 已研读**
- **摘要**: Mobile manipulators must adapt not only to objects, but also to the spatial context in which they appear: where to position the base, how to manipulate, and where to look while navigating surrounding scene geometry. To address this, we present COWBOY, a scalable sim-to-real framework for learning such contextual whole-body manipulation. On whole-body dexter…

### 2. SP-HLM: Sparse-Pose-Driven Motion Generation and Whole-Body Control for Humanoid Loco-Manipulation

- **arXiv**: [2610.30044v1](https://arxiv.org/abs/2610.30044v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30044v1)
- **作者**: Zhaohui Yang, Quanbao Lin, Chengqi Shi et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 18  ·  **✅ 已研读**
- **摘要**: Humanoid loco-manipulation requires an effective interface between high-level task policies and whole-body control. Existing interfaces typically rely on a single action representation for both task intent and whole-body coordination. This may burden the high-level policy or leave one aspect underspecified. We present SP-HLM, a framework built on a sparse-p…

### 3. From Tabletop to Walking Bot: Deploying a VLA Model on a Legged Manipulator Robot

- **arXiv**: [2610.32271v1](https://arxiv.org/abs/2610.32271v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.32271v1)
- **作者**: Giovanni Minelli, Antonio Langella, Giovanni B. Dessy et al.
- **发表**: 2026-10-23  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models are typically pretrained on broad, diverse datasets and subsequently fine-tuned on a comparatively small dataset tailored to a specific target robot. Such adaptation recipe is now widely established, achieving its most mature results on fixed-base arms due to their static base dynamics and consistent reference frame. Moun…

### 4. Motion Retargeting with Spatiotemporal Preferences for Humanoid Loco-Manipulation

- **arXiv**: [2610.30540v1](https://arxiv.org/abs/2610.30540v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30540v1)
- **作者**: Xiongbo Shi, Shihang Du, Zongyou Yu et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Human motion retargeting bridges the embodiment gap between humans and humanoid robots by converting human demonstrations into reference trajectories for whole-body control and loco-manipulation. For object-interaction tasks, successful execution depends on accurately preserving body--object relations at critical stages. However, uniform per-frame iteration…

### 5. PHD-Hand: A Printable Humanoid Dexterous Hand with Linkage-Driven 3-DOA Digits

- **arXiv**: [2610.29030v1](https://arxiv.org/abs/2610.29030v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.29030v1)
- **作者**: Neel Adwani, Muhaiminul Islam Akash, Saffia Ouali et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Currently, dexterous humanoid robot hands are widely considered the final hardware bottleneck that hampers generalist robots from physically assisting people at home and work. As conventional tendon-driven designs suffer from high cost, demanding maintenance, poor reliability, and short durability, alternative linkage-driven designs have increasingly gained…

### 6. OccluDex: Hierarchical 3D Visuo-Tactile Representation Learning for Egocentric Dexterous Manipulation under Self-Occlusion

- **arXiv**: [2609.39017v1](https://arxiv.org/abs/2609.39017v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39017v1)
- **作者**: Ziheng Xu, Yueyuan Chen, Xinyuan He et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Reliable dexterous manipulation requires continuous estimation of object geometry and hand-object contact throughout interaction. With egocentric sensing, however, the manipulating hand frequently occludes task-relevant object surfaces and contact regions, reducing the visual evidence available for state estimation and thereby making robust closed-loop cont…

### 7. E2DRL: End-to-End Differentiable Reinforcement Learning for 3D Obstacle Avoidance in Quadruped Robots

- **arXiv**: [2610.19627v1](https://arxiv.org/abs/2610.19627v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19627v1)
- **作者**: Cheng Fan, Bingyang Zhou, Gang Yang et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Differentiable reinforcement learning shows strong promise for robot policy learning, but its application to legged locomotion has remained limited to blind walking or simulated 2D tasks. Extending it to end-to-end visual obstacle avoidance is challenging because hard collision constraints and early termination upon contact corrupt first-order gradients, tr…

### 8. Fast Motion Retargeting Pipeline for Scalable Humanoid Robot Learning

- **arXiv**: [2610.28470v1](https://arxiv.org/abs/2610.28470v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.28470v1)
- **作者**: Daniel Marew, Sangjun Park, Nisal Perera et al.
- **发表**: 2026-10-20  ·  **类别**: cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: While large-scale human motion capture datasets provide a rich source of demonstrations for humanoid robot learning, retargeting the diverse motions to different humanoid robots remains a nontrivial challenge. Existing kinodynamic trajectory optimization pipelines are computationally expensive and often require manual adjustments per motion. We present FRDV…

### 9. EmbodyHOI: Embodiment-Aware Generation of Hand-Object Interactions for Humanoid Dexterous Manipulation

- **arXiv**: [2610.27242v1](https://arxiv.org/abs/2610.27242v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.27242v1)
- **作者**: Chaitanya Chawla, Kartik Sharma, Ananya Bal et al.
- **发表**: 2026-10-19  ·  **类别**: cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Humanoid dexterous manipulation needs reference motions that are both semantically rich and kinematically feasible for the target robot. Text-conditioned hand-object interaction (HOI) generators supply diverse, language-specified demonstrations, but they synthesize motion in human (MANO) space. The embodiment gap is therefore deferred to post-hoc retargetin…

### 10. LocoManiLab: A Unified Testbed for Data, Policies, Controllers, and Deployment in Humanoid Loco-Manipulation

- **arXiv**: [2610.30876v2](https://arxiv.org/abs/2610.30876v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30876v2)
- **作者**: Dewei Wang, Jinrui Han, Jiyuan Shi et al.
- **发表**: 2026-10-22  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Humanoid robots must coordinate locomotion and manipulation in everyday environments, yet progress is difficult to assess across differing policies, controllers, and task settings. LocoManiLab provides an integrated testbed spanning data collection and generation, policy training, evaluation, and physical deployment. Its task suite covers 234 atomic and com…

## 🦾 操控 / 灵巧手 / 抓取 (29 篇)

### 1. Tactile-Based Robotic Manipulation: From Mechanics-Driven to Data-Driven Perspectives

- **arXiv**: [2610.30438v1](https://arxiv.org/abs/2610.30438v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30438v1)
- **作者**: Jingyi Xiang, Yixuan Wang, Wenzhen Yuan
- **发表**: 2026-10-21  ·  **类别**: cs.RO
- **相关性评分**: 20  ·  **📚 综述(归档备查,按协议 §4 不深读)**
- **摘要**: Tactile sensing provides robots with direct access to physical interactions at the contact interface, making it a critical modality for robust and dexterous manipulation. Over the past several decades, tactile-based manipulation research has evolved from mechanics-driven approaches, which explicitly interpret tactile signals through contact mechanics and ta…

### 2. SoTa: Soft Tactile Skins for Dexterous Manipulation

- **arXiv**: [2610.02338v1](https://arxiv.org/abs/2610.02338v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.02338v1)
- **作者**: Jingyun Yang, Baiyu Shi, Timothy Yu et al.
- **发表**: 2026-10-01  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: A growing body of work suggests that tactile sensing gives robot policies contact information that complements vision in dexterous manipulation. However, visuo-tactile robot data remains scarce: dexterous demonstrations require teleoperating robots, which limits dataset scale. Human demonstrations are far cheaper to collect and offer a path to scale this da…

### 3. DexPort: A Hand-Held Skill Interface for Dexterous Hand Data Collection

- **arXiv**: [2610.32969v1](https://arxiv.org/abs/2610.32969v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.32969v1)
- **作者**: Amber Xie, Jiawei Fu, Xiaofeng Guo et al.
- **发表**: 2026-10-23  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Collecting high-quality demonstrations remains a central bottleneck for learning dexterous manipulation. Teleoperation records executable robot actions, but it requires a complete robot setup and places the burden of coordinating many finger joints on the operator. Human demonstrations are easier to collect, but their motions must be estimated and retargete…

### 4. MAST-VLA: Skill-Conditioned Adaptation with Trajectory-Affordance Priors for Multi-Skill Robot Manipulation

- **arXiv**: [2610.32312v1](https://arxiv.org/abs/2610.32312v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.32312v1)
- **作者**: Jiachi Yang, Zhiyi Xu, Hongquan Zhang et al.
- **发表**: 2026-10-23  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Generalist robot manipulation requires a single vision-language-action (VLA) policy to execute diverse skills across scenes and instructions. However, current multi-skill VLA policies often leave two aspects of an instruction insufficiently modeled: which primitive skill to execute and where/how to contact and move objects. We propose MAST-VLA (Multi-skill…

### 5. PiHand: Latent Hand-Object Interaction Priors for Physics-Based Policy Learning

- **arXiv**: [2610.31299v1](https://arxiv.org/abs/2610.31299v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.31299v1)
- **作者**: Niklas Berndt, Xianghui Xie, Enes Duran et al.
- **发表**: 2026-10-22  ·  **类别**: cs.CV
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Synthesizing physically grounded dexterous hand-object interactions is important for VR/AR, gaming, and robotics, yet remains challenging because subtle contact dynamics, diverse object geometries, and target trajectories must be jointly respected while maintaining natural grasps. Existing methods either track mocap trajectories with limited transfer to nov…

### 6. In-Context Learning World Models for Robot Dual-Arm Manipulation of Soft Garment with Partial Observations

- **arXiv**: [2610.30988v1](https://arxiv.org/abs/2610.30988v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30988v1)
- **作者**: Hengyi Sim, Quentin Rouxel, Dennis Hong et al.
- **发表**: 2026-10-22  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Robust manipulation of soft objects, such as garments, is a critical skill for service and household robots to adopt, but remains challenging due to its high-dimensional state space, and material-dependent deformations. Humans address this challenge by using mental world models that "imagine" the shape and material properties from partial observations, whic…

### 7. Training in Deployment: Human-in-the-loop Online Post-Training for Robot Manipulation

- **arXiv**: [2610.29264v2](https://arxiv.org/abs/2610.29264v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.29264v2)
- **作者**: Chun Gu, Xiaofei Wei, Yiming Chen et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Large pretrained robot foundation models provide strong priors for manipulation, yet adapting them to target tasks with offline teleoperated demonstrations often fails to cover the contact-rich, recovery, and precision-critical states encountered during deployment. Existing methods mitigate this issue by augmenting offline demonstrations with human-in-the-l…

### 8. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

### 9. DeXplicit: Making Physical State Explicit in Dexterous Manipulation World Models

- **arXiv**: [2610.30781v1](https://arxiv.org/abs/2610.30781v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30781v1)
- **作者**: Adam Lee, Mutian Xu, Yukang Cao et al.
- **发表**: 2026-10-22  ·  **类别**: cs.CV
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Before acting on an object, a robot needs to anticipate how its hand motion will change the physical world and what the resulting scene will look like. Existing approaches typically entangle action-conditioned dynamics, camera motion, and visual synthesis within a video generation model, or represent dynamics as point trajectories without explicit object st…

### 10. Physical Words: A Vocabulary for Structuring Latent Reasoning in Robot Manipulation

- **arXiv**: [2610.26854v3](https://arxiv.org/abs/2610.26854v3)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.26854v3)
- **作者**: Jiaming Liu, Xinghao Zhu, Yiming Zhang et al.
- **发表**: 2026-10-19  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Multimodal reasoning provides robotic foundation models with predictive context needed for reliable action generation. However, language-based reasoning captures task semantics but struggles to express fine-grained physical dynamics, while latent reasoning models future state evolution but offers limited structure for organizing these dynamics into reusable…

## 🎓 模仿学习 / 强化学习 (14 篇)

### 1. NeuralSRender: G-Buffer Guided Video Diffusion for Sim-to-Real Rendering

- **arXiv**: [2610.29200v1](https://arxiv.org/abs/2610.29200v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.29200v1)
- **作者**: Yipeng Lu, Youqi Liao, Zhenyu Wang et al.
- **发表**: 2026-10-21  ·  **类别**: cs.CV
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: The scarcity of high-quality annotated visual data remains a critical bottleneck for autonomous-driving perception. Simulators provide training data at scale, but the limited realism of synthetic videos compromises perception performance in real-world applications. To address this limitation, we propose NeuralSRender, a sim-to-real video translation framewo…

### 2. Degeneracy-Orthogonal Geometric Constraints for LiDAR SLAM

- **arXiv**: [2609.36753v1](https://arxiv.org/abs/2609.36753v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.36753v1)
- **作者**: Minseo Kim, Yina Kim, Jinhwa Hwang et al.
- **发表**: 2026-09-29  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Autonomous robot navigation relies on simultaneous localization and mapping (SLAM) to estimate motion and maintain an accurate pose within an environment. However, in axially uniform corridors such as long tunnels and pipelines, LiDAR odometry is fundamentally limited by unconstrained drift along the feature-weak travel direction. This structural degeneracy…

### 3. RingNav: Task-Shaped Circular Memory for Visual Heading

- **arXiv**: [2610.19044v1](https://arxiv.org/abs/2610.19044v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19044v1)
- **作者**: Naitri Rajyaguru, Aryan Tajne, Stephen Jardim et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Tiny robots have limited computation and memory, yet visual navigation systems often maintain more state than a task requires. We ask whether persistent memory can instead be shaped by the task. We present \textbf{RingNav}, a \(10.6\)k--parameter visual heading estimator that constrains its memory to the circular manifold \(S^1\). RingNav learns only the tu…

### 4. Chain-SLAM: Globally Consistent Backend for Multi-Session LiDAR SLAM via Chained Loop Closure

- **arXiv**: [2609.12221v1](https://arxiv.org/abs/2609.12221v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.12221v1)
- **作者**: Zhiheng Li, Xinhao Liu, Juexiao Zhang et al.
- **发表**: 2026-09-10  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Maintaining consistency over long spatial and temporal horizons remains a fundamental challenge in large-scale LiDAR SLAM, particularly when integrating maps collected across multiple sessions. We present Chain-SLAM, a LiDAR SLAM backend enabling online multi-session map alignment and reuse with global consistency at large scale. We implement a chained loop…

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

### 7. Regularised RL improves sim-to-real transfer

- **arXiv**: [2610.32855v1](https://arxiv.org/abs/2610.32855v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.32855v1)
- **作者**: Danilo Vucetic, Mohamad H. Danesh, Florence Clerc et al.
- **发表**: 2026-10-23  ·  **类别**: cs.LG, cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Regularised reinforcement learning (RL) has provable robustness guarantees that should ease the transfer of policies from simulation to robots, known as sim-to-real. Yet, weakly regularised algorithms like Proximal Policy Optimisation (PPO) remain the de facto choice in sim-to-real pipelines, while the practical benefits of regularisation for transfer remai…

### 8. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 9. Improving Map Consistency in Graph-Based LiDAR SLAM Through Information-Aware Odometry and Retroactive Loop Closure

- **arXiv**: [2607.13516v1](https://arxiv.org/abs/2607.13516v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.13516v1)
- **作者**: Saurabh Gupta, Niklas Trekel, Louis Wiesmann et al.
- **发表**: 2026-07-15  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: High-quality maps are fundamental for robotics tasks such as navigation and planning. Although modern graph-based LiDAR SLAM systems achieve good trajectory accuracies, a low trajectory error alone does not guarantee geometrically consistent maps, particularly at revisit locations where missed loop closures and residual drift can produce local misalignments…

### 10. Unblur-SLAM: Dense Neural SLAM for Blurry Inputs

- **arXiv**: [2603.26810v1](https://arxiv.org/abs/2603.26810v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.26810v1)
- **作者**: Qi Zhang, Denis Rozumny, Francesco Girlanda et al.
- **发表**: 2026-03-26  ·  **类别**: cs.CV, eess.IV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We propose Unblur-SLAM, a novel RGB SLAM pipeline for sharp 3D reconstruction from blurred image inputs. In contrast to previous work, our approach is able to handle different types of blur and demonstrates state-of-the-art performance in the presence of both motion blur and defocus blur. Moreover, we adjust the computation effort with the amount of blur in…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (11 篇)

### 1. Evaluation of Front-End Feature Matching for Lunar Visual SLAM

- **arXiv**: [2610.30774v1](https://arxiv.org/abs/2610.30774v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30774v1)
- **作者**: Guillem Casadesus Vila, Grace Gao
- **发表**: 2026-10-22  ·  **类别**: cs.CV
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Lunar rovers will primarily rely on cameras for localization until navigation satellite services are deployed, and will continue to need them afterwards for relative navigation, hazard detection, and surface operations. Visual odometry (VO) and Simultaneous Localization and Mapping (SLAM) mostly estimate motion by matching features between frames. However,…

### 2. LIN-SLAM: Lightweight LiDAR--Inertial Neural SLAM for Real-Time Onboard Navigation

- **arXiv**: [2610.21199v1](https://arxiv.org/abs/2610.21199v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.21199v1)
- **作者**: Shiqi Che, Yijie Liu, Shuo Wang et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **✅ 已研读**
- **摘要**: Geometric light detection and ranging (LiDAR)--inertial simultaneous localization and mapping (SLAM) provides efficient state estimation but lacks the continuous map representation and global refinement capabilities of neural implicit SLAM, while neural implicit methods remain computationally expensive. We propose Lightweight LiDAR--Inertial Neural SLAM (LI…

### 3. HP2-SLAM: Adaptive Hybrid ICP for Robust and Efficient LiDAR SLAM

- **arXiv**: [2608.14996v1](https://arxiv.org/abs/2608.14996v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.14996v1)
- **作者**: Nam Tran, Thu Tran, Hieu Phan et al.
- **发表**: 2026-08-15  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Achieving robustness, accuracy, and efficiency simultaneously remains a central challenge in light detection and ranging (LiDAR) simultaneous localization and mapping (SLAM). While learning-based approaches deliver strong benchmark performance, they often require extensive training, substantial computational resources, and struggle to generalize to unseen o…

### 4. Line-Augmented cuVSLAM: Robust Visual Odometry in Low-Texture Environments

- **arXiv**: [2610.20958v1](https://arxiv.org/abs/2610.20958v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20958v1)
- **作者**: Dara Molloy, Terry Wu, Wonju Lee et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Autonomous mobile robots in warehouses and production facilities operate in precisely the environments that defeat point-feature visual odometry: featureless aisles, uniform walls, repetitive racking and specular floors. Such environments are, however, rich in straight-edge structure: rack uprights, door frames, wall junctions and cabinet outlines present h…

### 5. Human-in-the-Loop Neuro-Symbolic Drift Anticipation for Reliable Visual SLAM

- **arXiv**: [2610.05757v1](https://arxiv.org/abs/2610.05757v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05757v1)
- **作者**: Junhyun Nam, Wonse Jo
- **发表**: 2026-10-05  ·  **类别**: cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: This paper introduces Hybrid DeepSEE (HDS), a Human-in-the-Loop (HITL) neuro-symbolic framework for proactive drift anticipation in Visual SLAM (V-SLAM). While data-driven models offer predictive power, their "black-box" nature often yields physically inconsistent outputs in out-of-distribution (OOD) environments. To address this, HDS integrates neural drif…

### 6. Know-Your-Scene (KYS)-SLAM: Hierarchical Semantic-Motion Priors for Feature Matching in Stereo Visual SLAM

- **arXiv**: [2609.27509v1](https://arxiv.org/abs/2609.27509v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27509v1)
- **作者**: Preeti Chatterjee, Jin Lu, Jin Sun et al.
- **发表**: 2026-09-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Stereo visual SLAM systems built on local descriptors suffer from semantic ambiguity, instance-level confusion, and independently moving objects, each corrupting data association and accumulating as trajectory drift. Prevailing semantic and dynamic SLAM methods address this through binary feature rejection, sacrificing correspondence density for outlier sup…

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
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Dynamic-point filters are routinely added to feature-based visual SLAM, and several recent systems argue that removing dynamic features can leave too few static features in low-texture regions. So far, these systems have been evaluated only on texture-rich benchmark sequences. We present a controlled study that isolates this interaction. We render synthetic…

### 9. MVP-SLAM: Multi-Camera Visual-Inertial Floorplan-Prior SLAM

- **arXiv**: [2609.39596v1](https://arxiv.org/abs/2609.39596v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39596v1)
- **作者**: Asier Bikandi-Noya, Miguel Fernandez-Cortizas, Muhammad Shaheer et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Indoor building construction sites are demanding environments for visual SLAM, where variable lighting and repetitive, low-textured structures make the system drift over long trajectories, though structural elements such as walls remain distinguishable despite these conditions. These buildings are constructed according to their as-planned floor plans, avail…

### 10. Parameter Sensitivity Analysis for Aerial LiDAR-Inertial Odometries in low-altitude flights

- **arXiv**: [2609.12837v1](https://arxiv.org/abs/2609.12837v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.12837v1)
- **作者**: Robert Milijas, Jose Ramiro Martinez-de Dios, Stjepan Bogdan
- **发表**: 2026-09-11  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: LiDAR-based SLAM (Simultaneous Localization and Mapping) and LIO (LiDAR-inertial odometry) algorithms are often used for precise navigation of unmanned aerial vehicles, especially during interactions with the aerial robot's environment. However, the performance of these algorithms is greatly dependent on the scenario, LiDAR, and robot motion characteristics…

## 🧪 仿真 / Sim2Real (1 篇)

### 1. SKG in Practice: OOD Generalization Cases Across FourDomains

- **arXiv**: [2610.32314v1](https://arxiv.org/abs/2610.32314v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.32314v1)
- **作者**: Jian An, Chaoshi Wu, Xinpan Luo
- **发表**: 2026-10-23  ·  **类别**: cs.LG
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: This paper presents the engineering implementation methods of the SKG inference framework and provides complete case studies across four domains. Case 1, 2D Dissipative Mechanical System: OOD MSE is 1.69 to 4.12 times lower than the best neural baseline; the state-dependent metric yields a 10^8-order improvement under controlled conditions. Case 2, Target D…

## 🤏 软体机器人 / 柔性控制 (3 篇)

### 1. An End-to-End Framework for Modelling Pneumatic Soft Robots Based on Differentiable Finite Element Methods

- **arXiv**: [2610.04612v1](https://arxiv.org/abs/2610.04612v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.04612v1)
- **作者**: Shaohong Zhong, Yao Yao, Perla Maiolino et al.
- **发表**: 2026-10-03  ·  **类别**: cs.RO, eess.SY
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Soft robots present significant modelling challenges due to their non-linearity, complex dynamics and potentially intricate geometries. These difficulties in accurate system identification and dynamics modelling limit their applications in precise robotics tasks. Prior modelling approaches typically suffer from trade-offs in accuracy, computational efficien…

### 2. A Reconfigurable Fabric Based Pneumatic Actuator with Button Fastened Constraint Modules for Multi Mode Actuation

- **arXiv**: [2610.11054v1](https://arxiv.org/abs/2610.11054v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.11054v1)
- **作者**: Kentaro Kimura, Hiroki Ishizuka, Yusuke Sakaue et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Soft pneumatic actuators are widely used in soft robotics. However, their actuation modes are typically fixed by internal chamber designs or reinforcements, making post fabrication reconfiguration difficult. This paper presents a reconfigurable fabric-based pneumatic actuator that enables rapid, tool free, and reusable switching among multiple actuation mod…

### 3. CROPS: Cosserat-Rod-Based Co-Design of Soft Slender Programmable Material Systems for Biomedical Applications

- **arXiv**: [2610.24209v1](https://arxiv.org/abs/2610.24209v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.24209v1)
- **作者**: Aaditya Chandrasekhar, Dex Doksoo Lee, Hyunwoo Kwon et al.
- **发表**: 2026-10-16  ·  **类别**: cs.CE, cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Slender structures made of stimuli-responsive materials represent an emerging class of programmable material systems, with applications in soft robotics, minimally invasive surgery, wearable electronics, and deployable structures. In biomedical applications, the on-demand design of slender structures, encompassing both their material layout and actuation, i…

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
1. [From Tabletop to Walking Bot: Deploying a VLA Model on a Legged Manipulator Robot](https://arxiv.org/abs/2610.32271v1) — score 17
2. [Motion Retargeting with Spatiotemporal Preferences for Humanoid Loco-Manipulation](https://arxiv.org/abs/2610.30540v1) — score 17
3. [SoTa: Soft Tactile Skins for Dexterous Manipulation](https://arxiv.org/abs/2610.02338v1) — score 17

> 筛选说明:本次 Top 3 已排除(已研读跳过 3 篇、综述跳过 2 篇)。

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
