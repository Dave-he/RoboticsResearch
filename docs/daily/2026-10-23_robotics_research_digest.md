# 机器人研究每日摘要 · 2026-10-23

> 自动生成,共 67 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (6 篇)

### 1. ACCRUE: Continual Off-Policy Reinforcement Learning for Robot Foundation Models

- **arXiv**: [2610.18596v1](https://arxiv.org/abs/2610.18596v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.18596v1)
- **作者**: Changyeon Kim, Kimin Lee, Yashraj Narang et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 10  ·  **✅ 已研读**
- **摘要**: Reinforcement learning (RL) post-training improves robot foundation models (RFMs) beyond their demonstrations, but real-world deployment demands more: learning new tasks efficiently while retaining previously acquired behaviors. Existing continual RL methods on top of VLAs mitigate forgetting but rely on on-policy updates with limited forward transfer, wher…

### 2. Post-hoc Epistemic Uncertainty for Vision-Language-Action Policies

- **arXiv**: [2610.29730v1](https://arxiv.org/abs/2610.29730v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.29730v1)
- **作者**: Johannes Keller, Albrecht M. Bloße, Adrian Lindenmeyer et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO, cs.LG, stat.ML
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Vision-language-action (VLA) policies need to recognize gaps in their training knowledge to request useful demonstrations or assistance in new situations, especially when failures are costly. Disagreement within an ensemble of independently trained policies can guide these decisions, but requires training and running multiple policies. We propose post-hoc k…

### 3. Multi-Dimensional Featurizers Yield Fine-Grained Steering and Data Shaping in Robot Foundation Models

- **arXiv**: [2610.20767v1](https://arxiv.org/abs/2610.20767v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20767v1)
- **作者**: Aiden Swann, Mozes Jacobs, Mathilde Papillon et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Can better feature discovery improve control over robot behavior through internal interventions and training data? Recent work in vision and language models reveals multidimensional features, motivating block-sparse featurizers (BSFs), which represent each feature in a low-dimensional subspace. We investigate whether recovering this structure provides an in…

### 4. $Δ$ Flow Matching for Robot Foundation Models

- **arXiv**: [2610.15794v1](https://arxiv.org/abs/2610.15794v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.15794v1)
- **作者**: Kuangji Zuo, Tuo An, Xinying Guo et al.
- **发表**: 2026-10-11  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Flow matching is a common generative recipe for robot foundation models. Vision-language-action models (VLAs) generate action chunks, while world-action models (WAMs) additionally generate future visual states. Both start generation from a fixed Gaussian prior, despite temporal continuity between past and future states and actions. This requires costly trai…

### 5. FlowVLA: Learning Flow-Aware Physical Completion for Quantitative Robotic Pouring

- **arXiv**: [2610.29692v1](https://arxiv.org/abs/2610.29692v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.29692v1)
- **作者**: Liwen Yang, Yutian Zhang, Jiaqi Zhai et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: During steady pouring, images and robot pose may remain nearly unchanged while transferred mass accumulates, making the return decision ambiguous for a whole-task vision-language-action (VLA) policy. We present FlowVLA, which separates motor generation from physical-completion estimation. A shared $π_{0.5}$ action expert learns approach, pour, and return wi…

### 6. NavBind: Diagnosing Instruction-Action Binding at Route Forks in Navigation VLAs

- **arXiv**: [2610.29203v1](https://arxiv.org/abs/2610.29203v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.29203v1)
- **作者**: Josh Qixuan Sun, Xiaoying Xing, Yurun Chen et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-language-action (VLA) navigation models translate visual observations and instructions into actions. Navigation success assesses whether an agent reaches the goal. However, reaching the goal successfully does not establish whether the model genuinely follows the instructions or relies on visual cues or navigation history. We introduce NavBind to diag…

## 🌐 具身智能 / 机器人基础模型 (13 篇)

### 1. TARSphere: A Robot-Oriented Full-Stack Framework for Long-Horizon Embodied Agents in Evolving Physical and Social Environments

- **arXiv**: [2610.30043v1](https://arxiv.org/abs/2610.30043v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30043v1)
- **作者**: Yicheng Xu, Zhikai Xu, Ziyuan Chen et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Robots must act under physical and social constraints while adapting to changes in their environment and human needs. Existing embodied-agent systems often focus on specified goals or abstract execution into symbolic actions, limiting evaluation in an evolving world. We introduce TARSphere, a robot-oriented full-stack framework for physically and socially g…

### 2. Scaling in Games: Continued Pre-Training For Embodied Agents In Diverse Virtual Worlds

- **arXiv**: [2610.28698v1](https://arxiv.org/abs/2610.28698v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.28698v1)
- **作者**: Kuan Zhang, Yukun Chen, Zhihao Yang et al.
- **发表**: 2026-10-20  ·  **类别**: cs.AI, cs.CV, cs.LG
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Scaling data, diversity and model capacity has improved embodied learning in physical environments, where diverse experiences remain grounded in shared physical laws. Whether these gains extend to virtual worlds with different visual styles, dynamics, controls, and objectives remains unclear. We investigate this question through a controlled study of contin…

### 3. DewHand: Direct Metric World-Space Hand Motion Reconstruction from Egocentric Videos

- **arXiv**: [2610.29936v1](https://arxiv.org/abs/2610.29936v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.29936v1)
- **作者**: Naru Suzuki, Satoshi Ikehata, Takehiko Ohkawa et al.
- **发表**: 2026-10-21  ·  **类别**: cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Recovering metric world-space hand motion from egocentric video supports understanding human interactions and transferring them to embodied agents. Three challenges complicate this task: multi-stage pipelines propagate errors from independently estimated hand and camera motion; monocular observations leave physical scale ambiguous; and occlusion and out-of-…

### 4. CLOSER: Evidence-Aware Active Visual Verification for Embodied Object-Goal Navigation

- **arXiv**: [2610.28476v1](https://arxiv.org/abs/2610.28476v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.28476v1)
- **作者**: Pengying Wu, Mingye Jiang, Yunze Hu et al.
- **发表**: 2026-10-20  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Object-goal navigation (ObjectNav) requires an embodied agent to find an instance of a specified category in an unseen environment and stop near it. The agent typically relies on an object detector but must judge online from a limited egocentric video stream, sometimes a single frame, whether a detected candidate is the target. Detectors often confidently m…

### 5. JARVIS: From Visual Manuals to Autonomous Robotic Assembly

- **arXiv**: [2610.27618v1](https://arxiv.org/abs/2610.27618v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.27618v1)
- **作者**: Fan Ding, Fucai Ke, Kevin Yuchen Ma et al.
- **发表**: 2026-10-20  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Visual manuals communicate procedural knowledge through stepwise diagrams, but translating these instructions into reliable long-horizon robotic execution remains challenging. We introduce JARVIS, a method-agnostic benchmark for autonomous visual-manual-guided execution without additional language instructions. JARVIS comprises 236,679 LEGO assembly tasks a…

### 6. Multimodal Embodied Agents: A Unified Capability-centric Perspective from Computer-Use to Robot-Use

- **arXiv**: [2610.30108v1](https://arxiv.org/abs/2610.30108v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30108v1)
- **作者**: Yanzhe Chen, Ziyi Yang, Jifeng Zhu et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 8  ·  **📚 综述(归档备查,按协议 §4 不深读)**
- **摘要**: Multimodal agents (MMAs) sustain interaction through reasoning, memory, tools, and feedback, most visibly as computer-use agents, while robotic systems (RSs) couple sensing and actuation under physical dynamics. We define multimodal embodied agents (MMEAs) as goal-directed systems that couple multimodal task reasoning with physical action and revise decisio…

### 7. CAPSafe: A Benchmark for Contextual Action and Plan Safety Reasoning in Embodied Agents

- **arXiv**: [2610.28381v1](https://arxiv.org/abs/2610.28381v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.28381v1)
- **作者**: Youmna Farag, Svetlana Stoyanchev, Simon Keizer et al.
- **发表**: 2026-10-20  ·  **类别**: cs.RO, cs.CL
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Reasoning about safety is essential for embodied agents powered by large language models (LLMs). We introduce the Contextual Action and Plan Safety benchmark (CAPSafe), designed to evaluate safety reasoning at two levels: (1) an action-level dataset that tests whether a single action is safe given its environmental context, and (2) a plan-level dataset that…

### 8. Physical AI: Concepts, Techniques, and Challenges

- **arXiv**: [2610.27045v1](https://arxiv.org/abs/2610.27045v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.27045v1)
- **作者**: Weinan Zhang, Chunhua Shen, Tianfan Xue et al.
- **发表**: 2026-10-19  ·  **类别**: cs.AI, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: In recent years, physical artificial intelligence (physical AI) has experienced rapid development, capturing significant attention in academia and industry. However, the field has yet to reach consensus on its definition, technical landscape, and core challenges. To address this gap, this monograph seeks to define physical AI, present its technical landscap…

### 9. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 10. PRISM: Learning Realistic Depth via Physics-Grounded Noise Disentanglement with Semantic-Geometric Collaboration

- **arXiv**: [2610.29432v1](https://arxiv.org/abs/2610.29432v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.29432v1)
- **作者**: Xiujian Liang, Jiacheng Liu, Mingyang Sun et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Real-world physical sensing exhibits complex, heterogeneous noise patterns that deviate significantly from idealized simulation, posing a fundamental bottleneck for sim-to-real transfer. Existing sensor modelings typically treat depth noise as a monolithic black-box process, overlooking the distinct physical mechanisms that govern different error modalities…

## 🦵 人形 / 足式机器人 (20 篇)

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

### 3. Reinforcement Learning Based Multi-Terrain Adaptive Whole-Body Control for a Quadruped Manipulator

- **arXiv**: [2610.23548v1](https://arxiv.org/abs/2610.23548v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.23548v1)
- **作者**: Yanzhou Jin, Fei Suo, Chang Liu et al.
- **发表**: 2026-10-16  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **✅ 已研读**
- **摘要**: Legged robots equipped with manipulators offer promising capabilities for loco-manipulation tasks in unstructured environments. However, achieving task-consistent end-effector behavior during locomotion remains challenging due to terrain-induced disturbances and the strong coupling between locomotion and manipulation, particularly for small-scale quadruped…

### 4. PHD-Hand: A Printable Humanoid Dexterous Hand with Linkage-Driven 3-DOA Digits

- **arXiv**: [2610.29030v1](https://arxiv.org/abs/2610.29030v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.29030v1)
- **作者**: Neel Adwani, Muhaiminul Islam Akash, Saffia Ouali et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Currently, dexterous humanoid robot hands are widely considered the final hardware bottleneck that hampers generalist robots from physically assisting people at home and work. As conventional tendon-driven designs suffer from high cost, demanding maintenance, poor reliability, and short durability, alternative linkage-driven designs have increasingly gained…

### 5. Action-Aligned Latent Planning for Versatile Humanoid Loco-Manipulation

- **arXiv**: [2610.24675v2](https://arxiv.org/abs/2610.24675v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.24675v2)
- **作者**: Yutang Lin, Guanya Shi, C. Karen Liu
- **发表**: 2026-10-17  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Learning a single perceptive policy for diverse humanoid loco-manipulation requires unifying high-level task decisions without losing the state-dependent physical responses that make each interaction succeed. This makes the representation between high-level planning and whole-body control critical: kinematic or contact targets provide compact abstractions b…

### 6. Physical AI for Intralogistics: Benchmarking the NVIDIA Sim-to-Real Ecosystem for Cosmos-Enhanced COMPASS Navigation on Industrial Mobile Robots

- **arXiv**: [2610.28432v2](https://arxiv.org/abs/2610.28432v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.28432v2)
- **作者**: Charbel Abi Hana, Rayan Zaitouni, Kameel Amareen et al.
- **发表**: 2026-10-20  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Classical robot navigation stacks are reliable but often require re-engineering for each new robot type and site. Learning-based navigation shifts this effort from hand-tuned parameters to data generation and training, where a policy adapts to each new embodiment or facility by fine-tuning in simulation. Whether policies adapted this way stay reliable on re…

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
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: While large-scale human motion capture datasets provide a rich source of demonstrations for humanoid robot learning, retargeting the diverse motions to different humanoid robots remains a nontrivial challenge. Existing kinodynamic trajectory optimization pipelines are computationally expensive and often require manual adjustments per motion. We present FRDV…

### 9. Learning Structured Locomotion References for Optimization-Based Whole-Body Control

- **arXiv**: [2610.24779v1](https://arxiv.org/abs/2610.24779v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.24779v1)
- **作者**: Ömer Tarık Banuş, Uluç Saranlı, M. Mert Ankaralı
- **发表**: 2026-10-17  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Quadruped locomotion requires coordinating body motion,contact forces, foothold placement, and gait timing. We present a hierarchical controller in which reinforcement learning adapts these structured locomotion references while a gait scheduler, reactive footstep planner, and whole-body impulse controller retain responsibility for high-frequency execution.…

### 10. Plausible Future, Wrong Choice: Steering World-Action Models toward Intended Future

- **arXiv**: [2610.28431v1](https://arxiv.org/abs/2610.28431v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.28431v1)
- **作者**: Zhuohao Li, Jiawei He, Yuxuan Yan et al.
- **发表**: 2026-10-20  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: World-Action Models (WAMs) have emerged as a promising paradigm for embodied generalist policies by jointly modeling future world evolution and robot actions across diverse manipulation tasks. However, representing diverse futures is only the first step: a capable WAM must also generate futures that match the requirements of the current task and execution p…

## 🦾 操控 / 灵巧手 / 抓取 (13 篇)

### 1. HandsOn: A Large-Scale Simulation Benchmark for Generalizable Dexterous Manipulation

- **arXiv**: [2610.26765v1](https://arxiv.org/abs/2610.26765v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.26765v1)
- **作者**: Tianwei Luo, Yiming He, Hongjin Wu et al.
- **发表**: 2026-10-19  ·  **类别**: cs.RO
- **相关性评分**: 23  ·  **✅ 已研读**
- **摘要**: General-purpose manipulation requires reliable behavior across embodiments, objects, and task demands. We introduce HandsOn, a composable simulation platform and benchmark for cross-embodiment dexterous manipulation. It supports five robotic arms, six dexterous hands, and approximately 200 rigid, articulated, and deformable assets in randomized scenes. The…

### 2. BiDex-100: A Comprehensive Benchmark for Bimanual Dexterous Manipulation Across 100+ Simulation Tasks

- **arXiv**: [2610.25459v1](https://arxiv.org/abs/2610.25459v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.25459v1)
- **作者**: Yong Wang, Kecheng Zheng, Xing Zhu et al.
- **发表**: 2026-10-18  ·  **类别**: cs.RO, cs.CV, cs.LG
- **相关性评分**: 21  ·  **✅ 已研读**
- **摘要**: Bimanual manipulation with dexterous hands has attracted growing attention in research on robotic action models. However, few studies have developed benchmarks specifically tailored for dexterous manipulation, leaving the dexterous manipulation capabilities of existing models insufficiently characterized. In this paper, we present BiDex-100, a simulation be…

### 3. AtomicRL: Atomic Reinforcement Learning for Long-Horizon Robotic Manipulation

- **arXiv**: [2610.30097v1](https://arxiv.org/abs/2610.30097v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30097v1)
- **作者**: Likui Zhang, Zhe Zhu, Zhihao Zhan et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 18  ·  **✅ 已研读**
- **摘要**: Vision-language-action (VLA) models have shown promise in robotic manipulation, but imitation learning (IL) alone often struggles to master complex long-horizon skills. Reinforcement learning (RL) offers an effective avenue for further improving VLA policies. However, existing VLA-RL methods typically suffer from delayed and biased credit assignment due to…

### 4. Physical Words: A Vocabulary for Structuring Latent Reasoning in Robot Manipulation

- **arXiv**: [2610.26854v3](https://arxiv.org/abs/2610.26854v3)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.26854v3)
- **作者**: Jiaming Liu, Xinghao Zhu, Yiming Zhang et al.
- **发表**: 2026-10-19  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Multimodal reasoning provides robotic foundation models with predictive context needed for reliable action generation. However, language-based reasoning captures task semantics but struggles to express fine-grained physical dynamics, while latent reasoning models future state evolution but offers limited structure for organizing these dynamics into reusable…

### 5. Training in Deployment: Human-in-the-loop Online Post-Training for Robot Manipulation

- **arXiv**: [2610.29264v1](https://arxiv.org/abs/2610.29264v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.29264v1)
- **作者**: Chun Gu, Xiaofei Wei, Yiming Chen et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Large pretrained robot foundation models provide strong priors for manipulation, yet adapting them to target tasks with offline teleoperated demonstrations often fails to cover the contact-rich, recovery, and precision-critical states encountered during deployment. Existing methods mitigate this issue by augmenting offline demonstrations with human-in-the-l…

### 6. GeoMem-VLA: Internalizing 3D Scene Understanding into Temporal Memory for Vision-Language-Action Models

- **arXiv**: [2610.29866v1](https://arxiv.org/abs/2610.29866v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.29866v1)
- **作者**: Qinfan Zhang, Yifan Luo, Haoyuan Shi et al.
- **发表**: 2026-10-21  ·  **类别**: cs.CV
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Geometric structure is essential for robotic manipulation and understanding the 3D world. Most VLA models rely on 2D representations of current observations, while geometry-aware approaches often require additional 3D information. However, geometry inferred independently from individual observations is often discarded rather than accumulated into a persiste…

### 7. Causal Analysis of Robot Foundation Models Enables Efficiency Gains

- **arXiv**: [2610.20750v1](https://arxiv.org/abs/2610.20750v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20750v1)
- **作者**: Aiden Swann, Mathilde Papillon, Mozes Jacobs et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models are a promising approach to general purpose robot manipulation. While the internal computation of vision-language models, which compose the backbone of VLAs, has been studied extensively, less is known about how their perceptual and semantic representations are transformed into action in VLA models. We study this question…

### 8. From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation

- **arXiv**: [2610.29560v1](https://arxiv.org/abs/2610.29560v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.29560v1)
- **作者**: Tingwen Du, Haoyu Guo, Hanxue Zhang et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Vision-language-action (VLA) models achieve strong performance across embodied manipulation tasks by unifying visual understanding, language conditioning, and action generation. However, long-horizon tasks can involve non-Markovian dependencies: successful decisions may require retaining task progress and past interaction outcomes, while partial observabili…

### 9. Distance Field Driven Reinforcement Learning for Reactive and Robust Collision Avoidance

- **arXiv**: [2610.29452v1](https://arxiv.org/abs/2610.29452v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.29452v1)
- **作者**: Taiga Ikeshima, Sheila Sutjipto, Lan Wu et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Robust and reactive collision avoidance remains a central challenge for deploying Reinforcement Learning (RL) policies on real robotic manipulators, particularly when transferring behaviours learned in simulation to the physical world. This paper presents an RL framework that integrates the Euclidean Distance Field (EDF) directly into the observation space,…

### 10. Plan First, Act Later: Streaming Reasoning for Executable Memory in Robot Control

- **arXiv**: [2610.29329v1](https://arxiv.org/abs/2610.29329v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.29329v1)
- **作者**: Qinghang Liu, Conglin Wang, Zongsheng Li et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Long-horizon robot manipulation requires a robot to remember task-relevant information beyond its short observation window. Existing memory-augmented policies typically retrieve relevant information from history and reason over it at execution time, placing a heavy reasoning burden on the high-level model. To address this challenge, we propose PAL (\textbf{…

## 🎓 模仿学习 / 强化学习 (7 篇)

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

### 3. PCLA-Bridge: A Framework for Cross-Domain Deployment of CARLA Agents

- **arXiv**: [2610.28696v1](https://arxiv.org/abs/2610.28696v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.28696v1)
- **作者**: Masoud Jamshidiyan Tehrani, Jinhan Kim, Paolo Tonella
- **发表**: 2026-10-20  ·  **类别**: cs.SE, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Most high-performing end-to-end autonomous driving agents (ADAs) are developed for the CARLA Leaderboard, tightly coupling them to CARLA's APIs, sensor layouts, coordinate systems, and internal clock. Reusing these models on real datasets, alternative simulators, or physical platforms necessitates substantial manual re-engineering. We present PCLA-Bridge, a…

### 4. Unblur-SLAM: Dense Neural SLAM for Blurry Inputs

- **arXiv**: [2603.26810v1](https://arxiv.org/abs/2603.26810v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.26810v1)
- **作者**: Qi Zhang, Denis Rozumny, Francesco Girlanda et al.
- **发表**: 2026-03-26  ·  **类别**: cs.CV, eess.IV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We propose Unblur-SLAM, a novel RGB SLAM pipeline for sharp 3D reconstruction from blurred image inputs. In contrast to previous work, our approach is able to handle different types of blur and demonstrates state-of-the-art performance in the presence of both motion blur and defocus blur. Moreover, we adjust the computation effort with the amount of blur in…

### 5. Query Quantized Neural SLAM

- **arXiv**: [2412.16476v1](https://arxiv.org/abs/2412.16476v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2412.16476v1)
- **作者**: Sijia Jiang, Jing Hua, Zhizhong Han
- **发表**: 2024-12-21  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural implicit representations have shown remarkable abilities in jointly modeling geometry, color, and camera poses in simultaneous localization and mapping (SLAM). Current methods use coordinates, positional encodings, or other geometry features as input to query neural implicit functions for signed distances and color which produce rendering errors to d…

### 6. ACE-SLAM: Scene Coordinate Regression for Neural Implicit Real-Time SLAM

- **arXiv**: [2512.14032v1](https://arxiv.org/abs/2512.14032v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2512.14032v1)
- **作者**: Ignacio Alzugaray, Marwan Taher, Andrew J. Davison
- **发表**: 2025-12-16  ·  **类别**: cs.CV, cs.AI, eess.IV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: We present a novel neural RGB-D Simultaneous Localization And Mapping (SLAM) system that learns an implicit map of the scene in real time. For the first time, we explore the use of Scene Coordinate Regression (SCR) as the core implicit map representation in a neural SLAM pipeline, a paradigm that trains a lightweight network to directly map 2D image feature…

### 7. MISO: Multiresolution Submap Optimization for Efficient Globally Consistent Neural Implicit Reconstruction

- **arXiv**: [2504.19104v1](https://arxiv.org/abs/2504.19104v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2504.19104v1)
- **作者**: Yulun Tian, Hanwen Cao, Sunghwan Kim et al.
- **发表**: 2025-04-27  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Neural implicit representations have had a significant impact on simultaneous localization and mapping (SLAM) by enabling robots to build continuous, differentiable, and high-fidelity 3D maps from sensor data. However, as the scale and complexity of the environment increase, neural SLAM approaches face renewed challenges in the back-end optimization process…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (8 篇)

### 1. LIN-SLAM: Lightweight LiDAR--Inertial Neural SLAM for Real-Time Onboard Navigation

- **arXiv**: [2610.21199v1](https://arxiv.org/abs/2610.21199v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.21199v1)
- **作者**: Shiqi Che, Yijie Liu, Shuo Wang et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **✅ 已研读**
- **摘要**: Geometric light detection and ranging (LiDAR)--inertial simultaneous localization and mapping (SLAM) provides efficient state estimation but lacks the continuous map representation and global refinement capabilities of neural implicit SLAM, while neural implicit methods remain computationally expensive. We propose Lightweight LiDAR--Inertial Neural SLAM (LI…

### 2. Line-Augmented cuVSLAM: Robust Visual Odometry in Low-Texture Environments

- **arXiv**: [2610.20958v1](https://arxiv.org/abs/2610.20958v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20958v1)
- **作者**: Dara Molloy, Terry Wu, Wonju Lee et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Autonomous mobile robots in warehouses and production facilities operate in precisely the environments that defeat point-feature visual odometry: featureless aisles, uniform walls, repetitive racking and specular floors. Such environments are, however, rich in straight-edge structure: rack uprights, door frames, wall junctions and cabinet outlines present h…

### 3. Human-in-the-Loop Neuro-Symbolic Drift Anticipation for Reliable Visual SLAM

- **arXiv**: [2610.05757v1](https://arxiv.org/abs/2610.05757v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05757v1)
- **作者**: Junhyun Nam, Wonse Jo
- **发表**: 2026-10-05  ·  **类别**: cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: This paper introduces Hybrid DeepSEE (HDS), a Human-in-the-Loop (HITL) neuro-symbolic framework for proactive drift anticipation in Visual SLAM (V-SLAM). While data-driven models offer predictive power, their "black-box" nature often yields physically inconsistent outputs in out-of-distribution (OOD) environments. To address this, HDS integrates neural drif…

### 4. Know-Your-Scene (KYS)-SLAM: Hierarchical Semantic-Motion Priors for Feature Matching in Stereo Visual SLAM

- **arXiv**: [2609.27509v1](https://arxiv.org/abs/2609.27509v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27509v1)
- **作者**: Preeti Chatterjee, Jin Lu, Jin Sun et al.
- **发表**: 2026-09-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Stereo visual SLAM systems built on local descriptors suffer from semantic ambiguity, instance-level confusion, and independently moving objects, each corrupting data association and accumulating as trajectory drift. Prevailing semantic and dynamic SLAM methods address this through binary feature rejection, sacrificing correspondence density for outlier sup…

### 5. Does Dynamic-Point Filtering Help When Texture Is Scarce? A Controlled Study of ORB-SLAM2 Front-Ends in Synthetic Indoor Scenes

- **arXiv**: [2610.10564v1](https://arxiv.org/abs/2610.10564v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10564v1)
- **作者**: Zekui Xue
- **发表**: 2026-10-02  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Dynamic-point filters are routinely added to feature-based visual SLAM, and several recent systems argue that removing dynamic features can leave too few static features in low-texture regions. So far, these systems have been evaluated only on texture-rich benchmark sequences. We present a controlled study that isolates this interaction. We render synthetic…

### 6. MVP-SLAM: Multi-Camera Visual-Inertial Floorplan-Prior SLAM

- **arXiv**: [2609.39596v1](https://arxiv.org/abs/2609.39596v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39596v1)
- **作者**: Asier Bikandi-Noya, Miguel Fernandez-Cortizas, Muhammad Shaheer et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Indoor building construction sites are demanding environments for visual SLAM, where variable lighting and repetitive, low-textured structures make the system drift over long trajectories, though structural elements such as walls remain distinguishable despite these conditions. These buildings are constructed according to their as-planned floor plans, avail…

### 7. Cube-Splat: High-Fidelity 360° Gaussian Splatting SLAM via Cubemap Factorization and Adjoint-Consistent Optimization

- **arXiv**: [2609.21347v1](https://arxiv.org/abs/2609.21347v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.21347v1)
- **作者**: Xiangfei Guo, Hao Shi, Yufan Zhang et al.
- **发表**: 2026-09-18  ·  **类别**: cs.CV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Recent progress in 3D Gaussian Splatting (3DGS) has enabled dense visual SLAM with pinhole cameras, yet most pipelines are not designed for panoramic imagery. We present Cube-Splat, the first panoramic GS-SLAM framework that factorizes each 360° frame into a cubemap of four fixed-orientation virtual pinhole views sharing a single optical center. By designat…

### 8. Geodesic Flow Matching for Denoising High-Dimensional Structured Representations

- **arXiv**: [2606.00248v1](https://arxiv.org/abs/2606.00248v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.00248v1)
- **作者**: Karim Habashy, Chris Eliasmith
- **发表**: 2026-05-29  ·  **类别**: cs.AI
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Vector Symbolic Algebras (VSAs) enable robust neurosymbolic reasoning by encoding symbolic information into high-dimensional distributed representations. For continuous domains, Spatial Semantic Pointers (SSPs) extend this framework by mapping variables onto continuous toroidal manifolds. However, standard approaches like Flow Matching assume a flat Euclide…

---

## 📋 本日操作建议

**建议今日深读 (Top 3):**
1. [Physical Words: A Vocabulary for Structuring Latent Reasoning in Robot Manipulation](https://arxiv.org/abs/2610.26854v3) — score 15
2. [PHD-Hand: A Printable Humanoid Dexterous Hand with Linkage-Driven 3-DOA Digits](https://arxiv.org/abs/2610.29030v1) — score 14
3. [Training in Deployment: Human-in-the-loop Online Post-Training for Robot Manipulation](https://arxiv.org/abs/2610.29264v1) — score 14

> 筛选说明:本次 Top 3 已排除(已研读跳过 8 篇、综述跳过 1 篇)。

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
