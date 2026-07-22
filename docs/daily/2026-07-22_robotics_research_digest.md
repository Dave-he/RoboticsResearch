# 机器人研究每日摘要 · 2026-07-22

> 自动生成,共 87 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (6 篇)

### 1. PhyAgentOS: A Self-Evolving Operating System for Embodied Agents with Decoupled Cognitive Planning and Physical Execution

- **arXiv**: [2607.16636v1](https://arxiv.org/abs/2607.16636v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.16636v1)
- **作者**: Yang Liu, Weixing Chen, Xinshuai Song et al.
- **发表**: 2026-07-18  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Vision-language-action models, world models, and agentic planners each advance physical intelligence, yet their composition lacks a common execution abstraction, shared state, semantic verification, and persistent experience across heterogeneous embodiments. We present PhyAgentOS, a runtime foundation delivering scheduling, verification, memory, benchmarkin…

### 2. Reasoning as a Double-Edged Sword: Architecture and Cross-Stage Robustness in Vision-Language-Action Models

- **arXiv**: [2607.17786v1](https://arxiv.org/abs/2607.17786v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.17786v1)
- **作者**: Tuan Duong Trinh, Naveed Akhtar, Basim Azam
- **发表**: 2026-07-20  ·  **类别**: cs.RO, cs.AI, cs.CR
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Does adding a reasoning step make a Vision-Language-Action (VLA) model more robust to perturbation? Intuitively, a policy that reasons before acting should absorb a perturbed input better than one that maps observations directly to actions. We test this premise head-on across three models that span the reasoning spectrum (no reasoning, a text chain-of-thoug…

### 3. What Do They See? Interpreting Complex Road Scenarios Through the Eyes of Vision-Language-Action Models for Safe and Trustworthy Autonomous Vehicle Learning

- **arXiv**: [2607.16938v1](https://arxiv.org/abs/2607.16938v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.16938v1)
- **作者**: Kalpana Panda, Wesley Maia, Vinti Agarwal et al.
- **发表**: 2026-07-18  ·  **类别**: cs.CV, cs.AI, cs.LG
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: End-to-end autonomous driving models are now able to navigate complex road scenarios, mapping raw sensor observations directly to observed paths for open-loop evaluation and often effective driving in closed-loop evaluation. Yet the internal logic of these safety-critical systems remains largely opaque, due to the complexity of traffic scenes. We propose a…

### 4. Patch Policy: Efficient Embodied Control via Dense Visual Representations

- **arXiv**: [2607.18236v1](https://arxiv.org/abs/2607.18236v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.18236v1)
- **作者**: Gaoyue Zhou, Zichen Jeff Cui, Ada Langford et al.
- **发表**: 2026-07-20  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Pretrained dense visual features from Vision Transformers (ViTs) are powerful yet have been underutilized in robot learning. Modern robot policies either compress each observation into a single global token, or rely on visual backbones trained from scratch, sacrificing both fine-grained spatial detail and the benefits of large-scale visual pre-training. Whi…

### 5. Artificial Foveated Perception for Mitigating Shortcut Learning in Robotic Foundation Models

- **arXiv**: [2607.10655v1](https://arxiv.org/abs/2607.10655v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.10655v1)
- **作者**: Xiatao Sun, Yuan Zhuang, Mateo Sanchez Lopez Negrete et al.
- **发表**: 2026-07-12  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Robotic foundation models have recently made substantial progress in multi-task capability, cross-embodiment transfer, and language-conditioned control. Yet robust deployment across diverse real-world settings remains difficult, in part because policies often fail to distinguish causally relevant visual structure from spurious scene-level correlations. We i…

### 6. STeP: Signal Temporal Logic for Precise Specifications for Action Generation with Vision Language Models

- **arXiv**: [2607.18580v1](https://arxiv.org/abs/2607.18580v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.18580v1)
- **作者**: Kasra Torshizi, Anukriti Singh, Sidharth Mathur et al.
- **发表**: 2026-07-20  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-language-action (VLA) models have shown impressive generalization, but often lack interpretability and can struggle to follow precise natural language instructions that encode spatial, temporal, and logical requirements. We propose a hierarchical framework that uses Signal Temporal Logic (STL) as a shared representation connecting high-level language…

## 🌐 具身智能 / 机器人基础模型 (9 篇)

### 1. SafeRelBench: A Spatial-Relation-Aware Benchmark for Process-Level Safety in VLM-Driven Embodied Agents

- **arXiv**: [2607.14543v1](https://arxiv.org/abs/2607.14543v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.14543v1)
- **作者**: Huaigang Yang, Ya Li, Min Ren et al.
- **发表**: 2026-07-16  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Vision-language models (VLMs) are increasingly used as the reasoning backbone of embodied agents, enabling robots to interpret visual scenes, follow language instructions, and plan multi-step actions. In household environments, however, safety depends not only on recognizing objects, but also on how actions change the physical scene over time. Existing embo…

### 2. VTM-Nav: Hierarchical Visual-Topological Memory for Cross-Episode Object-Goal Navigation

- **arXiv**: [2607.14514v1](https://arxiv.org/abs/2607.14514v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.14514v1)
- **作者**: Xiaoran Xu, Yupeng Wu, Tianyu Xue et al.
- **发表**: 2026-07-16  ·  **类别**: cs.CV, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Object-goal navigation requires an embodied agent to locate and reach an instance of a specified object category in an indoor environment. Recent training-free approaches leverage vision-language models (VLMs) for open-vocabulary semantic reasoning, but are typically evaluated under an episodic protocol that resets all scene-specific state after each episod…

### 3. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 4. Athena-Brain Technical Report: An Efficient Robot Brain for General Intelligence and Embodied Interactio

- **arXiv**: [2607.18985v1](https://arxiv.org/abs/2607.18985v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.18985v1)
- **作者**: Jialian Li, Junhong Liu, Yuchen Cao et al.
- **发表**: 2026-07-21  ·  **类别**: cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Large language models (LLMs) have demonstrated remarkable capabilities in language understanding, reasoning, and world knowledge. As embodied agents become increasingly capable, there is a growing demand for compact models that can serve as an on-device brain, preserving the broad general intelligence of LLMs while enabling effective high-level interaction…

### 5. Text-conditioned Segmentation for Tomato Phenotyping via Procedural Synthetic Data

- **arXiv**: [2607.18576v1](https://arxiv.org/abs/2607.18576v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.18576v1)
- **作者**: Samy Mounir, Mikolaj Cieslak, Najmeddine Dhieb et al.
- **发表**: 2026-07-20  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-based automation is an excellent candidate for reducing manual labor in greenhouse crop production and phenotyping. However, progress is constrained by the lack of annotated training data. Recent advances in vision-based foundational models have shown promising results in zero-shot generalization to novel domains, but their performance drops in compl…

### 6. PGN: Design and Implementation of a Vision-Language Navigation System Based on Pangu Multimodal Foundation Model

- **arXiv**: [2607.17806v1](https://arxiv.org/abs/2607.17806v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.17806v1)
- **作者**: Li Xian, Mingxi Li, Yizheng Wang et al.
- **发表**: 2026-07-20  ·  **类别**: cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-Language Navigation (VLN) requires an embodied agent to interpret a natural-language instruction and predict actions from temporally ordered visual observations. Adapting a multimodal large language model to VLN requires visual-language alignment, compact temporal inputs, action-space grounding, and stable training on the target hardware. This techni…

### 7. When Words Are Safe But Actions Kill: Probing Physical Danger Beyond Text Safety in Hidden-State Risk Space

- **arXiv**: [2607.15218v1](https://arxiv.org/abs/2607.15218v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.15218v1)
- **作者**: Weimeng Wang, Ziqiang Wang, Zihang Zhan et al.
- **发表**: 2026-07-16  ·  **类别**: cs.AI, cs.CR
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Large language models (LLMs) increasingly serve as high-level planners for embodied agents, where linguistically benign instructions can become unsafe once grounded in the physical world. We study whether this physically grounded danger is the same safety problem as ordinary text-level content danger. Through hidden-state direction analysis and random-split…

### 8. Knowing You at First Glance: Inferring Apparent Personality from Faces

- **arXiv**: [2607.14631v1](https://arxiv.org/abs/2607.14631v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.14631v1)
- **作者**: Shuhuan Chen, Xiangyu Zhu, Weisong Zhao et al.
- **发表**: 2026-07-16  ·  **类别**: cs.CV, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Inferring apparent personality from facial images is important in social scenarios for embodied agents in human-robot interaction. Unlike inferring intrinsic personality traits via conversation, this task models first-impression personality perception based solely on facial appearance before interaction begins. Existing studies mainly focus on the Big Five…

### 9. Hypothesis-driven Model Expansion under Uncertainty for Open-World Robot Planning

- **arXiv**: [2607.06501v1](https://arxiv.org/abs/2607.06501v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06501v1)
- **作者**: Anxing Xiao, Hanbo Zhang, Tianrun Hu et al.
- **发表**: 2026-07-07  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: We consider an open-world planning setting in which service robots must operate in unknown environments with incomplete knowledge of objects and actions. Traditional closed-world approaches with pre-programmed knowledge bases fail when robots encounter unexpected situations and tasks, posing a fundamental challenge for autonomous knowledge expansion in huma…

## 🦵 人形 / 足式机器人 (26 篇)

### 1. TAC-LOCO: Unified Whole-Body Control for Quadrupedal TACtile-Informed LOCO-Manipulation

- **arXiv**: [2607.10132v2](https://arxiv.org/abs/2607.10132v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.10132v2)
- **作者**: Muqun Hu, Yuhao Zhou, Kabir Ray Malik et al.
- **发表**: 2026-07-11  ·  **类别**: cs.RO
- **相关性评分**: 22  ·  **🔥 read_now**
- **摘要**: Dynamic loco-manipulation requires legged robots to coordinate whole-body motion while maintaining stable physical interaction with grasped objects under uncertain external forces. While tactile sensing has been widely studied for robotic manipulation, its role in dynamic whole-body control remains largely unexplored. Existing works without tactile feedback…

### 2. Isaac Sim-to-Real: Reinforcement Learning based Locomotion for Quadrupeds

- **arXiv**: [2607.18135v1](https://arxiv.org/abs/2607.18135v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.18135v1)
- **作者**: Jordan Dowdy, Jean Chagas Vaz
- **发表**: 2026-07-20  ·  **类别**: cs.RO
- **相关性评分**: 21  ·  **🔥 read_now**
- **摘要**: Learning-based approaches to locomotion have risen in popularity in recent years, showing the capability for complex legged locomotion and whole-body control. Reinforcement learning (RL), the primary learning-based approach for locomotion, often utilizes a high-performance simulation tool, providing a controlled and efficient training and development enviro…

### 3. Handroid: Bridging Dexterous Hand and Humanoid

- **arXiv**: [2607.16187v1](https://arxiv.org/abs/2607.16187v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.16187v1)
- **作者**: Ruogu Li, Chenyang Ma, Sikai Li et al.
- **发表**: 2026-07-17  ·  **类别**: cs.RO
- **相关性评分**: 20  ·  **🔥 read_now**
- **摘要**: Dexterous hands and humanoid robots are typically developed as distinct embodiments: the former enable contact-rich manipulation at the object scale, whereas the latter provide mobility and whole-body interaction in human-centered environments. We introduce \textbf{Handroid}, a desktop-scale dual-embodiment robot that integrates both capabilities within a s…

### 4. Optimization of sim-to-real transfer in the humanoid robot NICO

- **arXiv**: [2607.18210v1](https://arxiv.org/abs/2607.18210v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.18210v1)
- **作者**: Juraj Gavura, Igor Farkaš
- **发表**: 2026-07-20  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Robotic grasping requires accurate coordination between visual perception, object localization, inverse kinematics, and hand control. However, when movements planned in simulation are executed on a physical robot, the sim-to-real gap can cause small positioning errors that prevent successful grasping. In our previous work, we introduced a low-cost haptic ca…

### 5. Predictive Training with Latent Imagination for Visual Quadruped Navigation

- **arXiv**: [2607.17574v1](https://arxiv.org/abs/2607.17574v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.17574v1)
- **作者**: Yancheng Zhu, Wanli Ma, Chen Han et al.
- **发表**: 2026-07-20  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Reinforcement-learning navigation policies for legged robots select actions reactively from current observations and short-term memory, with limited capacity to anticipate how moving obstacles will evolve in the near future. In dynamic environments, this reactivity causes the robot to respond too late because collision risk depends on short-horizon scene st…

### 6. A Minimalist Retargeting-Guided Reinforcement Learning Recipe for Dexterous Manipulation

- **arXiv**: [2607.11874v1](https://arxiv.org/abs/2607.11874v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.11874v1)
- **作者**: Yunhai Feng, Natalie Leung, Jiaxuan Wang et al.
- **发表**: 2026-07-13  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Recent work in humanoid whole-body control has found success with a simple recipe: retarget human motion to robot kinematic references, then train policies via reinforcement learning (RL) to track them. But how does this recipe transfer to dexterous manipulation? The answer is not obvious, as manipulation involves complex, contact-rich dynamics and requires…

### 7. The Quadruped Soft Tail: Compliant Grasping and Swabbing for Contamination Surveys in Harsh Environments

- **arXiv**: [2606.30900v2](https://arxiv.org/abs/2606.30900v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.30900v2)
- **作者**: Harald Minde Hansen, Nandita Gallacher, Kristin Y. Pettersen et al.
- **发表**: 2026-06-29  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Beryllium contamination surveys in radioactive areas are challenging for robots in environments cluttered with cables and electronics. To address this problem, we have developed a novel quadruped system augmentation: A lightweight, soft, and compliant tendon-actuated robotic tail mounted on a quadruped robot. The tail features a hollow, flexible backbone an…

### 8. World Translation: Minimizing Sim-to-Real Gap with Backward Dynamics Extraction and Unpaired Domain Translation

- **arXiv**: [2607.18154v1](https://arxiv.org/abs/2607.18154v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.18154v1)
- **作者**: Xinchen Yao, Leixin Chang, Hua Chen
- **发表**: 2026-07-20  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: The gap between simulation and reality remains a fundamental challenge in deploying simulation-trained robotic policies in the real world. Real-to-sim methods narrow this gap from the real side, learning transition dynamics from real data to build a more realistic digital world. Learned dynamics models are their dominant instance. Such methods, however, fac…

### 9. PAKE: Learning Whole-Body Loco-Manipulation with Partial Kinematic Embeddings

- **arXiv**: [2607.11041v1](https://arxiv.org/abs/2607.11041v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.11041v1)
- **作者**: Zhengmao He, Moonkyu Jung, Hyeongjun Kim et al.
- **发表**: 2026-07-13  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Loco-manipulation has recently shown promising capabilities; however, achieving high-precision control, managing the high-dimensional action space induced by many degrees of freedom (DoFs), and fully exploiting the inherent redundancy of whole-body systems remain challenging. In this paper, we propose a novel whole-body control framework that effectively ad…

### 10. Immersive Social Interaction with VR and LLM-Assisted Humanoids

- **arXiv**: [2607.07430v1](https://arxiv.org/abs/2607.07430v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.07430v1)
- **作者**: Niraj Pudasaini, Geeta Chandra Raju Bethala, Pranav Doma et al.
- **发表**: 2026-07-08  ·  **类别**: cs.RO, eess.SY
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Humanoid robots can extend human presence to remote, constrained, or hazardous environments, but existing teleoperation interfaces often require physically demanding motion tracking or cognitively demanding low-level control. This paper presents an immersive teleoperation framework that integrates voice-controlled locomotion, VR-based manipulation, and bidi…

## 🦾 操控 / 灵巧手 / 抓取 (26 篇)

### 1. DexVerse: A Modular Benchmark for Multi-Task, Multi-Embodiment Dexterous Manipulation

- **arXiv**: [2607.08751v1](https://arxiv.org/abs/2607.08751v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.08751v1)
- **作者**: Yunchao Yao, Zhuxiu Xu, Tianqi Zhang et al.
- **发表**: 2026-07-09  ·  **类别**: cs.RO
- **相关性评分**: 22  ·  **🔥 read_now**
- **摘要**: Building general-purpose dexterous manipulation policies requires benchmarks that go beyond isolated tasks to systematically evaluate policies across diverse interaction modes, sensory conditions, and robot embodiments. However, existing benchmarks remain limited in task and data diversity, embodiment coverage, or controllable visual variation, hindering st…

### 2. FM-VLA: Force-based Memory for Vision-Language-Action Models in Contact-Rich Manipulation

- **arXiv**: [2607.18231v1](https://arxiv.org/abs/2607.18231v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.18231v1)
- **作者**: Ruicheng Li, Qixiu Li, Ruichun Ma et al.
- **发表**: 2026-07-20  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models have achieved impressive generalization in robotic manipulation, and recent memory-augmented VLAs have relaxed the Markovian assumption by conditioning on past images or language summaries. Vision-based memory approaches address this by conditioning on sampled past image frames, but they are computationally expensive and…

### 3. Industrial Dexterity Benchmark: A Hardware-Software Benchmarking Platform for Industrial Dexterous Manipulation

- **arXiv**: [2607.14021v1](https://arxiv.org/abs/2607.14021v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.14021v1)
- **作者**: Honglu He, Jacob Laufer, Zhiwu Zheng et al.
- **发表**: 2026-07-15  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation remains a critical bottleneck in industrial automation; tasks such as cable routing, connector insertion, and precision assembly still rely heavily on manual labor despite decades of robotics research. This work presents a progression from classical, modular robotics pipelines toward an end-to-end multimodal imitation-learning framewo…

### 4. LAMP: Latent Motion Prior-Guided Real-World Learning for Dexterous Hand Manipulation

- **arXiv**: [2607.06323v1](https://arxiv.org/abs/2607.06323v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06323v1)
- **作者**: Xinye Yang, Zhiyuan Ma, Hongze Yu et al.
- **发表**: 2026-07-07  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Real-world learning for dexterous hands remains brittle because high-dimensional hand actions amplify imitation errors and make reinforcement-learning exploration prone to contact-breaking motion. While combining imitation learning (IL) with online reinforcement learning (RL) can reduce manual supervision, unconstrained exploration in raw hand-action spaces…

### 5. MEVION: Low-Cost Open-Source Data Collection System for Powerful and High-Speed Dual-Arm Manipulation

- **arXiv**: [2607.17970v1](https://arxiv.org/abs/2607.17970v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.17970v1)
- **作者**: Kento Kawaharazuka, Yoshiki Obinata, Hirokazu Ishida et al.
- **发表**: 2026-07-20  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: The global competition for developing robotic foundation models is intensifying. Among the data collection systems used for dual-arm robots, ALOHA is representative of being low-cost and open-source, and is widely adopted by researchers as a de facto standard. However, due to its limited ability to generate high forces and speeds, it is difficult to handle…

### 6. MIDAS Hand: Modular low-Impedance Direct-drive Anthropomorphic Sensing Hand

- **arXiv**: [2607.14487v1](https://arxiv.org/abs/2607.14487v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.14487v1)
- **作者**: Alvin Zhu, Mingzhang Zhu, Beom Jun Kim et al.
- **发表**: 2026-07-16  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation is limited not only by algorithms but by a shortage of accessible hand hardware that combines human-scale morphology, ease of manufacturing or maintenance, tactile sensing, and practical cost. Existing dexterous hands tend to optimize some of these properties at the expense of others. We present MIDAS Hand, a low-cost, open-source, hu…

### 7. TactiDex: A Real-World Tactile-Guided Benchmark for Human-Like Dexterous Manipulation

- **arXiv**: [2607.09190v1](https://arxiv.org/abs/2607.09190v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.09190v1)
- **作者**: Suting Ni, Hanbing Zhang, Zhenyu Wei et al.
- **发表**: 2026-07-10  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Tactile feedback is fundamental to Hand-Object Interaction (HOI), governing contact formation, force regulation, and stable manipulation, making it essential for achieving true human-like dexterous manipulation. Yet, current human-to-robot dexterous transfer pipelines primarily rely on kinematic trajectories, resulting in motion imitation without physically…

### 8. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

### 9. Foresight Residual RL for Long-Horizon Robot Manipulation with Vision-Language-Action Models

- **arXiv**: [2607.16506v1](https://arxiv.org/abs/2607.16506v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.16506v1)
- **作者**: Yuhan Liu, Xinyu Zhang, Litao Liu et al.
- **发表**: 2026-07-17  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) policies offer strong general-purpose manipulation priors, but often fail on tight-tolerance, contact-rich assembly due to long-horizon credit assignment and subtask coupling: a state that is geometrically successful for the current skill can be brittle for downstream skills. We show this failure mode in residual reinforcement l…

### 10. RoboTTT: Context Scaling for Robot Policies

- **arXiv**: [2607.15275v1](https://arxiv.org/abs/2607.15275v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.15275v1)
- **作者**: Yunfan Jiang, Yevgen Chebotar, Ruijie Zheng et al.
- **发表**: 2026-07-16  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Recent robot foundation models operate with single-step or short-history visuomotor context. We introduce Test-Time-Training Robot Policies (RoboTTT), a robot model and training recipe that scale visuomotor context to 8K timesteps, three orders of magnitude beyond state-of-the-art policies, without growing inference latency. At this context length, we unloc…

## 🎓 模仿学习 / 强化学习 (13 篇)

### 1. Generative adversarial imitation learning for robot swarms: Learning from human demonstrations and trained policies

- **arXiv**: [2603.02783v1](https://arxiv.org/abs/2603.02783v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.02783v1)
- **作者**: Mattes Kraus, Jonas Kuckling
- **发表**: 2026-03-03  ·  **类别**: cs.RO, cs.LG, cs.MA
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, robots are supposed to learn from demonstrations of the desired behavior. Most of the work in imitation learning for swarm robotics provides the demonstrations as rollouts of an existing policy. In this work, we provide a framework based on generative adversarial imitation learning that aims to learn collective behaviors from human de…

### 2. End-to-End Deep Imitation Learning: Robot Soccer Case Study

- **arXiv**: [1807.09205v1](https://arxiv.org/abs/1807.09205v1)  ·  **PDF**: [link](https://arxiv.org/pdf/1807.09205v1)
- **作者**: Okan Aşık, Binnur Görer, H. Levent Akın
- **发表**: 2018-06-28  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, behavior learning is generally done using the features extracted from the demonstration data. Recent deep learning algorithms enable the development of machine learning methods that can get high dimensional data as an input. In this work, we use imitation learning to teach the robot to dribble the ball to the goal. We use B-Human robo…

### 3. GeoGS-SLAM: Geometry-Only Gaussian Splatting for Dense Monocular SLAM

- **arXiv**: [2607.07452v1](https://arxiv.org/abs/2607.07452v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.07452v1)
- **作者**: Lipu Zhou, Yaoyun Kang, Junxiang Pang et al.
- **发表**: 2026-07-08  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Dense visual SLAM is a fundamental problem in robotics. Recent advances in 3DGS have demonstrated its potential for dense SLAM. Existing 3DGS frameworks focus on both appearance and geometry modeling. However, scene geometry is typically more critical for SLAM than novel view synthesis because downstream robotic tasks, such as navigation and obstacle avoida…

### 4. Why does Deep Learning Improve Visual SLAM?

- **arXiv**: [2607.06023v1](https://arxiv.org/abs/2607.06023v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06023v1)
- **作者**: Giovanni Cioffi, Davide Scaramuzza
- **发表**: 2026-07-07  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Visual SLAM is a well-established technology utilized in a wide range of real-world applications. However, its performance still degrades under challenging visual conditions, such as low texture, severe motion blur, and poor illumination. Systems based on deep learning outperform classical geometry-based ones and achieve state-of-the-art results by combinin…

### 5. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 6. Beyond Transformers: Linear Attention Policy for Open-Vocabulary Object Goal Navigation

- **arXiv**: [2607.18794v1](https://arxiv.org/abs/2607.18794v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.18794v1)
- **作者**: Jiahong Zhang, Yifan Lin, Yandong Zhang et al.
- **发表**: 2026-07-21  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Open-Vocabulary Object Goal Navigation (OVON) requires agents to operate under partial observability, making effective internal state updates critical for navigation performance. This update is implemented by the policy network, where recent approaches adopt Transformer-based backbones with self-attention over a context window to integrate temporal informat…

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

### 9. Hilti-Trimble-Oxford Dataset: 360 Visual-Inertial Benchmark with Floor Plan Priors for SLAM and Localization

- **arXiv**: [2607.06464v1](https://arxiv.org/abs/2607.06464v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06464v1)
- **作者**: Samuele Centanni, Yuhao Zhang, Yifu Tao et al.
- **发表**: 2026-07-07  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Automated progress monitoring on construction sites is an active area of research and development. Robot and human-carried mapping systems have been developed to build 3D maps of building and infrastructure projects. While LiDAR-based mapping systems achieve high accuracy, the cost of LiDAR can be prohibitive. Consumer-grade cameras with wide field of view…

### 10. MiLSD: A Micro Line-Segment Detector for Resource-Constrained Devices

- **arXiv**: [2607.06600v1](https://arxiv.org/abs/2607.06600v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06600v1)
- **作者**: Parsa Hassani Shariat Panahi, Amir Hossein Jalilvand, M. Hassan Najafi
- **发表**: 2026-07-07  ·  **类别**: cs.CV, cs.AI, cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Line segment detection is a key building block in visual SLAM, 3D reconstruction, and industrial inspection. Recent deep learning methods have greatly improved accuracy, yet even the smallest models require several megabytes of memory, exceeding low-cost MCU capacity. This work investigates the maximum achievable accuracy under a sub-megabyte budget. We pro…

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
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Precise metric depth estimation is fundamental for autonomous robot navigation, yet monocular systems inherently suffer from scale ambiguity and scale drift. While recent recurrent flow-based SLAM systems have demonstrated state-of-the-art robustness, they remain scale-ambiguous. In this paper, we propose Metric-DROID, an end-to-end recurrent architecture t…

### 3. GLidE-SLAM: GL-Accelerated Indirect-Direct Embedded SLAM

- **arXiv**: [2607.16897v1](https://arxiv.org/abs/2607.16897v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.16897v1)
- **作者**: Carlos A. Pinheiro de Sousa, Heiko Hamann, Oliver Deussen
- **发表**: 2026-07-18  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
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

## 🧪 仿真 / Sim2Real (1 篇)

### 1. Bridging the Sim-to-Real Gap under Real-Time Constraints in Autonomous Racing

- **arXiv**: [2607.18586v1](https://arxiv.org/abs/2607.18586v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.18586v1)
- **作者**: Hossein Maghsoumi, Yaser P. Fallah
- **发表**: 2026-07-20  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Autonomous racing exposes the sim-to-real gap under extreme operating conditions characterized by high speed, tight stability margins, and stringent real-time constraints. Although simulation is indispensable for development, controllers that perform well in simulation often degrade abruptly on physical platforms due to interacting effects of dynamics misma…

---

## 📋 本日操作建议

**建议今日深读 (Top 3):**
1. [TAC-LOCO: Unified Whole-Body Control for Quadrupedal TACtile-Informed LOCO-Manipulation](https://arxiv.org/abs/2607.10132v2) — score 22
2. [DexVerse: A Modular Benchmark for Multi-Task, Multi-Embodiment Dexterous Manipulation](https://arxiv.org/abs/2607.08751v1) — score 22
3. [Isaac Sim-to-Real: Reinforcement Learning based Locomotion for Quadrupeds](https://arxiv.org/abs/2607.18135v1) — score 21

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
