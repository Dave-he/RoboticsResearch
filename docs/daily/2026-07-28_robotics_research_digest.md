# 机器人研究每日摘要 · 2026-07-28

> 自动生成,共 89 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (6 篇)

### 1. A Motion-Aware Vector Quantization Framework with Centroid Reuse for Efficient VLA Inference

- **arXiv**: [2607.24148v1](https://arxiv.org/abs/2607.24148v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.24148v1)
- **作者**: Zhuoran Song, Haozhe Jiang, Chunyu Qi et al.
- **发表**: 2026-07-27  ·  **类别**: cs.AI
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models have demonstrated strong potential for embodied AI, yet their high inference latency on GPUs limits real-time deployment. Existing accelerators, such as Dadu-Corki, improve efficiency but treat VLA models as full-precision workloads, leaving substantial redundancy in both memory and computation underexploited. In this pap…

### 2. WCM: World-Cognition Model for Generalizable Human-Robot Interaction

- **arXiv**: [2607.22999v1](https://arxiv.org/abs/2607.22999v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.22999v1)
- **作者**: Yuzhen Chen, KC Zhou
- **发表**: 2026-07-25  ·  **类别**: cs.RO, cs.AI, cs.HC
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Language agents can now interact fluently with users in software, but robots still struggle to bring comparable interaction to physical tasks. Current robot-control paradigms, including vision-language-action policies and world-model-based planners, are mainly optimized for instruction execution, leaving users with little visibility into why an action is ch…

### 3. Artificial Foveated Perception for Mitigating Shortcut Learning in Robotic Foundation Models

- **arXiv**: [2607.10655v1](https://arxiv.org/abs/2607.10655v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.10655v1)
- **作者**: Xiatao Sun, Yuan Zhuang, Mateo Sanchez Lopez Negrete et al.
- **发表**: 2026-07-12  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Robotic foundation models have recently made substantial progress in multi-task capability, cross-embodiment transfer, and language-conditioned control. Yet robust deployment across diverse real-world settings remains difficult, in part because policies often fail to distinguish causally relevant visual structure from spurious scene-level correlations. We i…

### 4. FutureRTC: Real-Time Robot Execution with Anticipatory-Conditioned Action Chunking

- **arXiv**: [2607.24008v1](https://arxiv.org/abs/2607.24008v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.24008v1)
- **作者**: Hai Jiang, Yixian Zou, Binbin Liang et al.
- **发表**: 2026-07-27  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Real-time deployment of Vision-Language-Action (VLA) policies necessitates asynchronous execution, wherein subsequent action chunks are computed concurrently with the execution of the current chunk, leading to prediction-execution misalignment and manifesting as inter-chunk discontinuities. Existing methods either superficially smooth chunk boundaries, requ…

### 5. MulRobBench: A Decision-Level Benchmark for Safe and Security-Policy-Compliant Multimodal UAV Agents

- **arXiv**: [2607.23870v1](https://arxiv.org/abs/2607.23870v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.23870v1)
- **作者**: Belal S. Alsinglawi, Weizheng Wang, Junyi Wu et al.
- **发表**: 2026-07-26  ·  **类别**: cs.MA, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Smart-city airspace is transforming Uncrewed Aerial Vehicles (UAVs) from passive sensing platforms into cyber-physical decision makers that must follow operational rules under degraded observations and ambiguous language. Existing UAV and multimodal benchmarks evaluate perception, navigation, collaboration, and reasoning, but few assess whether physical evi…

### 6. LabRobFail: A Benchmark for Robotic Failure Analysis in Chemical Self-driving Laboratories

- **arXiv**: [2607.23704v1](https://arxiv.org/abs/2607.23704v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.23704v1)
- **作者**: Haobo Wang, Baoli Sun, Anqi Zou et al.
- **发表**: 2026-07-26  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: The deployment of embodied agents in self-driving laboratories could accelerate scientific discovery, yet their reliability is constrained by the irreversible and safety-critical nature of chemical experiments. Progress is further hindered by scarce failure data and the lack of fine-grained evaluation protocols. To address these challenges, we introduce Lab…

## 🌐 具身智能 / 机器人基础模型 (6 篇)

### 1. Zero-Shot Mission-Level Evaluation for Aerial MLLM Agents

- **arXiv**: [2607.22014v1](https://arxiv.org/abs/2607.22014v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.22014v1)
- **作者**: Suman Navaratnarajah, Taehyoung Kim, Jona Ruthardt et al.
- **发表**: 2026-07-24  ·  **类别**: cs.AI, cs.CL, cs.CV
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Multimodal Large Language Models (MLLMs) are emerging as core reasoning modules for embodied agents, yet it remains unclear how well general-purpose models can solve long-horizon embodied tasks from a single high-level instruction. We introduce MissionBench, a benchmark for mission-level evaluation of MLLMs in aerial 3D environments. It comprises 120 missio…

### 2. VoLN: Vision-Only Long-Horizon Navigation---Paradigm, Benchmark, and Method

- **arXiv**: [2607.21400v1](https://arxiv.org/abs/2607.21400v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.21400v1)
- **作者**: Jiabin Lou, Haopeng Wang, Yuanshuai Wang et al.
- **发表**: 2026-07-23  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Vision-and-Language Navigation (VLN) enables embodied agents to follow natural-language instructions. However, route-level instructions commonly encode spatial priors, such as orientation, distance, and layout, that are not explicitly available from onboard sensing at deployment in open, GPS-denied environments. Benchmark performance under such interfaces t…

### 3. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 4. Athena-Brain Technical Report: An Efficient Robot Brain for General Intelligence and Embodied Interaction

- **arXiv**: [2607.18985v2](https://arxiv.org/abs/2607.18985v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.18985v2)
- **作者**: Jialian Li, Junhong Liu, Yuchen Cao et al.
- **发表**: 2026-07-21  ·  **类别**: cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Large language models (LLMs) have demonstrated remarkable capabilities in language understanding, reasoning, and world knowledge. As embodied agents become increasingly capable, there is a growing demand for compact models that can serve as an on-device brain, preserving the broad general intelligence of LLMs while enabling effective high-level interaction…

### 5. PGN: Design and Implementation of a Vision-Language Navigation System Based on Pangu Multimodal Foundation Model

- **arXiv**: [2607.17806v1](https://arxiv.org/abs/2607.17806v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.17806v1)
- **作者**: Li Xian, Mingxi Li, Yizheng Wang et al.
- **发表**: 2026-07-20  ·  **类别**: cs.AI
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Vision-Language Navigation (VLN) requires an embodied agent to interpret a natural-language instruction and predict actions from temporally ordered visual observations. Adapting a multimodal large language model to VLN requires visual-language alignment, compact temporal inputs, action-space grounding, and stable training on the target hardware. This techni…

### 6. Hypothesis-driven Model Expansion under Uncertainty for Open-World Robot Planning

- **arXiv**: [2607.06501v1](https://arxiv.org/abs/2607.06501v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06501v1)
- **作者**: Anxing Xiao, Hanbo Zhang, Tianrun Hu et al.
- **发表**: 2026-07-07  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: We consider an open-world planning setting in which service robots must operate in unknown environments with incomplete knowledge of objects and actions. Traditional closed-world approaches with pre-programmed knowledge bases fail when robots encounter unexpected situations and tasks, posing a fundamental challenge for autonomous knowledge expansion in huma…

## 🦵 人形 / 足式机器人 (26 篇)

### 1. Real2Sim2Real for Vision-Language-Action Manipulation: An AMD ROCm-Based Pipeline

- **arXiv**: [2607.22997v1](https://arxiv.org/abs/2607.22997v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.22997v1)
- **作者**: Qing Yang, Xun Wang, Ziguan Wang et al.
- **发表**: 2026-07-25  ·  **类别**: cs.RO, cs.AI, cs.GR
- **相关性评分**: 27  ·  **🔥 read_now**
- **摘要**: Physical AI -- the integration of large vision-language-action (VLA) models with embodied agents that act in the real world -- has emerged as the next major frontier for AI, echoed by industry leaders such as Jensen Huang (``the next big thing is Physical AI, AI with a body,'' GTC Paris, June 2025) and Dr. Lisa Su (`we're entering the world of Physical AI .…

### 2. TAC-LOCO: Unified Whole-Body Control for Quadrupedal TACtile-Informed LOCO-Manipulation

- **arXiv**: [2607.10132v2](https://arxiv.org/abs/2607.10132v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.10132v2)
- **作者**: Muqun Hu, Yuhao Zhou, Kabir Ray Malik et al.
- **发表**: 2026-07-11  ·  **类别**: cs.RO
- **相关性评分**: 22  ·  **🔥 read_now**
- **摘要**: Dynamic loco-manipulation requires legged robots to coordinate whole-body motion while maintaining stable physical interaction with grasped objects under uncertain external forces. While tactile sensing has been widely studied for robotic manipulation, its role in dynamic whole-body control remains largely unexplored. Existing works without tactile feedback…

### 3. Isaac Sim-to-Real: Reinforcement Learning based Locomotion for Quadrupeds

- **arXiv**: [2607.18135v1](https://arxiv.org/abs/2607.18135v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.18135v1)
- **作者**: Jordan Dowdy, Jean Chagas Vaz
- **发表**: 2026-07-20  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: Learning-based approaches to locomotion have risen in popularity in recent years, showing the capability for complex legged locomotion and whole-body control. Reinforcement learning (RL), the primary learning-based approach for locomotion, often utilizes a high-performance simulation tool, providing a controlled and efficient training and development enviro…

### 4. Handroid: Bridging Dexterous Hand and Humanoid

- **arXiv**: [2607.16187v1](https://arxiv.org/abs/2607.16187v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.16187v1)
- **作者**: Ruogu Li, Chenyang Ma, Sikai Li et al.
- **发表**: 2026-07-17  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Dexterous hands and humanoid robots are typically developed as distinct embodiments: the former enable contact-rich manipulation at the object scale, whereas the latter provide mobility and whole-body interaction in human-centered environments. We introduce \textbf{Handroid}, a desktop-scale dual-embodiment robot that integrates both capabilities within a s…

### 5. A Minimalist Retargeting-Guided Reinforcement Learning Recipe for Dexterous Manipulation

- **arXiv**: [2607.11874v1](https://arxiv.org/abs/2607.11874v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.11874v1)
- **作者**: Yunhai Feng, Natalie Leung, Jiaxuan Wang et al.
- **发表**: 2026-07-13  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Recent work in humanoid whole-body control has found success with a simple recipe: retarget human motion to robot kinematic references, then train policies via reinforcement learning (RL) to track them. But how does this recipe transfer to dexterous manipulation? The answer is not obvious, as manipulation involves complex, contact-rich dynamics and requires…

### 6. The Quadruped Soft Tail: Compliant Grasping and Swabbing for Contamination Surveys in Harsh Environments

- **arXiv**: [2606.30900v2](https://arxiv.org/abs/2606.30900v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.30900v2)
- **作者**: Harald Minde Hansen, Nandita Gallacher, Kristin Y. Pettersen et al.
- **发表**: 2026-06-29  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Beryllium contamination surveys in radioactive areas are challenging for robots in environments cluttered with cables and electronics. To address this problem, we have developed a novel quadruped system augmentation: A lightweight, soft, and compliant tendon-actuated robotic tail mounted on a quadruped robot. The tail features a hollow, flexible backbone an…

### 7. PAKE: Learning Whole-Body Loco-Manipulation with Partial Kinematic Embeddings

- **arXiv**: [2607.11041v1](https://arxiv.org/abs/2607.11041v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.11041v1)
- **作者**: Zhengmao He, Moonkyu Jung, Hyeongjun Kim et al.
- **发表**: 2026-07-13  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Loco-manipulation has recently shown promising capabilities; however, achieving high-precision control, managing the high-dimensional action space induced by many degrees of freedom (DoFs), and fully exploiting the inherent redundancy of whole-body systems remain challenging. In this paper, we propose a novel whole-body control framework that effectively ad…

### 8. Optimization of sim-to-real transfer in the humanoid robot NICO

- **arXiv**: [2607.18210v1](https://arxiv.org/abs/2607.18210v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.18210v1)
- **作者**: Juraj Gavura, Igor Farkaš
- **发表**: 2026-07-20  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Robotic grasping requires accurate coordination between visual perception, object localization, inverse kinematics, and hand control. However, when movements planned in simulation are executed on a physical robot, the sim-to-real gap can cause small positioning errors that prevent successful grasping. In our previous work, we introduced a low-cost haptic ca…

### 9. Immersive Social Interaction with VR and LLM-Assisted Humanoids

- **arXiv**: [2607.07430v1](https://arxiv.org/abs/2607.07430v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.07430v1)
- **作者**: Niraj Pudasaini, Geeta Chandra Raju Bethala, Pranav Doma et al.
- **发表**: 2026-07-08  ·  **类别**: cs.RO, eess.SY
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Humanoid robots can extend human presence to remote, constrained, or hazardous environments, but existing teleoperation interfaces often require physically demanding motion tracking or cognitively demanding low-level control. This paper presents an immersive teleoperation framework that integrates voice-controlled locomotion, VR-based manipulation, and bidi…

### 10. Motion Primitive Discovery in a Humanoid Robot via Self-Organising Maps for Phase Recognition

- **arXiv**: [2607.18737v1](https://arxiv.org/abs/2607.18737v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.18737v1)
- **作者**: Radovan Gregor, Igor Farkaš
- **发表**: 2026-07-21  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Understanding the computational basis of action recognition is a central challenge in social cognition as well as in human-robot interaction. Inspired by the Mirror Neuron System (MNS), we propose a two-level architecture for motor primitive discovery and online phase recognition applied to the NICO humanoid robot. At the first level, two Self-Organising Ma…

## 🦾 操控 / 灵巧手 / 抓取 (31 篇)

### 1. DexVerse: A Modular Benchmark for Multi-Task, Multi-Embodiment Dexterous Manipulation

- **arXiv**: [2607.08751v1](https://arxiv.org/abs/2607.08751v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.08751v1)
- **作者**: Yunchao Yao, Zhuxiu Xu, Tianqi Zhang et al.
- **发表**: 2026-07-09  ·  **类别**: cs.RO
- **相关性评分**: 21  ·  **🔥 read_now**
- **摘要**: Building general-purpose dexterous manipulation policies requires benchmarks that go beyond isolated tasks to systematically evaluate policies across diverse interaction modes, sensory conditions, and robot embodiments. However, existing benchmarks remain limited in task and data diversity, embodiment coverage, or controllable visual variation, hindering st…

### 2. Data Pyramid for Embodied Manipulation

- **arXiv**: [2607.24744v1](https://arxiv.org/abs/2607.24744v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.24744v1)
- **作者**: Yifan Ye, Yankai Fu, Yaoxu Lv et al.
- **发表**: 2026-07-27  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 20  ·  **🔥 read_now**
- **摘要**: Multimodal foundation models learned to see and to speak by consuming the whole internet. Embodied agents admit no such shortcut, since they require data that couple observations with physical states and actions. These signals can be provided, to varying degrees, by multiple data sources. In this work, we organize the embodied data ecosystem as a "pyramid"…

### 3. Industrial Dexterity Benchmark: A Hardware-Software Benchmarking Platform for Industrial Dexterous Manipulation

- **arXiv**: [2607.14021v2](https://arxiv.org/abs/2607.14021v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.14021v2)
- **作者**: Honglu He, Jacob Laufer, Zhiwu Zheng et al.
- **发表**: 2026-07-15  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation remains a critical bottleneck in industrial automation; tasks such as cable routing, connector insertion, and precision assembly still rely heavily on manual labor despite decades of robotics research. This work presents a progression from classical, modular robotics pipelines toward an end-to-end multimodal imitation-learning framewo…

### 4. Effective Parameters, Real Behavior: Renormalization for Robotics -- From Infinite Electron Mass to Sim-to-Real Gap

- **arXiv**: [2607.24079v1](https://arxiv.org/abs/2607.24079v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.24079v1)
- **作者**: Youran Sun, Jiaxuan Guo, Xingyu Ren et al.
- **发表**: 2026-07-27  ·  **类别**: cs.RO, hep-th
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Bridging the sim-to-real gap is a central problem in robotics, and the prevailing approach is to build increasingly accurate simulators. Here, we propose another approach based on renormalization: using effective, resolution-dependent parameters to absorb details omitted by the simulator and reproduce real behavior. These parameters may differ from measured…

### 5. τ: Learning Touch-Augmented Vision-Language-Action Models from Future Visual Supervision

- **arXiv**: [2607.24485v1](https://arxiv.org/abs/2607.24485v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.24485v1)
- **作者**: Ning Cheng, Jinan Xu, Wanlin Li et al.
- **发表**: 2026-07-27  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Learning the informative tactile representation while effectively adapting it to pretrained Vision-Language-Action (VLA) models remains challenging at both the data and modeling levels. At the data level, limited task-specific demonstrations constrain representation quality, whereas large-scale pretraining incurs substantial costs. At the modeling level, ex…

### 6. MEVION: Low-Cost Open-Source Data Collection System for Powerful and High-Speed Dual-Arm Manipulation

- **arXiv**: [2607.17970v1](https://arxiv.org/abs/2607.17970v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.17970v1)
- **作者**: Kento Kawaharazuka, Yoshiki Obinata, Hirokazu Ishida et al.
- **发表**: 2026-07-20  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: The global competition for developing robotic foundation models is intensifying. Among the data collection systems used for dual-arm robots, ALOHA is representative of being low-cost and open-source, and is widely adopted by researchers as a de facto standard. However, due to its limited ability to generate high forces and speeds, it is difficult to handle…

### 7. MIDAS Hand: Modular low-Impedance Direct-drive Anthropomorphic Sensing Hand

- **arXiv**: [2607.14487v1](https://arxiv.org/abs/2607.14487v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.14487v1)
- **作者**: Alvin Zhu, Mingzhang Zhu, Beom Jun Kim et al.
- **发表**: 2026-07-16  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation is limited not only by algorithms but by a shortage of accessible hand hardware that combines human-scale morphology, ease of manufacturing or maintenance, tactile sensing, and practical cost. Existing dexterous hands tend to optimize some of these properties at the expense of others. We present MIDAS Hand, a low-cost, open-source, hu…

### 8. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

### 9. WSA$_1$: a 3D-Centric World-Spatial-Action Model for Generalizable Robot Control

- **arXiv**: [2607.03941v1](https://arxiv.org/abs/2607.03941v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.03941v1)
- **作者**: Jiahao Jiang, Jianing Zhang, Zhenhan Yin et al.
- **发表**: 2026-07-04  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Recent advances in embodied AI have established robot foundation models (RFMs) as the dominant approach for generalist robotic systems to date. By leveraging imitation learning on extensive robot demonstrations, RFMs have achieved impressive capabilities in mapping visual observations and language instructions to continuous robotic actions. However, current…

### 10. AnyDexRT: Calibration-Free Dexterous Hand Retargeting with Few-Shot Human Guidance

- **arXiv**: [2607.08341v1](https://arxiv.org/abs/2607.08341v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.08341v1)
- **作者**: Chenxi Wang, Ying Feng, Hongjie Fang et al.
- **发表**: 2026-07-09  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Teleoperation is a key interface for controlling dexterous robotic hands and collecting demonstrations for imitation learning. Its effectiveness largely depends on kinematic retargeting, which maps operator hand motions to feasible and intuitive robot hand motions. Existing methods often require hand-crafted objectives, precise calibration, or global shape…

## 🎓 模仿学习 / 强化学习 (14 篇)

### 1. FORGE-plus: Force-Budgeted Recovery for Contact-Rich Assembly with a Frozen LLM Supervisor

- **arXiv**: [2607.21227v1](https://arxiv.org/abs/2607.21227v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.21227v1)
- **作者**: Kyupaeck Jeff Rah, Midum Oh
- **发表**: 2026-07-23  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Force-conditioned reinforcement learning (RL) enables tight-clearance assembly under a commanded force ceiling, but practical deployment requires determining an appropriate force limit for each object and recovering from insertion failures without exceeding it. We present a two-layer framework in which a frozen, text-only large language model (LLM) assigns…

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

### 4. GeoGS-SLAM: Geometry-Only Gaussian Splatting for Dense Monocular SLAM

- **arXiv**: [2607.07452v1](https://arxiv.org/abs/2607.07452v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.07452v1)
- **作者**: Lipu Zhou, Yaoyun Kang, Junxiang Pang et al.
- **发表**: 2026-07-08  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Dense visual SLAM is a fundamental problem in robotics. Recent advances in 3DGS have demonstrated its potential for dense SLAM. Existing 3DGS frameworks focus on both appearance and geometry modeling. However, scene geometry is typically more critical for SLAM than novel view synthesis because downstream robotic tasks, such as navigation and obstacle avoida…

### 5. Why does Deep Learning Improve Visual SLAM?

- **arXiv**: [2607.06023v1](https://arxiv.org/abs/2607.06023v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06023v1)
- **作者**: Giovanni Cioffi, Davide Scaramuzza
- **发表**: 2026-07-07  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Visual SLAM is a well-established technology utilized in a wide range of real-world applications. However, its performance still degrades under challenging visual conditions, such as low texture, severe motion blur, and poor illumination. Systems based on deep learning outperform classical geometry-based ones and achieve state-of-the-art results by combinin…

### 6. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 7. Anticipatory Risk-Guided Reinforcement Learning for Safe Flight Through Dynamic Clutter

- **arXiv**: [2607.23565v1](https://arxiv.org/abs/2607.23565v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.23565v1)
- **作者**: Yuchao Mei, Guohao Zhang, Luxia Ai et al.
- **发表**: 2026-07-26  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Safe quadrotor navigation in cluttered and dynamic environments depends not only on instantaneous geometric perception, but more critically on anticipating collision risks induced by relative motion. Conventional modular pipelines frequently suffer from perception latency, while end-to-end learning methods relying on implicit scalar rewards often struggle t…

### 8. Unblur-SLAM: Dense Neural SLAM for Blurry Inputs

- **arXiv**: [2603.26810v1](https://arxiv.org/abs/2603.26810v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.26810v1)
- **作者**: Qi Zhang, Denis Rozumny, Francesco Girlanda et al.
- **发表**: 2026-03-26  ·  **类别**: cs.CV, eess.IV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We propose Unblur-SLAM, a novel RGB SLAM pipeline for sharp 3D reconstruction from blurred image inputs. In contrast to previous work, our approach is able to handle different types of blur and demonstrates state-of-the-art performance in the presence of both motion blur and defocus blur. Moreover, we adjust the computation effort with the amount of blur in…

### 9. Query Quantized Neural SLAM

- **arXiv**: [2412.16476v1](https://arxiv.org/abs/2412.16476v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2412.16476v1)
- **作者**: Sijia Jiang, Jing Hua, Zhizhong Han
- **发表**: 2024-12-21  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural implicit representations have shown remarkable abilities in jointly modeling geometry, color, and camera poses in simultaneous localization and mapping (SLAM). Current methods use coordinates, positional encodings, or other geometry features as input to query neural implicit functions for signed distances and color which produce rendering errors to d…

### 10. Hilti-Trimble-Oxford Dataset: 360 Visual-Inertial Benchmark with Floor Plan Priors for SLAM and Localization

- **arXiv**: [2607.06464v1](https://arxiv.org/abs/2607.06464v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06464v1)
- **作者**: Samuele Centanni, Yuhao Zhang, Yifu Tao et al.
- **发表**: 2026-07-07  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Automated progress monitoring on construction sites is an active area of research and development. Robot and human-carried mapping systems have been developed to build 3D maps of building and infrastructure projects. While LiDAR-based mapping systems achieve high accuracy, the cost of LiDAR can be prohibitive. Consumer-grade cameras with wide field of view…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (6 篇)

### 1. Desc++: Efficient Descriptor Enhancement for Data Association in Existing Visual SLAM Systems

- **arXiv**: [2607.11099v1](https://arxiv.org/abs/2607.11099v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.11099v1)
- **作者**: Ting-Wei Ou, Huang-Ting Lin, Kuu-Young Young
- **发表**: 2026-07-13  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Reliable visual data association is fundamental to visual SLAM (V-SLAM), as it directly determines the quality of the camera pose estimation and map consistency. However, the handcrafted descriptors used by most mature real-time systems degrade under illumination and viewpoint changes, while learning-based front-ends that address this weakness typically req…

### 2. DROID-ANCHOR: Odometry-Anchored Recurrent Metric Depth Estimation

- **arXiv**: [2607.17058v1](https://arxiv.org/abs/2607.17058v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.17058v1)
- **作者**: Yuxuan Chen, Brook Du
- **发表**: 2026-07-19  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Precise metric depth estimation is fundamental for autonomous robot navigation, yet monocular systems inherently suffer from scale ambiguity and scale drift. While recent recurrent flow-based SLAM systems have demonstrated state-of-the-art robustness, they remain scale-ambiguous. In this paper, we propose Metric-DROID, an end-to-end recurrent architecture t…

### 3. GLidE-SLAM: GL-Accelerated Indirect-Direct Embedded SLAM

- **arXiv**: [2607.16897v1](https://arxiv.org/abs/2607.16897v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.16897v1)
- **作者**: Carlos A. Pinheiro de Sousa, Heiko Hamann, Oliver Deussen
- **发表**: 2026-07-18  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: With the growing demand for robotics, autonomous drones, and wearable extended reality systems, the deployment of Visual SLAM on embedded devices remains challenging. Tracking must sustain high frame rates while preserving compute resources for map extension and maintenance. This paper presents GLidE-SLAM, a monocular hybrid indirect-direct framework that a…

### 4. PLED-VINS: A Point-Line Event-Based Visual Inertial SLAM for Dynamic Environments

- **arXiv**: [2607.07374v1](https://arxiv.org/abs/2607.07374v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.07374v1)
- **作者**: Seunghun Lee, Jihun Nam, Dong-Uk Seo et al.
- **发表**: 2026-07-08  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Dynamic environments remain a fundamental challenge for visual SLAM, where unreliable observations from moving objects and rapid motion degrade state estimation accuracy. Although event cameras preserve fine-grained spatio-temporal information, most existing event-based SLAM frameworks still assume static scenes and lack approaches to estimate the reliabili…

### 5. Geodesic Flow Matching for Denoising High-Dimensional Structured Representations

- **arXiv**: [2606.00248v1](https://arxiv.org/abs/2606.00248v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.00248v1)
- **作者**: Karim Habashy, Chris Eliasmith
- **发表**: 2026-05-29  ·  **类别**: cs.AI
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Vector Symbolic Algebras (VSAs) enable robust neurosymbolic reasoning by encoding symbolic information into high-dimensional distributed representations. For continuous domains, Spatial Semantic Pointers (SSPs) extend this framework by mapping variables onto continuous toroidal manifolds. However, standard approaches like Flow Matching assume a flat Euclide…

### 6. HI-SLAM2: Geometry-Aware Gaussian SLAM for Fast Monocular Scene Reconstruction

- **arXiv**: [2411.17982v3](https://arxiv.org/abs/2411.17982v3)  ·  **PDF**: [link](https://arxiv.org/pdf/2411.17982v3)
- **作者**: Wei Zhang, Qing Cheng, David Skuddis et al.
- **发表**: 2024-11-27  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: We present HI-SLAM2, a geometry-aware Gaussian SLAM system that achieves fast and accurate monocular scene reconstruction using only RGB input. Existing Neural SLAM or 3DGS-based SLAM methods often trade off between rendering quality and geometry accuracy, our research demonstrates that both can be achieved simultaneously with RGB input alone. The key idea…

---

## 📋 本日操作建议

**建议今日深读 (Top 3):**
1. [Real2Sim2Real for Vision-Language-Action Manipulation: An AMD ROCm-Based Pipeline](https://arxiv.org/abs/2607.22997v1) — score 27
2. [TAC-LOCO: Unified Whole-Body Control for Quadrupedal TACtile-Informed LOCO-Manipulation](https://arxiv.org/abs/2607.10132v2) — score 22
3. [DexVerse: A Modular Benchmark for Multi-Task, Multi-Embodiment Dexterous Manipulation](https://arxiv.org/abs/2607.08751v1) — score 21

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
