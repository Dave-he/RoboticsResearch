# 机器人研究每日摘要 · 2026-10-22

> 自动生成,共 89 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (7 篇)

### 1. ACCRUE: Continual Off-Policy Reinforcement Learning for Robot Foundation Models

- **arXiv**: [2610.18596v1](https://arxiv.org/abs/2610.18596v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.18596v1)
- **作者**: Changyeon Kim, Kimin Lee, Yashraj Narang et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 10  ·  **✅ 已研读**
- **摘要**: Reinforcement learning (RL) post-training improves robot foundation models (RFMs) beyond their demonstrations, but real-world deployment demands more: learning new tasks efficiently while retaining previously acquired behaviors. Existing continual RL methods on top of VLAs mitigate forgetting but rely on on-policy updates with limited forward transfer, wher…

### 2. Perceives but Doesn't Brake: A Perception-Action Binding Gap in Reasoning Driving VLAs

- **arXiv**: [2610.28184v1](https://arxiv.org/abs/2610.28184v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.28184v1)
- **作者**: Matteo Cercola, Katie Z Luo, Simone Formentin et al.
- **发表**: 2026-10-20  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Reasoning-augmented vision-language-action (VLA) driving models can perceive and reason about safety-critical hazards yet fail to translate that evidence into safe actions. We characterize this failure as a perception-action binding gap: hazard information is available inside the model but exerts insufficient control over trajectory generation. Using matche…

### 3. PACT-VLA: Speculative Action-Chunk Verification with Pre-Commit Observations

- **arXiv**: [2610.28019v1](https://arxiv.org/abs/2610.28019v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.28019v1)
- **作者**: Yixiang Zhu, Ruilong Wu, Yonghao Chen et al.
- **发表**: 2026-10-20  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Vision-language-action (VLA) policies are commonly deployed with asynchronous inference in real-world settings, where the next action chunk is generated while the robot is still executing the previous one. By the time the new chunk is committed, the robot and scene have changed, so the chunk is conditioned on a stale observation and task success drops sharp…

### 4. Multi-Dimensional Featurizers Yield Fine-Grained Steering and Data Shaping in Robot Foundation Models

- **arXiv**: [2610.20767v1](https://arxiv.org/abs/2610.20767v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20767v1)
- **作者**: Aiden Swann, Mozes Jacobs, Mathilde Papillon et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Can better feature discovery improve control over robot behavior through internal interventions and training data? Recent work in vision and language models reveals multidimensional features, motivating block-sparse featurizers (BSFs), which represent each feature in a low-dimensional subspace. We investigate whether recovering this structure provides an in…

### 5. $Δ$ Flow Matching for Robot Foundation Models

- **arXiv**: [2610.15794v1](https://arxiv.org/abs/2610.15794v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.15794v1)
- **作者**: Kuangji Zuo, Tuo An, Xinying Guo et al.
- **发表**: 2026-10-11  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Flow matching is a common generative recipe for robot foundation models. Vision-language-action models (VLAs) generate action chunks, while world-action models (WAMs) additionally generate future visual states. Both start generation from a fixed Gaussian prior, despite temporal continuity between past and future states and actions. This requires costly trai…

### 6. ScaleNav: Scalable Internet Video Pretraining for Language-Conditioned Local Navigation

- **arXiv**: [2610.25690v1](https://arxiv.org/abs/2610.25690v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.25690v1)
- **作者**: Yihui Yang, Yuanhong Yu, Jiawei Wang et al.
- **发表**: 2026-10-19  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: We study language-conditioned local navigation, where a robot must navigate to a text-specified target visible in its initial observation and stop at the described location. End-to-end navigation policies require diverse training data to generalize across scenes, yet real-robot data is costly to collect and simulated data leaves a sim-to-real gap. Internet…

### 7. ARC: A Reasoning Recipe for Robot Foundation Models

- **arXiv**: [2610.12386v1](https://arxiv.org/abs/2610.12386v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12386v1)
- **作者**: Gokul Puthumanaillam, Tao Sun, Elie Aljalbout et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The prevailing approach to improving robot foundation models (RFMs) relies on larger models, more robot demonstrations, and costly training at scale. We show that there exists an effective and efficient complementary approach: the right reasoning recipe can substantially improve the zero-shot task performance of existing state-of-the-art RFMs. We refer to t…

## 🌐 具身智能 / 机器人基础模型 (10 篇)

### 1. CLOSER: Evidence-Aware Active Visual Verification for Embodied Object-Goal Navigation

- **arXiv**: [2610.28476v1](https://arxiv.org/abs/2610.28476v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.28476v1)
- **作者**: Pengying Wu, Mingye Jiang, Yunze Hu et al.
- **发表**: 2026-10-20  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Object-goal navigation (ObjectNav) requires an embodied agent to find an instance of a specified category in an unseen environment and stop near it. The agent typically relies on an object detector but must judge online from a limited egocentric video stream, sometimes a single frame, whether a detected candidate is the target. Detectors often confidently m…

### 2. JARVIS: From Visual Manuals to Autonomous Robotic Assembly

- **arXiv**: [2610.27618v1](https://arxiv.org/abs/2610.27618v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.27618v1)
- **作者**: Fan Ding, Fucai Ke, Kevin Yuchen Ma et al.
- **发表**: 2026-10-20  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Visual manuals communicate procedural knowledge through stepwise diagrams, but translating these instructions into reliable long-horizon robotic execution remains challenging. We introduce JARVIS, a method-agnostic benchmark for autonomous visual-manual-guided execution without additional language instructions. JARVIS comprises 236,679 LEGO assembly tasks a…

### 3. CAPSafe: A Benchmark for Contextual Action and Plan Safety Reasoning in Embodied Agents

- **arXiv**: [2610.28381v1](https://arxiv.org/abs/2610.28381v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.28381v1)
- **作者**: Youmna Farag, Svetlana Stoyanchev, Simon Keizer et al.
- **发表**: 2026-10-20  ·  **类别**: cs.RO, cs.CL
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Reasoning about safety is essential for embodied agents powered by large language models (LLMs). We introduce the Contextual Action and Plan Safety benchmark (CAPSafe), designed to evaluate safety reasoning at two levels: (1) an action-level dataset that tests whether a single action is safe given its environmental context, and (2) a plan-level dataset that…

### 4. BetaMem: Learning to Remember a Changing World for Embodied Agents

- **arXiv**: [2610.26554v1](https://arxiv.org/abs/2610.26554v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.26554v1)
- **作者**: Mai Liu, He Sun, Siru Zhong et al.
- **发表**: 2026-10-19  ·  **类别**: cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Long-horizon embodied agents face temporal confusion and incomplete or distorted records, recurring errors from fixed memory rules, and growing storage and retrieval costs. We present BetaMem, a framework for building and evolving traceable long-term memory through six linked layers: working, spatial, entity, episodic, experiential, and procedural memory. A…

### 5. Physical AI: Concepts, Techniques, and Challenges

- **arXiv**: [2610.27045v1](https://arxiv.org/abs/2610.27045v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.27045v1)
- **作者**: Weinan Zhang, Chunhua Shen, Tianfan Xue et al.
- **发表**: 2026-10-19  ·  **类别**: cs.AI, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: In recent years, physical artificial intelligence (physical AI) has experienced rapid development, capturing significant attention in academia and industry. However, the field has yet to reach consensus on its definition, technical landscape, and core challenges. To address this gap, this monograph seeks to define physical AI, present its technical landscap…

### 6. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 7. CovNav: Conformal Prediction-Guided Adaptive Inference for Object Goal Navigation

- **arXiv**: [2610.27677v1](https://arxiv.org/abs/2610.27677v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.27677v1)
- **作者**: Pengying Wu, Zhejia Wen, Kang Ding et al.
- **发表**: 2026-10-20  ·  **类别**: cs.RO, cs.AI, cs.CL
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: In object goal navigation (ObjectNav), an embodied agent must find a target object (e.g., "find a bed") in a previously unseen environment, relying on spatial commonsense such as object co-occurrence. Large Language Models (LLMs) encode this commonsense, but deploying them on robots exposes a trade-off between reasoning quality and efficiency: cloud-based m…

### 8. LVMem: Image-Augmented Memory for Long-Horizon Question Answering

- **arXiv**: [2610.27104v1](https://arxiv.org/abs/2610.27104v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.27104v1)
- **作者**: Victoria Khoruzhaya, Maksim Kalmykov, Tuong Do Minh et al.
- **发表**: 2026-10-19  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Reliable language-guided perception is essential for embodied agents, where questions about objects, events, and their locations must be answered from long observation histories. Unlike conventional visual question answering, realistic robotic settings require reasoning over extended temporal horizons and persistent scene memory. We build upon the view-base…

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

## 🦵 人形 / 足式机器人 (29 篇)

### 1. Reinforcement Learning Based Multi-Terrain Adaptive Whole-Body Control for a Quadruped Manipulator

- **arXiv**: [2610.23548v1](https://arxiv.org/abs/2610.23548v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.23548v1)
- **作者**: Yanzhou Jin, Fei Suo, Chang Liu et al.
- **发表**: 2026-10-16  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **✅ 已研读**
- **摘要**: Legged robots equipped with manipulators offer promising capabilities for loco-manipulation tasks in unstructured environments. However, achieving task-consistent end-effector behavior during locomotion remains challenging due to terrain-induced disturbances and the strong coupling between locomotion and manipulation, particularly for small-scale quadruped…

### 2. RoboMMT: Learning Stable Tracking of Modulated Expressive and Interactive Robot Motion

- **arXiv**: [2610.26414v1](https://arxiv.org/abs/2610.26414v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.26414v1)
- **作者**: Till Hielscher, Kai O. Arras
- **发表**: 2026-10-19  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Expressive robot motion can improve naturalness, effectiveness, and perceived likability in human-robot interaction. When deployed on dynamically unstable platforms, however, reactive execution of expressive body motion may bring the robot to its stability limits, especially when expressivity is decoupled from physical control. In this paper, we present Rob…

### 3. Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience

- **arXiv**: [2610.26855v1](https://arxiv.org/abs/2610.26855v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.26855v1)
- **作者**: Tianqi Liu, Hanfei Zhao, Qifeng Liang et al.
- **发表**: 2026-10-19  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: World models enable embodied agents to anticipate action consequences, yet jointly modeling locomotion and manipulation across diverse embodiments remains challenging due to heterogeneous action spaces and limited multimodal supervision. We present Ropedia W0, the first egocentric loco-manipulation world foundation model spanning humans and robots with dive…

### 4. Action-Aligned Latent Planning for Versatile Humanoid Loco-Manipulation

- **arXiv**: [2610.24675v2](https://arxiv.org/abs/2610.24675v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.24675v2)
- **作者**: Yutang Lin, Guanya Shi, C. Karen Liu
- **发表**: 2026-10-17  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Learning a single perceptive policy for diverse humanoid loco-manipulation requires unifying high-level task decisions without losing the state-dependent physical responses that make each interaction succeed. This makes the representation between high-level planning and whole-body control critical: kinematic or contact targets provide compact abstractions b…

### 5. CQDC-Warp: GPU-Accelerated Differentiable Quasi-Dynamic Simulation for Contact-Rich Manipulation

- **arXiv**: [2610.21349v1](https://arxiv.org/abs/2610.21349v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.21349v1)
- **作者**: Yanchen Ding, Jiayi Chen, Jianfeng Xu et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Efficient synthesis of contact-rich manipulation trajectories is essential for downstream robot learning. Gradient-based planning offers a promising approach, but jointly optimizing motion and contact decisions remains challenging. Meanwhile, many existing planners run on CPUs with limited throughput. We present CQDC-Warp, a GPU-accelerated differentiable q…

### 6. EmbodyHOI: Embodiment-Aware Generation of Hand-Object Interactions for Humanoid Dexterous Manipulation

- **arXiv**: [2610.27242v1](https://arxiv.org/abs/2610.27242v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.27242v1)
- **作者**: Chaitanya Chawla, Kartik Sharma, Ananya Bal et al.
- **发表**: 2026-10-19  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Humanoid dexterous manipulation needs reference motions that are both semantically rich and kinematically feasible for the target robot. Text-conditioned hand-object interaction (HOI) generators supply diverse, language-specified demonstrations, but they synthesize motion in human (MANO) space. The embodiment gap is therefore deferred to post-hoc retargetin…

### 7. KODA: Kinematics--Observation Data Alignment for Humanoid Learning from Human Egocentric Demonstration

- **arXiv**: [2610.21152v1](https://arxiv.org/abs/2610.21152v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.21152v1)
- **作者**: Zibo Zhou, Yueru Chen, Junsong Wu et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Training humanoid whole-body vision-language-action (VLA) policies requires costly robot demonstrations with aligned robot-view observations and controller-compatible whole-body state-action labels. Egocentric human demonstrations offer scalable supervision but have misaligned views and sparse motion cues. Existing approaches either pretrain policies that s…

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

- **arXiv**: [2610.28432v1](https://arxiv.org/abs/2610.28432v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.28432v1)
- **作者**: Charbel Abi Hana, Rayan Zaitouni, Kameel Amareen et al.
- **发表**: 2026-10-20  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Classical robot navigation stacks are reliable but often require re-engineering for each new robot type and site. Learning-based navigation shifts this effort from hand-tuned parameters to data generation and training, where a policy adapts to each new embodiment or facility by fine-tuning in simulation. Whether policies adapted this way stay reliable on re…

## 🦾 操控 / 灵巧手 / 抓取 (26 篇)

### 1. HandsOn: A Large-Scale Simulation Benchmark for Generalizable Dexterous Manipulation

- **arXiv**: [2610.26765v1](https://arxiv.org/abs/2610.26765v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.26765v1)
- **作者**: Tianwei Luo, Yiming He, Hongjin Wu et al.
- **发表**: 2026-10-19  ·  **类别**: cs.RO
- **相关性评分**: 25  ·  **🔥 read_now**
- **摘要**: General-purpose manipulation requires reliable behavior across embodiments, objects, and task demands. We introduce HandsOn, a composable simulation platform and benchmark for cross-embodiment dexterous manipulation. It supports five robotic arms, six dexterous hands, and approximately 200 rigid, articulated, and deformable assets in randomized scenes. The…

### 2. BiDex-100: A Comprehensive Benchmark for Bimanual Dexterous Manipulation Across 100+ Simulation Tasks

- **arXiv**: [2610.25459v1](https://arxiv.org/abs/2610.25459v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.25459v1)
- **作者**: Yong Wang, Kecheng Zheng, Xing Zhu et al.
- **发表**: 2026-10-18  ·  **类别**: cs.RO, cs.CV, cs.LG
- **相关性评分**: 22  ·  **🔥 read_now**
- **摘要**: Bimanual manipulation with dexterous hands has attracted growing attention in research on robotic action models. However, few studies have developed benchmarks specifically tailored for dexterous manipulation, leaving the dexterous manipulation capabilities of existing models insufficiently characterized. In this paper, we present BiDex-100, a simulation be…

### 3. No Eyes, No Problem: What Does Touch Contribute to Blind Baoding Ball Manipulation?

- **arXiv**: [2610.23438v1](https://arxiv.org/abs/2610.23438v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.23438v1)
- **作者**: Ayush Deshmukh, Nalin Agarwal, Elle Miller et al.
- **发表**: 2026-10-16  ·  **类别**: cs.RO
- **相关性评分**: 21  ·  **✅ 已研读**
- **摘要**: Humans manipulate objects within their hands through touch alone with remarkable ease, but for robots, achieving sustained real-world manipulation without vision remains an open challenge. Although reinforcement learning (RL) can generate sophisticated blind manipulation policies in simulation, transferring them to a real dexterous hand remains hindered by…

### 4. FIT-MAC: A Closed-Loop Multi-Agent Framework for Robust Vision-Language-Action Models

- **arXiv**: [2610.28109v1](https://arxiv.org/abs/2610.28109v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.28109v1)
- **作者**: Jiatong Li, Jisheng Dang, Qiangqiang Ma et al.
- **发表**: 2026-10-20  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models have achieved strong performance on standard robotic manipulation benchmarks. However, their reliability can degrade substantially when task conditions deviate from the nominal setting. Perturbations in object positions and task instructions may lead to complete task failure. Existing VLA policies generally lack an explic…

### 5. ReDOA: Real-World Distillation via Observation Alignment for Image-Based Manipulation Policy Learning

- **arXiv**: [2610.25691v1](https://arxiv.org/abs/2610.25691v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.25691v1)
- **作者**: Kotaro Kajitsuka, Masaki Murooka, Fumio Kanehiro
- **发表**: 2026-10-19  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Data-driven learning for general-purpose robotic manipulation presents a fundamental trade-off between data-collection cost and adaptability to real-world environments. Imitation learning (IL) requires costly human demonstrations, whereas simulation-based learning is vulnerable to sim-to-real gaps in dynamics and sensor observations. We propose ReDOA (Real-…

### 6. Physical Words: A Vocabulary for Structuring Latent Reasoning in Robot Manipulation

- **arXiv**: [2610.26854v2](https://arxiv.org/abs/2610.26854v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.26854v2)
- **作者**: Jiaming Liu, Xinghao Zhu, Yiming Zhang et al.
- **发表**: 2026-10-19  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Multimodal reasoning provides robotic foundation models with predictive context needed for reliable action generation. However, language-based reasoning captures task semantics but struggles to express fine-grained physical dynamics, while latent reasoning models future state evolution but offers limited structure for organizing these dynamics into reusable…

### 7. Reasoning as a Distribution: Generative Plan Latents for Vision-Language-Action Models

- **arXiv**: [2610.28166v1](https://arxiv.org/abs/2610.28166v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.28166v1)
- **作者**: Matteo Cercola, Katie Z Luo, Milan Ganai et al.
- **发表**: 2026-10-20  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) policies increasingly reason before acting, but existing reasoning models compress this intermediate decision into a single representation. When several plans are valid, this commitment hides alternatives that could otherwise be selected or revised. We introduce the Generative Plan Latent (GPL), which represents the reasoning st…

### 8. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

### 9. RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation

- **arXiv**: [2610.27861v1](https://arxiv.org/abs/2610.27861v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.27861v1)
- **作者**: Haocheng Wang, Youquan Liu, Weiyu Guo et al.
- **发表**: 2026-10-20  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) robustness is commonly summarized by aggregate task success, which obscures how individual executions change under distribution shifts and where failures emerge in long-horizon tasks. We introduce \textbf{RoboCasa-Shift}, a diagnostic robustness benchmark built on RoboCasa365 that combines controlled single-factor shifts, matche…

### 10. Gen2Dex: Learning Dexterous Manipulation from Simulation-Initialized Generated Video Demonstrations

- **arXiv**: [2610.24392v1](https://arxiv.org/abs/2610.24392v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.24392v1)
- **作者**: Xiaowen Qiu, Yian Wang, Haoxiang You et al.
- **发表**: 2026-10-17  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Human video demonstrations provide rich manipulation strategies for dexterous manipulation learning. We study a setting in which a fully specified simulated scene is used to generate videos that specify the demonstrated manipulation behavior. This setup provides access to scene information such as object geometry, articulation, and camera parameters, while…

## 🎓 模仿学习 / 强化学习 (8 篇)

### 1. RingNav: Task-Shaped Circular Memory for Visual Heading

- **arXiv**: [2610.19044v1](https://arxiv.org/abs/2610.19044v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19044v1)
- **作者**: Naitri Rajyaguru, Aryan Tajne, Stephen Jardim et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Tiny robots have limited computation and memory, yet visual navigation systems often maintain more state than a task requires. We ask whether persistent memory can instead be shaped by the task. We present \textbf{RingNav}, a \(10.6\)k--parameter visual heading estimator that constrains its memory to the circular manifold \(S^1\). RingNav learns only the tu…

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

### 4. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 5. Unblur-SLAM: Dense Neural SLAM for Blurry Inputs

- **arXiv**: [2603.26810v1](https://arxiv.org/abs/2603.26810v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.26810v1)
- **作者**: Qi Zhang, Denis Rozumny, Francesco Girlanda et al.
- **发表**: 2026-03-26  ·  **类别**: cs.CV, eess.IV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We propose Unblur-SLAM, a novel RGB SLAM pipeline for sharp 3D reconstruction from blurred image inputs. In contrast to previous work, our approach is able to handle different types of blur and demonstrates state-of-the-art performance in the presence of both motion blur and defocus blur. Moreover, we adjust the computation effort with the amount of blur in…

### 6. Query Quantized Neural SLAM

- **arXiv**: [2412.16476v1](https://arxiv.org/abs/2412.16476v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2412.16476v1)
- **作者**: Sijia Jiang, Jing Hua, Zhizhong Han
- **发表**: 2024-12-21  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural implicit representations have shown remarkable abilities in jointly modeling geometry, color, and camera poses in simultaneous localization and mapping (SLAM). Current methods use coordinates, positional encodings, or other geometry features as input to query neural implicit functions for signed distances and color which produce rendering errors to d…

### 7. ACE-SLAM: Scene Coordinate Regression for Neural Implicit Real-Time SLAM

- **arXiv**: [2512.14032v1](https://arxiv.org/abs/2512.14032v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2512.14032v1)
- **作者**: Ignacio Alzugaray, Marwan Taher, Andrew J. Davison
- **发表**: 2025-12-16  ·  **类别**: cs.CV, cs.AI, eess.IV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: We present a novel neural RGB-D Simultaneous Localization And Mapping (SLAM) system that learns an implicit map of the scene in real time. For the first time, we explore the use of Scene Coordinate Regression (SCR) as the core implicit map representation in a neural SLAM pipeline, a paradigm that trains a lightweight network to directly map 2D image feature…

### 8. MISO: Multiresolution Submap Optimization for Efficient Globally Consistent Neural Implicit Reconstruction

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
- **相关性评分**: 12  ·  **✅ 已研读**
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
1. [HandsOn: A Large-Scale Simulation Benchmark for Generalizable Dexterous Manipulation](https://arxiv.org/abs/2610.26765v1) — score 25
2. [BiDex-100: A Comprehensive Benchmark for Bimanual Dexterous Manipulation Across 100+ Simulation Tasks](https://arxiv.org/abs/2610.25459v1) — score 22
3. [FIT-MAC: A Closed-Loop Multi-Agent Framework for Robust Vision-Language-Action Models](https://arxiv.org/abs/2610.28109v1) — score 16

> 筛选说明:本次 Top 3 已排除(已研读跳过 4 篇)。

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
