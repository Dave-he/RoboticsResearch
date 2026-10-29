# 机器人研究每日摘要 · 2026-10-30

> 自动生成,共 109 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (6 篇)

### 1. PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations

- **arXiv**: [2610.37381v1](https://arxiv.org/abs/2610.37381v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.37381v1)
- **作者**: Hanqing Wang, Zhaotian Cai, Ruichuan An et al.
- **发表**: 2026-10-27  ·  **类别**: cs.RO, cs.CV, cs.LG
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Vision--Language--Action (VLA) models generate robot actions from visual observations and language instructions, but their understanding of physical dynamics remains limited. Video world models can capture scene dynamics, yet generating future videos introduces high latency into the control loop. We introduce PDRVLA, whose lightweight Physical Dynamics Modu…

### 2. Retrieve to Act: Motion Primitive Graph Retrieval for Robust VLA Execution

- **arXiv**: [2610.37215v1](https://arxiv.org/abs/2610.37215v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.37215v1)
- **作者**: Pham Tri Quang, Bao-Ngoc Dao, Minh Duc Nguyen et al.
- **发表**: 2026-10-27  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Vision-Language-Action (VLA) policies demonstrate remarkable semantic generalization, yet remain highly vulnerable to out-of-distribution (OOD) visual shifts during execution. While existing test-time methods attempt to suppress spurious visual cues, they fundamentally overlook the rich, uncorrupted kinematic priors embedded in the policy's own training exp…

### 3. Vision-Language-Action or World-Action? Just Action Models

- **arXiv**: [2610.37219v1](https://arxiv.org/abs/2610.37219v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.37219v1)
- **作者**: Yonghao Yu, Lang Huang, Runyi Li et al.
- **发表**: 2026-10-27  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: The vision-language-action (VLA) and world-action model (WAM) communities debate whether control policies should inherit pretrained knowledge from vision-language models or from visual generators. The debate, however, bundles three separable choices: backbone initialization, the objective applied to future observations, and whether the machinery for that fu…

### 4. Multi-Dimensional Featurizers Yield Fine-Grained Steering and Data Shaping in Robot Foundation Models

- **arXiv**: [2610.20767v1](https://arxiv.org/abs/2610.20767v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20767v1)
- **作者**: Aiden Swann, Mozes Jacobs, Mathilde Papillon et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Can better feature discovery improve control over robot behavior through internal interventions and training data? Recent work in vision and language models reveals multidimensional features, motivating block-sparse featurizers (BSFs), which represent each feature in a low-dimensional subspace. We investigate whether recovering this structure provides an in…

### 5. World Dreamer v5-lite: A Multi-Robot World Action Model with One Dreamer

- **arXiv**: [2610.37518v1](https://arxiv.org/abs/2610.37518v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.37518v1)
- **作者**: Guoning Wu, Zijian Cai, Yuhang Zhang et al.
- **发表**: 2026-10-27  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Multi-robot control requires integrating distributed camera views while predicting separate action sequences. Most vision-language-action and world-action models target one robot. Combining multiple views alone does not establish spatial correspondence between them. World Dreamer v5-lite is a multi-robot world-action model built around a shared world state…

### 6. Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success

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

### 3. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 4. MemVLN: Streaming Episodic Memory for Vision-Language Navigation

- **arXiv**: [2610.35066v2](https://arxiv.org/abs/2610.35066v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.35066v2)
- **作者**: Yan Wang, Jiangyong Huang, Siyuan Huang et al.
- **发表**: 2026-10-26  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-language navigation (VLN) requires an embodied agent to follow language instructions through 3D environments. Maintaining persistent episodic memory remains a challenge for VLM-based streaming agents in long-horizon navigation. We present MEMVLN, a streaming episodic memory framework that maintains a bounded bank of compressed perceptual features ann…

### 5. ScheNav: Schematic-Guided Object Goal Navigation

- **arXiv**: [2610.34286v1](https://arxiv.org/abs/2610.34286v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.34286v1)
- **作者**: Guichen Huang, Chenchen Jing, Che Sun et al.
- **发表**: 2026-10-25  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Object goal navigation requires an embodied agent to locate and reach target objects in complex environments. Humans often rely on low-cost yet informative schematic maps, such as rough sketches or directional annotations. We develop a workflow for schematic-guided embodied navigation with two components: a training-data generation pipeline and ScheNav, a c…

### 6. LegoOcc++: Towards Consistent Open-Vocabulary 3D Occupancy Prediction

- **arXiv**: [2610.34093v1](https://arxiv.org/abs/2610.34093v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.34093v1)
- **作者**: Changqing Zhou, Yueru Luo, Han Zhang et al.
- **发表**: 2026-10-25  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Open-vocabulary 3D occupancy prediction is important for embodied agents operating in complex environments whose semantic categories extend beyond fixed taxonomies. While recent studies have explored open-vocabulary occupancy in outdoor driving scenarios, indoor environments remain challenging due to dense occlusions, complex geometry, and fine-grained long…

### 7. Replicate What Varies: Resource Sharing for Domain-Randomized Embodied Simulation

- **arXiv**: [2610.33582v1](https://arxiv.org/abs/2610.33582v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.33582v1)
- **作者**: Zixu Hao, Weijun Wang, Xiangyu Li et al.
- **发表**: 2026-10-24  ·  **类别**: cs.DC, cs.AI, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Simulation provides a low-cost sandbox where embodied agents can attempt tasks, observe outcomes, and learn from experience. Running many diverse simulation environments concurrently can consume substantial CPU and GPU memory because independently constructed scenes duplicate resources that remain unchanged across instances. We present Patchwork, a resource…

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

## 🦵 人形 / 足式机器人 (30 篇)

### 1. A fully articulated humanoid dexterous hand with human-level joint structure enabled by linkage-based actuation

- **arXiv**: [2610.36789v1](https://arxiv.org/abs/2610.36789v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.36789v1)
- **作者**: Jihao Li, Jianguo Wang, Haotian Guo et al.
- **发表**: 2026-10-27  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Humanoid dexterous hands are a core component of embodied intelligence, enabling robots to translate high-level intent into rich and adaptive physical interaction. However, existing designs remain constrained by a persistent trade-off among anthropomorphic kinematic complexity, mechanical robustness, load capacity and control simplicity, limiting dexterous…

### 2. From Tabletop to Walking Bot: Deploying a VLA Model on a Legged Manipulator Robot

- **arXiv**: [2610.32271v1](https://arxiv.org/abs/2610.32271v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.32271v1)
- **作者**: Giovanni Minelli, Antonio Langella, Giovanni B. Dessy et al.
- **发表**: 2026-10-23  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models are typically pretrained on broad, diverse datasets and subsequently fine-tuned on a comparatively small dataset tailored to a specific target robot. Such adaptation recipe is now widely established, achieving its most mature results on fixed-base arms due to their static base dynamics and consistent reference frame. Moun…

### 3. SP-HLM: Sparse-Pose-Driven Motion Generation and Whole-Body Control for Humanoid Loco-Manipulation

- **arXiv**: [2610.30044v1](https://arxiv.org/abs/2610.30044v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30044v1)
- **作者**: Zhaohui Yang, Quanbao Lin, Chengqi Shi et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 15  ·  **✅ 已研读**
- **摘要**: Humanoid loco-manipulation requires an effective interface between high-level task policies and whole-body control. Existing interfaces typically rely on a single action representation for both task intent and whole-body coordination. This may burden the high-level policy or leave one aspect underspecified. We present SP-HLM, a framework built on a sparse-p…

### 4. Motion Retargeting with Spatiotemporal Preferences for Humanoid Loco-Manipulation

- **arXiv**: [2610.30540v2](https://arxiv.org/abs/2610.30540v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30540v2)
- **作者**: Xiongbo Shi, Shihang Du, Zongyou Yu et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Human motion retargeting bridges the embodiment gap between humans and humanoid robots by converting human demonstrations into reference trajectories for whole-body control and loco-manipulation. For object-interaction tasks, successful execution depends on accurately preserving body--object relations at critical stages. However, uniform per-frame iteration…

### 5. HuGe: Scaling Humanoid Generalist Vision-Language-Action Models with Egocentric Experience

- **arXiv**: [2610.34186v1](https://arxiv.org/abs/2610.34186v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.34186v1)
- **作者**: Yang Liu, Jiacheng Liu, Hengtao Li et al.
- **发表**: 2026-10-25  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Extending Vision-Language-Action models (VLAs) to humanoid robots requires coordinated whole-body control and diverse demonstrations that are costly to collect in real-world scenarios. Although egocentric human demonstrations provide a complementary source of task experience, differences in visual embodiment and missing robot proprioception complicate trans…

### 6. ThinkLocoManip: A Whole-Body Control Agentic Harness for Legged Loco-Manipulation

- **arXiv**: [2610.34370v1](https://arxiv.org/abs/2610.34370v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.34370v1)
- **作者**: Nuo Chen, Shizeng Zhang, Yujie Yang et al.
- **发表**: 2026-10-25  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: In this paper, we propose ThinkLocoManip, an agentic harness for legged loco-manipulation designed to tackle complex, long-horizon tasks in large-scale environments. Existing approaches typically follow either direct action generation or a plan-then-act paradigm, both of which can struggle with the generalization and error-recovery capabilities required for…

### 7. OccluDex: Hierarchical 3D Visuo-Tactile Representation Learning for Egocentric Dexterous Manipulation under Self-Occlusion

- **arXiv**: [2609.39017v1](https://arxiv.org/abs/2609.39017v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39017v1)
- **作者**: Ziheng Xu, Yueyuan Chen, Xinyuan He et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Reliable dexterous manipulation requires continuous estimation of object geometry and hand-object contact throughout interaction. With egocentric sensing, however, the manipulating hand frequently occludes task-relevant object surfaces and contact regions, reducing the visual evidence available for state estimation and thereby making robust closed-loop cont…

### 8. PHD-Hand: A Printable Humanoid Dexterous Hand with Linkage-Driven 3-DOA Digits

- **arXiv**: [2610.29030v1](https://arxiv.org/abs/2610.29030v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.29030v1)
- **作者**: Neel Adwani, Muhaiminul Islam Akash, Saffia Ouali et al.
- **发表**: 2026-10-21  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Currently, dexterous humanoid robot hands are widely considered the final hardware bottleneck that hampers generalist robots from physically assisting people at home and work. As conventional tendon-driven designs suffer from high cost, demanding maintenance, poor reliability, and short durability, alternative linkage-driven designs have increasingly gained…

### 9. E2DRL: End-to-End Differentiable Reinforcement Learning for 3D Obstacle Avoidance in Quadruped Robots

- **arXiv**: [2610.19627v1](https://arxiv.org/abs/2610.19627v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19627v1)
- **作者**: Cheng Fan, Bingyang Zhou, Gang Yang et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Differentiable reinforcement learning shows strong promise for robot policy learning, but its application to legged locomotion has remained limited to blind walking or simulated 2D tasks. Extending it to end-to-end visual obstacle avoidance is challenging because hard collision constraints and early termination upon contact corrupt first-order gradients, tr…

### 10. Tokens of Motion: Primitive Motion Learning for Human-Humanoid Skill Transfer

- **arXiv**: [2610.37330v1](https://arxiv.org/abs/2610.37330v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.37330v1)
- **作者**: Hanwen Ren, Meng Zheng, Wenzhe Cui et al.
- **发表**: 2026-10-27  ·  **类别**: cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Vision-language-action (VLA) models provide a promising paradigm for scalable robotic manipulation, yet their reliance on success-only behavioral cloning leaves them brittle; lacking corrective training signals, minor execution errors rapidly compound into unrecoverable, out-of-distribution failures. To address this limitation, we propose Adaptive Failure-I…

## 🦾 操控 / 灵巧手 / 抓取 (33 篇)

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

### 3. Scaling Dexterous Manipulation via Action Representation Pretraining

- **arXiv**: [2610.34453v1](https://arxiv.org/abs/2610.34453v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.34453v1)
- **作者**: Yanjinghao Xu, Jiexin Zhang, Huan Zhao et al.
- **发表**: 2026-10-25  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Large-scale vision, language, and video pretraining has substantially improved the perception and generalization capabilities of robotic manipulation models, but action generation for complex dexterous manipulation remains constrained by the scarcity of robot demonstrations. Limited robot demonstrations must be used to learn both action representations and…

### 4. RBGA: Residual-Budget Guide Arbitration for Offline-to-Online Safe Reinforcement Learning in Dexterous Manipulation

- **arXiv**: [2610.33494v1](https://arxiv.org/abs/2610.33494v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.33494v1)
- **作者**: Zongyou Yu, Ao Zhou, Xiongbo Shi et al.
- **发表**: 2026-10-24  ·  **类别**: cs.LG
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation requires robots to leverage existing datasets for rapid skill acquisition while maintaining safety during real-world deployment to prevent damage to the robot or its surroundings. Offline-to-online safe reinforcement learning (O2O safe RL) provides a promising solution for this problem by leveraging prior experience for online improve…

### 5. SoTa: Soft Tactile Skins for Dexterous Manipulation

- **arXiv**: [2610.02338v1](https://arxiv.org/abs/2610.02338v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.02338v1)
- **作者**: Jingyun Yang, Baiyu Shi, Timothy Yu et al.
- **发表**: 2026-10-01  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: A growing body of work suggests that tactile sensing gives robot policies contact information that complements vision in dexterous manipulation. However, visuo-tactile robot data remains scarce: dexterous demonstrations require teleoperating robots, which limits dataset scale. Human demonstrations are far cheaper to collect and offer a path to scale this da…

### 6. VLA-Stem: A Lightweight Safety Mechanism for Vision-Language-Action Models via Reinforcement Learning

- **arXiv**: [2610.37378v1](https://arxiv.org/abs/2610.37378v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.37378v1)
- **作者**: Bojun Zou, Wenhao Yu, Jiaohao Li et al.
- **发表**: 2026-10-27  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models integrate high-level reasoning with low-level action execution for end-to-end robotic control. However, most VLA models target static manipulation in unconstrained environments, overlooking spatial constraints and dynamic obstacles. Fine-tuning VLAs on obstacle-avoidance data is a straightforward solution, but collecting…

### 7. AdaDexTrack: Dynamic Modulation for Adaptive and Generalizable Dexterous Manipulation Tracking

- **arXiv**: [2610.33852v1](https://arxiv.org/abs/2610.33852v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.33852v1)
- **作者**: Jianibieke Adalibieke, Qianwei Han, Xueyi Liu et al.
- **发表**: 2026-10-24  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Language is a natural way to command robots, but converting a single instruction into a long-horizon, contact-rich hand-object interaction remains challenging: synthesized references are noisy, human-to-robot retargeting introduces embodiment bias, and fixed-reference tracking lets small errors snowball. We address this with AdaDexTrack, a modulator-in-the-…

### 8. DexPort: A Hand-Held Skill Interface for Dexterous Hand Data Collection

- **arXiv**: [2610.32969v1](https://arxiv.org/abs/2610.32969v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.32969v1)
- **作者**: Amber Xie, Jiawei Fu, Xiaofeng Guo et al.
- **发表**: 2026-10-23  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Collecting high-quality demonstrations remains a central bottleneck for learning dexterous manipulation. Teleoperation records executable robot actions, but it requires a complete robot setup and places the burden of coordinating many finger joints on the operator. Human demonstrations are easier to collect, but their motions must be estimated and retargete…

### 9. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

### 10. CARD: Contact-Anchored Retargeting for Dexterous Manipulation

- **arXiv**: [2610.36539v1](https://arxiv.org/abs/2610.36539v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.36539v1)
- **作者**: Cunxi Dai, Botao He, Francois R Hogan et al.
- **发表**: 2026-10-27  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Humans are dexterous, but traditional data collection paradigms such as teleoperation, kinesthetic teaching, and wearable exoskeletons force humans to act through the robot embodiment, bottlenecking their dexterity. Retargeting can avoid this. However, existing methods purely translate kinematics and ignore the real-world contact dynamics essential for task…

## 🎓 模仿学习 / 强化学习 (16 篇)

### 1. Bracketing Shows the Way: Adaptive Multi-Exposure Policy as Input for Robust Visual SLAM

- **arXiv**: [2610.33174v1](https://arxiv.org/abs/2610.33174v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.33174v1)
- **作者**: Olivier Gamache, Anthony Lavertu, David-Alexandre Duclos et al.
- **发表**: 2026-10-23  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
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

### 10. Dream to Assist: Intent-Conditioned World Models for Shared Vehicle Control

- **arXiv**: [2610.34650v1](https://arxiv.org/abs/2610.34650v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.34650v1)
- **作者**: Jonathan DeCastro, Thomas Balch, Emily Sumner et al.
- **发表**: 2026-10-26  ·  **类别**: cs.RO, cs.HC, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Assistive agents in shared-control settings face a dual challenge: acting proactively to align with the human's intentions while remaining legible enough for the human to comprehend and fluently respond in real time. We present Dream2Assist, a model-based reinforcement learning framework for tightly-coupled shared decision making that addresses both sides o…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (11 篇)

### 1. Learning Interaction-Aware Path Corrections from Unlabeled Trajectories: A LiDAR-Based Sim-to-Real GNN Framework for Construction Robots

- **arXiv**: [2610.34060v1](https://arxiv.org/abs/2610.34060v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.34060v1)
- **作者**: Yilong Chen, Yong K. Cho
- **发表**: 2026-10-25  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Construction robots operating near workers require navigation that can anticipate human motion while remaining robust to dynamic and unstructured site conditions. However, existing social navigation methods depend on hand-crafted interaction rules, labeled demonstrations, or robot-specific control policies, limiting their scalability and transferability in…

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

### 4. Evaluation of Front-End Feature Matching for Lunar Visual SLAM

- **arXiv**: [2610.30774v1](https://arxiv.org/abs/2610.30774v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30774v1)
- **作者**: Guillem Casadesus Vila, Grace Gao
- **发表**: 2026-10-22  ·  **类别**: cs.CV
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Lunar rovers will primarily rely on cameras for localization until navigation satellite services are deployed, and will continue to need them afterwards for relative navigation, hazard detection, and surface operations. Visual odometry (VO) and Simultaneous Localization and Mapping (SLAM) mostly estimate motion by matching features between frames. However,…

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
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Indoor building construction sites are demanding environments for visual SLAM, where variable lighting and repetitive, low-textured structures make the system drift over long trajectories, though structural elements such as walls remain distinguishable despite these conditions. These buildings are constructed according to their as-planned floor plans, avail…

### 10. Parameter Sensitivity Analysis for Aerial LiDAR-Inertial Odometries in low-altitude flights

- **arXiv**: [2609.12837v1](https://arxiv.org/abs/2609.12837v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.12837v1)
- **作者**: Robert Milijas, Jose Ramiro Martinez-de Dios, Stjepan Bogdan
- **发表**: 2026-09-11  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: LiDAR-based SLAM (Simultaneous Localization and Mapping) and LIO (LiDAR-inertial odometry) algorithms are often used for precise navigation of unmanned aerial vehicles, especially during interactions with the aerial robot's environment. However, the performance of these algorithms is greatly dependent on the scenario, LiDAR, and robot motion characteristics…

## 🤏 软体机器人 / 柔性控制 (3 篇)

### 1. From Biological Curves to Soft Modular Robots: Learning-Based Inverse Design with Uncertainty-Guided Refinement

- **arXiv**: [2610.36681v1](https://arxiv.org/abs/2610.36681v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.36681v1)
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
2. [A fully articulated humanoid dexterous hand with human-level joint structure enabled by linkage-based actuation](https://arxiv.org/abs/2610.36789v1) — score 19
3. [Learning Dexterous Manipulation: Hands, Simulators, Training, and Evaluation](https://arxiv.org/abs/2610.33486v1) — score 19

> 筛选说明:本次 Top 3 已排除(已研读跳过 2 篇、综述跳过 1 篇)。

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
