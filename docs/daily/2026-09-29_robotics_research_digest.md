# 机器人研究每日摘要 · 2026-09-29

> 自动生成,共 94 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (7 篇)

### 1. RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents

- **arXiv**: [2609.25636v1](https://arxiv.org/abs/2609.25636v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.25636v1)
- **作者**: Chang Guo, Yukun Xie, Bohan Tan et al.
- **发表**: 2026-09-22  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Modern embodied agents achieve impressive success rates, yet their actual instruction-following ability is far weaker than these numbers suggest. We trace this illusion to a structural property we term low scene entropy: when a visual scene admits only one valid task, language becomes redundant and a policy can score highly while barely using it. We introdu…

### 2. Towards VLA-Dreamer: Refining VLA Behavior Using World Models

- **arXiv**: [2609.31313v1](https://arxiv.org/abs/2609.31313v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.31313v1)
- **作者**: Parsa Mastouri Kashani, Jan-Gerrit Habekost, Stefan Wermter
- **发表**: 2026-09-25  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Vision-Language-Action models (VLAs), while showing strong potential for robot control, require massive amounts of high-quality imitation learning data. Moreover, the absence of an explicit world model casts further doubt on their control capabilities. In this concept paper, we propose a novel architecture that addresses sample efficiency in VLAs by trainin…

### 3. Breaking the Vision-Action Shortcut: Latent Interface Training for Generalizable Robotics Foundation Models

- **arXiv**: [2609.12641v1](https://arxiv.org/abs/2609.12641v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.12641v1)
- **作者**: Jianman Lin, Shailesh Shailesh, Zhongyi Luo et al.
- **发表**: 2026-09-11  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Robot foundation models achieve strong in-distribution performance but often degrade under visual distribution shifts. When learning to generate actions from pretrained visual representations, models may exploit task-irrelevant visual cues that correlate with demonstrated actions within the training distribution. Such vision-action shortcuts can undermine g…

### 4. The Linear Representation Hypothesis for Vision-Language-Action Models

- **arXiv**: [2609.30996v1](https://arxiv.org/abs/2609.30996v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.30996v1)
- **作者**: Minseok Jeong, Hyewon Choi, Hiroyasu Tsukamoto et al.
- **发表**: 2026-09-25  ·  **类别**: cs.LG, cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: The linear representation hypothesis (LRH) has become a standard lens for measuring and intervening on semantic information through the internal representations of large language models (LLMs). A growing body of work has begun extending this perspective to vision-language-action (VLA) models, but the dynamical nature of embodied interaction introduces an ad…

### 5. Fast Plans, Faithful Actions: Closing the Planning-Execution Gap in Hierarchical Vision-Language-Action Models

- **arXiv**: [2609.30833v1](https://arxiv.org/abs/2609.30833v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.30833v1)
- **作者**: Chuanliang Xie, Boyu Ma, Gen Li et al.
- **发表**: 2026-09-25  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Hierarchical vision-language-action (VLA) systems consist of a high-level vision-language planner and a low-level action expert that generates continuous actions. This hierarchical design has practical value only if the planner can generate plans fast enough to meet real-time control requirements, and the resulting plans actually contribute to the generatio…

### 6. Measuring Language Transfer in Robot Policies: Adding Greek to a Cosmos3 Vision-Language-Action Policy

- **arXiv**: [2609.07470v1](https://arxiv.org/abs/2609.07470v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.07470v1)
- **作者**: Ayoub Kirouane, Georgios Giaples, Christos Petrocheilos
- **发表**: 2026-09-07  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Robot foundation models are trained and evaluated predominantly in English, and robot demonstration corpora do not exist for most languages. We study the addition of Greek to an open vision-language-action stack using only machine-rephrased instructions and no architecture changes. The main challenge is measurement rather than translation. Several plausible…

### 7. Causeway: Restoring Task Accessibility for Instruction Switching in VLA Policies

- **arXiv**: [2609.30913v1](https://arxiv.org/abs/2609.30913v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.30913v1)
- **作者**: Qingzi Wang, Kaixi Feng, Guangyao Shi et al.
- **发表**: 2026-09-25  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-language-action (VLA) policies can execute many tasks from standard initial states, yet a new instruction may fail after another task has altered the robot's physical state. We study instruction switching, where a new task is issued during or after the execution of a different one. We observe that a target task that is reliably completed from its sta…

## 🌐 具身智能 / 机器人基础模型 (8 篇)

### 1. Deploying Foundation Models for Embodied Navigation

- **arXiv**: [2609.25666v1](https://arxiv.org/abs/2609.25666v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.25666v1)
- **作者**: Vishnu Sashank Dorbala, Dinesh Manocha
- **发表**: 2026-09-22  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: We present and tackle two problems associated with deploying Foundation Models (FMs) on Embodied Agents performing navigation: 1) Training bias in FMs leading to poor personalization in unseen environments, and 2) Limited FM context length hindering success, especially on long horizon tasks. Our solution for the former involves priming the FM with human-hab…

### 2. PUBG Ally: A Conversational Embodied Agent as an AI Teammate

- **arXiv**: [2609.29837v2](https://arxiv.org/abs/2609.29837v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.29837v2)
- **作者**: PUBG Ally Team, Irene Chen, Youngin Cho et al.
- **发表**: 2026-09-24  ·  **类别**: cs.AI, cs.CL, cs.HC
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: We introduce PUBG Ally, an embodied agent for PUBG: BATTLEGROUNDS that can reason, act autonomously, and play alongside players as a voice-enabled teammate. Building such a teammate requires combining two difficult capabilities: it must perceive and respond to a constantly changing game world under strict latency constraints while interacting naturally with…

### 3. AquaMend: Minimal Re-probing and Conditional Rollback for Latent-Belief Failures in Embodied Agents

- **arXiv**: [2609.28973v1](https://arxiv.org/abs/2609.28973v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28973v1)
- **作者**: Yufan Liu, Shang Luo, Yang Liu et al.
- **发表**: 2026-09-24  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Physical changes or sensing errors can invalidate embodied agents' task-relevant beliefs. AquaMend compares re-probing, rollback, and supported continuation on a probe-belief-action graph under an expected-loss objective covering sensing, physical recovery, and uncorrected failures. A joint posterior guides a one-step policy with conditional detection-power…

### 4. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 5. NavGen: Visual Generative Models as a Scalable Data Engine for Embodied 3D Navigation

- **arXiv**: [2609.30770v1](https://arxiv.org/abs/2609.30770v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.30770v1)
- **作者**: Xijie Huang, Yongyang Wan, Chengbin Dong et al.
- **发表**: 2026-09-25  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: General-purpose robot models increasingly rely on large and diverse datasets. For embodied 3D navigation, however, existing data sources face a fundamental trade-off: simulated data can be generated at scale but often suffer from the visual sim-to-real gap, whereas real-world flight data provide realistic observations but are costly to collect. This paper s…

### 6. Skip the Talk, Re-Focus on Vision: Latent Reasoning for Reasoning Segmentation in Multimodal Large Language Models

- **arXiv**: [2609.30783v1](https://arxiv.org/abs/2609.30783v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.30783v1)
- **作者**: Tianhang Guo, Yulin He, Wei Chen et al.
- **发表**: 2026-09-25  ·  **类别**: cs.CV, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Reasoning segmentation aims to interpret implicit textual queries and enable fine-grained visual perception, which is critical for applications such as human-computer interaction and embodied agents. Existing methods typically generate explicit Chain-of-Thought (CoT) by multimodal large language models (MLLMs) before localizing the target. Although intuitiv…

### 7. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

### 8. Monocular Depth Estimation from a Single Image: Progress and Opportunities

- **arXiv**: [2609.01172v1](https://arxiv.org/abs/2609.01172v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.01172v1)
- **作者**: Muxin Liu, Xiaoyang Lyu, Yang-Tian Sun et al.
- **发表**: 2026-09-01  ·  **类别**: cs.CV
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Monocular depth estimation has long stood as a fundamental challenge in computer vision, enabling a wide range of applications including 3D reconstruction, robotics, autonomous driving, and augmented reality. This survey traces the field's evolution from early learning-based methods to the emergence of transformative foundation models. We begin by framing t…

## 🦵 人形 / 足式机器人 (30 篇)

### 1. Aerial Manipulation in the Wild with Onboard Perception, Policy Learning, and Whole-Body Control

- **arXiv**: [2609.30521v1](https://arxiv.org/abs/2609.30521v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.30521v1)
- **作者**: Yuanzhu Zhan, Yufei Jiang, Zemu Zhang et al.
- **发表**: 2026-09-24  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Aerial manipulation in outdoor environments remains challenging due to the simultaneous requirements of reliable state estimation, stable aerial motion, and precise manipulation under external disturbances. In this work, we present a real-world outdoor aerial manipulation framework that integrates imitation learning, onboard LiDAR-inertial state estimation,…

### 2. Opt2VLA: Force-Aware Vision-Language-Action for Contact-Rich Humanoid Whole-Body Manipulation

- **arXiv**: [2609.23968v1](https://arxiv.org/abs/2609.23968v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.23968v1)
- **作者**: Fukang Liu, Yipu Chen, Jaehwi Jang et al.
- **发表**: 2026-09-21  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Humanoid robots are expected to perform diverse human-level tasks in daily environments, many of which require precise regulation of interaction forces. While recent vision-language-action (VLA) models have shown promise for semantic planning and visuomotor control, existing humanoid systems primarily represent actions through geometric motion goals and rel…

### 3. The Cartesian Hand: In-Hand Manipulation with All-Linear Fingers

- **arXiv**: [2609.25696v1](https://arxiv.org/abs/2609.25696v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.25696v1)
- **作者**: Boxi Xia, Bokuan Li, Ryan Shin et al.
- **发表**: 2026-09-22  ·  **类别**: cs.RO
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: Robotic manipulation has increasingly pursued human-like dexterous hands with many articulated degrees of freedom, offering rich manipulation capabilities at the cost of mechanical and control complexity. At the other extreme, parallel grippers are simple and robust, but provide little ability to manipulate an object after grasping it. Operating articulated…

### 4. Smoothness as a Constraint for Stable Humanoid Locomotion

- **arXiv**: [2609.24552v1](https://arxiv.org/abs/2609.24552v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.24552v1)
- **作者**: Utsav Panchal, Denis Kleyko, Unal Artan et al.
- **发表**: 2026-09-21  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Embodied AI systems, particularly humanoid robots deployed in real world scenarios require whole-body control policies that are both task-responsive and physically smooth. However, smoothness is not uniform across the body: lower body must remain sufficiently reactive, while the upper body must be tightly regulated to preserve stability. Existing reinforcem…

### 5. MATE: Multi-Agent Virtual Teleoperation Platform for Humanoid Collaboration Data Collection

- **arXiv**: [2609.26520v1](https://arxiv.org/abs/2609.26520v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.26520v1)
- **作者**: Yichuan Yu, Youzhuo Wang, Yiming Ren et al.
- **发表**: 2026-09-22  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Humanoid robots require diverse embodied experiences to acquire complex loco-manipulation and collaborative skills. However, existing humanoid data pipelines primarily focus on individual agents, while physical multi-robot collaboration remains difficult to scale due to costly hardware, dedicated spaces, and repeated resets. In this work, we introduce MATE,…

### 6. Praxis: Distilling Physical Interaction Priors from Egocentric Videos for Generalizable Whole-Body Manipulation

- **arXiv**: [2609.30735v1](https://arxiv.org/abs/2609.30735v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.30735v1)
- **作者**: Shuliang He, Ruiyan Xu, Bo Yue et al.
- **发表**: 2026-09-25  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Mobile humanoid manipulation requires both reaching a usable workspace and preserving precise hand-object interactions as object poses and contact conditions change. Learning these behaviors from limited task-specific data remains challenging. To bridge this gap, we introduce Praxis, a whole-body manipulation framework that combines physical interaction pri…

### 7. Online Sim-to-Real Adaptation via Closed-Loop System Modeling

- **arXiv**: [2609.28878v1](https://arxiv.org/abs/2609.28878v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28878v1)
- **作者**: Yuhao Huang, Samuel A. Moore, Boyuan Chen
- **发表**: 2026-09-24  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Sim-to-real transfer has made substantial progress, but can still produce controllers that remain stable and functional on hardware while suffering from degraded tracking accuracy due to residual dynamics mismatch. Correcting these errors typically requires identifying the underlying system dynamics, adapting the control policy, or returning to simulation f…

### 8. Learning Expressive Humanoid Locomotion from Monocular Runway Videos for Robot Fashion Shows

- **arXiv**: [2609.27003v1](https://arxiv.org/abs/2609.27003v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27003v1)
- **作者**: Kyrylo Kolesnichenko, Irvin Steve Cardenas, Jong-Hoon Kim
- **发表**: 2026-09-22  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Runway walking requires coordinated control of posture, stride, foot placement, and whole-body motion to effectively present clothing and convey a distinctive style. However, humanoid robots used in fashion shows typically rely on locomotion policies optimized primarily for stability and walking speed, limiting their ability to reproduce expressive, human-l…

### 9. TactileStep: Sole Tactile Learning for Regulating Foot-Terrain Interaction in Humanoid Locomotion

- **arXiv**: [2609.28959v1](https://arxiv.org/abs/2609.28959v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28959v1)
- **作者**: Zizhuo Wang, Ming-ju Lee, Shaoting Zhu et al.
- **发表**: 2026-09-24  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Humanoid parkour policies can traverse various terrains, but task completion may mask challenges of harsh landings, edge contacts, and unstable stance contacts. Humans naturally regulate foot-terrain interaction through tactile feedback, modulating contact compliance according to terrain stiffness. This highlights a key domain gap between humans and humanoi…

### 10. Breaking speed scaling in quadrupedal robots via Huygens' coupled-pendulum dynamics

- **arXiv**: [2609.13290v1](https://arxiv.org/abs/2609.13290v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.13290v1)
- **作者**: Yucheng Tao, Yongbin Jin, Shaowen Cheng et al.
- **发表**: 2026-09-09  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Achieving biological-level running speeds has largely been pursued through advances in control algorithms, which improve the utilization of existing hardware. However, the ultimate speed limits remain governed by the underlying force and torque requirements of rapid locomotion, which are typically addressed through increased actuator capacity. Inspired by H…

## 🦾 操控 / 灵巧手 / 抓取 (32 篇)

### 1. VisForce: Visual Grounding of Current and Desired Forces for Goal-Conditioned Dexterous Manipulation

- **arXiv**: [2609.25785v1](https://arxiv.org/abs/2609.25785v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.25785v1)
- **作者**: Jung-Woo Lee, Soo-Chul Lim
- **发表**: 2026-09-22  ·  **类别**: cs.RO
- **相关性评分**: 20  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models have emerged as general-purpose robotic manipulation policies. However, in dexterous hand manipulation, contact forces are typically provided as separate states or force-specific representations, making it difficult to explicitly represent the spatial correspondence between force and their corresponding visual locations.…

### 2. Res-HIL: Human-Guided Residual Reinforcement Learning for Sample-Efficient Dexterous Manipulation

- **arXiv**: [2609.30023v1](https://arxiv.org/abs/2609.30023v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.30023v1)
- **作者**: Mariia Iavorskaia, Christian Dietz, Sebastian Albrecht et al.
- **发表**: 2026-09-24  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Imitation learning enables robots to acquire manipulation skills from demonstrations, but the resulting policies can fail outside the training data, while collecting more demonstrations requires substantial human effort. Human-in-the-loop reinforcement learning uses corrective feedback during online training, but typically learns the complete task policy ra…

### 3. Towards High-DoF Dexterous Manipulation through VLA Post-Training

- **arXiv**: [2609.19666v1](https://arxiv.org/abs/2609.19666v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.19666v1)
- **作者**: Junlei Zhu, Shenzhe Yao, Chaogui Huang et al.
- **发表**: 2026-09-17  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Imitation-learned vision--language--action (VLA) foundation models acquire broad manipulation capabilities by scaling robot data across tasks and embodiments, but reliable deployment on a specific downstream task and hardware platform still requires post-training. Dexterous hands make this adaptation particularly difficult: their broad behavioural repertoir…

### 4. Enabling a Unified Cross-Domain Representation for Two-Finger Gripper Manipulation via Interaction-Centric Modeling

- **arXiv**: [2609.31207v1](https://arxiv.org/abs/2609.31207v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.31207v1)
- **作者**: Guanlin Li, Shifeng Bao, Yihan Zhao et al.
- **发表**: 2026-09-25  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Achieving robust cross-embodiment generalization in imitation learning demands overcoming a critical representation flaw that inextricably entangles task semantics with hardware-specific visual geometry. We propose an interaction-centric framework that leverages the shared structure of two-finger grippers via a parameterized universal gripper abstraction, y…

### 5. CALM: Current Aligned Link Manipulation for Single Arm Oversized Object Lifting

- **arXiv**: [2609.29017v1](https://arxiv.org/abs/2609.29017v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.29017v1)
- **作者**: Jun Hu, Sihan Chen, Kosta Jovanovic et al.
- **发表**: 2026-09-24  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Most robots manipulate objects solely with their end effectors, whereas humans flexibly leverage different body parts, such as the forearm and elbow, especially when handling oversized objects. Learning such whole-arm manipulation is chal-lenging due to long-horizon sparse rewards, limited contact sens-ing, and the sim-to-real gap in contact and actuator dy…

### 6. Morphometric Imitation: From Morphology and Contact Aware Hand Retargeting to Sim-to-Real Visuomotor Policy

- **arXiv**: [2609.28660v1](https://arxiv.org/abs/2609.28660v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28660v1)
- **作者**: Tara Sadjadpour, Siming He, C. K. Wolfe et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Human hand-object interactions (HOIs) provide a rich source of demonstrations for dexterous manipulation, but learning directly from them presents challenges in bridging morphology gaps, ensuring dynamical feasibility, and sim-to-real deployment. We present Morphometric Imitation, a three-stage framework that transforms reconstructed HOIs into zero-shot sim…

### 7. TANDEM: Task and Motion Planning with As-Needed Demonstrations for Efficient Vision-Language-Action Model Fine-tuning

- **arXiv**: [2609.28314v1](https://arxiv.org/abs/2609.28314v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28314v1)
- **作者**: Samrat Sahoo, Liang Ji, Tom Silver et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Human teleoperators spend substantial time demonstrating behaviors that robots can already perform autonomously, limiting the scalability of data collection for robot foundation models. Task and motion planning (TAMP) can automate many of these behaviors, but a fixed planning domain may not support every stage of a long-horizon manipulation task. We present…

### 8. LiMA: Bridging Long-term Imagination to Real-time Dexterous Manipulation via Asynchronous Diffusion

- **arXiv**: [2609.28431v1](https://arxiv.org/abs/2609.28431v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28431v1)
- **作者**: Ning Chen, Yankai Fu, Junkai Zhao et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation demands long-term foresight and rapid reactive control. Vision-Language-Action (VLA) models, while proficient in high-level reasoning, often lack a fine-grained understanding of physical dynamics and spatial perception. Conversely, World-Action Models (WAMs) typically suffer from high inference latency due to iterative generation. The…

### 9. Listening and Mirroring: The Effects of Verbal Attunement and Behavioral Mimicry on Social and Empathic Perceptions of Embodied AI Agents in VR

- **arXiv**: [2609.27246v1](https://arxiv.org/abs/2609.27246v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27246v1)
- **作者**: Nathalia Gomez, Haig Shamlian, Omar Khan et al.
- **发表**: 2026-09-23  ·  **类别**: cs.HC, cs.AI
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: As embodied agents take on increasingly social and relational roles in VR, visual realism and embodiment alone may be insufficient; users must also perceive these agents as emotionally attuned, supportive, and humanlike. Prior work suggests that verbal attunement and nonverbal mimicry can each improve users' social evaluations of embodied agents. However, b…

### 10. EgoWild2Dex: Learning Dexterous Robotic Manipulation from In-the-Wild Human Experience

- **arXiv**: [2609.23755v1](https://arxiv.org/abs/2609.23755v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.23755v1)
- **作者**: Kunyang Lin, Xutao Wen, Jingxi Lin et al.
- **发表**: 2026-09-20  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Egocentric human data provide a principled source of supervision for learning dexterous robot manipulation. Unlike prior approaches that often collect such data in constrained or specially constructed environments, we collect in-the-wild egocentric demonstrations in real-world settings, including homes, factories, and pharmacies, etc., where people perform…

## 🎓 模仿学习 / 强化学习 (12 篇)

### 1. Sim-to-Real Aware End-to-End Learning Environment for Micromobility

- **arXiv**: [2609.28969v1](https://arxiv.org/abs/2609.28969v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28969v1)
- **作者**: Shouma Amano, Takuya Azumi
- **发表**: 2026-09-24  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: While end-to-end autonomous driving systems show promise, their application to micromobility vehicles is hindered by simulators failing to capture specific kinematics, such as differential drives and omni-wheels. This paper pro- poses a sim-to-real-aware, vehicle-specific end-to-end learning environment for the WHILL Model CR on AWSIM and ROS 2. To minimize…

### 2. HuMemSLAM: Efficient Human-Inspired Semantic Place Recognition for Robust Visual SLAM

- **arXiv**: [2609.17168v1](https://arxiv.org/abs/2609.17168v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.17168v1)
- **作者**: Mayowa Adebambo, Sebastian Donnelly, Armand Amaritei et al.
- **发表**: 2026-09-15  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Autonomous systems require reliable place recognition for efficient and effective simultaneous localisation and mapping (SLAM). Traditional geometric visual SLAM approaches rely on low-level features and geometric consistency, but remain vulnerable to perceptual aliasing, where different places appear similar, and perceptual variation, where the same place…

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

### 5. RawSLAM: Online HDR Gaussian SLAM from Linear Radiance

- **arXiv**: [2609.20589v1](https://arxiv.org/abs/2609.20589v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.20589v1)
- **作者**: Marina Orozco González, Luis Merino
- **发表**: 2026-09-17  ·  **类别**: cs.CV
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Current dense visual SLAM systems rely almost exclusively on 8-bit tonemapped Low Dynamic Range (LDR) inputs, limiting their robustness in extreme lighting where shadows and highlights trigger tracking drift and mapping collapse. Conversely, existing raw and High Dynamic Range (HDR) reconstruction pipelines operate strictly offline. They depend on Structure…

### 6. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

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

### 9. Failure or Drift? Evaluating Monocular SLAM under Synthetic and Real-World Corruptions

- **arXiv**: [2608.30690v1](https://arxiv.org/abs/2608.30690v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.30690v1)
- **作者**: Abhay Skaria Thomas, Shashank Agnihotri, Margret Keuper
- **发表**: 2026-08-31  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Visual SLAM is commonly evaluated on clean trajectories, although deployment failures are often caused by adverse weather, illumination, blur, and sensor artifacts. Controlled corruptions are attractive because they isolate such factors, but a synthetic stress test is useful only when it leads to the same engineering conclusion as the condition it is intend…

### 10. ACE-SLAM: Scene Coordinate Regression for Neural Implicit Real-Time SLAM

- **arXiv**: [2512.14032v1](https://arxiv.org/abs/2512.14032v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2512.14032v1)
- **作者**: Ignacio Alzugaray, Marwan Taher, Andrew J. Davison
- **发表**: 2025-12-16  ·  **类别**: cs.CV, cs.AI, eess.IV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: We present a novel neural RGB-D Simultaneous Localization And Mapping (SLAM) system that learns an implicit map of the scene in real time. For the first time, we explore the use of Scene Coordinate Regression (SCR) as the core implicit map representation in a neural SLAM pipeline, a paradigm that trains a lightweight network to directly map 2D image feature…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (4 篇)

### 1. Know-Your-Scene (KYS)-SLAM: Hierarchical Semantic-Motion Priors for Feature Matching in Stereo Visual SLAM

- **arXiv**: [2609.27509v1](https://arxiv.org/abs/2609.27509v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27509v1)
- **作者**: Preeti Chatterjee, Jin Lu, Jin Sun et al.
- **发表**: 2026-09-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Stereo visual SLAM systems built on local descriptors suffer from semantic ambiguity, instance-level confusion, and independently moving objects, each corrupting data association and accumulating as trajectory drift. Prevailing semantic and dynamic SLAM methods address this through binary feature rejection, sacrificing correspondence density for outlier sup…

### 2. BLASt3R: Bundle Adjustment of Any Image Set with Multi-View Matching and Monocular Priors

- **arXiv**: [2609.05210v1](https://arxiv.org/abs/2609.05210v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.05210v1)
- **作者**: Vincent Leroy, Philippe Weinzaepfel, Lojze Zust et al.
- **发表**: 2026-09-04  ·  **类别**: cs.CV
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Recent hybrid Structure-from-Motion (SfM) systems combine the robustness of feed-forward 3D reconstruction with the accuracy of traditional bundle adjustment (BA) with pixel matching. They are usually the best performing methods however their scalability and usability remains limited since estimating dense correspondences between views is prohibitively cost…

### 3. Cube-Splat: High-Fidelity 360° Gaussian Splatting SLAM via Cubemap Factorization and Adjoint-Consistent Optimization

- **arXiv**: [2609.21347v1](https://arxiv.org/abs/2609.21347v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.21347v1)
- **作者**: Xiangfei Guo, Hao Shi, Yufan Zhang et al.
- **发表**: 2026-09-18  ·  **类别**: cs.CV
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Recent progress in 3D Gaussian Splatting (3DGS) has enabled dense visual SLAM with pinhole cameras, yet most pipelines are not designed for panoramic imagery. We present Cube-Splat, the first panoramic GS-SLAM framework that factorizes each 360° frame into a cubemap of four fixed-orientation virtual pinhole views sharing a single optical center. By designat…

### 4. Geodesic Flow Matching for Denoising High-Dimensional Structured Representations

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
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Imitation-learned robot policies are frequently overfit to the visual conditions present in their training demonstrations. Consequently, variations in object color or background appearance often induce substantial performance degradation. A common mitigation strategy is to acquire additional demonstrations in each novel visual context; however, this approac…

---

## 📋 本日操作建议

**建议今日深读 (Top 3):**
1. [VisForce: Visual Grounding of Current and Desired Forces for Goal-Conditioned Dexterous Manipulation](https://arxiv.org/abs/2609.25785v1) — score 20
2. [Res-HIL: Human-Guided Residual Reinforcement Learning for Sample-Efficient Dexterous Manipulation](https://arxiv.org/abs/2609.30023v1) — score 19
3. [Aerial Manipulation in the Wild with Onboard Perception, Policy Learning, and Whole-Body Control](https://arxiv.org/abs/2609.30521v1) — score 19

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
