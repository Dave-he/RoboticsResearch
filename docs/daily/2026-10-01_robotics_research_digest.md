# 机器人研究每日摘要 · 2026-10-01

> 自动生成,共 90 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (3 篇)

### 1. Vision-Language-Action Autonomous Driving Agent with Language-based Memory

- **arXiv**: [2609.38641v1](https://arxiv.org/abs/2609.38641v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.38641v1)
- **作者**: Kai Yan, Xiangyu Chen, Yulong Cao et al.
- **发表**: 2026-09-29  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) foundation models have recently emerged as one of the prevailing solutions for autonomous driving, as they can utilize knowledge acquired during vision-language pretraining for accurate and interpretable driving. However, VLAs can take only a limited number of frames as visual input due to the high token cost of an image, which…

### 2. Blackout vs. Freeze: Analyzing Physical Failure Modes of VLAs under Camera Faults

- **arXiv**: [2609.39145v1](https://arxiv.org/abs/2609.39145v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39145v1)
- **作者**: Heejae Suh, Jongwook Han, Zahra Gholami et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Unreliable visual inputs can harm task performance and cause potential physical safety risks for vision-language-action (VLA) models. We analyze how $π0.5$ and GR00T models act under input faults such as image blackouts and freezing. We find that blackout and freezing produce distinct physical failure modes even when task-success rates are similarly low: fr…

### 3. Breaking the Vision-Action Shortcut: Latent Interface Training for Generalizable Robotics Foundation Models

- **arXiv**: [2609.12641v1](https://arxiv.org/abs/2609.12641v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.12641v1)
- **作者**: Jianman Lin, Shailesh Shailesh, Zhongyi Luo et al.
- **发表**: 2026-09-11  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Robot foundation models achieve strong in-distribution performance but often degrade under visual distribution shifts. When learning to generate actions from pretrained visual representations, models may exploit task-irrelevant visual cues that correlate with demonstrated actions within the training distribution. Such vision-action shortcuts can undermine g…

## 🌐 具身智能 / 机器人基础模型 (11 篇)

### 1. Exemplar2VQA: A Scalable Exemplar-Driven Visual Question Answering Generation Framework via Multi-Agent Coding

- **arXiv**: [2609.37655v1](https://arxiv.org/abs/2609.37655v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.37655v1)
- **作者**: Jiayu Ying, Qijian Tian, Ruijie Xu et al.
- **发表**: 2026-09-29  ·  **类别**: cs.CV
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Advancing spatial intelligence in Multimodal Large Language Models (MLLMs) is bottlenecked by the scarcity of complex, scalable 3D question-answer (QA) data. While manual annotation is labor-intensive, directly utilizing LLMs to synthesize these QA pairs often fails due to their inherent deficiencies in spatial and geometric computation. We introduce Exempl…

### 2. Beyond the Remembered World: Predictive 4D Belief for Persistent Navigation in Evolving Worlds

- **arXiv**: [2609.39166v1](https://arxiv.org/abs/2609.39166v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39166v1)
- **作者**: Mingjian Gao, Zhaocheng Li, Haoyang Huang et al.
- **发表**: 2026-09-30  ·  **类别**: cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Persistent spatial memory enables embodied agents to navigate familiar environments across repeated visits. However, targets may move while unobserved, including during navigation, making remembered locations unreliable by the time an agent arrives. Despite advances in memory retrieval and state prediction, accounting for continued hidden world evolution an…

### 3. Does This Action Still Explain the Task? Reverse Scoring for Diffusion Language Model Agents

- **arXiv**: [2609.38536v1](https://arxiv.org/abs/2609.38536v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.38536v1)
- **作者**: Jiacheng Qiu, Christopher E. Mower, Jan Peters et al.
- **发表**: 2026-09-29  ·  **类别**: cs.LG, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Diffusion-based large language models (dLLMs) promise to break the sequential latency bottleneck of autoregressive agents through parallel decoding, but recent evaluations show this efficiency does not transfer to embodied agentic competence: dLLM-backed agents repeatedly fall into retry loops, re-issuing an action long after it has failed. We give a mechan…

### 4. Pixels to Keys: Exploring Spatial and Motion Cues in Gameplay Inverse Dynamics

- **arXiv**: [2609.37907v2](https://arxiv.org/abs/2609.37907v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.37907v2)
- **作者**: Abhishek Pillai, Ekta Prashnani, Joohwan Kim et al.
- **发表**: 2026-09-29  ·  **类别**: cs.AI, cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Video games offer scalable environments for studying perception and control in embodied agents. Abundant online gameplay videos could supply demonstrations, but they rarely include player inputs for training. Inverse Dynamics Models (IDMs) have thus been proposed to infer inputs from frames. Large (up to 1B parameters) IDMs trained on $\sim$1K-2K gameplay h…

### 5. Generative Interactions: Weaving Multiparty Human Motion with Bilevel Latent Dynamics

- **arXiv**: [2609.37708v1](https://arxiv.org/abs/2609.37708v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.37708v1)
- **作者**: Ojas Shirekar, Yash Surange, Agustinas Jučas et al.
- **发表**: 2026-09-29  ·  **类别**: cs.AI, cs.LG
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Human social behaviour is not a collection of independent motions, but a jointly organised process in which group dynamics and individual variation continuously shape one another. Yet existing social motion models often prioritise plausible trajectories while leaving interaction state implicit, limiting their ability to transfer across groups, tasks, and pa…

### 6. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 7. ASENA: Self-evolving Agents for Embodied Navigation

- **arXiv**: [2609.39207v1](https://arxiv.org/abs/2609.39207v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39207v1)
- **作者**: An-Chieh Cheng, Isabella Liu, Edmund Bu et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We present ASENA, an embodied agent system that connects general-purpose coding agents to robot sensing, computation, supervised execution, and persistent experience. Agents can write and execute programs, inspect recorded outcomes, repair failures, and reuse notes and executable skills while keeping their model weights fixed. We further introduce ASENA-VLN…

### 8. Uruqi: Learning Spatial Cognition from Visual Experience

- **arXiv**: [2609.39195v1](https://arxiv.org/abs/2609.39195v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39195v1)
- **作者**: Shichao Li, Meiqi Wang, Fei Su et al.
- **发表**: 2026-09-30  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Spatial intelligence requires maintaining a coherent understanding of the world as the embodied agent moves. Like humans, the agent must use its own motion to interpret changes across observations and update object locations and spatial relations accordingly. Despite spatial post-training having substantially broadened the spatial intelligence of vision-lan…

### 9. HEIR: Learning Human-Entity Interactions with Functional Roles

- **arXiv**: [2609.35955v1](https://arxiv.org/abs/2609.35955v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.35955v1)
- **作者**: Di Wen, Wenhao Guo, Yuedong Tan et al.
- **发表**: 2026-09-28  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Understanding human-entity interactions requires recovering each person-action event's participants, roles, and shared identities. This structure can support embodied agents by clarifying who acts on which entities and how, informing anticipation and coordination in shared environments. Standard HOI metrics score individual links, leaving complete event com…

### 10. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

## 🦵 人形 / 足式机器人 (30 篇)

### 1. Aerial Manipulation in the Wild with Onboard Perception, Policy Learning, and Whole-Body Control

- **arXiv**: [2609.30521v1](https://arxiv.org/abs/2609.30521v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.30521v1)
- **作者**: Yuanzhu Zhan, Yufei Jiang, Zemu Zhang et al.
- **发表**: 2026-09-24  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Aerial manipulation in outdoor environments remains challenging due to the simultaneous requirements of reliable state estimation, stable aerial motion, and precise manipulation under external disturbances. In this work, we present a real-world outdoor aerial manipulation framework that integrates imitation learning, onboard LiDAR-inertial state estimation,…

### 2. OccluDex: Hierarchical 3D Visuo-Tactile Representation Learning for Egocentric Dexterous Manipulation under Self-Occlusion

- **arXiv**: [2609.39017v1](https://arxiv.org/abs/2609.39017v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39017v1)
- **作者**: Ziheng Xu, Yueyuan Chen, Xinyuan He et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Reliable dexterous manipulation requires continuous estimation of object geometry and hand-object contact throughout interaction. With egocentric sensing, however, the manipulating hand frequently occludes task-relevant object surfaces and contact regions, reducing the visual evidence available for state estimation and thereby making robust closed-loop cont…

### 3. NEXUS: Perceptive Whole-Body Control for Terrain-Adaptive Teleoperation

- **arXiv**: [2609.39000v1](https://arxiv.org/abs/2609.39000v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39000v1)
- **作者**: Xiangyu Miao, Junsong Wu, Jiyuan Shi et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Whole-body teleoperation requires a humanoid robot to reproduce a human operator's behavior even when their terrains differ. This demands that the robot perceive local terrain and adapt its posture and contacts accordingly, rather than copy the operator's motion frame by frame. However, paired motion data linking the same behaviors across flat ground and di…

### 4. Fiatlux: A Long-Horizon Benchmark for Humanoid Ladder Climbing and Light-Bulb Replacement

- **arXiv**: [2609.38216v1](https://arxiv.org/abs/2609.38216v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.38216v1)
- **作者**: Pavel Bushuyeu, Yujin Chen, Anton Nikolaev et al.
- **发表**: 2026-09-27  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Existing benchmarks evaluate tabletop manipulation, flat-floor household activity, or humanoid locomotion and manipulation as separate task groups; none scores vertical mobility and dexterous work on a fragile payload in one long-horizon episode. We present Fiatlux, a light-bulb replacement benchmark built on NVIDIA Isaac Lab. In one episode, a Unitree G1 h…

### 5. Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation

- **arXiv**: [2609.38172v1](https://arxiv.org/abs/2609.38172v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.38172v1)
- **作者**: Zihan Wang, Zhen Wu, Pieter Abbeel et al.
- **发表**: 2026-09-29  ·  **类别**: cs.RO, cs.CV, cs.GR
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Teaching humanoids loco-manipulation skills, such as carrying diverse objects, via visual imitation is a promising path toward generalist robots. However, collecting diverse, high-quality interaction videos, such as clips that clearly show a person's full body and unoccluded interactions with objects, poses a practical barrier to scaling this approach. We p…

### 6. EgoAlign: Bridging the Human-Humanoid Gap for Long-Range Loco-Manipulation

- **arXiv**: [2609.38046v2](https://arxiv.org/abs/2609.38046v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.38046v2)
- **作者**: Yiming Jiang, Jin Chen, Chongyang Xu et al.
- **发表**: 2026-09-29  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Egocentric human demonstrations offer an accessible source of task experience, but differences in body scale and controller response, together with missing robot states, limit their value as humanoid training supervision. We present EgoAlign, a data-construction framework that converts these demonstrations into action and state supervision compatible with a…

### 7. WB-WAM: Heterogeneous Body-Hand Pre-training for Humanoid Loco-Manipulation

- **arXiv**: [2609.34199v1](https://arxiv.org/abs/2609.34199v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.34199v1)
- **作者**: Chuan Qin, Shaoting Zhu, Siyuan Luo et al.
- **发表**: 2026-09-28  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Humanoid loco-manipulation demands coordinated body and hand behavior, while conventional robot pre-training data provide limited coverage of such whole-body motion. We present WB-WAM, a World Action Model that incorporates explicit whole-body action supervision into generative video pre-training. A shared physical action space integrates body, root, and de…

### 8. DexRoam: Learning Mobile Bimanual Dexterous Manipulation from Egocentric Whole-Body Human Demonstrations

- **arXiv**: [2609.35761v1](https://arxiv.org/abs/2609.35761v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.35761v1)
- **作者**: Rui Zhou, Yibo Yuan, Junkai Zhao et al.
- **发表**: 2026-09-28  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Mobile bimanual dexterous manipulation requires continuous coordination of locomotion, whole-body motion, and finger-level dexterity within a single trajectory, creating a severe robot demonstration bottleneck. Egocentric human demonstrations offer a scalable alternative, but prior approaches ease the transfer by simplifying human motion, discarding exactly…

### 9. Model-Informed Safe Reinforcement Learning for Bipedal Locomotion via Step-to-Step Prediction

- **arXiv**: [2609.34486v1](https://arxiv.org/abs/2609.34486v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.34486v1)
- **作者**: Victor Paredes, Ayonga Hereid
- **发表**: 2026-09-28  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Humanoid robots promise versatile mobility in cluttered, human-centric environments, but real deployment demands principled safety. Classical model-based gait generators yield interpretable motions but often lack the robustness and adaptability of modern reinforcement learning (RL) based approaches. We propose a model-informed reinforcement learning framewo…

### 10. Breaking speed scaling in quadrupedal robots via Huygens' coupled-pendulum dynamics

- **arXiv**: [2609.13290v1](https://arxiv.org/abs/2609.13290v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.13290v1)
- **作者**: Yucheng Tao, Yongbin Jin, Shaowen Cheng et al.
- **发表**: 2026-09-09  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Achieving biological-level running speeds has largely been pursued through advances in control algorithms, which improve the utilization of existing hardware. However, the ultimate speed limits remain governed by the underlying force and torque requirements of rapid locomotion, which are typically addressed through increased actuator capacity. Inspired by H…

## 🦾 操控 / 灵巧手 / 抓取 (26 篇)

### 1. HACo: Learning Haptic Active Compliance for Force-Aware Dexterous Manipulation

- **arXiv**: [2609.36596v1](https://arxiv.org/abs/2609.36596v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.36596v1)
- **作者**: Naisheng Ye, Yinzhe Zhou, Junkai Zhao et al.
- **发表**: 2026-09-29  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Contact-rich dexterous manipulation requires policies that translate physical feedback into motion commands while regulating interaction loads across evolving multi-contact interactions. This requires haptic observations of contact state and action supervision showing how commands should adapt. Existing policies often overlook complementary fingertip tactil…

### 2. Unified Visual-Tactile-Action Modeling from Human Demonstrations for Dexterous Manipulation

- **arXiv**: [2609.34182v2](https://arxiv.org/abs/2609.34182v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.34182v2)
- **作者**: Wenqiao Li, Qianyou Zhao, Jiawen Hao et al.
- **发表**: 2026-09-28  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation requires tactile feedback. However, robot tactile demonstrations are difficult to scale,because dexterous-hand teleoperation provides limited tactile feedback to the operator. In contrast, human demonstrations offer a substantially more scalable source of diverse tactile interactions. Motivated by a simple premise: hands can change, b…

### 3. Kinematic Nonlinear Spatio-Temporal Trajectory Warping for Contact-Rich Dexterous Manipulation Demonstrations

- **arXiv**: [2609.36676v1](https://arxiv.org/abs/2609.36676v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.36676v1)
- **作者**: Hyojae Park, Arjun S. Lakshmipathy, Nancy S. Pollard
- **发表**: 2026-09-29  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: We present a straightforward but effective method for repurposing existing contact-rich dexterous manipulation demonstrations. Starting from inputs of hand and object trajectories, our method outputs high-quality nonlinear trajectory warps that account for intermediate waypoints, environmental barriers, temporal shifts, and varied start/end configurations.…

### 4. X-Reset: Scaling Object-Centric Reinforcement Learning via Cross-Embodiment Resets

- **arXiv**: [2609.35715v1](https://arxiv.org/abs/2609.35715v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.35715v1)
- **作者**: Prithwish Dan, Chenyang Ma, Wei Zhan
- **发表**: 2026-09-28  ·  **类别**: cs.LG, cs.AI, cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Reinforcement learning (RL) in simulation can train dexterous manipulation policies without robot demonstrations, but training a single generalist policy with task-agnostic rewards faces a severe exploration problem: approaching, grasping, and reorienting diverse objects with many degrees of freedom is difficult to discover from scratch. Prior works make ex…

### 5. DexAgent: An Agentic Human2Sim2Robot Framework for Dexterous Manipulation with Self-Evolving Tool Library

- **arXiv**: [2609.35318v1](https://arxiv.org/abs/2609.35318v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.35318v1)
- **作者**: Youhui Wang, Yunzhu Li, Li Fei-Fei et al.
- **发表**: 2026-09-28  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Human videos offer a scalable source of demonstrations for dexterous robot manipulation. However, existing human-to-simulation-to-robot (Human2Sim2Robot) pipelines rely on predefined procedures that struggle to accommodate diverse object properties and interactions, particularly those involving articulated and deformable objects. We introduce DexAgent, an a…

### 6. DSDyn-VLA: A Dual-Stream Dynamic Manipulation Framework with Motion Perception, Future Awareness, and Realtime Correction

- **arXiv**: [2609.39198v1](https://arxiv.org/abs/2609.39198v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39198v1)
- **作者**: Wenhao Li, Xiu Su, Yu Han et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: While Vision-Language-Action (VLA) models excel in static tasks, they struggle in dynamic environments where objects are in motion (e.g., conveyor belt manipulation). We identify three fundamental limitations hindering current VLAs in these scenarios: the \textbf{perception gap}, where static visual inputs lack temporal motion cues; the \textbf{latency gap}…

### 7. Exploiting Vulnerabilities: Universal Adversarial Attacks on Vision-Language-Action Models in Robotics

- **arXiv**: [2609.39178v1](https://arxiv.org/abs/2609.39178v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39178v1)
- **作者**: Songhua Yang, Ziyu Liu, Yuanwei Liu et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO, cs.CR, cs.CV
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Recently, Vision-Language-Action (VLA) models have revolutionized robotic manipulation by seamlessly integrating visual perception, language understanding, and action generation in an end-to-end learning framework. However, since these models are designed to interact directly with the physical world and humans, their security is critical, and even small vul…

### 8. Correcting WHERE, Preserving HOW: Compositional Generalization for Vision-Language-Action Models via Referential Guidance

- **arXiv**: [2609.38616v1](https://arxiv.org/abs/2609.38616v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.38616v1)
- **作者**: Yanyan Zhang, Disheng Liu, Xinpeng Li et al.
- **发表**: 2026-09-29  ·  **类别**: cs.RO, cs.CV, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: While Vision-Language-Action (VLA) models enable flexible action generation, their generalization across diverse environmental elements, including manipulated objects, destinations, and backgrounds, is limited by the lack of diversity in robotic training data. Trained end-to-end on such data, VLAs tend to exploit visual shortcuts, associating actions with t…

### 9. TANDEM: Task and Motion Planning with As-Needed Demonstrations for Efficient Vision-Language-Action Model Fine-tuning

- **arXiv**: [2609.28314v1](https://arxiv.org/abs/2609.28314v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28314v1)
- **作者**: Samrat Sahoo, Liang Ji, Tom Silver et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Human teleoperators spend substantial time demonstrating behaviors that robots can already perform autonomously, limiting the scalability of data collection for robot foundation models. Task and motion planning (TAMP) can automate many of these behaviors, but a fixed planning domain may not support every stage of a long-horizon manipulation task. We present…

### 10. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

## 🎓 模仿学习 / 强化学习 (12 篇)

### 1. HuMemSLAM: Efficient Human-Inspired Semantic Place Recognition for Robust Visual SLAM

- **arXiv**: [2609.17168v1](https://arxiv.org/abs/2609.17168v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.17168v1)
- **作者**: Mayowa Adebambo, Sebastian Donnelly, Armand Amaritei et al.
- **发表**: 2026-09-15  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Autonomous systems require reliable place recognition for efficient and effective simultaneous localisation and mapping (SLAM). Traditional geometric visual SLAM approaches rely on low-level features and geometric consistency, but remain vulnerable to perceptual aliasing, where different places appear similar, and perceptual variation, where the same place…

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

### 4. RoboFin3D: A Sim-to-Real Platform for Robotic Surface Finishing

- **arXiv**: [2609.37560v1](https://arxiv.org/abs/2609.37560v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.37560v1)
- **作者**: Haowei Wen, Shangtao Li, Vaibhav Sanjay et al.
- **发表**: 2026-09-29  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Grinding and sanding are fundamental processes in industrial robotic surface finishing. However, physical trials are expensive and consume workpieces, making reproducible experiments difficult. We present RoboFin3D, a sim-to-real platform built on Isaac Sim and the Newton physics engine, that provides physics-based grinding and sanding simulation for cheap…

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
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Visual SLAM is commonly evaluated on clean trajectories, although deployment failures are often caused by adverse weather, illumination, blur, and sensor artifacts. Controlled corruptions are attractive because they isolate such factors, but a synthetic stress test is useful only when it leads to the same engineering conclusion as the condition it is intend…

### 10. ACE-SLAM: Scene Coordinate Regression for Neural Implicit Real-Time SLAM

- **arXiv**: [2512.14032v1](https://arxiv.org/abs/2512.14032v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2512.14032v1)
- **作者**: Ignacio Alzugaray, Marwan Taher, Andrew J. Davison
- **发表**: 2025-12-16  ·  **类别**: cs.CV, cs.AI, eess.IV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: We present a novel neural RGB-D Simultaneous Localization And Mapping (SLAM) system that learns an implicit map of the scene in real time. For the first time, we explore the use of Scene Coordinate Regression (SCR) as the core implicit map representation in a neural SLAM pipeline, a paradigm that trains a lightweight network to directly map 2D image feature…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (4 篇)

### 1. BLASt3R: Bundle Adjustment of Any Image Set with Multi-View Matching and Monocular Priors

- **arXiv**: [2609.05210v1](https://arxiv.org/abs/2609.05210v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.05210v1)
- **作者**: Vincent Leroy, Philippe Weinzaepfel, Lojze Zust et al.
- **发表**: 2026-09-04  ·  **类别**: cs.CV
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Recent hybrid Structure-from-Motion (SfM) systems combine the robustness of feed-forward 3D reconstruction with the accuracy of traditional bundle adjustment (BA) with pixel matching. They are usually the best performing methods however their scalability and usability remains limited since estimating dense correspondences between views is prohibitively cost…

### 2. Know-Your-Scene (KYS)-SLAM: Hierarchical Semantic-Motion Priors for Feature Matching in Stereo Visual SLAM

- **arXiv**: [2609.27509v1](https://arxiv.org/abs/2609.27509v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27509v1)
- **作者**: Preeti Chatterjee, Jin Lu, Jin Sun et al.
- **发表**: 2026-09-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Stereo visual SLAM systems built on local descriptors suffer from semantic ambiguity, instance-level confusion, and independently moving objects, each corrupting data association and accumulating as trajectory drift. Prevailing semantic and dynamic SLAM methods address this through binary feature rejection, sacrificing correspondence density for outlier sup…

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

## 🧭 导航 / 路径规划 (1 篇)

### 1. Credit-Guided Policy Improvement for Test-time Adaptive Vision-Language Navigation

- **arXiv**: [2609.37591v1](https://arxiv.org/abs/2609.37591v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.37591v1)
- **作者**: Yang Li, Sijia Zhang, Yihan Li et al.
- **发表**: 2026-09-29  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Test-time adaptation for vision-language navigation (TTA-VLN) enables pretrained policies to adapt online to unseen environments using only test-time observations and interaction history. However, distribution shifts can distort local action preferences and lead to off-course decisions. Existing methods rely on predictive uncertainty, trajectory-level feedb…

## 🧪 仿真 / Sim2Real (2 篇)

### 1. Curating Synthetic Data for Task-Specific Visual Perception

- **arXiv**: [2609.38476v1](https://arxiv.org/abs/2609.38476v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.38476v1)
- **作者**: Saptarshi Neil Sinha, Paul Julius Kühn, Michael Weinmann
- **发表**: 2026-09-29  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Synthetic data are most valuable where general-purpose datasets cannot provide the domain-specific priors a task requires, and where manual annotation is expensive, imprecise, or infeasible. In this article we argue that the central question for specialized vision systems is not how to generate more data, but which data to generate. We therefore discuss cur…

### 2. The Domain Is a Residue: Adapting Self-Supervised Features, Not Generators

- **arXiv**: [2609.37330v1](https://arxiv.org/abs/2609.37330v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.37330v1)
- **作者**: Thomas Deixelberger, Markus Steinberger
- **发表**: 2026-09-29  ·  **类别**: cs.CV, cs.GR, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Clearing fog, rain or snow from footage, or turning renders into photographs, must remove the source domain and keep the scene. Unpaired translators carry it through because their generator sees the source appearance (pixels, a near-invertible latent or a control map) and keeps it. A DINO feature map fixes what is in the scene and carries weather, lighting…

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
1. [Aerial Manipulation in the Wild with Onboard Perception, Policy Learning, and Whole-Body Control](https://arxiv.org/abs/2609.30521v1) — score 19
2. [OccluDex: Hierarchical 3D Visuo-Tactile Representation Learning for Egocentric Dexterous Manipulation under Self-Occlusion](https://arxiv.org/abs/2609.39017v1) — score 17
3. [HACo: Learning Haptic Active Compliance for Force-Aware Dexterous Manipulation](https://arxiv.org/abs/2609.36596v1) — score 17

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
