# 机器人研究每日摘要 · 2026-10-24

> 自动生成,共 85 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (4 篇)

### 1. HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games

- **arXiv**: [2610.31162v1](https://arxiv.org/abs/2610.31162v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.31162v1)
- **作者**: Zecong Tang, Zian Guan, Yuncheng Guo et al.
- **发表**: 2026-10-22  ·  **类别**: cs.CV
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Building virtual embodied agents that operate in open-ended games like human players is a long-standing goal requiring both long-horizon autonomy and reliable native-interface control. As a procedurally generated open world, Minecraft provides a natural testbed for studying the integration of these capabilities. Existing agents typically provide either nati…

### 2. ACCRUE: Continual Off-Policy Reinforcement Learning for Robot Foundation Models

- **arXiv**: [2610.18596v1](https://arxiv.org/abs/2610.18596v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.18596v1)
- **作者**: Changyeon Kim, Kimin Lee, Yashraj Narang et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 10  ·  **✅ 已研读**
- **摘要**: Reinforcement learning (RL) post-training improves robot foundation models (RFMs) beyond their demonstrations, but real-world deployment demands more: learning new tasks efficiently while retaining previously acquired behaviors. Existing continual RL methods on top of VLAs mitigate forgetting but rely on on-policy updates with limited forward transfer, wher…

### 3. Multi-Dimensional Featurizers Yield Fine-Grained Steering and Data Shaping in Robot Foundation Models

- **arXiv**: [2610.20767v1](https://arxiv.org/abs/2610.20767v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20767v1)
- **作者**: Aiden Swann, Mozes Jacobs, Mathilde Papillon et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Can better feature discovery improve control over robot behavior through internal interventions and training data? Recent work in vision and language models reveals multidimensional features, motivating block-sparse featurizers (BSFs), which represent each feature in a low-dimensional subspace. We investigate whether recovering this structure provides an in…

### 4. Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success

- **arXiv**: [2610.31670v1](https://arxiv.org/abs/2610.31670v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.31670v1)
- **作者**: Yunfei Xie, Howard H. Qian, Shiyi Lan et al.
- **发表**: 2026-10-22  ·  **类别**: cs.CV, cs.LG, cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Robotic foundation models are typically evaluated through costly closed-loop rollouts, which motivates cheap offline proxies for model capability. The Platonic Representation Hypothesis (PRH) suggests that as representations improve, different modalities such as vision and language converge toward a shared statistical model of reality. We ask whether motion…

## 🌐 具身智能 / 机器人基础模型 (10 篇)

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

### 3. DewHand: Direct Metric World-Space Hand Motion Reconstruction from Egocentric Videos

- **arXiv**: [2610.29936v1](https://arxiv.org/abs/2610.29936v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.29936v1)
- **作者**: Naru Suzuki, Satoshi Ikehata, Takehiko Ohkawa et al.
- **发表**: 2026-10-21  ·  **类别**: cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Recovering metric world-space hand motion from egocentric video supports understanding human interactions and transferring them to embodied agents. Three challenges complicate this task: multi-stage pipelines propagate errors from independently estimated hand and camera motion; monocular observations leave physical scale ambiguous; and occlusion and out-of-…

### 4. Know When to Escalate: Critic-Guided Adaptive Execution for Cloud-Local Embodied Agents

- **arXiv**: [2610.30587v1](https://arxiv.org/abs/2610.30587v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30587v1)
- **作者**: Wei Zhang, Lirong Xiang, Charles Fleming
- **发表**: 2026-10-22  ·  **类别**: cs.RO, cs.DC
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Recent advances in foundation-model agents have enabled increasingly capable embodied systems for long-horizon planning and interaction. However, embodied agents require fast, closed-loop decisions as they continuously perceive and act on a changing environment. Deploying strong cloud agents leaves the platform idle for seconds between consecutive actions,…

### 5. Externalise the Memory: A Pre-Registered Study of Where an Embodied Agent's Experience Should Live

- **arXiv**: [2610.30478v1](https://arxiv.org/abs/2610.30478v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30478v1)
- **作者**: Cheng-Yin Tu
- **发表**: 2026-10-21  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Should an embodied agent's experience be baked into its policy weights, or kept external and retrieved at inference? A memory-augmented teacher (a VLM that retrieves lessons, with their episode images, from its own past attempts) produces trajectories on a vision-conditioned reach task; from the same trajectories we distil LoRA student policies and evaluate…

### 6. Multimodal Embodied Agents: A Unified Capability-centric Perspective from Computer-Use to Robot-Use

- **arXiv**: [2610.30108v1](https://arxiv.org/abs/2610.30108v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30108v1)
- **作者**: Yanzhe Chen, Ziyi Yang, Jifeng Zhu et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 8  ·  **📚 综述(归档备查,按协议 §4 不深读)**
- **摘要**: Multimodal agents (MMAs) sustain interaction through reasoning, memory, tools, and feedback, most visibly as computer-use agents, while robotic systems (RSs) couple sensing and actuation under physical dynamics. We define multimodal embodied agents (MMEAs) as goal-directed systems that couple multimodal task reasoning with physical action and revise decisio…

### 7. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 8. PRISM: Learning Realistic Depth via Physics-Grounded Noise Disentanglement with Semantic-Geometric Collaboration

- **arXiv**: [2610.29432v1](https://arxiv.org/abs/2610.29432v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.29432v1)
- **作者**: Xiujian Liang, Jiacheng Liu, Mingyang Sun et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Real-world physical sensing exhibits complex, heterogeneous noise patterns that deviate significantly from idealized simulation, posing a fundamental bottleneck for sim-to-real transfer. Existing sensor modelings typically treat depth noise as a monolithic black-box process, overlooking the distinct physical mechanisms that govern different error modalities…

### 9. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

### 10. FoundationVIO: Enforcing Metric Scale in Feed-forward Visual-Inertial Odometry

- **arXiv**: [2610.14951v1](https://arxiv.org/abs/2610.14951v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.14951v1)
- **作者**: Jin Rhee, Yuhao Zhang, Frank Dellaert et al.
- **发表**: 2026-10-10  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Feed-forward geometric foundation models (GFMs) directly predict dense geometry and camera poses from batches of images. Emerging visual SLAM methods chain together consecutive GFM batches to form dense point cloud maps. A core challenge is how to address the ambiguous geometric scale of GFM predictions: independent predictions are locally consistent up-to-…

## 🦵 人形 / 足式机器人 (26 篇)

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

### 3. Motion Retargeting with Spatiotemporal Preferences for Humanoid Loco-Manipulation

- **arXiv**: [2610.30540v1](https://arxiv.org/abs/2610.30540v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30540v1)
- **作者**: Xiongbo Shi, Shihang Du, Zongyou Yu et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Human motion retargeting bridges the embodiment gap between humans and humanoid robots by converting human demonstrations into reference trajectories for whole-body control and loco-manipulation. For object-interaction tasks, successful execution depends on accurately preserving body--object relations at critical stages. However, uniform per-frame iteration…

### 4. PHD-Hand: A Printable Humanoid Dexterous Hand with Linkage-Driven 3-DOA Digits

- **arXiv**: [2610.29030v1](https://arxiv.org/abs/2610.29030v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.29030v1)
- **作者**: Neel Adwani, Muhaiminul Islam Akash, Saffia Ouali et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Currently, dexterous humanoid robot hands are widely considered the final hardware bottleneck that hampers generalist robots from physically assisting people at home and work. As conventional tendon-driven designs suffer from high cost, demanding maintenance, poor reliability, and short durability, alternative linkage-driven designs have increasingly gained…

### 5. Reinforcement Learning Based Multi-Terrain Adaptive Whole-Body Control for a Quadruped Manipulator

- **arXiv**: [2610.23548v1](https://arxiv.org/abs/2610.23548v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.23548v1)
- **作者**: Yanzhou Jin, Fei Suo, Chang Liu et al.
- **发表**: 2026-10-16  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **✅ 已研读**
- **摘要**: Legged robots equipped with manipulators offer promising capabilities for loco-manipulation tasks in unstructured environments. However, achieving task-consistent end-effector behavior during locomotion remains challenging due to terrain-induced disturbances and the strong coupling between locomotion and manipulation, particularly for small-scale quadruped…

### 6. Action-Aligned Latent Planning for Versatile Humanoid Loco-Manipulation

- **arXiv**: [2610.24675v2](https://arxiv.org/abs/2610.24675v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.24675v2)
- **作者**: Yutang Lin, Guanya Shi, C. Karen Liu
- **发表**: 2026-10-17  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Learning a single perceptive policy for diverse humanoid loco-manipulation requires unifying high-level task decisions without losing the state-dependent physical responses that make each interaction succeed. This makes the representation between high-level planning and whole-body control critical: kinematic or contact targets provide compact abstractions b…

### 7. EmbodyHOI: Embodiment-Aware Generation of Hand-Object Interactions for Humanoid Dexterous Manipulation

- **arXiv**: [2610.27242v1](https://arxiv.org/abs/2610.27242v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.27242v1)
- **作者**: Chaitanya Chawla, Kartik Sharma, Ananya Bal et al.
- **发表**: 2026-10-19  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Humanoid dexterous manipulation needs reference motions that are both semantically rich and kinematically feasible for the target robot. Text-conditioned hand-object interaction (HOI) generators supply diverse, language-specified demonstrations, but they synthesize motion in human (MANO) space. The embodiment gap is therefore deferred to post-hoc retargetin…

### 8. OccluDex: Hierarchical 3D Visuo-Tactile Representation Learning for Egocentric Dexterous Manipulation under Self-Occlusion

- **arXiv**: [2609.39017v1](https://arxiv.org/abs/2609.39017v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39017v1)
- **作者**: Ziheng Xu, Yueyuan Chen, Xinyuan He et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Reliable dexterous manipulation requires continuous estimation of object geometry and hand-object contact throughout interaction. With egocentric sensing, however, the manipulating hand frequently occludes task-relevant object surfaces and contact regions, reducing the visual evidence available for state estimation and thereby making robust closed-loop cont…

### 9. EchoNav: Evidential BEV Completion from Historical Observations for Visual Navigation

- **arXiv**: [2610.27616v1](https://arxiv.org/abs/2610.27616v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.27616v1)
- **作者**: Diwen Liu, Yiyang Shao, Borui Wang et al.
- **发表**: 2026-10-20  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Visual navigation in cluttered environments requires robots to recover previously observed structure and infer obstacles and free space that remain occluded. We present a framework that combines temporal aggregation and occupancy completion in an evidential bird's-eye-view (BEV) representation predicted from short RGB sequences. A decoder adapts frozen VGGT…

### 10. Physical AI for Intralogistics: Benchmarking the NVIDIA Sim-to-Real Ecosystem for Cosmos-Enhanced COMPASS Navigation on Industrial Mobile Robots

- **arXiv**: [2610.28432v2](https://arxiv.org/abs/2610.28432v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.28432v2)
- **作者**: Charbel Abi Hana, Rayan Zaitouni, Kameel Amareen et al.
- **发表**: 2026-10-20  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Classical robot navigation stacks are reliable but often require re-engineering for each new robot type and site. Learning-based navigation shifts this effort from hand-tuned parameters to data generation and training, where a policy adapts to each new embodiment or facility by fine-tuning in simulation. Whether policies adapted this way stay reliable on re…

## 🦾 操控 / 灵巧手 / 抓取 (26 篇)

### 1. HandsOn: A Large-Scale Simulation Benchmark for Generalizable Dexterous Manipulation

- **arXiv**: [2610.26765v1](https://arxiv.org/abs/2610.26765v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.26765v1)
- **作者**: Tianwei Luo, Yiming He, Hongjin Wu et al.
- **发表**: 2026-10-19  ·  **类别**: cs.RO
- **相关性评分**: 24  ·  **✅ 已研读**
- **摘要**: General-purpose manipulation requires reliable behavior across embodiments, objects, and task demands. We introduce HandsOn, a composable simulation platform and benchmark for cross-embodiment dexterous manipulation. It supports five robotic arms, six dexterous hands, and approximately 200 rigid, articulated, and deformable assets in randomized scenes. The…

### 2. Tactile-Based Robotic Manipulation: From Mechanics-Driven to Data-Driven Perspectives

- **arXiv**: [2610.30438v1](https://arxiv.org/abs/2610.30438v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30438v1)
- **作者**: Jingyi Xiang, Yixuan Wang, Wenzhen Yuan
- **发表**: 2026-10-21  ·  **类别**: cs.RO
- **相关性评分**: 20  ·  **📚 综述(归档备查,按协议 §4 不深读)**
- **摘要**: Tactile sensing provides robots with direct access to physical interactions at the contact interface, making it a critical modality for robust and dexterous manipulation. Over the past several decades, tactile-based manipulation research has evolved from mechanics-driven approaches, which explicitly interpret tactile signals through contact mechanics and ta…

### 3. FocusVLA: Future-Intent Guided Dynamic View Routing for Vision-Language-Action Models

- **arXiv**: [2610.31423v1](https://arxiv.org/abs/2610.31423v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.31423v1)
- **作者**: Huixin Xu, Ziya Yu, Peng Li
- **发表**: 2026-10-22  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models have become an important paradigm for robotic manipulation by unifying visual perception, language understanding, and action generation. Since reliable manipulation requires sufficient observation of objects, end-effectors, and their spatial relationships, multi-view inputs are widely used to provide complementary spatial…

### 4. Physical Words: A Vocabulary for Structuring Latent Reasoning in Robot Manipulation

- **arXiv**: [2610.26854v3](https://arxiv.org/abs/2610.26854v3)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.26854v3)
- **作者**: Jiaming Liu, Xinghao Zhu, Yiming Zhang et al.
- **发表**: 2026-10-19  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Multimodal reasoning provides robotic foundation models with predictive context needed for reliable action generation. However, language-based reasoning captures task semantics but struggles to express fine-grained physical dynamics, while latent reasoning models future state evolution but offers limited structure for organizing these dynamics into reusable…

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

- **arXiv**: [2610.29264v1](https://arxiv.org/abs/2610.29264v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.29264v1)
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

### 10. PaceVLA: Adaptive Temporal Action Quantization in Vision-Language-Action Models

- **arXiv**: [2610.25961v2](https://arxiv.org/abs/2610.25961v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.25961v2)
- **作者**: Hojin Jeon, Jimin Lee, Taekwan Kim et al.
- **发表**: 2026-10-19  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Fast and reliable manipulation is crucial for practical robot deployment. Although Vision-Language-Action (VLA) models have recently shown remarkable progress as generalist robot policies, their execution often remains temporally inefficient. A key source of this inefficiency is that policies learn fine-grained temporal patterns from teleoperated demonstrat…

## 🎓 模仿学习 / 强化学习 (10 篇)

### 1. NeuralSRender: G-Buffer Guided Video Diffusion for Sim-to-Real Rendering

- **arXiv**: [2610.29200v1](https://arxiv.org/abs/2610.29200v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.29200v1)
- **作者**: Yipeng Lu, Youqi Liao, Zhenyu Wang et al.
- **发表**: 2026-10-21  ·  **类别**: cs.CV
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: The scarcity of high-quality annotated visual data remains a critical bottleneck for autonomous-driving perception. Simulators provide training data at scale, but the limited realism of synthetic videos compromises perception performance in real-world applications. To address this limitation, we propose NeuralSRender, a sim-to-real video translation framewo…

### 2. RingNav: Task-Shaped Circular Memory for Visual Heading

- **arXiv**: [2610.19044v1](https://arxiv.org/abs/2610.19044v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19044v1)
- **作者**: Naitri Rajyaguru, Aryan Tajne, Stephen Jardim et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Tiny robots have limited computation and memory, yet visual navigation systems often maintain more state than a task requires. We ask whether persistent memory can instead be shaped by the task. We present \textbf{RingNav}, a \(10.6\)k--parameter visual heading estimator that constrains its memory to the circular manifold \(S^1\). RingNav learns only the tu…

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

### 5. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 6. PCLA-Bridge: A Framework for Cross-Domain Deployment of CARLA Agents

- **arXiv**: [2610.28696v1](https://arxiv.org/abs/2610.28696v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.28696v1)
- **作者**: Masoud Jamshidiyan Tehrani, Jinhan Kim, Paolo Tonella
- **发表**: 2026-10-20  ·  **类别**: cs.SE, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Most high-performing end-to-end autonomous driving agents (ADAs) are developed for the CARLA Leaderboard, tightly coupling them to CARLA's APIs, sensor layouts, coordinate systems, and internal clock. Reusing these models on real datasets, alternative simulators, or physical platforms necessitates substantial manual re-engineering. We present PCLA-Bridge, a…

### 7. Unblur-SLAM: Dense Neural SLAM for Blurry Inputs

- **arXiv**: [2603.26810v1](https://arxiv.org/abs/2603.26810v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.26810v1)
- **作者**: Qi Zhang, Denis Rozumny, Francesco Girlanda et al.
- **发表**: 2026-03-26  ·  **类别**: cs.CV, eess.IV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We propose Unblur-SLAM, a novel RGB SLAM pipeline for sharp 3D reconstruction from blurred image inputs. In contrast to previous work, our approach is able to handle different types of blur and demonstrates state-of-the-art performance in the presence of both motion blur and defocus blur. Moreover, we adjust the computation effort with the amount of blur in…

### 8. Query Quantized Neural SLAM

- **arXiv**: [2412.16476v1](https://arxiv.org/abs/2412.16476v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2412.16476v1)
- **作者**: Sijia Jiang, Jing Hua, Zhizhong Han
- **发表**: 2024-12-21  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural implicit representations have shown remarkable abilities in jointly modeling geometry, color, and camera poses in simultaneous localization and mapping (SLAM). Current methods use coordinates, positional encodings, or other geometry features as input to query neural implicit functions for signed distances and color which produce rendering errors to d…

### 9. ACE-SLAM: Scene Coordinate Regression for Neural Implicit Real-Time SLAM

- **arXiv**: [2512.14032v1](https://arxiv.org/abs/2512.14032v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2512.14032v1)
- **作者**: Ignacio Alzugaray, Marwan Taher, Andrew J. Davison
- **发表**: 2025-12-16  ·  **类别**: cs.CV, cs.AI, eess.IV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: We present a novel neural RGB-D Simultaneous Localization And Mapping (SLAM) system that learns an implicit map of the scene in real time. For the first time, we explore the use of Scene Coordinate Regression (SCR) as the core implicit map representation in a neural SLAM pipeline, a paradigm that trains a lightweight network to directly map 2D image feature…

### 10. MISO: Multiresolution Submap Optimization for Efficient Globally Consistent Neural Implicit Reconstruction

- **arXiv**: [2504.19104v1](https://arxiv.org/abs/2504.19104v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2504.19104v1)
- **作者**: Yulun Tian, Hanwen Cao, Sunghwan Kim et al.
- **发表**: 2025-04-27  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Neural implicit representations have had a significant impact on simultaneous localization and mapping (SLAM) by enabling robots to build continuous, differentiable, and high-fidelity 3D maps from sensor data. However, as the scale and complexity of the environment increase, neural SLAM approaches face renewed challenges in the back-end optimization process…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (8 篇)

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

### 3. Line-Augmented cuVSLAM: Robust Visual Odometry in Low-Texture Environments

- **arXiv**: [2610.20958v1](https://arxiv.org/abs/2610.20958v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20958v1)
- **作者**: Dara Molloy, Terry Wu, Wonju Lee et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Autonomous mobile robots in warehouses and production facilities operate in precisely the environments that defeat point-feature visual odometry: featureless aisles, uniform walls, repetitive racking and specular floors. Such environments are, however, rich in straight-edge structure: rack uprights, door frames, wall junctions and cabinet outlines present h…

### 4. Human-in-the-Loop Neuro-Symbolic Drift Anticipation for Reliable Visual SLAM

- **arXiv**: [2610.05757v1](https://arxiv.org/abs/2610.05757v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05757v1)
- **作者**: Junhyun Nam, Wonse Jo
- **发表**: 2026-10-05  ·  **类别**: cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: This paper introduces Hybrid DeepSEE (HDS), a Human-in-the-Loop (HITL) neuro-symbolic framework for proactive drift anticipation in Visual SLAM (V-SLAM). While data-driven models offer predictive power, their "black-box" nature often yields physically inconsistent outputs in out-of-distribution (OOD) environments. To address this, HDS integrates neural drif…

### 5. Know-Your-Scene (KYS)-SLAM: Hierarchical Semantic-Motion Priors for Feature Matching in Stereo Visual SLAM

- **arXiv**: [2609.27509v1](https://arxiv.org/abs/2609.27509v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27509v1)
- **作者**: Preeti Chatterjee, Jin Lu, Jin Sun et al.
- **发表**: 2026-09-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Stereo visual SLAM systems built on local descriptors suffer from semantic ambiguity, instance-level confusion, and independently moving objects, each corrupting data association and accumulating as trajectory drift. Prevailing semantic and dynamic SLAM methods address this through binary feature rejection, sacrificing correspondence density for outlier sup…

### 6. Does Dynamic-Point Filtering Help When Texture Is Scarce? A Controlled Study of ORB-SLAM2 Front-Ends in Synthetic Indoor Scenes

- **arXiv**: [2610.10564v1](https://arxiv.org/abs/2610.10564v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10564v1)
- **作者**: Zekui Xue
- **发表**: 2026-10-02  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Dynamic-point filters are routinely added to feature-based visual SLAM, and several recent systems argue that removing dynamic features can leave too few static features in low-texture regions. So far, these systems have been evaluated only on texture-rich benchmark sequences. We present a controlled study that isolates this interaction. We render synthetic…

### 7. MVP-SLAM: Multi-Camera Visual-Inertial Floorplan-Prior SLAM

- **arXiv**: [2609.39596v1](https://arxiv.org/abs/2609.39596v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39596v1)
- **作者**: Asier Bikandi-Noya, Miguel Fernandez-Cortizas, Muhammad Shaheer et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Indoor building construction sites are demanding environments for visual SLAM, where variable lighting and repetitive, low-textured structures make the system drift over long trajectories, though structural elements such as walls remain distinguishable despite these conditions. These buildings are constructed according to their as-planned floor plans, avail…

### 8. Geodesic Flow Matching for Denoising High-Dimensional Structured Representations

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
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Imitation-learned robot policies are frequently overfit to the visual conditions present in their training demonstrations. Consequently, variations in object color or background appearance often induce substantial performance degradation. A common mitigation strategy is to acquire additional demonstrations in each novel visual context; however, this approac…

---

## 📋 本日操作建议

**建议今日深读 (Top 3):**
1. [Motion Retargeting with Spatiotemporal Preferences for Humanoid Loco-Manipulation](https://arxiv.org/abs/2610.30540v1) — score 17
2. [FocusVLA: Future-Intent Guided Dynamic View Routing for Vision-Language-Action Models](https://arxiv.org/abs/2610.31423v1) — score 16
3. [PHD-Hand: A Printable Humanoid Dexterous Hand with Linkage-Driven 3-DOA Digits](https://arxiv.org/abs/2610.29030v1) — score 15

> 筛选说明:本次 Top 3 已排除(已研读跳过 6 篇、综述跳过 2 篇)。

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
