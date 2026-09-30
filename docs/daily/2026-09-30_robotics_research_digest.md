# 机器人研究每日摘要 · 2026-09-30

> 自动生成,共 91 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (6 篇)

### 1. Reactive Real-Time Flow Policies via Asynchronous Distribution Alignment

- **arXiv**: [2609.36540v1](https://arxiv.org/abs/2609.36540v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.36540v1)
- **作者**: Moritz Zoellner, Reece O'Mahoney, Ioannis Havoutis et al.
- **发表**: 2026-09-29  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Generalist robot policies such as vision-language-action models (VLAs) have achieved remarkable generalization, but their inference delays can conflict with the demands of real-time control. Asynchronous execution avoids pauses between action chunks by predicting the next sequence of actions while the robot carries out the previous one. In this paper, we st…

### 2. Breaking the Vision-Action Shortcut: Latent Interface Training for Generalizable Robotics Foundation Models

- **arXiv**: [2609.12641v1](https://arxiv.org/abs/2609.12641v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.12641v1)
- **作者**: Jianman Lin, Shailesh Shailesh, Zhongyi Luo et al.
- **发表**: 2026-09-11  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Robot foundation models achieve strong in-distribution performance but often degrade under visual distribution shifts. When learning to generate actions from pretrained visual representations, models may exploit task-irrelevant visual cues that correlate with demonstrated actions within the training distribution. Such vision-action shortcuts can undermine g…

### 3. Measuring Language Transfer in Robot Policies: Adding Greek to a Cosmos3 Vision-Language-Action Policy

- **arXiv**: [2609.07470v1](https://arxiv.org/abs/2609.07470v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.07470v1)
- **作者**: Ayoub Kirouane, Georgios Giaples, Christos Petrocheilos
- **发表**: 2026-09-07  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Robot foundation models are trained and evaluated predominantly in English, and robot demonstration corpora do not exist for most languages. We study the addition of Greek to an open vision-language-action stack using only machine-rephrased instructions and no architecture changes. The main challenge is measurement rather than translation. Several plausible…

### 4. LexiconVLA: Learning Reusable Atomic Action Codebooks for Unseen Tasks

- **arXiv**: [2609.36774v1](https://arxiv.org/abs/2609.36774v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.36774v1)
- **作者**: Zeming Wei, Jianheng Ye, Xinshuai Song et al.
- **发表**: 2026-09-29  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-language-action (VLA) models struggle to reuse recurring interactions in unseen tasks. Our diagnostic study reveals that reliable task completion does not imply consistent execution of constituent atomic actions across task contexts. We present LexiconVLA, a retrievable atomic-action lexicon for cross-task reuse. Global and detail codebooks capture s…

### 5. Where Predictive Supervision Goes Shapes What VLA Policies Learn

- **arXiv**: [2609.36645v1](https://arxiv.org/abs/2609.36645v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.36645v1)
- **作者**: Hanseul Kim, Jewon Yeom, Youngjoon Jeong et al.
- **发表**: 2026-09-29  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Future prediction is increasingly used to improve vision-language-action (VLA) policies, based on the premise that anticipating scene evolution encourages representations useful for control. However, forecast quality alone does not establish that a policy has learned a better representation for action. This distinction matters under distribution shift, wher…

### 6. LLMs are General Asynchronous Agents

- **arXiv**: [2609.35427v1](https://arxiv.org/abs/2609.35427v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.35427v1)
- **作者**: George Yakushev, Denis Mazur, Vladimir Bartenev et al.
- **发表**: 2026-09-28  ·  **类别**: cs.LG, cs.CL
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Modern LLMs are increasingly capable as autonomous agents, but they follow sequential interaction cycles: read, think, reply or call tools, repeat. Many real-world use cases are not sequential: voice assistants, embodied agents, and monitoring systems receive new inputs while they think or perform another task. Modern LLMs address this with specialized arch…

## 🌐 具身智能 / 机器人基础模型 (10 篇)

### 1. JRDB-AVR: An Active Visual Reasoning Benchmark for Embodied Agents in Real-World Environments

- **arXiv**: [2609.35032v1](https://arxiv.org/abs/2609.35032v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.35032v1)
- **作者**: Zhixi Cai, Fucai Ke, Sukai Huang et al.
- **发表**: 2026-09-28  ·  **类别**: cs.AI, cs.CV, cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: In complex embodied visual reasoning scenarios, an agent often has only a limited field of view, and the evidence needed to answer a question may be distributed across time, viewpoint, and interacting objects. A model may therefore give a plausible answer without ever observing the relevant object, time, or view that supports it. Current visual reasoning be…

### 2. NavJev: Efficient Vision-Language Navigation via Action-Centric Visual Compression and Discriminative Action-Semantic Memory

- **arXiv**: [2609.34969v1](https://arxiv.org/abs/2609.34969v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.34969v1)
- **作者**: Kai Sheng, Liuyi Wang, Jinlong Li et al.
- **发表**: 2026-09-28  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Recent zero-shot Vision-and-Language Navigation (VLN) methods increasingly rely on multimodal large language models (MLLMs) to reason over visual observations, navigation instructions, and candidate actions. Although effective, repeatedly invoking autoregressive multimodal reasoning at every navigation step introduces substantial inference latency, limiting…

### 3. SOR-Nav: Search or Relocate? Context-Gated Exploration and Cross-Region Relocation for Object Navigation

- **arXiv**: [2609.34707v1](https://arxiv.org/abs/2609.34707v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.34707v1)
- **作者**: Yuan Ji, Zirui Li, Yuxin Cai et al.
- **发表**: 2026-09-28  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Object navigation requires an embodied agent to find an object in an unseen environment under partial observability and a limited motion budget. Existing methods primarily optimize where the robot should go next by ranking candidate destinations. In contrast to these methods, we present SOR-Nav, a hierarchical navigation system that explicitly arbitrates be…

### 4. VCN-Bench: A Video-Contextualized Navigation Benchmark for Spatial Reasoning over Prior Visual Experience

- **arXiv**: [2609.34687v1](https://arxiv.org/abs/2609.34687v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.34687v1)
- **作者**: Siqi Zhang, Meng Wei, Chenyang Wan et al.
- **发表**: 2026-09-28  ·  **类别**: cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Spatial reasoning is fundamental to embodied agents, yet it remains unclear whether spatial understanding can be carried forward to guide sequential interactions. Existing spatial-reasoning benchmarks typically terminate at offline predictions, while navigation benchmarks evaluate spatial reasoning as part of instruction following and exploration. We introd…

### 5. SAIL: Spatial Audio Intelligence with Large Language Models via Disentangled Acoustic-Spatial Encoding and Dual-Stream Q-Former

- **arXiv**: [2609.34347v1](https://arxiv.org/abs/2609.34347v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.34347v1)
- **作者**: Zhengding Luo, Jinyang Wu, Haozhe Ma et al.
- **发表**: 2026-09-28  ·  **类别**: cs.SD, cs.AI, eess.AS
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Spatial audio large language models (LLMs) enable embodied agents, wearable assistants, and immersive systems to recognize sound events, localize sources, and reason about their spatial relationships. However, existing spatial audio LLMs often rely on early fusion of acoustic and spatial features and source-agnostic token representations. These designs make…

### 6. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 7. HEIR: Learning Human-Entity Interactions with Functional Roles

- **arXiv**: [2609.35955v1](https://arxiv.org/abs/2609.35955v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.35955v1)
- **作者**: Di Wen, Wenhao Guo, Yuedong Tan et al.
- **发表**: 2026-09-28  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Understanding human-entity interactions requires recovering each person-action event's participants, roles, and shared identities. This structure can support embodied agents by clarifying who acts on which entities and how, informing anticipation and coordination in shared environments. Standard HOI metrics score individual links, leaving complete event com…

### 8. VehicleArena: A Realistic Urban Environment for Multi-Agent Driving

- **arXiv**: [2609.35916v1](https://arxiv.org/abs/2609.35916v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.35916v1)
- **作者**: Jie Yang, Jiajun Chen, Jiazheng Zhou et al.
- **发表**: 2026-09-28  ·  **类别**: cs.MA, cs.CL, cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Real-world embodied agents often pursue independent objectives within a shared physical environment, where their actions can alter the conditions faced by others. Existing benchmarks, however, typically assume shared goals or explicitly prescribed interaction protocols, leaving such emergent physical coupling underexplored. We introduce VehicleArena, a 3D u…

### 9. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

### 10. Monocular Depth Estimation from a Single Image: Progress and Opportunities

- **arXiv**: [2609.01172v1](https://arxiv.org/abs/2609.01172v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.01172v1)
- **作者**: Muxin Liu, Xiaoyang Lyu, Yang-Tian Sun et al.
- **发表**: 2026-09-01  ·  **类别**: cs.CV
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Monocular depth estimation has long stood as a fundamental challenge in computer vision, enabling a wide range of applications including 3D reconstruction, robotics, autonomous driving, and augmented reality. This survey traces the field's evolution from early learning-based methods to the emergence of transformative foundation models. We begin by framing t…

## 🦵 人形 / 足式机器人 (29 篇)

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

### 3. Smoothness as a Constraint for Stable Humanoid Locomotion

- **arXiv**: [2609.24552v1](https://arxiv.org/abs/2609.24552v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.24552v1)
- **作者**: Utsav Panchal, Denis Kleyko, Unal Artan et al.
- **发表**: 2026-09-21  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Embodied AI systems, particularly humanoid robots deployed in real world scenarios require whole-body control policies that are both task-responsive and physically smooth. However, smoothness is not uniform across the body: lower body must remain sufficiently reactive, while the upper body must be tightly regulated to preserve stability. Existing reinforcem…

### 4. WB-WAM: Heterogeneous Body-Hand Pre-training for Humanoid Loco-Manipulation

- **arXiv**: [2609.34199v1](https://arxiv.org/abs/2609.34199v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.34199v1)
- **作者**: Chuan Qin, Shaoting Zhu, Siyuan Luo et al.
- **发表**: 2026-09-28  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Humanoid loco-manipulation demands coordinated body and hand behavior, while conventional robot pre-training data provide limited coverage of such whole-body motion. We present WB-WAM, a World Action Model that incorporates explicit whole-body action supervision into generative video pre-training. A shared physical action space integrates body, root, and de…

### 5. DexRoam: Learning Mobile Bimanual Dexterous Manipulation from Egocentric Whole-Body Human Demonstrations

- **arXiv**: [2609.35761v1](https://arxiv.org/abs/2609.35761v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.35761v1)
- **作者**: Rui Zhou, Yibo Yuan, Junkai Zhao et al.
- **发表**: 2026-09-28  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Mobile bimanual dexterous manipulation requires continuous coordination of locomotion, whole-body motion, and finger-level dexterity within a single trajectory, creating a severe robot demonstration bottleneck. Egocentric human demonstrations offer a scalable alternative, but prior approaches ease the transfer by simplifying human motion, discarding exactly…

### 6. Model-Informed Safe Reinforcement Learning for Bipedal Locomotion via Step-to-Step Prediction

- **arXiv**: [2609.34486v1](https://arxiv.org/abs/2609.34486v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.34486v1)
- **作者**: Victor Paredes, Ayonga Hereid
- **发表**: 2026-09-28  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Humanoid robots promise versatile mobility in cluttered, human-centric environments, but real deployment demands principled safety. Classical model-based gait generators yield interpretable motions but often lack the robustness and adaptability of modern reinforcement learning (RL) based approaches. We propose a model-informed reinforcement learning framewo…

### 7. Breaking speed scaling in quadrupedal robots via Huygens' coupled-pendulum dynamics

- **arXiv**: [2609.13290v1](https://arxiv.org/abs/2609.13290v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.13290v1)
- **作者**: Yucheng Tao, Yongbin Jin, Shaowen Cheng et al.
- **发表**: 2026-09-09  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Achieving biological-level running speeds has largely been pursued through advances in control algorithms, which improve the utilization of existing hardware. However, the ultimate speed limits remain governed by the underlying force and torque requirements of rapid locomotion, which are typically addressed through increased actuator capacity. Inspired by H…

### 8. OTRetarget: Joint Robot and Object Motion Retargeting via Optimal Transport

- **arXiv**: [2609.36602v1](https://arxiv.org/abs/2609.36602v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.36602v1)
- **作者**: Guillaume Besset, Erwann Carn, Timothée Carecchio et al.
- **发表**: 2026-09-29  ·  **类别**: cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Transferring human motion to humanoid robots requires adapting the demonstrated motion to the robot morphology while preserving interactions with the environment. This is particularly challenging for loco-manipulation tasks, where contacts with the ground and manipulated objects must remain consistent despite differences in body proportions. Yet, skeletal m…

### 9. ChronoSRL: Temporal Geometry for Self-Supervised Reinforcement Learning

- **arXiv**: [2609.36238v1](https://arxiv.org/abs/2609.36238v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.36238v1)
- **作者**: Nico Bohlinger, Jan Peters
- **发表**: 2026-09-28  ·  **类别**: cs.AI, cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: A goal that is close in space can be far away in time. Obstacles, terrain, and the agent's own capabilities determine how long it takes to get there. Yet, critics in contrastive and survival reinforcement learning do not measure the distances in their representation space in units of time. We therefore introduce ChronoSRL, which gives the critic's embedding…

### 10. Action Chunking Proximal Policy Optimization with Feedback Correction

- **arXiv**: [2609.36250v1](https://arxiv.org/abs/2609.36250v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.36250v1)
- **作者**: Sanghyun Hahn, Jonghyun Choi
- **发表**: 2026-09-28  ·  **类别**: cs.LG, cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Action chunking provides temporal abstraction in reinforcement learning by selecting short action sequences instead of individual actions, but many existing approaches face two limitations in high-dimensional robotic control. First, many rely on value functions over action chunks, which can be difficult to learn as action dimensionality and chunk length gro…

## 🦾 操控 / 灵巧手 / 抓取 (28 篇)

### 1. AeroManip-VLA: Scalable Vision-Language-Action Learning for Aerial Manipulation with RL-Generated Demonstrations

- **arXiv**: [2609.36915v1](https://arxiv.org/abs/2609.36915v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.36915v1)
- **作者**: Rui Huang, Yanlin Mu, Lidong Li et al.
- **发表**: 2026-09-29  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 21  ·  **🔥 read_now**
- **摘要**: Aerial manipulators extend robotic manipulation into 3D workspaces that are difficult for ground-based robots to access, creating new opportunities for general-purpose manipulation. However, extending Vision-Language-Action (VLA) models to aerial robots introduces distinct challenges due to the tight coupling between manipulation and flight, continuously ch…

### 2. Unified Visual-Tactile-Action Modeling from Human Demonstrations for Dexterous Manipulation

- **arXiv**: [2609.34182v2](https://arxiv.org/abs/2609.34182v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.34182v2)
- **作者**: Wenqiao Li, Qianyou Zhao, Jiawen Hao et al.
- **发表**: 2026-09-28  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation requires tactile feedback. However, robot tactile demonstrations are difficult to scale,because dexterous-hand teleoperation provides limited tactile feedback to the operator. In contrast, human demonstrations offer a substantially more scalable source of diverse tactile interactions. Motivated by a simple premise: hands can change, b…

### 3. HACo: Learning Haptic Active Compliance for Force-Aware Dexterous Manipulation

- **arXiv**: [2609.36596v1](https://arxiv.org/abs/2609.36596v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.36596v1)
- **作者**: Naisheng Ye, Yinzhe Zhou, Junkai Zhao et al.
- **发表**: 2026-09-29  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Contact-rich dexterous manipulation requires policies that translate physical feedback into motion commands while regulating interaction loads across evolving multi-contact interactions. This requires haptic observations of contact state and action supervision showing how commands should adapt. Existing policies often overlook complementary fingertip tactil…

### 4. Kinematic Nonlinear Spatio-Temporal Trajectory Warping for Contact-Rich Dexterous Manipulation Demonstrations

- **arXiv**: [2609.36676v1](https://arxiv.org/abs/2609.36676v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.36676v1)
- **作者**: Hyojae Park, Arjun S. Lakshmipathy, Nancy S. Pollard
- **发表**: 2026-09-29  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: We present a straightforward but effective method for repurposing existing contact-rich dexterous manipulation demonstrations. Starting from inputs of hand and object trajectories, our method outputs high-quality nonlinear trajectory warps that account for intermediate waypoints, environmental barriers, temporal shifts, and varied start/end configurations.…

### 5. X-Reset: Scaling Object-Centric Reinforcement Learning via Cross-Embodiment Resets

- **arXiv**: [2609.35715v1](https://arxiv.org/abs/2609.35715v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.35715v1)
- **作者**: Prithwish Dan, Chenyang Ma, Wei Zhan
- **发表**: 2026-09-28  ·  **类别**: cs.LG, cs.AI, cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Reinforcement learning (RL) in simulation can train dexterous manipulation policies without robot demonstrations, but training a single generalist policy with task-agnostic rewards faces a severe exploration problem: approaching, grasping, and reorienting diverse objects with many degrees of freedom is difficult to discover from scratch. Prior works make ex…

### 6. TANDEM: Task and Motion Planning with As-Needed Demonstrations for Efficient Vision-Language-Action Model Fine-tuning

- **arXiv**: [2609.28314v1](https://arxiv.org/abs/2609.28314v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.28314v1)
- **作者**: Samrat Sahoo, Liang Ji, Tom Silver et al.
- **发表**: 2026-09-23  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Human teleoperators spend substantial time demonstrating behaviors that robots can already perform autonomously, limiting the scalability of data collection for robot foundation models. Task and motion planning (TAMP) can automate many of these behaviors, but a fixed planning domain may not support every stage of a long-horizon manipulation task. We present…

### 7. DexAgent: An Agentic Human2Sim2Robot Framework for Dexterous Manipulation with Self-Evolving Tool Library

- **arXiv**: [2609.35318v1](https://arxiv.org/abs/2609.35318v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.35318v1)
- **作者**: Youhui Wang, Yunzhu Li, Li Fei-Fei et al.
- **发表**: 2026-09-28  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Human videos offer a scalable source of demonstrations for dexterous robot manipulation. However, existing human-to-simulation-to-robot (Human2Sim2Robot) pipelines rely on predefined procedures that struggle to accommodate diverse object properties and interactions, particularly those involving articulated and deformable objects. We introduce DexAgent, an a…

### 8. VidAct: Learning Manipulation from In-the-Wild Videos with Object-Centric 3D Awareness

- **arXiv**: [2609.36870v1](https://arxiv.org/abs/2609.36870v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.36870v1)
- **作者**: Hang Li, Mingxin Zhang, Zihan Wu et al.
- **发表**: 2026-09-29  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Video demonstrations offer a scalable alternative to costly robot data for learning manipulation, yet existing reconstruction-based approaches often rely on constrained camera viewpoints or human-to-robot retargeting, while the reconstructed trajectories are difficult to adapt to new objects configurations without distorting the trajectory shape. Another ke…

### 9. Beyond Token Importance: Preserving Spatial Scaffolds for Efficient Vision-Language-Action Inference

- **arXiv**: [2609.36967v1](https://arxiv.org/abs/2609.36967v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.36967v1)
- **作者**: Jiayu Chen, Shuyong Gao, Jingkai Jia et al.
- **发表**: 2026-09-29  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Existing VLA pruning strategies primarily select individual visual tokens according to task-level semantic relevance, while overlooking the spatial information required for robotic manipulation. To examine this limitation, we construct a simple Stride baseline that uniformly samples tokens along the flattened one-dimensional visual sequence, representing a…

### 10. DexTaG: Tactile-as-Guidance in Reinforcement Learning for Dexterous Manipulation

- **arXiv**: [2609.33882v1](https://arxiv.org/abs/2609.33882v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.33882v1)
- **作者**: Han Yang, Yian Wang, Yunlong Song et al.
- **发表**: 2026-09-27  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Glove-based motion capture is emerging as a scalable approach to collecting dexterous-hand demonstration data. However, due to the kinematic gap between the human and robot hand, the recorded human motions cannot be executed directly on the robot, especially for contact-rich tool-use tasks involving in-hand reorientation. Prior work bridges this gap in simu…

## 🎓 模仿学习 / 强化学习 (13 篇)

### 1. RoXDrive: Closed-Loop Reinforcement Learning for End-to-End Autonomous Driving via Action-Faithful Rollouts

- **arXiv**: [2609.36851v1](https://arxiv.org/abs/2609.36851v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.36851v1)
- **作者**: Hongbin Lin, Chaoda Zheng, Yiming Yang et al.
- **发表**: 2026-09-29  ·  **类别**: cs.CV
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: End-to-end autonomous driving policies are commonly trained via imitation learning on logged demonstrations without observing the consequences of their own actions, leading to causal confusion in closed-loop real-world deployment. To address this issue, reinforcement learning (RL) post-training offers a promising alternative by leveraging world models as in…

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

### 7. DQ-MPCC: Dual-Quaternion MPCC for Quadrotor Racing

- **arXiv**: [2609.36482v1](https://arxiv.org/abs/2609.36482v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.36482v1)
- **作者**: Bryan S. Guevara, Luis F. Recalde, Guanrui Li et al.
- **发表**: 2026-09-29  ·  **类别**: cs.RO, eess.SY
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Quadrotor racing demands aggressive attitude and progress control while passing through every gate, and conventional quadrotor MPCC formulations state the prediction model in inertial coordinates and the attitude error in the body frame. We present a Dual-Quaternion Model Predictive Contouring Control (DQ-MPCC) for quadrotor racing in which the pose is a un…

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

### 10. Failure or Drift? Evaluating Monocular SLAM under Synthetic and Real-World Corruptions

- **arXiv**: [2608.30690v1](https://arxiv.org/abs/2608.30690v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.30690v1)
- **作者**: Abhay Skaria Thomas, Shashank Agnihotri, Margret Keuper
- **发表**: 2026-08-31  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Visual SLAM is commonly evaluated on clean trajectories, although deployment failures are often caused by adverse weather, illumination, blur, and sensor artifacts. Controlled corruptions are attractive because they isolate such factors, but a synthetic stress test is useful only when it leads to the same engineering conclusion as the condition it is intend…

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
1. [AeroManip-VLA: Scalable Vision-Language-Action Learning for Aerial Manipulation with RL-Generated Demonstrations](https://arxiv.org/abs/2609.36915v1) — score 21
2. [Aerial Manipulation in the Wild with Onboard Perception, Policy Learning, and Whole-Body Control](https://arxiv.org/abs/2609.30521v1) — score 19
3. [Opt2VLA: Force-Aware Vision-Language-Action for Contact-Rich Humanoid Whole-Body Manipulation](https://arxiv.org/abs/2609.23968v1) — score 19

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
