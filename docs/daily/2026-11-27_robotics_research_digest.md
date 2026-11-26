# 机器人研究每日摘要 · 2026-11-27

> 自动生成,共 118 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (6 篇)

### 1. Sparks of Weight-Space Programming for Robot Foundation Models

- **arXiv**: [2611.31715v1](https://arxiv.org/abs/2611.31715v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.31715v1)
- **作者**: Kyle Coelho, Eugen Solowjow
- **发表**: 2026-11-24  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: This paper demonstrates an approach for correcting failures of robot foundation models (RFMs) without additional data collection, demonstrations, or training. We apply weight-space programming (WSP), in which a language-model agent directly reads and writes a neural network's parameters, to a large, pre-trained vision-language-action policy. The idea is sim…

### 2. RePace: Reasoning about Demonstration Speedup for Faster Vision-Language-Action Policies

- **arXiv**: [2611.34864v1](https://arxiv.org/abs/2611.34864v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.34864v1)
- **作者**: Insup Lee, Hojin Jeon, Sunguk Shin et al.
- **发表**: 2026-11-25  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Since vision-language-action (VLA) policies can inherit the slow pace of human demonstrations, accelerating these demonstrations before fine-tuning can lead to faster VLA policies without an additional speed-selection module at deployment. Several offline speedup methods have focused on identifying segments that require less precision and assigning predefin…

### 3. $Z$-sight: Unifying Vision-Language-Action and Latent World Modeling

- **arXiv**: [2611.24940v1](https://arxiv.org/abs/2611.24940v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.24940v1)
- **作者**: Junjie Ye, Yiqi Zhao, Muchen Xu et al.
- **发表**: 2026-11-18  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: We introduce $Z$-sight, a unified robot foundation model that couples vision-language-action (VLA) and generative latent world modeling. Video-based world action models (WAMs) show the value of joint future-and-action generation for control, yet inherit the heavy cost of video generators. Recent latent-space policies avoid pixel generation, yet typically al…

### 4. RoboCoEvo: Expanding Robot Capabilities through Agent-Policy Co-Evolution

- **arXiv**: [2611.19081v1](https://arxiv.org/abs/2611.19081v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.19081v1)
- **作者**: Ran Qi, Yixin Xiao, Dawei Wang et al.
- **发表**: 2026-11-14  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Integrating MLLM-based agents with robotic foundation models has attracted increasing attention as a means of enhancing robotic capabilities. However, the improvement of such integrated systems remains largely decoupled across their agent and model components, with advances in one component not necessarily benefiting the other, substantially limiting the ca…

### 5. RoboEvo$^2$: Recursive Robot Self-Improvement via Harness-Policy Co-Evolution

- **arXiv**: [2611.34675v1](https://arxiv.org/abs/2611.34675v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.34675v1)
- **作者**: Chenzhi Liu, Jiehong Lin, Wei Huang et al.
- **发表**: 2026-11-25  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Robots should adapt to unfamiliar environments and acquire new skills through interaction, then execute those skills efficiently with practice. Vision-language-action policies provide efficient control, but often need additional human demonstrations to handle unfamiliar settings; reasoning agents can discover solutions using broad prior knowledge and robot-…

### 6. La-JEPA: Compact Robot Policies with Latent World Modeling

- **arXiv**: [2611.08156v2](https://arxiv.org/abs/2611.08156v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.08156v2)
- **作者**: Mateo Clémente, George Z. Xue, Amin Abyaneh et al.
- **发表**: 2026-11-05  ·  **类别**: cs.RO, cs.CV, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: World-action models adapt pretrained video generators, and vision-language-action models build on vision-language backbones, tying policy architecture and inference cost to large transformers designed for generation rather than control. While recent world-action models mostly scale the video backbone and its data, we argue that the choice of latent space is…

## 🌐 具身智能 / 机器人基础模型 (10 篇)

### 1. Self-Upgrading Embodied Agents

- **arXiv**: [2611.31117v1](https://arxiv.org/abs/2611.31117v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.31117v1)
- **作者**: Jiajun Fan, Neil He, Qinglong Zheng et al.
- **发表**: 2026-11-23  ·  **类别**: cs.AI
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: An embodied agent built on a language model goes to work with the weights it was given and keeps them for life. To get better, it needs more training, or reflection, memory, search or prompts that cost every step and are lost when the task changes. Editing weights by reasoning, weight-space programming, could end this, but has stayed with models that only r…

### 2. AIRIS: Benchmarking Social Embodied Intelligence in Egocentric Streaming Videos

- **arXiv**: [2611.34347v1](https://arxiv.org/abs/2611.34347v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.34347v1)
- **作者**: Yuchen Zhou, Hongsheng Wu, Jiayu Tang et al.
- **发表**: 2026-11-25  ·  **类别**: cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Embodied agents operating around people must not only recognize social cues, but also decide when the available evidence is sufficient, whether to intervene, and how to respond without violating social norms. Existing benchmarks typically evaluate these abilities in isolation or with access to completed videos, obscuring where an online social decision fail…

### 3. EviCraft: Can Minecraft Agents Find What They Cannot See?

- **arXiv**: [2611.32765v1](https://arxiv.org/abs/2611.32765v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.32765v1)
- **作者**: Wenyou Yi, Lantian Zhang, Guanlin Chen et al.
- **发表**: 2026-11-24  ·  **类别**: cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In Minecraft, a common testbed for embodied agents, semantic tools such as mineBlock pick targets from the simulator's loaded world state without a visibility test, so a buried ore the agent has never seen is one call away, and scores cannot show whether the agent searched. We formalize the missing requirement as evidence closure: every decision of an agent…

### 4. IncR-3DSGG: Incremental Posed RGB Image Based 3D Scene Graph Generation via Privileged Depth Supervision

- **arXiv**: [2611.15429v1](https://arxiv.org/abs/2611.15429v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.15429v1)
- **作者**: Mrunmai Phatak, Daniel Kienzle, Roman Küble et al.
- **发表**: 2026-11-11  ·  **类别**: cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Scene graphs provide a compact, structured representation of environments by capturing objects and their spatial or semantic relationships in a form suitable for embodied agents. Existing 3D scene graph generation methods often rely on depth sensing at inference, either to associate object instances across views via point cloud overlap or to compute inter-o…

### 5. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 6. MMotion: Collaborative Cross-Scale Memory for Text-to-Motion Generation

- **arXiv**: [2611.33819v1](https://arxiv.org/abs/2611.33819v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.33819v1)
- **作者**: Zhaoxin Fan, Qingchen Yu, Kejian Wu et al.
- **发表**: 2026-11-25  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Text-to-motion generation aims to synthesize realistic human motions from natural-language descriptions, enabling applications in animation, virtual avatars, and embodied agents. Despite recent progress, existing methods either retrieve motion exemplars or retain long-range context, but rarely exploit memory to jointly reason about semantics, dynamics, and…

### 7. PoseVLN: Learning Geometric State Evolution for Vision-Language Navigation

- **arXiv**: [2611.32218v1](https://arxiv.org/abs/2611.32218v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.32218v1)
- **作者**: Pengyu Hou, Mingfei Han, Haihong Hao et al.
- **发表**: 2026-11-24  ·  **类别**: cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-Language Navigation (VLN) requires an embodied agent to relate past experience, current spatial state, and future motion while following natural-language instructions. Recent approaches improve these capabilities through long-horizon memory, state-aware reasoning, and future prediction, yet these components are often modeled separately, leaving navig…

### 8. ReWeave: Emergent Physical Task Topologies for Embodied Harness Optimization and Cross-Task Meta-Distillation

- **arXiv**: [2611.31053v1](https://arxiv.org/abs/2611.31053v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.31053v1)
- **作者**: Yicheng Xu, Wencan Jiang, Zihao Zhu et al.
- **发表**: 2026-11-23  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Long-horizon embodied tasks involve physical dependencies that may only become clear through interaction. As task understanding deepens, past trials can reveal new information for adaptation and transfer. However, coarse progress feedback cannot identify which physical preconditions held, leaving search unguided, while task-specific optimization easily over…

### 9. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

### 10. Trajectory-Calibrated Merging of Embodied Policies

- **arXiv**: [2611.25575v1](https://arxiv.org/abs/2611.25575v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.25575v1)
- **作者**: Wenshuo Chen, Honglei Jin, Le Yang et al.
- **发表**: 2026-11-19  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Robot foundation models are increasingly adapted into task specialists to expand their embodied capabilities. Yet these capabilities remain fragmented across separate policies, and existing model-merging methods do not reliably preserve them during closed-loop execution: parameter-space alignment provides only an indirect proxy for behavior, while regressio…

## 🦵 人形 / 足式机器人 (29 篇)

### 1. LocoMuJoCo: A Comprehensive Imitation Learning Benchmark for Whole-Body Control

- **arXiv**: [2611.26293v2](https://arxiv.org/abs/2611.26293v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.26293v2)
- **作者**: Firas Al-Hafez, Davide Tateo, Oleg Kaidanov et al.
- **发表**: 2026-11-19  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: LocoMuJoCo is an open-source benchmark for imitation learning (IL) and reinforcement learning (RL) on whole-body control. The library couples MuJoCo (CPU) with MJX and the MjWarp backend (GPU) under a single API, exposes 9 humanoid, 3 (musculo-)skeletal, and 4 quadruped embodiments, and ships a curated native motion-capture dataset for every humanoid, to wh…

### 2. WEVO: World Model-Enabled VLA Optimization for Whole-Body Loco-Manipulation

- **arXiv**: [2611.25251v1](https://arxiv.org/abs/2611.25251v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.25251v1)
- **作者**: Qianzhong Chen, Muyuan Lin, Yuyin Sun et al.
- **发表**: 2026-11-18  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Reinforcement learning (RL) can improve vision-language-action (VLA) policies beyond imitation, but humanoid exploration is unsafe and simulator RL can exploit residual sim-to-real gaps. We present WEVO, a teleoperation-free framework for post-training a whole-body humanoid VLA in an action-conditioned video world model (WM). Simulated manipulation and loco…

### 3. Confidently Lost: Silent Failure and Edge Deployment of Dense Visual SLAM under Photon Starvation

- **arXiv**: [2611.30173v1](https://arxiv.org/abs/2611.30173v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.30173v1)
- **作者**: Shrikrishna Bhagirath Rajule, Srinath Neelamagam, Aniket Bera
- **发表**: 2026-11-23  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Dense visual SLAM built on learned two-view geometry is evaluated in good light; in low light it fails silently. Two frames of 9-level quantized noise, no scene at all, give MASt3R-SLAM's network a cross-view geometric self-consistency of 0.936; a real dark frame pair gives 0.935. Starved of structure, the network invents the same geometry for both views an…

### 4. MoViC: Real-Time Humanoid Whole-Body Control from Monocular Video Streams

- **arXiv**: [2611.19998v1](https://arxiv.org/abs/2611.19998v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.19998v1)
- **作者**: Yimin Han, Jiahui Zhang, Wanyue Li et al.
- **发表**: 2026-11-15  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Real-time whole-body imitation from monocular video requires both a robust universal tracker and high-quality real-time reconstruction. We present MoViC, a framework that uses live RGB video as a control signal for humanoid robots without wearable tracking devices. The framework combines monocular human motion reconstruction, robot retargeting, and a transf…

### 5. FineDex: Bridging Fine-Grained Human-Object Interaction Generation to Dexterous Humanoid Manipulation

- **arXiv**: [2611.34884v1](https://arxiv.org/abs/2611.34884v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.34884v1)
- **作者**: Yujia Zeng, Yuxin Chen, Yuzhen Song et al.
- **发表**: 2026-11-25  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Dexterity is, at its core, finger-level control, yet existing dexterous manipulation and human-object interaction (HOI) generation methods rarely let one specify how an interaction is performed: five-fingered hands are often reduced to grippers, or finger usage is copied from individual human demonstrations. We present FineDex, a framework that makes finger…

### 6. AirLeg: A Robust and Accurate Self-Supervised Visual-Inertial-Leg SLAM System

- **arXiv**: [2611.32523v1](https://arxiv.org/abs/2611.32523v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.32523v1)
- **作者**: Kuan Xu, Tianxin Hu, Ruofei Bai et al.
- **发表**: 2026-11-24  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Visual-inertial-leg (VIL) state estimation offers cost-effective localization for legged robots, adding only a camera to the onboard IMU and joint encoders. However, learning-based leg odometry is limited by its supervision: networks trained in simulation suffer from the sim-to-real gap, while real-world labels require costly sensors or inherit the errors o…

### 7. From Tabletop to Walking Bot: Deploying a VLA Model on a Legged Manipulator Robot

- **arXiv**: [2610.32271v1](https://arxiv.org/abs/2610.32271v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.32271v1)
- **作者**: Giovanni Minelli, Antonio Langella, Giovanni B. Dessy et al.
- **发表**: 2026-10-23  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models are typically pretrained on broad, diverse datasets and subsequently fine-tuned on a comparatively small dataset tailored to a specific target robot. Such adaptation recipe is now widely established, achieving its most mature results on fixed-base arms due to their static base dynamics and consistent reference frame. Moun…

### 8. DiffGR00T: Execution-Aware Differentiable Training for Humanoid Whole-Body Vision-Language-Action Models

- **arXiv**: [2611.32665v2](https://arxiv.org/abs/2611.32665v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.32665v2)
- **作者**: Sichen Wu, Qian Sun, Mengfan Liu et al.
- **发表**: 2026-11-24  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models have achieved strong results in arm-centric manipulation, yet humanoid whole-body control (WBC) requires dynamic balance and tightly coupled full-body coordination. Existing hierarchical humanoid VLAs typically decouple motion generation from physical execution, leaving tracking and balance errors unable to directly optim…

### 9. CHAMP: Coordinated Humanoid Loco-Manipulation with Whole-Body Motion Priors

- **arXiv**: [2611.30449v1](https://arxiv.org/abs/2611.30449v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.30449v1)
- **作者**: Lijun Han, Muyuan Ma, Zichen Wang et al.
- **发表**: 2026-11-23  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Coordinating locomotion and dexterous manipulation is fundamental to humanoid robots operating in human environments. A key challenge is learning motion priors from diverse data and using them effectively for coordinated robot control. We present CHAMP, a unified framework for humanoid loco-manipulation that combines whole-body motion pretraining with adapt…

### 10. ECHO: In-Context Behavior foundation model for Humanoid Whole-Body Control

- **arXiv**: [2611.25778v1](https://arxiv.org/abs/2611.25778v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.25778v1)
- **作者**: Xingyi Wang, Bin Li, Jiyuan Shi et al.
- **发表**: 2026-11-19  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Humanoid behavior foundation models (BFMs) acquire diverse skills through large-scale motion imitation and massively parallel reinforcement learning, yet broad behavioral capability does not ensure precise execution across physical conditions. Without distinguishing the underlying dynamics, policies may favor conservative compromises over environment-specif…

## 🦾 操控 / 灵巧手 / 抓取 (41 篇)

### 1. Ego2Real: Learning Bimanual Dexterous Manipulation from Egocentric Visuo-Tactile Demonstrations

- **arXiv**: [2611.32101v1](https://arxiv.org/abs/2611.32101v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.32101v1)
- **作者**: Ange Bao, Haishan Zhang, Lingzi Xie et al.
- **发表**: 2026-11-24  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Learning dexterous manipulation from egocentric human demonstrations offers a scalable path toward robot skill acquisition. Vision alone, however, provides limited information about physical contacts and the demonstrator's force intent, leading to ambiguities in interpreting hand-object interactions. Capturing human touch via tactile sensing is therefore cr…

### 2. Real2Worlds2Real: Scaling Self-Improving Agentic Real2Sim2Real for Robot Manipulation

- **arXiv**: [2611.31098v1](https://arxiv.org/abs/2611.31098v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.31098v1)
- **作者**: Jinzhong Gu, Jiakai Chen, Xinyi Cao et al.
- **发表**: 2026-11-23  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Scaling robot manipulation learning remains challenging due to the high cost of collecting real-world interaction data. Real-to-Sim-to-Real (Real2Sim2Real) offers a promising route by enabling policy learning in simulation grounded in real-world observations, yet scaling this paradigm across diverse tasks and physical interactions remains difficult. We intr…

### 3. TactileLab: Sim-to-Real Dexterous Robot Manipulation with Efficient Shear-Sensitive Tactile Simulation

- **arXiv**: [2611.07881v1](https://arxiv.org/abs/2611.07881v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.07881v1)
- **作者**: Yijiong Lin, Wenhao He, Toby Jack et al.
- **发表**: 2026-11-05  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Robotic simulators that represent shear within tactile sensing are becoming increasingly important for contact-rich manipulation. However, simulating contact shear with high-fidelity deformable or soft-body simulation is computationally demanding, limiting scalability to large-scale reinforcement learning. Here we introduce \textit{TactileLab}, a scalable m…

### 4. ViTacLab: Physically Consistent Visuo-Tactile Simulation, Benchmarking, and Representation Learning for Robotic Manipulation

- **arXiv**: [2611.32476v1](https://arxiv.org/abs/2611.32476v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.32476v1)
- **作者**: Linjing You, Zeming Yang, Zhenhao Shen et al.
- **发表**: 2026-11-24  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Tactile sensing is essential for contact-rich robotic manipulation, but existing visuo-tactile simulators trade physical fidelity for scalability, and benchmarks largely focus on two-finger grippers. We present ViTacLab, a framework comprising ViTacSim, ViTacBench, and ViTacPolicy. ViTacSim uses a tri-modal tactile primitive: a global sparse contact-force l…

### 5. DexLatentWorld: 3D Cross-Embodiment Latent Action World Models for Zero-Shot Robotic Manipulation

- **arXiv**: [2611.30907v1](https://arxiv.org/abs/2611.30907v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.30907v1)
- **作者**: Vinay Udit Mohan, Xuchuan Huang, Rolandos Alexandros Potamias
- **发表**: 2026-11-23  ·  **类别**: cs.RO, cs.CV, cs.LG
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: World models facilitate planning and control in robotic manipulation by enabling agents to anticipate the consequences of their actions. However, they typically rely on action-labelled interaction data that is costly to acquire and difficult to scale. These models are also often tied to the specific embodiment they were trained on, limiting transferability…

### 6. SoTa: Soft Tactile Skins for Dexterous Manipulation

- **arXiv**: [2610.02338v1](https://arxiv.org/abs/2610.02338v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.02338v1)
- **作者**: Jingyun Yang, Baiyu Shi, Timothy Yu et al.
- **发表**: 2026-10-01  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: A growing body of work suggests that tactile sensing gives robot policies contact information that complements vision in dexterous manipulation. However, visuo-tactile robot data remains scarce: dexterous demonstrations require teleoperating robots, which limits dataset scale. Human demonstrations are far cheaper to collect and offer a path to scale this da…

### 7. Nav4Manip: From Navigation to Dexterous Mobile Manipulation through Co-Evolution

- **arXiv**: [2611.34655v1](https://arxiv.org/abs/2611.34655v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.34655v1)
- **作者**: Yusen Feng, Zixi Kang, Zhijun Yin et al.
- **发表**: 2026-11-25  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Dexterous mobile manipulation is essential for robots to perform useful tasks in complex, unstructured environments. However, existing systems face two challenges. First, navigation remains too coarse for downstream manipulation, which often requires a precise base position and approach orientation rather than merely reaching a meter-scale goal region. Seco…

### 8. Dynamic Task Update Benchmark (DTU-Bench): Evaluating Runtime Task Adaptation in Robotic Manipulation

- **arXiv**: [2611.34538v1](https://arxiv.org/abs/2611.34538v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.34538v1)
- **作者**: Yanran Jiang, Cécile Paris, Dana Kulić et al.
- **发表**: 2026-11-25  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) policies perform well on fixed-instruction robotic manipulation benchmarks, but their ability to adapt to instruction changes during execution remains understudied. We introduce the Dynamic Task Update Benchmark (DTU-Bench), evaluating 40 task revisions across seven update types and three execution stages using LIBERO, a simulat…

### 9. PyRUA-Dex: Learning Programmatic Policies for Dexterous Bimanual Manipulation with Coding Agents

- **arXiv**: [2611.33144v1](https://arxiv.org/abs/2611.33144v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.33144v1)
- **作者**: Feixiang Ruan, Guodong Lv, Kewei Zhang et al.
- **发表**: 2026-11-24  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Learning for dexterous manipulation is limited by the scarcity of high-quality demonstrations: retargeting from human video is imprecise, teleoperation gives no force feedback to the operator, and exoskeleton-based collection is hard to scale up. We present PyRUA-Dex, a framework that enables coding agents to develop dexterous manipulation through programma…

### 10. One Phase Is Enough: Sim-to-Real Transfer with Direct Visual Reinforcement Learning

- **arXiv**: [2611.31588v1](https://arxiv.org/abs/2611.31588v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.31588v1)
- **作者**: John Marangola, Antonia Bronars, Younghyo Park et al.
- **发表**: 2026-11-23  ·  **类别**: cs.LG, cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Sim-to-real reinforcement learning (RL) has enabled impressive robotic behaviors, yet deploying policies directly from vision remains challenging. A common approach first trains a teacher policy with RL using privileged state observations, then distills its behavior into a vision-based student via imitation. However, the resulting student can substantially…

## 🎓 模仿学习 / 强化学习 (13 篇)

### 1. Bracketing Shows the Way: Adaptive Multi-Exposure Policy as Input for Robust Visual SLAM

- **arXiv**: [2610.33174v1](https://arxiv.org/abs/2610.33174v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.33174v1)
- **作者**: Olivier Gamache, Anthony Lavertu, David-Alexandre Duclos et al.
- **发表**: 2026-10-23  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Rapid illumination transitions can disturb Visual SLAM (VSLAM) by saturating images before the Automatic Exposure (AE) policy adapts, removing the visual correspondences needed to maintain tracking. Our proposed methods mitigate this disturbance at two levels: B-Adapt acquires adaptive exposure brackets to cover the scene dynamic range while promoting photo…

### 2. Degeneracy-Orthogonal Geometric Constraints for LiDAR SLAM

- **arXiv**: [2609.36753v1](https://arxiv.org/abs/2609.36753v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.36753v1)
- **作者**: Minseo Kim, Yina Kim, Jinhwa Hwang et al.
- **发表**: 2026-09-29  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Autonomous robot navigation relies on simultaneous localization and mapping (SLAM) to estimate motion and maintain an accurate pose within an environment. However, in axially uniform corridors such as long tunnels and pipelines, LiDAR odometry is fundamentally limited by unconstrained drift along the feature-weak travel direction. This structural degeneracy…

### 3. Chain-SLAM: Globally Consistent Backend for Multi-Session LiDAR SLAM via Chained Loop Closure

- **arXiv**: [2609.12221v1](https://arxiv.org/abs/2609.12221v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.12221v1)
- **作者**: Zhiheng Li, Xinhao Liu, Juexiao Zhang et al.
- **发表**: 2026-09-10  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Maintaining consistency over long spatial and temporal horizons remains a fundamental challenge in large-scale LiDAR SLAM, particularly when integrating maps collected across multiple sessions. We present Chain-SLAM, a LiDAR SLAM backend enabling online multi-session map alignment and reuse with global consistency at large scale. We implement a chained loop…

### 4. Generative adversarial imitation learning for robot swarms: Learning from human demonstrations and trained policies

- **arXiv**: [2603.02783v1](https://arxiv.org/abs/2603.02783v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.02783v1)
- **作者**: Mattes Kraus, Jonas Kuckling
- **发表**: 2026-03-03  ·  **类别**: cs.RO, cs.LG, cs.MA
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, robots are supposed to learn from demonstrations of the desired behavior. Most of the work in imitation learning for swarm robotics provides the demonstrations as rollouts of an existing policy. In this work, we provide a framework based on generative adversarial imitation learning that aims to learn collective behaviors from human de…

### 5. End-to-End Deep Imitation Learning: Robot Soccer Case Study

- **arXiv**: [1807.09205v1](https://arxiv.org/abs/1807.09205v1)  ·  **PDF**: [link](https://arxiv.org/pdf/1807.09205v1)
- **作者**: Okan Aşık, Binnur Görer, H. Levent Akın
- **发表**: 2018-06-28  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, behavior learning is generally done using the features extracted from the demonstration data. Recent deep learning algorithms enable the development of machine learning methods that can get high dimensional data as an input. In this work, we use imitation learning to teach the robot to dribble the ball to the goal. We use B-Human robo…

### 6. DPGS-SLAM: Diffusion-Prior and Provenance-Aware Monocular Gaussian Splatting SLAM for Dynamic Visual Sensing

- **arXiv**: [2611.12038v2](https://arxiv.org/abs/2611.12038v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.12038v2)
- **作者**: Yifan Luo, Takafumi Matsumaru, Vibekananda Dutta et al.
- **发表**: 2026-11-09  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: This paper presents DPGS-SLAM (Diffusion-Prior and Provenance-Aware Monocular Gaussian Splatting SLAM) for dense mapping in environments containing dynamic objects. Objects in dynamic motion remain a significant challenge for dense visual SLAM since dynamic observations can contaminate camera tracking and scene reconstruction. Although 3DGS (3D Gaussian spl…

### 7. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 8. A 3D Simulator for Passive SPAD Imaging

- **arXiv**: [2611.33498v1](https://arxiv.org/abs/2611.33498v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.33498v1)
- **作者**: Elia Mergaert, Rong Zou, Roberto Pellerito et al.
- **发表**: 2026-11-24  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Passive single-photon avalanche diode (SPAD) cameras provide short-exposure observations for low-light perception, but collecting task annotations for these sensors remains difficult, and annotated datasets are scarce. We present a 3D simulation pipeline that generates realistic photon detections together with camera-motion and semantic labels, enabling per…

### 9. Unblur-SLAM: Dense Neural SLAM for Blurry Inputs

- **arXiv**: [2603.26810v1](https://arxiv.org/abs/2603.26810v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.26810v1)
- **作者**: Qi Zhang, Denis Rozumny, Francesco Girlanda et al.
- **发表**: 2026-03-26  ·  **类别**: cs.CV, eess.IV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We propose Unblur-SLAM, a novel RGB SLAM pipeline for sharp 3D reconstruction from blurred image inputs. In contrast to previous work, our approach is able to handle different types of blur and demonstrates state-of-the-art performance in the presence of both motion blur and defocus blur. Moreover, we adjust the computation effort with the amount of blur in…

### 10. Query Quantized Neural SLAM

- **arXiv**: [2412.16476v1](https://arxiv.org/abs/2412.16476v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2412.16476v1)
- **作者**: Sijia Jiang, Jing Hua, Zhizhong Han
- **发表**: 2024-12-21  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural implicit representations have shown remarkable abilities in jointly modeling geometry, color, and camera poses in simultaneous localization and mapping (SLAM). Current methods use coordinates, positional encodings, or other geometry features as input to query neural implicit functions for signed distances and color which produce rendering errors to d…

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
- **相关性评分**: 9  ·  **✅ 已研读**
- **摘要**: Geometric light detection and ranging (LiDAR)--inertial simultaneous localization and mapping (SLAM) provides efficient state estimation but lacks the continuous map representation and global refinement capabilities of neural implicit SLAM, while neural implicit methods remain computationally expensive. We propose Lightweight LiDAR--Inertial Neural SLAM (LI…

### 4. What a Drop Reveals: Sim-to-Real Material Estimation for Deformable Objects from Video

- **arXiv**: [2611.34894v1](https://arxiv.org/abs/2611.34894v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.34894v1)
- **作者**: Ziyue Peng, Yanxi Hu, Junyoung Kim et al.
- **发表**: 2026-11-25  ·  **类别**: cs.CV, cs.GR, cs.LG
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: How an object deforms when it hits the ground reveals what it is made of. From a single real video of a drop, we estimate a deformable object's density-normalized stiffness $E/ρ$, and its yield stress $σ_Y/ρ$ when the impact causes plastic deformation, with a feed-forward predictor trained only in simulation. Real videos carry no material labels, so such pr…

### 5. Evaluation of Front-End Feature Matching for Lunar Visual SLAM

- **arXiv**: [2610.30774v1](https://arxiv.org/abs/2610.30774v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30774v1)
- **作者**: Guillem Casadesus Vila, Grace Gao
- **发表**: 2026-10-22  ·  **类别**: cs.CV
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Lunar rovers will primarily rely on cameras for localization until navigation satellite services are deployed, and will continue to need them afterwards for relative navigation, hazard detection, and surface operations. Visual odometry (VO) and Simultaneous Localization and Mapping (SLAM) mostly estimate motion by matching features between frames. However,…

### 6. Smartphone Indoor Localization Enhanced by Hierarchical Multi-Sensor Context Recognition

- **arXiv**: [2610.39691v1](https://arxiv.org/abs/2610.39691v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.39691v1)
- **作者**: Wenhui Feng, Muhan Weng, Jianyu Liu et al.
- **发表**: 2026-10-29  ·  **类别**: cs.LG, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Smartphone indoor localization requires low-cost, robust positioning across scene transitions and phone-use variations. Pedestrian dead reckoning (PDR) enables infrastructure-free deployment but accumulates errors from heading drift, structural transitions, and carrying-mode changes. Existing methods often treat contextual cues as a single event stream or l…

### 7. Line-Augmented cuVSLAM: Robust Visual Odometry in Low-Texture Environments

- **arXiv**: [2610.20958v1](https://arxiv.org/abs/2610.20958v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20958v1)
- **作者**: Dara Molloy, Terry Wu, Wonju Lee et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Autonomous mobile robots in warehouses and production facilities operate in precisely the environments that defeat point-feature visual odometry: featureless aisles, uniform walls, repetitive racking and specular floors. Such environments are, however, rich in straight-edge structure: rack uprights, door frames, wall junctions and cabinet outlines present h…

### 8. RTISSLAM-3D: Full 6-DoF SLAM With an In-Air 3D Imaging Sonar

- **arXiv**: [2610.22552v1](https://arxiv.org/abs/2610.22552v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.22552v1)
- **作者**: Jan Steckel, Vincent Katter, Wouter Jansen
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
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

### 1. Part-wise Certified State Estimation of Articulated Objects from Passive Stereo

- **arXiv**: [2611.30646v1](https://arxiv.org/abs/2611.30646v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.30646v1)
- **作者**: Orion Desbonnet, Kei Higuchi, Alex Sykes et al.
- **发表**: 2026-11-23  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Robots in manufacturing often handle thin, hinged objects known from CAD models that change shape during the task, like folding cartons. Monitoring such tasks requires estimating the object's articulation state, its pose and the shape of any semi-deformable part. Learning-based estimators generalise across objects but lose precision while handling thin part…

## 🤏 软体机器人 / 柔性控制 (6 篇)

### 1. PneuGen: Task-Driven Agentic Co-Design of Soft Pneumatic Robots

- **arXiv**: [2611.13344v1](https://arxiv.org/abs/2611.13344v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.13344v1)
- **作者**: Shaohong Zhong, Marco Pontin, Perla Maiolino
- **发表**: 2026-11-09  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Task-driven design of soft robots requires the consideration of factors such as geometry, morphology, material properties, and actuation, resulting in a large and complex design space that is challenging to explore. Computational optimisation methods leverage signals from simulation to iteratively improve designs to achieve task objectives. However, these m…

### 2. Accelerated Reinforcement Learning for Soft Robotics: Hours Instead of Years

- **arXiv**: [2611.11718v1](https://arxiv.org/abs/2611.11718v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.11718v1)
- **作者**: Roshan S. Kaundinya, Hehui Zheng, Robert K. Katzschmann et al.
- **发表**: 2026-11-09  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Reinforcement learning (RL) requires large amounts of interaction data or a reliable simulator, both hard to obtain for nonlinear soft robotic hardware. Recent work shows that a time-scale separation inherent to soft robot dynamics justifies their reduction to low-dimensional invariant manifolds, known as adiabatic spectral submanifolds (aSSMs). We demonstr…

### 3. Ferrofluid Shape Control with Deep Reinforcement Learning

- **arXiv**: [2611.25232v1](https://arxiv.org/abs/2611.25232v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.25232v1)
- **作者**: Anthony Czubarow, Antonio Terpin, Raffaello D'Andrea
- **发表**: 2026-11-18  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Ferrofluids are liquids containing magnetic nanoparticles, enabling shape control through external magnetic fields. This deformability supports their use as soft robotic bodies that can navigate confined spaces and manipulate objects. Their nonlinear continuum dynamics, however, make reliable control challenging. Existing work shows how spatial magnetic fie…

### 4. Actuation and Control of Passive Tendon-Driven Soft Extensions Through Rigid Manipulator Motion

- **arXiv**: [2611.15386v1](https://arxiv.org/abs/2611.15386v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.15386v1)
- **作者**: Ignacio Cuiral-Zueco, Gonzalo López-Nicolás, Youcef Mezouar
- **发表**: 2026-11-11  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Industrial manipulators offer reach and precision but can damage nearby structures in confined spaces. Soft robots provide compliant contact but typically have limited reach. Rigid-soft systems combine their advantages, although they often require dedicated actuation and control hardware. We propose actuating a passive tendon-driven soft extension through m…

### 5. SunLightBots: Turning sunlight into self-sustained, high-power motion in soft robots

- **arXiv**: [2611.14729v1](https://arxiv.org/abs/2611.14729v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.14729v1)
- **作者**: Yoo Jin Lee, Melanie Torres Crespo, Zhongxiao Deng et al.
- **发表**: 2026-11-10  ·  **类别**: cs.RO, cond-mat.soft, physics.app-ph
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Soft robots built from active materials can directly convert environmental stimuli into motion, offering a route to energy autonomy and embodied control. However, environmental energy is generally harvested at low power, whereas rapid, mechanically demanding actions require high mechanical output power. Reconciling this mismatch while sustaining self-regula…

### 6. DeepSoMo: Deformable Object Motion Estimation under Proprioceptive Partial Observability via Predictive Latent Dynamics

- **arXiv**: [2611.11242v1](https://arxiv.org/abs/2611.11242v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.11242v1)
- **作者**: Hanwen Zhao, Weicheng Dai, Luoyao Chen et al.
- **发表**: 2026-11-08  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Estimating the motion of deformable bodies in soft robotics from proprioceptive sensing is challenging due to partial observability, as internal observations provide only indirect access to global motion, contact, and shape evolution. In such settings, instantaneous observations are insufficient, and accurate estimation requires temporally consistent latent…

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
1. [Ego2Real: Learning Bimanual Dexterous Manipulation from Egocentric Visuo-Tactile Demonstrations](https://arxiv.org/abs/2611.32101v1) — score 19
2. [Real2Worlds2Real: Scaling Self-Improving Agentic Real2Sim2Real for Robot Manipulation](https://arxiv.org/abs/2611.31098v1) — score 19
3. [LocoMuJoCo: A Comprehensive Imitation Learning Benchmark for Whole-Body Control](https://arxiv.org/abs/2611.26293v2) — score 19

> 筛选说明:本次 Top 3 已排除(已研读跳过 1 篇、综述跳过 1 篇)。

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
