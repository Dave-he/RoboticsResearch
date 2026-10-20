# 机器人研究每日摘要 · 2026-10-21

> 自动生成,共 87 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (6 篇)

### 1. Multi-Dimensional Featurizers Yield Fine-Grained Steering and Data Shaping in Robot Foundation Models

- **arXiv**: [2610.20767v1](https://arxiv.org/abs/2610.20767v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20767v1)
- **作者**: Aiden Swann, Mozes Jacobs, Mathilde Papillon et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Can better feature discovery improve control over robot behavior through internal interventions and training data? Recent work in vision and language models reveals multidimensional features, motivating block-sparse featurizers (BSFs), which represent each feature in a low-dimensional subspace. We investigate whether recovering this structure provides an in…

### 2. ACCRUE: Continual Off-Policy Reinforcement Learning for Robot Foundation Models

- **arXiv**: [2610.18596v1](https://arxiv.org/abs/2610.18596v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.18596v1)
- **作者**: Changyeon Kim, Kimin Lee, Yashraj Narang et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 10  ·  **✅ 已研读**
- **摘要**: Reinforcement learning (RL) post-training improves robot foundation models (RFMs) beyond their demonstrations, but real-world deployment demands more: learning new tasks efficiently while retaining previously acquired behaviors. Existing continual RL methods on top of VLAs mitigate forgetting but rely on on-policy updates with limited forward transfer, wher…

### 3. Robotic Photography System based on Vision-Language-Action Model

- **arXiv**: [2610.26287v1](https://arxiv.org/abs/2610.26287v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.26287v1)
- **作者**: Song-Li Wu, Chubin Zhang, Wenbo Ding et al.
- **发表**: 2026-10-19  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Modern robotic photography requires understanding photographic intent, planning camera motions, and producing aesthetically pleasing images in complex environments. We present RoboPhoto-VLA, a unified Vision-Language-Action framework that jointly models perception, reasoning, and camera control for autonomous robotic photography. RoboPhoto-VLA incorporates…

### 4. $Δ$ Flow Matching for Robot Foundation Models

- **arXiv**: [2610.15794v1](https://arxiv.org/abs/2610.15794v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.15794v1)
- **作者**: Kuangji Zuo, Tuo An, Xinying Guo et al.
- **发表**: 2026-10-11  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Flow matching is a common generative recipe for robot foundation models. Vision-language-action models (VLAs) generate action chunks, while world-action models (WAMs) additionally generate future visual states. Both start generation from a fixed Gaussian prior, despite temporal continuity between past and future states and actions. This requires costly trai…

### 5. ScaleNav: Scalable Internet Video Pretraining for Language-Conditioned Local Navigation

- **arXiv**: [2610.25690v1](https://arxiv.org/abs/2610.25690v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.25690v1)
- **作者**: Yihui Yang, Yuanhong Yu, Jiawei Wang et al.
- **发表**: 2026-10-19  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: We study language-conditioned local navigation, where a robot must navigate to a text-specified target visible in its initial observation and stop at the described location. End-to-end navigation policies require diverse training data to generalize across scenes, yet real-robot data is costly to collect and simulated data leaves a sim-to-real gap. Internet…

### 6. ARC: A Reasoning Recipe for Robot Foundation Models

- **arXiv**: [2610.12386v1](https://arxiv.org/abs/2610.12386v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12386v1)
- **作者**: Gokul Puthumanaillam, Tao Sun, Elie Aljalbout et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The prevailing approach to improving robot foundation models (RFMs) relies on larger models, more robot demonstrations, and costly training at scale. We show that there exists an effective and efficient complementary approach: the right reasoning recipe can substantially improve the zero-shot task performance of existing state-of-the-art RFMs. We refer to t…

## 🌐 具身智能 / 机器人基础模型 (8 篇)

### 1. LateMatch: Breaking the Interaction Bottleneck via Cacheable Matching for Efficient Visual Localization

- **arXiv**: [2610.25358v1](https://arxiv.org/abs/2610.25358v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.25358v1)
- **作者**: Mohammad Omama, Aeyan Ashraf, Sandeep Chinchali
- **发表**: 2026-10-18  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Visual localization is critical for embodied agents, but deploying state-of-the-art deep feature matchers on edge devices is fundamentally limited by their massive computational cost. Standard deep matchers tightly interleave intra-image context building and inter-image matching at every layer, creating a severe interaction bottleneck. Localizing a single q…

### 2. BetaMem: Learning to Remember a Changing World for Embodied Agents

- **arXiv**: [2610.26554v1](https://arxiv.org/abs/2610.26554v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.26554v1)
- **作者**: Mai Liu, He Sun, Siru Zhong et al.
- **发表**: 2026-10-19  ·  **类别**: cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Long-horizon embodied agents face temporal confusion and incomplete or distorted records, recurring errors from fixed memory rules, and growing storage and retrieval costs. We present BetaMem, a framework for building and evolving traceable long-term memory through six linked layers: working, spatial, entity, episodic, experiential, and procedural memory. A…

### 3. Discovery-Probability Graph Planning for Embodied Agents in Tasks with Hidden Cooperation Requirements

- **arXiv**: [2610.26359v1](https://arxiv.org/abs/2610.26359v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.26359v1)
- **作者**: Zihuang Cai, Changjian Chen, Zhuo Tang et al.
- **发表**: 2026-10-19  ·  **类别**: cs.MA
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Embodied agents are increasingly capable of perceiving, planning, and acting autonomously in dynamic environments, demonstrating strong performance on complex cooperative tasks. Recent advances typically assume that cooperative tasks are known in advance. In real-world applications, however, hidden-cooperation tasks are more common: the need for cooperation…

### 4. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 5. EmbodiedWorld-200K: Toward Embodied World Agents via Embodied-Planning Dataset and Interactive World Models

- **arXiv**: [2610.25959v1](https://arxiv.org/abs/2610.25959v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.25959v1)
- **作者**: X. Feng, J. Tang, Z. Lin et al.
- **发表**: 2026-10-19  ·  **类别**: cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Building embodied agents that can perceive, reason, and act across diverse 3D worlds is a central research direction toward artificial general intelligence. Yet most existing work remains confined to specific tasks in a single scene and transfers poorly to new environments, leaving general embodied agents for open-world settings under-explored. We refer to…

### 6. DialogMem: Evaluating Dialogue-Grounded Embodied Memory in 3D Environments

- **arXiv**: [2610.24767v1](https://arxiv.org/abs/2610.24767v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.24767v1)
- **作者**: SeongJun Jeong, Junghyun Kim, Gi-Cheon Kang et al.
- **发表**: 2026-10-17  ·  **类别**: cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Embodied agents in human-centered environments require memory that integrates what they observe with what humans tell them over time. However, existing embodied memories are built primarily from visual experience, leaving open how dialogue with humans can be grounded in the objects encountered throughout that experience. We introduce DialogMem, a two-phase…

### 7. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

### 8. FoundationVIO: Enforcing Metric Scale in Feed-forward Visual-Inertial Odometry

- **arXiv**: [2610.14951v1](https://arxiv.org/abs/2610.14951v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.14951v1)
- **作者**: Jin Rhee, Yuhao Zhang, Frank Dellaert et al.
- **发表**: 2026-10-10  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Feed-forward geometric foundation models (GFMs) directly predict dense geometry and camera poses from batches of images. Emerging visual SLAM methods chain together consecutive GFM batches to form dense point cloud maps. A core challenge is how to address the ambiguous geometric scale of GFM predictions: independent predictions are locally consistent up-to-…

## 🦵 人形 / 足式机器人 (30 篇)

### 1. Reinforcement Learning Based Multi-Terrain Adaptive Whole-Body Control for a Quadruped Manipulator

- **arXiv**: [2610.23548v1](https://arxiv.org/abs/2610.23548v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.23548v1)
- **作者**: Yanzhou Jin, Fei Suo, Chang Liu et al.
- **发表**: 2026-10-16  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **✅ 已研读**
- **摘要**: Legged robots equipped with manipulators offer promising capabilities for loco-manipulation tasks in unstructured environments. However, achieving task-consistent end-effector behavior during locomotion remains challenging due to terrain-induced disturbances and the strong coupling between locomotion and manipulation, particularly for small-scale quadruped…

### 2. Action-Aligned Latent Planning for Versatile Humanoid Loco-Manipulation

- **arXiv**: [2610.24675v1](https://arxiv.org/abs/2610.24675v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.24675v1)
- **作者**: Yutang Lin, Guanya Shi, C. Karen Liu
- **发表**: 2026-10-17  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Learning a single perceptive policy for diverse humanoid loco-manipulation requires unifying high-level task decisions without losing the state-dependent physical responses that make each interaction succeed. This makes the representation between high-level planning and whole-body control critical: kinematic or contact targets provide compact abstractions b…

### 3. RoboMMT: Learning Stable Tracking of Modulated Expressive and Interactive Robot Motion

- **arXiv**: [2610.26414v1](https://arxiv.org/abs/2610.26414v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.26414v1)
- **作者**: Till Hielscher, Kai O. Arras
- **发表**: 2026-10-19  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Expressive robot motion can improve naturalness, effectiveness, and perceived likability in human-robot interaction. When deployed on dynamically unstable platforms, however, reactive execution of expressive body motion may bring the robot to its stability limits, especially when expressivity is decoupled from physical control. In this paper, we present Rob…

### 4. Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience

- **arXiv**: [2610.26855v1](https://arxiv.org/abs/2610.26855v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.26855v1)
- **作者**: Tianqi Liu, Hanfei Zhao, Qifeng Liang et al.
- **发表**: 2026-10-19  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: World models enable embodied agents to anticipate action consequences, yet jointly modeling locomotion and manipulation across diverse embodiments remains challenging due to heterogeneous action spaces and limited multimodal supervision. We present Ropedia W0, the first egocentric loco-manipulation world foundation model spanning humans and robots with dive…

### 5. CQDC-Warp: GPU-Accelerated Differentiable Quasi-Dynamic Simulation for Contact-Rich Manipulation

- **arXiv**: [2610.21349v1](https://arxiv.org/abs/2610.21349v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.21349v1)
- **作者**: Yanchen Ding, Jiayi Chen, Jianfeng Xu et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Efficient synthesis of contact-rich manipulation trajectories is essential for downstream robot learning. Gradient-based planning offers a promising approach, but jointly optimizing motion and contact decisions remains challenging. Meanwhile, many existing planners run on CPUs with limited throughput. We present CQDC-Warp, a GPU-accelerated differentiable q…

### 6. E2DRL: End-to-End Differentiable Reinforcement Learning for 3D Obstacle Avoidance in Quadruped Robots

- **arXiv**: [2610.19627v1](https://arxiv.org/abs/2610.19627v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19627v1)
- **作者**: Cheng Fan, Bingyang Zhou, Gang Yang et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Differentiable reinforcement learning shows strong promise for robot policy learning, but its application to legged locomotion has remained limited to blind walking or simulated 2D tasks. Extending it to end-to-end visual obstacle avoidance is challenging because hard collision constraints and early termination upon contact corrupt first-order gradients, tr…

### 7. Beyond Kinematic Tracking: Preserving Expressive Characteristics in Humanoid Whole-Body Control

- **arXiv**: [2610.19393v1](https://arxiv.org/abs/2610.19393v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19393v1)
- **作者**: Lingfan Bao, Hanshang Zhu, Yan Pan et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Whole-body control plays a crucial role in enabling humanoid robots to execute expressive motions. Faithful execution requires preserving both the intended action and its expressive characteristics. Existing whole-body trackers typically balance joint and keypoint tracking with physical stability across diverse motions, but these objectives do not necessari…

### 8. HAF-VLA: Hierarchical Action Flow Framework for Humanoid Vision-Language-Action Control

- **arXiv**: [2610.26584v1](https://arxiv.org/abs/2610.26584v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.26584v1)
- **作者**: Langzhe Gu, Chengkai Hou, Meng Li et al.
- **发表**: 2026-10-19  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Humanoid robots hold great promise as general-purpose agents in human-centered environments, yet adapting generalist vision-language-action (VLA) policies to real-world humanoid loco-manipulation remains challenging. Unlike fixed-base or wheeled manipulators, humanoids must coordinate locomotion, posture, gaze, and dual-arm manipulation over a high-dimensio…

### 9. Spark-0: Scaling Spatially Aligned Tactile Pretraining for Robot Dexterous Manipulation

- **arXiv**: [2610.22342v1](https://arxiv.org/abs/2610.22342v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.22342v1)
- **作者**: Tianxing Chen, Wenwei Lin, Chuqiao Lyu et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **✅ 已研读**
- **摘要**: Generalist robot policies benefit from large-scale visual pretraining but often struggle with contact-rich dexterous manipulation, where force, compliance, and incipient slip are hard to observe from images. We present Spark-0, a spatially aligned vision-tactile-language-action (VTLA) model that uses touch in two complementary ways. During pretraining, imag…

### 10. KODA: Kinematics--Observation Data Alignment for Humanoid Learning from Human Egocentric Demonstration

- **arXiv**: [2610.21152v1](https://arxiv.org/abs/2610.21152v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.21152v1)
- **作者**: Zibo Zhou, Yueru Chen, Junsong Wu et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Training humanoid whole-body vision-language-action (VLA) policies requires costly robot demonstrations with aligned robot-view observations and controller-compatible whole-body state-action labels. Egocentric human demonstrations offer scalable supervision but have misaligned views and sparse motion cues. Existing approaches either pretrain policies that s…

## 🦾 操控 / 灵巧手 / 抓取 (25 篇)

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

### 4. HiFun: a Hierarchical Framework for Efficient Functional Dexterous Manipulation Learning

- **arXiv**: [2610.19518v1](https://arxiv.org/abs/2610.19518v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19518v1)
- **作者**: Linyi Huang, Guowei Huai, Weibin Liu et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **✅ 已研读**
- **摘要**: While multi-fingered dexterous robot hands have the potential to provide human-level dexterity, using them for functional manipulation remains difficult because task success depends on precise contact, coordinated arm-hand motion, and reactive recovery from execution errors. Precise contact depends on complex contact dynamics that are difficult to model acc…

### 5. Robot Learning with Vision-Language-Action Models for Agricultural Manipulation

- **arXiv**: [2610.26717v1](https://arxiv.org/abs/2610.26717v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.26717v1)
- **作者**: Hamid Hafezi, Javad Mohammadpour Velni, Mohammadreza Davoodi
- **发表**: 2026-10-19  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Robotic manipulation in agricultural environments remains challenging due to variations in plant geometry, occlusion, and camera viewpoints. Pretrained vision-language-action (VLA) and generalist robot policies offer a promising approach to addressing these challenges by learning manipulation behaviors from multimodal observations and language instructions.…

### 6. ReDOA: Real-World Distillation via Observation Alignment for Image-Based Manipulation Policy Learning

- **arXiv**: [2610.25691v1](https://arxiv.org/abs/2610.25691v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.25691v1)
- **作者**: Kotaro Kajitsuka, Masaki Murooka, Fumio Kanehiro
- **发表**: 2026-10-19  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Data-driven learning for general-purpose robotic manipulation presents a fundamental trade-off between data-collection cost and adaptability to real-world environments. Imitation learning (IL) requires costly human demonstrations, whereas simulation-based learning is vulnerable to sim-to-real gaps in dynamics and sensor observations. We propose ReDOA (Real-…

### 7. Physical Words: A Vocabulary for Structuring Latent Reasoning in Robot Manipulation

- **arXiv**: [2610.26854v1](https://arxiv.org/abs/2610.26854v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.26854v1)
- **作者**: Jiaming Liu, Xinghao Zhu, Yiming Zhang et al.
- **发表**: 2026-10-19  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Multimodal reasoning provides robotic foundation models with predictive context needed for reliable action generation. However, language-based reasoning captures task semantics but struggles to express fine-grained physical dynamics, while latent reasoning models future state evolution but offers limited structure for organizing these dynamics into reusable…

### 8. SPAR: Structural Pruning and Action Recovery for Vision-Language-Action Models

- **arXiv**: [2610.26487v1](https://arxiv.org/abs/2610.26487v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.26487v1)
- **作者**: Shenli Zheng, Zhou Fang, Yuan Du et al.
- **发表**: 2026-10-19  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: The limited onboard computing resources of robots make the inference demands of vision-language-action (VLA) models costly to accommodate. Reducing these demands through aggressive compression, however, can degrade manipulation performance beyond what supervised fine-tuning alone recovers. We present SPAR (Structural Pruning and Action Recovery), which simu…

### 9. Causal Analysis of Robot Foundation Models Enables Efficiency Gains

- **arXiv**: [2610.20750v1](https://arxiv.org/abs/2610.20750v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20750v1)
- **作者**: Aiden Swann, Mathilde Papillon, Mozes Jacobs et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models are a promising approach to general purpose robot manipulation. While the internal computation of vision-language models, which compose the backbone of VLAs, has been studied extensively, less is known about how their perceptual and semantic representations are transformed into action in VLA models. We study this question…

### 10. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

## 🎓 模仿学习 / 强化学习 (9 篇)

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

### 4. BodyBridge: Grounded Body Layers for Sim-to-Real Translation of Vulnerable Road Users

- **arXiv**: [2610.24436v1](https://arxiv.org/abs/2610.24436v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.24436v1)
- **作者**: Mark Azer, Fabian B. Flohr
- **发表**: 2026-10-17  ·  **类别**: cs.CV
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Simulation-to-real driving video diffusion models can translate photorealistic scenes, but they typically represent pedestrians and cyclists, vulnerable road users (VRUs), as generic object classes. This is insufficient for vulnerable road users whose safety-relevant appearance depends on articulated pose and identity. We present BodyBridge and Grounded Bod…

### 5. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 6. Unblur-SLAM: Dense Neural SLAM for Blurry Inputs

- **arXiv**: [2603.26810v1](https://arxiv.org/abs/2603.26810v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.26810v1)
- **作者**: Qi Zhang, Denis Rozumny, Francesco Girlanda et al.
- **发表**: 2026-03-26  ·  **类别**: cs.CV, eess.IV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We propose Unblur-SLAM, a novel RGB SLAM pipeline for sharp 3D reconstruction from blurred image inputs. In contrast to previous work, our approach is able to handle different types of blur and demonstrates state-of-the-art performance in the presence of both motion blur and defocus blur. Moreover, we adjust the computation effort with the amount of blur in…

### 7. Query Quantized Neural SLAM

- **arXiv**: [2412.16476v1](https://arxiv.org/abs/2412.16476v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2412.16476v1)
- **作者**: Sijia Jiang, Jing Hua, Zhizhong Han
- **发表**: 2024-12-21  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural implicit representations have shown remarkable abilities in jointly modeling geometry, color, and camera poses in simultaneous localization and mapping (SLAM). Current methods use coordinates, positional encodings, or other geometry features as input to query neural implicit functions for signed distances and color which produce rendering errors to d…

### 8. ACE-SLAM: Scene Coordinate Regression for Neural Implicit Real-Time SLAM

- **arXiv**: [2512.14032v1](https://arxiv.org/abs/2512.14032v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2512.14032v1)
- **作者**: Ignacio Alzugaray, Marwan Taher, Andrew J. Davison
- **发表**: 2025-12-16  ·  **类别**: cs.CV, cs.AI, eess.IV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: We present a novel neural RGB-D Simultaneous Localization And Mapping (SLAM) system that learns an implicit map of the scene in real time. For the first time, we explore the use of Scene Coordinate Regression (SCR) as the core implicit map representation in a neural SLAM pipeline, a paradigm that trains a lightweight network to directly map 2D image feature…

### 9. MISO: Multiresolution Submap Optimization for Efficient Globally Consistent Neural Implicit Reconstruction

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
- **相关性评分**: 8  ·  **👀 watch**
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
3. [Robot Learning with Vision-Language-Action Models for Agricultural Manipulation](https://arxiv.org/abs/2610.26717v1) — score 17

> 筛选说明:本次 Top 3 已排除(已研读跳过 6 篇)。

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
