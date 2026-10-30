# 机器人研究每日摘要 · 2026-10-31

> 自动生成,共 109 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (7 篇)

### 1. RoboSeed: Multidimensional Evaluation of Vision-Language-Action and World-Action Models: Capability, Resource Affordability, and Research Evidence

- **arXiv**: [2610.40026v1](https://arxiv.org/abs/2610.40026v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.40026v1)
- **作者**: Xin Ma, Furong Chen, Xinlong Man et al.
- **发表**: 2026-10-29  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Choosing a robot action model requires evidence about task capability, adaptation cost, deployment requirements, and the reliability of reported conclusions. Success rates alone offer limited guidance to researchers with different computing budgets and goals. We propose RoboSeed, a multidimensional evaluation framework for vision-language-action (VLA) and w…

### 2. Multi-Dimensional Featurizers Yield Fine-Grained Steering and Data Shaping in Robot Foundation Models

- **arXiv**: [2610.20767v1](https://arxiv.org/abs/2610.20767v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20767v1)
- **作者**: Aiden Swann, Mozes Jacobs, Mathilde Papillon et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Can better feature discovery improve control over robot behavior through internal interventions and training data? Recent work in vision and language models reveals multidimensional features, motivating block-sparse featurizers (BSFs), which represent each feature in a low-dimensional subspace. We investigate whether recovering this structure provides an in…

### 3. Gym-Anything for Robotics: Scaling physical simulations with digital agents

- **arXiv**: [2610.40565v1](https://arxiv.org/abs/2610.40565v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.40565v1)
- **作者**: Pranjal Aggarwal, Sean Welleck
- **发表**: 2026-10-29  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Realistic, fast robotics simulations could enable large-scale training of embodied AI models that transfer to the real world. However, despite decades of progress, available simulations cover only a narrow range of real-world tasks and physical phenomena. The core bottleneck is that creating better simulations requires significant expert effort and therefor…

### 4. BURGER: Benchmarking and Understanding Robotic Generalization via Embodied Drawing

- **arXiv**: [2610.40532v1](https://arxiv.org/abs/2610.40532v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.40532v1)
- **作者**: Xiangyu Xu, Bangshuai Peng, Ziyi Liu et al.
- **发表**: 2026-10-29  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: How effectively can vision-language-action (VLA) models learn diverse language-conditioned behaviors as training data scales? Investigating this question requires large and varied robot datasets, whose collection on physical robots remains costly. We introduce BURGER, a language-conditioned robotic drawing benchmark with a scalable, prompt-driven pipeline f…

### 5. LOGIV: Graph-Verified Execution with Causal Local Repair for Long-Horizon Robot Tasks

- **arXiv**: [2610.40016v1](https://arxiv.org/abs/2610.40016v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.40016v1)
- **作者**: Enqiao Lu, Yuxiang Xie, Xingrui Yu et al.
- **发表**: 2026-10-29  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Agentic robots must turn a high-level goal into actions while keeping the physical conditions needed for future steps valid. A completed action does not ensure that its effects will persist: a later disturbance can invalidate support that the remaining plan still assumes. We present LOGIV, a graph engineering framework for agentic robot execution that uses…

### 6. How Much Should a VLA Trust Its Reasoning? Step-Level Guidance as a Measured Action-Value Function

- **arXiv**: [2610.40002v1](https://arxiv.org/abs/2610.40002v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.40002v1)
- **作者**: Dabin Seo, Eunhyek Joa
- **发表**: 2026-10-29  ·  **类别**: cs.RO, cs.CV, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Reasoning vision-language-action (VLA) policies write a reasoning trace and then decode the action from it. A wrong trace yields a wrong action, and even a correct-looking trace can mislead the plan. Existing remedies ask whether the reasoning is right. We ask how strongly it should steer. CoC-CFG applies classifier-free guidance between the policy's contex…

### 7. Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success

- **arXiv**: [2610.31670v2](https://arxiv.org/abs/2610.31670v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.31670v2)
- **作者**: Yunfei Xie, Howard H. Qian, Shiyi Lan et al.
- **发表**: 2026-10-22  ·  **类别**: cs.CV, cs.LG, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Robot foundation models are typically evaluated through costly closed-loop rollouts, motivating low-cost offline proxies for model capability. The Platonic Representation Hypothesis (PRH) suggests that as representations improve, modalities such as vision and language converge toward a shared statistical model of reality. We ask whether motion trajectories…

## 🌐 具身智能 / 机器人基础模型 (9 篇)

### 1. VISTA: Active Exploration for Self-Improvement in Embodied Agents

- **arXiv**: [2610.35051v1](https://arxiv.org/abs/2610.35051v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.35051v1)
- **作者**: Zhang Zhang, Shengjun Zhang, Simin Huang et al.
- **发表**: 2026-10-26  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Agentic embodied intelligence plays a foundational role in open-ended, dynamic physical environments. Rather than treating policy learning as an end-to-end mapping from instructions to actions, recent studies reveal that embodied systems depend not only on pre-trained foundation models, but also on harness. Prior approaches largely treat rollouts as static…

### 2. TP-JSCC: Efficient Token Pruning and Joint Source-Channel Coding for LVLMs-based 3D-VQA in Cloud-Edge Collaboration

- **arXiv**: [2610.35489v1](https://arxiv.org/abs/2610.35489v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.35489v1)
- **作者**: Zhengxin Li, Chongzhen Tian, Hui Yuan et al.
- **发表**: 2026-10-26  ·  **类别**: cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Deploying large vision-language models (LVLMs) on resource-constrained embodied agents for 3D visual question answering necessitates cloud-edge collaboration. However, offloading massive visual data to the cloud over bandwidth-limited and noisy channels introduces severe latency and transmission distortion. To address this, we propose TP-JSCC, an efficient…

### 3. EmbodiExp: Compositional Experience Transfer for Embodied Agents

- **arXiv**: [2610.39180v1](https://arxiv.org/abs/2610.39180v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.39180v1)
- **作者**: Zhifeng Gu, Ying Chen, Rui Jiang et al.
- **发表**: 2026-10-29  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Experience can help embodied agents turn high-level plans into grounded actions, but transferring it across tasks remains challenging: previously effective strategies may be inapplicable to the current state or fail to produce their intended outcomes. We present EmbodiExp, a framework for constructing transferable experiences and composing them online durin…

### 4. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 5. Ask to Evolve: A Unified Harness for Lifelong Embodied Navigation with Hybrid Action Space and Persistent Memory

- **arXiv**: [2610.39446v1](https://arxiv.org/abs/2610.39446v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.39446v1)
- **作者**: Kai Sheng, Liuyi Wang, Jinlong Li et al.
- **发表**: 2026-10-29  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Giving embodied agents the freedom to act autonomously, initiate interactions, and understand their surroundings through experience is a step toward bringing them to life in the physical world. Realizing this vision requires action, interaction, and memory to work together, so that each encounter can inform current decisions and contribute experience for fu…

### 6. MemVLN: Streaming Episodic Memory for Vision-Language Navigation

- **arXiv**: [2610.35066v2](https://arxiv.org/abs/2610.35066v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.35066v2)
- **作者**: Yan Wang, Jiangyong Huang, Siyuan Huang et al.
- **发表**: 2026-10-26  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-language navigation (VLN) requires an embodied agent to follow language instructions through 3D environments. Maintaining persistent episodic memory remains a challenge for VLM-based streaming agents in long-horizon navigation. We present MEMVLN, a streaming episodic memory framework that maintains a bounded bank of compressed perceptual features ann…

### 7. ScheNav: Schematic-Guided Object Goal Navigation

- **arXiv**: [2610.34286v1](https://arxiv.org/abs/2610.34286v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.34286v1)
- **作者**: Guichen Huang, Chenchen Jing, Che Sun et al.
- **发表**: 2026-10-25  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Object goal navigation requires an embodied agent to locate and reach target objects in complex environments. Humans often rely on low-cost yet informative schematic maps, such as rough sketches or directional annotations. We develop a workflow for schematic-guided embodied navigation with two components: a training-data generation pipeline and ScheNav, a c…

### 8. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

### 9. FoundationVIO: Enforcing Metric Scale in Feed-forward Visual-Inertial Odometry

- **arXiv**: [2610.14951v1](https://arxiv.org/abs/2610.14951v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.14951v1)
- **作者**: Jin Rhee, Yuhao Zhang, Frank Dellaert et al.
- **发表**: 2026-10-10  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Feed-forward geometric foundation models (GFMs) directly predict dense geometry and camera poses from batches of images. Emerging visual SLAM methods chain together consecutive GFM batches to form dense point cloud maps. A core challenge is how to address the ambiguous geometric scale of GFM predictions: independent predictions are locally consistent up-to-…

## 🦵 人形 / 足式机器人 (29 篇)

### 1. ScheduleGen: Demonstration Generation via Skill Scheduling for Multi-Arm Imitation Learning

- **arXiv**: [2610.39429v1](https://arxiv.org/abs/2610.39429v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.39429v1)
- **作者**: Neel Jawale, Stephan Pleines, Soha Pouya et al.
- **发表**: 2026-10-29  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Multi-arm robot platforms, including bimanual and humanoid robots, have the capability to complete tasks with lower cycle times than single-arm systems, but they are more difficult to safely control due to the presence of multi-arm constraints. The paradigm of training generalist robot policies from massive datasets is a promising approach to address genera…

### 2. ELEVATE: Agentic Controller Acquisition from Task Failure for Quadrupedal Manipulation

- **arXiv**: [2610.38388v1](https://arxiv.org/abs/2610.38388v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.38388v1)
- **作者**: Shiqi Liu, Radu Corcodel, Ding Zhao
- **发表**: 2026-10-28  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Quadrupedal manipulators can extend their workspace through whole-body interaction, but task-planning agents' capabilities remain limited by their available controllers. We present ELEVATE, a framework that uses persistent failures during task-program refinement to identify and acquire missing whole-body control capabilities. When these failures suggest a m…

### 3. Catch It All!: Generalizable Dynamic Catching with a Dexterous Hand

- **arXiv**: [2610.39044v1](https://arxiv.org/abs/2610.39044v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.39044v1)
- **作者**: Arth Shukla, Kehlani Fay, Huaze Liu et al.
- **发表**: 2026-10-28  ·  **类别**: cs.RO
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: Catching arbitrary objects requires generalization to novel projectiles and real-time adaptation to unpredictable contact dynamics under noisy visual observations. This paper presents Catch It All!, a sim-to-real catching framework for humanoid robots that generalizes and adapts to unseen objects with variable physical properties for underhand and overhand…

### 4. A fully articulated humanoid dexterous hand with human-level joint structure enabled by linkage-based actuation

- **arXiv**: [2610.36789v1](https://arxiv.org/abs/2610.36789v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.36789v1)
- **作者**: Jihao Li, Jianguo Wang, Haotian Guo et al.
- **发表**: 2026-10-27  ·  **类别**: cs.RO
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: Humanoid dexterous hands are a core component of embodied intelligence, enabling robots to translate high-level intent into rich and adaptive physical interaction. However, existing designs remain constrained by a persistent trade-off among anthropomorphic kinematic complexity, mechanical robustness, load capacity and control simplicity, limiting dexterous…

### 5. SP-HLM: Sparse-Pose-Driven Motion Generation and Whole-Body Control for Humanoid Loco-Manipulation

- **arXiv**: [2610.30044v1](https://arxiv.org/abs/2610.30044v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30044v1)
- **作者**: Zhaohui Yang, Quanbao Lin, Chengqi Shi et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 15  ·  **✅ 已研读**
- **摘要**: Humanoid loco-manipulation requires an effective interface between high-level task policies and whole-body control. Existing interfaces typically rely on a single action representation for both task intent and whole-body coordination. This may burden the high-level policy or leave one aspect underspecified. We present SP-HLM, a framework built on a sparse-p…

### 6. From Tabletop to Walking Bot: Deploying a VLA Model on a Legged Manipulator Robot

- **arXiv**: [2610.32271v1](https://arxiv.org/abs/2610.32271v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.32271v1)
- **作者**: Giovanni Minelli, Antonio Langella, Giovanni B. Dessy et al.
- **发表**: 2026-10-23  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models are typically pretrained on broad, diverse datasets and subsequently fine-tuned on a comparatively small dataset tailored to a specific target robot. Such adaptation recipe is now widely established, achieving its most mature results on fixed-base arms due to their static base dynamics and consistent reference frame. Moun…

### 7. Motion Retargeting with Spatiotemporal Preferences for Humanoid Loco-Manipulation

- **arXiv**: [2610.30540v2](https://arxiv.org/abs/2610.30540v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30540v2)
- **作者**: Xiongbo Shi, Shihang Du, Zongyou Yu et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Human motion retargeting bridges the embodiment gap between humans and humanoid robots by converting human demonstrations into reference trajectories for whole-body control and loco-manipulation. For object-interaction tasks, successful execution depends on accurately preserving body--object relations at critical stages. However, uniform per-frame iteration…

### 8. HuGe: Scaling Humanoid Generalist Vision-Language-Action Models with Egocentric Experience

- **arXiv**: [2610.34186v1](https://arxiv.org/abs/2610.34186v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.34186v1)
- **作者**: Yang Liu, Jiacheng Liu, Hengtao Li et al.
- **发表**: 2026-10-25  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Extending Vision-Language-Action models (VLAs) to humanoid robots requires coordinated whole-body control and diverse demonstrations that are costly to collect in real-world scenarios. Although egocentric human demonstrations provide a complementary source of task experience, differences in visual embodiment and missing robot proprioception complicate trans…

### 9. ThinkLocoManip: A Whole-Body Control Agentic Harness for Legged Loco-Manipulation

- **arXiv**: [2610.34370v1](https://arxiv.org/abs/2610.34370v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.34370v1)
- **作者**: Nuo Chen, Shizeng Zhang, Yujie Yang et al.
- **发表**: 2026-10-25  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: In this paper, we propose ThinkLocoManip, an agentic harness for legged loco-manipulation designed to tackle complex, long-horizon tasks in large-scale environments. Existing approaches typically follow either direct action generation or a plan-then-act paradigm, both of which can struggle with the generalization and error-recovery capabilities required for…

### 10. E2DRL: End-to-End Differentiable Reinforcement Learning for 3D Obstacle Avoidance in Quadruped Robots

- **arXiv**: [2610.19627v1](https://arxiv.org/abs/2610.19627v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19627v1)
- **作者**: Cheng Fan, Bingyang Zhou, Gang Yang et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Differentiable reinforcement learning shows strong promise for robot policy learning, but its application to legged locomotion has remained limited to blind walking or simulated 2D tasks. Extending it to end-to-end visual obstacle avoidance is challenging because hard collision constraints and early termination upon contact corrupt first-order gradients, tr…

## 🦾 操控 / 灵巧手 / 抓取 (35 篇)

### 1. EXE: Egocentric Cross-Embodiment Pretraining via Factorized Latent Actions for VLA Models

- **arXiv**: [2610.33685v1](https://arxiv.org/abs/2610.33685v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.33685v1)
- **作者**: Qingyuan Cai, Bo Zhang, Yongzhen Huang et al.
- **发表**: 2026-10-24  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 20  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models are bottlenecked by the scarcity of robot data. Egocentric human manipulation videos offer an abundant, diverse, and semantically-rich alternative that inherently captures manipulation intent. However, the embodiment gap makes it difficult to extract action-relevant representations from these videos. From the perspective…

### 2. Learning Dexterous Manipulation: Hands, Simulators, Training, and Evaluation

- **arXiv**: [2610.33486v1](https://arxiv.org/abs/2610.33486v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.33486v1)
- **作者**: Luai Abuelsamen
- **发表**: 2026-10-24  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: A dexterous hand can change an object's pose without setting it down. This survey covers 113 learning-based methods that attempt it, the hands they run on, the simulators they train in, and how they report results. The field has largely converged on one recipe: reinforcement learning on privileged state in a GPU simulator, distilled into a vision-only stude…

### 3. TouchBridge: Tactile-Conditioned Human-to-Robot Transfer for Dexterous Manipulation

- **arXiv**: [2610.40349v1](https://arxiv.org/abs/2610.40349v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.40349v1)
- **作者**: Haozhe Zhang, Gu Zhang, Zirui Zou et al.
- **发表**: 2026-10-29  ·  **类别**: cs.RO
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: Human demonstrations offer an efficient and scalable source of data for dexterous robot manipulation, but differences in sensing and hand morphology complicate the transfer of contact-rich interactions. We present TouchBridge, a hardware--software co-designed framework for human-to-robot data transformation. A wearable human demonstration interface and a co…

### 4. DexSuite: An All-in-One Framework for Dexterous Manipulation Across Arms, Hands, and Tasks

- **arXiv**: [2610.37799v1](https://arxiv.org/abs/2610.37799v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.37799v1)
- **作者**: Anas Houssaini, Hugo He, Junming Shi et al.
- **发表**: 2026-10-27  ·  **类别**: cs.RO
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: Human-level dexterity remains a central open problem in robotics, yet few simulation frameworks cover the full workflow of dexterous manipulation, from setting up a robot to collecting dexterous demonstrations and evaluating policies. We present DexSuite, an all-in-one simulation framework for dexterous manipulation built on the Genesis simulator. DexSuite…

### 5. SoTa: Soft Tactile Skins for Dexterous Manipulation

- **arXiv**: [2610.02338v1](https://arxiv.org/abs/2610.02338v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.02338v1)
- **作者**: Jingyun Yang, Baiyu Shi, Timothy Yu et al.
- **发表**: 2026-10-01  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: A growing body of work suggests that tactile sensing gives robot policies contact information that complements vision in dexterous manipulation. However, visuo-tactile robot data remains scarce: dexterous demonstrations require teleoperating robots, which limits dataset scale. Human demonstrations are far cheaper to collect and offer a path to scale this da…

### 6. HiFOR: Hierarchical Foresight with Action-Guided World Grounding for Vision-Language-Action Model

- **arXiv**: [2610.40373v1](https://arxiv.org/abs/2610.40373v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.40373v1)
- **作者**: Rongxing Ding, Hongyu Qu, Kehong Wu et al.
- **发表**: 2026-10-29  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models have demonstrated promising capabilities in robotic manipulation by integrating visual perception, language understanding, and action generation. Recent advances have further incorporated future prediction to enhance the understanding of environmental dynamics and task progression. However, existing methods often model sh…

### 7. SimRetract: Zero-Shot Sim-to-Real Robotic Assistance for Retractor Take-Over in Open Surgery

- **arXiv**: [2610.38234v1](https://arxiv.org/abs/2610.38234v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.38234v1)
- **作者**: Xucheng Wang, Zhizhou Yang, Sung Eun Kim et al.
- **发表**: 2026-10-28  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We demonstrate the first zero-shot sim-to-real transfer for a surgeon-robot collaboration task in open surgery: retractor take-over. A robot arm takes a retractor from the surgeon's hand and preserves retraction at handoff, using a policy trained only on simulated demonstrations, without human demonstrations or real-world fine-tuning. Imitation learning fro…

### 8. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

### 9. AcrossDEX 1.0: From Human Motion Pretraining to Bimanual Dexterous Manipulation across Hand Embodiments

- **arXiv**: [2610.40210v1](https://arxiv.org/abs/2610.40210v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.40210v1)
- **作者**: Xiaoyu Yang, Nan Wu
- **发表**: 2026-10-29  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Bimanual dexterous manipulation requires continuous coordination of wrist motion, finger contact, and object motion. Human videos provide rich manipulation experience. Using this experience for robot control requires aligning human poses with robot commands and accounting for embodiment-specific kinematics and contact dynamics. We present AcrossDEX 1.0, a l…

### 10. ActiveAlign: Aligning Egocentric Manipulation via Active Perception

- **arXiv**: [2610.36859v1](https://arxiv.org/abs/2610.36859v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.36859v1)
- **作者**: Ri-Zhao Qiu, Bowen Wen, Yifeng Jiang et al.
- **发表**: 2026-10-27  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Real-to-Sim-to-Real (Real2Sim2Real) enables structured world representations for planning, interpretability, and safe execution. Most existing approaches rely on passive perception, which creates real2sim gaps due to imperfect observation. Inspired by how humans perceive actively through actions, we propose ActiveAlign, a framework that leverages active per…

## 🎓 模仿学习 / 强化学习 (14 篇)

### 1. Bracketing Shows the Way: Adaptive Multi-Exposure Policy as Input for Robust Visual SLAM

- **arXiv**: [2610.33174v1](https://arxiv.org/abs/2610.33174v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.33174v1)
- **作者**: Olivier Gamache, Anthony Lavertu, David-Alexandre Duclos et al.
- **发表**: 2026-10-23  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Rapid illumination transitions can disturb Visual SLAM (VSLAM) by saturating images before the Automatic Exposure (AE) policy adapts, removing the visual correspondences needed to maintain tracking. Our proposed methods mitigate this disturbance at two levels: B-Adapt acquires adaptive exposure brackets to cover the scene dynamic range while promoting photo…

### 2. Omni-IGN: Onboard Image-Goal Navigation for Drones with Omnidirectional Vision

- **arXiv**: [2610.36968v1](https://arxiv.org/abs/2610.36968v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.36968v1)
- **作者**: Zichen Yan, Rui Huang, Shenao Wang et al.
- **发表**: 2026-10-27  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Image-goal navigation (ImageNav) requires an agent to reach a location specified by a goal image in an unknown environment. For drones, this task demands exploration, goal- directed navigation, and collision avoidance under limited onboard computing resources. Existing aerial ImageNav methods are built on single-view observations, requiring additional rotat…

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

### 8. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 9. Provably Efficient Q-learning for Robust Reinforcement Learning

- **arXiv**: [2610.35656v1](https://arxiv.org/abs/2610.35656v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.35656v1)
- **作者**: Yuchen Jiao, Gen Li
- **发表**: 2026-10-26  ·  **类别**: stat.ML, cs.AI, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Standard reinforcement learning (RL) algorithms based on Markov Decision Processes (MDPs) are vulnerable to sim-to-real gaps. To address this issue, distributionally robust RL algorithms based on robust MDPs (RMDPs) have been proposed, for ensuring that agents can perform reliably to unpredictable conditions in real-world environments. Despite of the rich l…

### 10. Unblur-SLAM: Dense Neural SLAM for Blurry Inputs

- **arXiv**: [2603.26810v1](https://arxiv.org/abs/2603.26810v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.26810v1)
- **作者**: Qi Zhang, Denis Rozumny, Francesco Girlanda et al.
- **发表**: 2026-03-26  ·  **类别**: cs.CV, eess.IV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We propose Unblur-SLAM, a novel RGB SLAM pipeline for sharp 3D reconstruction from blurred image inputs. In contrast to previous work, our approach is able to handle different types of blur and demonstrates state-of-the-art performance in the presence of both motion blur and defocus blur. Moreover, we adjust the computation effort with the amount of blur in…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (11 篇)

### 1. SKiD-SLAM: Resource-Aware Distributed Multi-Robot LiDAR SLAM for Planetary Missions with Field Deployments at Analog Sites

- **arXiv**: [2610.38141v1](https://arxiv.org/abs/2610.38141v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.38141v1)
- **作者**: Hogyun Kim, Juwon Kim, Dongjin Cho et al.
- **发表**: 2026-10-28  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **📚 综述(归档备查,按协议 §4 不深读)**
- **摘要**: Future planetary exploration missions require teams of robots to collaboratively map unknown environments under severe communication limits, constrained onboard computation, and no central infrastructure. In this field report, we present SKiD-SLAM, a distributed multi-robot LiDAR simultaneous localization and mapping (SLAM) system for such environments, and…

### 2. LIN-SLAM: Lightweight LiDAR--Inertial Neural SLAM for Real-Time Onboard Navigation

- **arXiv**: [2610.21199v1](https://arxiv.org/abs/2610.21199v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.21199v1)
- **作者**: Shiqi Che, Yijie Liu, Shuo Wang et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **✅ 已研读**
- **摘要**: Geometric light detection and ranging (LiDAR)--inertial simultaneous localization and mapping (SLAM) provides efficient state estimation but lacks the continuous map representation and global refinement capabilities of neural implicit SLAM, while neural implicit methods remain computationally expensive. We propose Lightweight LiDAR--Inertial Neural SLAM (LI…

### 3. Evaluation of Front-End Feature Matching for Lunar Visual SLAM

- **arXiv**: [2610.30774v1](https://arxiv.org/abs/2610.30774v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30774v1)
- **作者**: Guillem Casadesus Vila, Grace Gao
- **发表**: 2026-10-22  ·  **类别**: cs.CV
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Lunar rovers will primarily rely on cameras for localization until navigation satellite services are deployed, and will continue to need them afterwards for relative navigation, hazard detection, and surface operations. Visual odometry (VO) and Simultaneous Localization and Mapping (SLAM) mostly estimate motion by matching features between frames. However,…

### 4. Smartphone Indoor Localization Enhanced by Hierarchical Multi-Sensor Context Recognition

- **arXiv**: [2610.39691v1](https://arxiv.org/abs/2610.39691v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.39691v1)
- **作者**: Wenhui Feng, Muhan Weng, Jianyu Liu et al.
- **发表**: 2026-10-29  ·  **类别**: cs.LG, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Smartphone indoor localization requires low-cost, robust positioning across scene transitions and phone-use variations. Pedestrian dead reckoning (PDR) enables infrastructure-free deployment but accumulates errors from heading drift, structural transitions, and carrying-mode changes. Existing methods often treat contextual cues as a single event stream or l…

### 5. Line-Augmented cuVSLAM: Robust Visual Odometry in Low-Texture Environments

- **arXiv**: [2610.20958v1](https://arxiv.org/abs/2610.20958v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20958v1)
- **作者**: Dara Molloy, Terry Wu, Wonju Lee et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Autonomous mobile robots in warehouses and production facilities operate in precisely the environments that defeat point-feature visual odometry: featureless aisles, uniform walls, repetitive racking and specular floors. Such environments are, however, rich in straight-edge structure: rack uprights, door frames, wall junctions and cabinet outlines present h…

### 6. Human-in-the-Loop Neuro-Symbolic Drift Anticipation for Reliable Visual SLAM

- **arXiv**: [2610.05757v1](https://arxiv.org/abs/2610.05757v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05757v1)
- **作者**: Junhyun Nam, Wonse Jo
- **发表**: 2026-10-05  ·  **类别**: cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: This paper introduces Hybrid DeepSEE (HDS), a Human-in-the-Loop (HITL) neuro-symbolic framework for proactive drift anticipation in Visual SLAM (V-SLAM). While data-driven models offer predictive power, their "black-box" nature often yields physically inconsistent outputs in out-of-distribution (OOD) environments. To address this, HDS integrates neural drif…

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
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Indoor building construction sites are demanding environments for visual SLAM, where variable lighting and repetitive, low-textured structures make the system drift over long trajectories, though structural elements such as walls remain distinguishable despite these conditions. These buildings are constructed according to their as-planned floor plans, avail…

### 10. Parameter Sensitivity Analysis for Aerial LiDAR-Inertial Odometries in low-altitude flights

- **arXiv**: [2609.12837v1](https://arxiv.org/abs/2609.12837v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.12837v1)
- **作者**: Robert Milijas, Jose Ramiro Martinez-de Dios, Stjepan Bogdan
- **发表**: 2026-09-11  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: LiDAR-based SLAM (Simultaneous Localization and Mapping) and LIO (LiDAR-inertial odometry) algorithms are often used for precise navigation of unmanned aerial vehicles, especially during interactions with the aerial robot's environment. However, the performance of these algorithms is greatly dependent on the scenario, LiDAR, and robot motion characteristics…

## 🤏 软体机器人 / 柔性控制 (3 篇)

### 1. From Biological Curves to Soft Modular Robots: Learning-Based Inverse Design with Uncertainty-Guided Refinement

- **arXiv**: [2610.36681v2](https://arxiv.org/abs/2610.36681v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.36681v2)
- **作者**: Dixiang Wang, Minghao Zha, Arifur Rahman et al.
- **发表**: 2026-10-27  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Animals exhibit diverse shape-changing behaviors, from the undulatory swimming of eels to the arching movements of inchworms. Reproducing these biological shapes with modular soft robots offers a promising approach to developing versatile bioinspired robotic systems. However, translating a desired shape into a feasible robotic configuration remains challeng…

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
1. [EXE: Egocentric Cross-Embodiment Pretraining via Factorized Latent Actions for VLA Models](https://arxiv.org/abs/2610.33685v1) — score 20
2. [ScheduleGen: Demonstration Generation via Skill Scheduling for Multi-Arm Imitation Learning](https://arxiv.org/abs/2610.39429v1) — score 19
3. [ELEVATE: Agentic Controller Acquisition from Task Failure for Quadrupedal Manipulation](https://arxiv.org/abs/2610.38388v1) — score 19

> 筛选说明:本次 Top 3 已排除(已研读跳过 2 篇、综述跳过 2 篇)。

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
