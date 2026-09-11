# 机器人研究每日摘要 · 2026-09-11

> 自动生成,共 87 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (5 篇)

### 1. Frequency-Conditioned Flow Matching for Vision-Language-Action Models

- **arXiv**: [2609.10405v1](https://arxiv.org/abs/2609.10405v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.10405v1)
- **作者**: Haochen Niu, Shengye Dong, Hao Liu et al.
- **发表**: 2026-09-09  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Robot actions are temporally correlated trajectories whose frequency components encode motion at different scales with highly non-uniform energy distributions. Yet Flow Matching--based vision-language-action (VLA) models typically generate actions in temporal coordinates, without explicitly modeling or systematically leveraging this frequency heterogeneity.…

### 2. Measuring Language Transfer in Robot Policies: Adding Greek to a Cosmos3 Vision-Language-Action Policy

- **arXiv**: [2609.07470v1](https://arxiv.org/abs/2609.07470v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.07470v1)
- **作者**: Ayoub Kirouane, Georgios Giaples, Christos Petrocheilos
- **发表**: 2026-09-07  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Robot foundation models are trained and evaluated predominantly in English, and robot demonstration corpora do not exist for most languages. We study the addition of Greek to an open vision-language-action stack using only machine-rephrased instructions and no architecture changes. The main challenge is measurement rather than translation. Several plausible…

### 3. The Embodiment Gap in Robot Foundation Models

- **arXiv**: [2608.18433v1](https://arxiv.org/abs/2608.18433v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.18433v1)
- **作者**: Yukiyasu Domae, Keisuke Shirai, Hanbit Oh et al.
- **发表**: 2026-08-19  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Robot foundation models (RFMs), including vision-language-action (VLA) policies, are often discussed through a scaling view: more data, larger models, and broader benchmarks should improve generalization. In robotics, however, a model can generalize while work still remains before it can run on a robot with a particular body. The work required differs acros…

### 4. No Free Checker: A Survey of Verifiers for Robot Policies

- **arXiv**: [2609.09250v1](https://arxiv.org/abs/2609.09250v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.09250v1)
- **作者**: Yang Wan, Xihang Yue, Zhirui Liu et al.
- **发表**: 2026-09-08  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: A verifier for robot policies reads a candidate behavior and returns a score for how well it did, used both to evaluate vision-language-action policies and to train them. Verifiers range from success detectors and reward models to runtime monitors, safety filters, and temporal-logic specifications. We survey roughly 150 verifiers and compare them along two…

### 5. Action Chunk Scheduling for Batched Robot Policy Serving

- **arXiv**: [2608.00337v1](https://arxiv.org/abs/2608.00337v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.00337v1)
- **作者**: Rohan Bansal, David He, Nadun Ranawaka Arachchige et al.
- **发表**: 2026-07-31  ·  **类别**: cs.RO
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Deploying robot foundation models at scale is the next step towards realizing the potential of general-purpose robots. However, Vision-Language-Action (VLA) and other foundation models are computationally demanding, and on-device compute is constrained by power and space. In this paper, we introduce the problem of serving a robot policy to multiple robots f…

## 🌐 具身智能 / 机器人基础模型 (10 篇)

### 1. EvoNav-Bench: Benchmarking Lifelong Navigation in Evolving Environments

- **arXiv**: [2609.08292v1](https://arxiv.org/abs/2609.08292v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.08292v1)
- **作者**: Xilin Wang, Guoxi Zhang, Hongming Xu et al.
- **发表**: 2026-09-08  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Lifelong navigation (LN) requires an embodied agent to solve a sequence of navigation subtasks in the same environment. Since solving each subtask from scratch incurs redundant exploration, an LN agent must consolidate experience from earlier stages and reuse it in later stages, often through persistent scene representations such as scene graphs or visual s…

### 2. Safe Task Planning with Long-Term Graph Memory for Embodied Agents

- **arXiv**: [2609.08444v1](https://arxiv.org/abs/2609.08444v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.08444v1)
- **作者**: Siyuan Li, Taiyan Lang, Aoqi Yan et al.
- **发表**: 2026-09-08  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Large language models (LLMs) and vision-language models (VLMs) have significantly advanced zero-shot task planning for embodied agents. However, most LLM- and VLM-driven methods struggle to generate safe high-level actions due to a lack of physical risk awareness, particularly under partial observability, where hazards lie outside the immediate field of vie…

### 3. Linguistic Trajectory Encoding for Efficient Long-Horizon Spatial Memory in Embodied Agents

- **arXiv**: [2609.04802v1](https://arxiv.org/abs/2609.04802v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.04802v1)
- **作者**: Tianyidan Xie, Shenyi Wang, Qiang Tang et al.
- **发表**: 2026-09-04  ·  **类别**: cs.CV, cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Embodied agents performing long-horizon tasks require a memory representation in which the state transitions of dynamic objects remain queryable in natural language across hours-to-days observation horizons. Existing systems either drop fine-grained motion (clip-level video-language embeddings), keep it only as raw coordinates (geometric SLAM), or organise…

### 4. SmoothRL: Online Reinforcement Learning During Asynchronous Execution

- **arXiv**: [2608.29768v1](https://arxiv.org/abs/2608.29768v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.29768v1)
- **作者**: Guang Gao, Yuxuan Nong, Baifu Huang et al.
- **发表**: 2026-08-30  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Deploying robot policies in the physical world requires satisfying two fundamental desiderata: reliability and smooth real-time execution. However, deploying state-of-the-art generalist models presents challenges on both fronts. Achieving the precision and robustness required for real-world deployment necessitates sample-efficient online reinforcement learn…

### 5. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 6. PhysReal: Learning Real-World Deformable Object Physics via Hybrid Constitutive Modeling

- **arXiv**: [2609.07532v1](https://arxiv.org/abs/2609.07532v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.07532v1)
- **作者**: Yinan Deng, Jianqiao Song, Yisi Zhang et al.
- **发表**: 2026-09-07  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Learning physically plausible dynamics from visual observations is essential for interactive world models and embodied agents. However, modeling real-world deformable objects remains challenging because their dynamics often arise from complex, spatially heterogeneous material responses. To address this challenge, we propose PhysReal, a video-driven framewor…

### 7. One MLLM, One Call: Efficient Zero-Shot Vision-and-Language Navigation via Spatial-Aware Waypoints

- **arXiv**: [2609.06476v1](https://arxiv.org/abs/2609.06476v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.06476v1)
- **作者**: Shiqi Pan, Qi Zheng, Hanqin Sun et al.
- **发表**: 2026-09-06  ·  **类别**: cs.CV, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-and-Language Navigation in Continuous Environments (VLN-CE) requires an embodied agent to navigate unseen environments by following natural language instructions. Current zero-shot VLN-CE methods either rely on pre-trained waypoint predictors or require multiple queries to large models per step. To address prohibitive inference latency and computatio…

### 8. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

### 9. LookStep: Efficient Vision-Language Navigation with Linguistic Foresight and Event Driven Memory

- **arXiv**: [2609.02350v2](https://arxiv.org/abs/2609.02350v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.02350v2)
- **作者**: Kun-Yang Yu, Yingzhe Li, Hongyu Xu et al.
- **发表**: 2026-09-02  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Vision-Language Navigation (VLN) requires an embodied agent to follow natural-language instructions in unseen environments. Recent progress has been largely driven by Multimodal Large Language Models (MLLMs). Existing methods follow a next-step action prediction paradigm, supervising only the expert action, which requires a high quantity of data for trainin…

### 10. Monocular Depth Estimation from a Single Image: Progress and Opportunities

- **arXiv**: [2609.01172v1](https://arxiv.org/abs/2609.01172v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.01172v1)
- **作者**: Muxin Liu, Xiaoyang Lyu, Yang-Tian Sun et al.
- **发表**: 2026-09-01  ·  **类别**: cs.CV
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Monocular depth estimation has long stood as a fundamental challenge in computer vision, enabling a wide range of applications including 3D reconstruction, robotics, autonomous driving, and augmented reality. This survey traces the field's evolution from early learning-based methods to the emergence of transformative foundation models. We begin by framing t…

## 🦵 人形 / 足式机器人 (21 篇)

### 1. A System for Fast, Resilient, and Adaptable Loco-Manipulation Behaviors on Humanoid Robots

- **arXiv**: [2609.01518v1](https://arxiv.org/abs/2609.01518v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.01518v1)
- **作者**: Duncan Calvert, Luigi Penco, Dexton Anderson et al.
- **发表**: 2026-09-01  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: There is tremendous value in humanoid robots taking on physically demanding, hazardous, and repetitive work in spaces built for humans. However, a useful robot for these spaces must coordinate locomotion, whole-body motion, perception, contact, and operator supervision. We present a robot-local, runtime-editable behavior authoring and runtime system that ad…

### 2. TANGO: Humanoid Navigation in Cluttered Environments with a Whole-Body Vision-Language-Action Model

- **arXiv**: [2609.09158v1](https://arxiv.org/abs/2609.09158v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.09158v1)
- **作者**: Anqi Li, Yuxin Chen, Zhaobo Li et al.
- **发表**: 2026-09-08  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: We study the problem of navigating cluttered indoor environments with a humanoid robot. Unlike conventional methods that model navigation as a 2D path planning problem, humanoid traversal in cluttered environments requires continuous geometry-aware whole-body adaptation, including coordinated arm placement, torso adjustment, and gait modulation for collisio…

### 3. Isaac Sim-to-Real: Reinforcement Learning based Locomotion for Quadrupeds

- **arXiv**: [2607.18135v1](https://arxiv.org/abs/2607.18135v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.18135v1)
- **作者**: Jordan Dowdy, Jean Chagas Vaz
- **发表**: 2026-07-20  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Learning-based approaches to locomotion have risen in popularity in recent years, showing the capability for complex legged locomotion and whole-body control. Reinforcement learning (RL), the primary learning-based approach for locomotion, often utilizes a high-performance simulation tool, providing a controlled and efficient training and development enviro…

### 4. GLoRI: Closed-Loop Whole-Body Tracking with Global-Local Reference Interaction for Humanoid Loco-Manipulation

- **arXiv**: [2609.05994v1](https://arxiv.org/abs/2609.05994v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.05994v1)
- **作者**: Qingyao Xu, Sheng Yin, Zibo Zhou et al.
- **发表**: 2026-09-05  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Humanoid loco-manipulation requires accurate whole-body motion tracking in the world frame for physical interaction. While local references preserve motion structure, they lack explicit constraints on absolute spatial placement, leading to accumulated global errors. Existing globally aware approaches augment teleoperation policies with global observations b…

### 5. The Quadruped Soft Tail: Compliant Grasping and Swabbing for Contamination Surveys in Harsh Environments

- **arXiv**: [2606.30900v2](https://arxiv.org/abs/2606.30900v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.30900v2)
- **作者**: Harald Minde Hansen, Nandita Gallacher, Kristin Y. Pettersen et al.
- **发表**: 2026-06-29  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Beryllium contamination surveys in radioactive areas are challenging for robots in environments cluttered with cables and electronics. To address this problem, we have developed a novel quadruped system augmentation: A lightweight, soft, and compliant tendon-actuated robotic tail mounted on a quadruped robot. The tail features a hollow, flexible backbone an…

### 6. ViBe: Visual Behavior Adaptation for Perceptive Humanoid Whole-Body Control

- **arXiv**: [2609.09918v1](https://arxiv.org/abs/2609.09918v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.09918v1)
- **作者**: Lokesh Krishna, Sarvesh Venkatesan, An Zhang et al.
- **发表**: 2026-09-09  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Motion tracking provides a scalable recipe for humanoid whole-body control. By design, the resulting trackers lack exteroceptive feedback hence reacting to the environment remains the responsibility of a higher-level planner. Existing perceptive controllers train geometry-only encoders from scratch, trading semantics for sim-to-real ease, and typically rely…

### 7. Anti-Gravity Walking by a Flying Humanoid Robot via Thrust-Rate Input Whole-Body Model Predictive Control

- **arXiv**: [2609.07544v1](https://arxiv.org/abs/2609.07544v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.07544v1)
- **作者**: Kazuki Sugihara, Kei Okada
- **发表**: 2026-09-07  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Flying humanoids are expected to perform tasks in diverse environments, while their existing locomotion is mainly limited to aerial flight and ground walking. The capability to move in complex three-dimensional space can greatly expand their application range. For such walking motion on ceilings and similar anti-gravity environments, whole-body MPC is effec…

### 8. FWBC-VLA: Force-Aware Whole-Body Compensation for Contact-Rich Loco-Manipulation

- **arXiv**: [2609.03889v2](https://arxiv.org/abs/2609.03889v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.03889v2)
- **作者**: Yutian Zhang, Siyuan Ma, Liwen Yang et al.
- **发表**: 2026-09-03  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Contact-rich loco-manipulation requires a bridge between semantic action generation and physical interaction control. Existing Vision-language-action (VLA) models generate task-level actions from visual and linguistic observations, but cannot interpret the physical interactions induced by those actions. While the whole-body control (WBC) policy can stabiliz…

### 9. Development of a Humanoid Robot Prototype for Multimodal Human-Robot Interaction

- **arXiv**: [2609.05361v1](https://arxiv.org/abs/2609.05361v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.05361v1)
- **作者**: Thang Tran Viet, Thanh Nguyen Canh, Huy Uong Gia et al.
- **发表**: 2026-09-04  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Human-robot interaction (HRI) enables intuitive and intelligent collaboration between humans and robots in real-world environments. This paper introduces a humanoid robot prototype designed as a flexible testbed for developing and integrating artificial intelligence (AI) modules in HRI tasks. The system features a 12 degree-of-freedom (DOFs) dual-arm mechan…

### 10. KYON: Semi-Modular Wheel-Legged Quadruped With Agile Bimanual Capability

- **arXiv**: [2606.30243v2](https://arxiv.org/abs/2606.30243v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.30243v2)
- **作者**: Luca Rossini, Arturo Laurenzi, Francesco Ruscelli et al.
- **发表**: 2026-06-29  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: This paper presents KYON, a hybrid wheel-legged quadruped robot equipped with a bimanual upper body for loco-manipulation tasks. The platform features a semi-modular design with a reconfigurable lower legs, enabling both wheeled and legged locomotion depending on the environment. A design approach that places actuators in the base and uses transmission mech…

## 🦾 操控 / 灵巧手 / 抓取 (30 篇)

### 1. Dex-X: Learning Visual-Tactile Dexterous Manipulation From Human Videos with Simulated Interaction

- **arXiv**: [2609.07747v2](https://arxiv.org/abs/2609.07747v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.07747v2)
- **作者**: Ruoqu Chen, Feixiang Ruan, Liu Cao et al.
- **发表**: 2026-09-07  ·  **类别**: cs.RO
- **相关性评分**: 23  ·  **🔥 read_now**
- **摘要**: Human videos are an abundant source of dexterous manipulation behaviors, but they lack tactile information that is crucial for contact-rich interaction. This raises a fundamental question: can robots learn deployable visual-tactile dexterous manipulation policies from human video demonstrations without robot-side data collection? We present DEX-X, a framewo…

### 2. Does Imitation Learning Preserve Temporal Robustness in Dexterous Manipulation? An Expert-Learner Comparison Across Task Execution Speeds

- **arXiv**: [2609.01453v1](https://arxiv.org/abs/2609.01453v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.01453v1)
- **作者**: Clinton Enwerem, John S. Baras, Calin Belta
- **发表**: 2026-09-01  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 20  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation policies learned by imitation are typically evaluated for robustness to variation in scenes, objects, or instructions, but their performance across task execution speeds is less often examined. This leaves open how much temporal robustness a learner retains relative to the expert it imitates. We compare an expert and learner under the…

### 3. DeCAL: Towards Physically-Grounded Dexterous Vision-Language-Action Models via Contact-Aware Latent Co-Imagination

- **arXiv**: [2609.09119v1](https://arxiv.org/abs/2609.09119v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.09119v1)
- **作者**: Yankai Fu, Ning Chen, Junkai Zhao et al.
- **发表**: 2026-09-08  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation involves contact-rich and fine-grained interactions with the physical world, posing significant challenges for existing vision-language-action (VLA) models due to severe visual occlusions and complex contact dynamics. While recent works have incorporated tactile sensing into robotic manipulation, most approaches still rely on homogene…

### 4. RoboSPA: Can VLA Models Go Beyond Simple Scenes and Short-Horizon Tasks?

- **arXiv**: [2609.05324v1](https://arxiv.org/abs/2609.05324v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.05324v1)
- **作者**: Zhenxuan Fan, Bo Zhang, Yutong Lin et al.
- **发表**: 2026-09-04  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models have shown promising progress in language-conditioned robotic manipulation. However, existing datasets and benchmarks mainly evaluate task completion under predefined settings, offering limited insight into model reasoning under increasing spatial and procedural complexity. We introduce \textbf{RoboSPA} (\textbf{Robo}t \t…

### 5. Motus2: A Self-Evolving General World Model for Dexterous Manipulation

- **arXiv**: [2608.30237v1](https://arxiv.org/abs/2608.30237v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.30237v1)
- **作者**: Hongzhe Bi, Zihao Zhou, Yihang Tang et al.
- **发表**: 2026-08-31  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: General embodied agents should perceive, predict, act, evaluate, and improve within a unified system. World models have shown great promise in building such agents, yet existing models typically append an action output head to a world simulator, without coupling them into a closed decision-and-learning loop for policy improvement. We present Motus2, a self-…

### 6. Distributed Dexterous Manipulation with Spatially Conditioned Multi-Agent Transformers

- **arXiv**: [2609.06930v1](https://arxiv.org/abs/2609.06930v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.06930v1)
- **作者**: Sarvesh Patil
- **发表**: 2026-09-07  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Distributed Dexterous Manipulation (DDM) is a novel paradigm that presents significant control challenges due to high action-space redundancy, inter-robot cooperation, and dynamic object-robot interactions. This paper introduces a framework based on spatially conditioned Multi-Agent Transformers (MATs) to efficiently learn robust control policies for a DDM…

### 7. FolDeX: A Physical-World Benchmark for Long-Horizon Robotic Manipulation of Deformable Objects

- **arXiv**: [2609.10243v1](https://arxiv.org/abs/2609.10243v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.10243v1)
- **作者**: Chenhuan Liu, Yi Xu, Feng Wu et al.
- **发表**: 2026-09-09  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Embodied AI, including vision-language-action and world-action models, must operate reliably in the physical world. Yet methods that perform well in simulation can degrade substantially on real robots, especially in long-horizon deformable-object manipulation, where policies must track changing states and execute reliable multi-stage bimanual interactions.…

### 8. How to Learn from What a Human Would Avoid? Intervention-Aware World Models with Real-World RL for Dexterous Manipulation

- **arXiv**: [2609.06009v1](https://arxiv.org/abs/2609.06009v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.06009v1)
- **作者**: Jiaju Yin, Zhenhui Zhang, Lixin Xu et al.
- **发表**: 2026-09-05  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Multi-fingered dexterous manipulation remains a frontier for real-world reinforcement learning (RL) due to the high-dimensional action space and the prohibitive cost of hardware failures. While human-in-the-loop (HIL) RL allows operators to intervene before failures occur, current pipelines often treat these interventions as reactive corrections, discarding…

### 9. ZETA: A Controlled Study of Zero-Shot Cross-Embodiment VLA Transfer for Tabletop Manipulation

- **arXiv**: [2609.02546v2](https://arxiv.org/abs/2609.02546v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.02546v2)
- **作者**: Mi Yan, Wenhao Zhang, Zhiqi Zhang et al.
- **发表**: 2026-09-02  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Zero-shot generalization to unseen embodiments is important for generalizable vision-language-action (VLA) models as robot hardware evolves and task-specific data collection remains costly. However, a systematic understanding of this problem remains limited, in part because the literature lacks a unified zero-shot transfer definition and controlled evaluati…

### 10. One Demonstration, Many Objects: Generalizing Manipulation via Local Contact Geometry

- **arXiv**: [2609.01938v2](https://arxiv.org/abs/2609.01938v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.01938v2)
- **作者**: Satvik Sharma, Samrat Sahoo, Huang Huang et al.
- **发表**: 2026-09-01  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation with multi-fingered robot hands promises human-level dexterity, but collecting large-scale dexterous robot hand data remains difficult. Learning from human demonstrations has emerged as a scalable alternative to robot teleoperation, providing strong priors on object interaction and contact strategies. Recent sim-to-real RL methods inc…

## 🎓 模仿学习 / 强化学习 (14 篇)

### 1. Zero-Shot Sim-to-Real Contact-Rich Assembly via Proprioception-Anchored Cross-Modal Pretraining

- **arXiv**: [2609.07534v1](https://arxiv.org/abs/2609.07534v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.07534v1)
- **作者**: Yuhan Wang, Yurou Chen, Hongye Jiang et al.
- **发表**: 2026-09-07  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Contact-rich assembly remains challenging because it requires submillimeter spatial accuracy and reliable interpretation of forces during sustained contact. Although simulation-based reinforcement learning offers a scalable training paradigm, discrepancies in visual observations, contact dynamics, and force/torque (F/T) measurements often limit policy trans…

### 2. Ostrich: Taking Large Strides Through Stiff Contact in Differentiable Dynamics

- **arXiv**: [2609.08800v1](https://arxiv.org/abs/2609.08800v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.08800v1)
- **作者**: Aleš Kučera, Karel Zimmermann
- **发表**: 2026-09-08  ·  **类别**: cs.RO, cs.GR, cs.LG
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Three properties determine whether a differentiable simulator can drive gradient-based optimization through contact: simulation accuracy, gradient reliability, and per-iteration cost. Tape-based engines such as MJX and Newton Semi-Implicit require timesteps small enough to keep contacts numerically tractable, and their backpropagation memory grows linearly…

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

### 5. Praxist: From Experimental Artifacts to Solution Lineages

- **arXiv**: [2608.25955v1](https://arxiv.org/abs/2608.25955v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.25955v1)
- **作者**: Jin Li, Ahmed Murtadha, Zhiyu Wang et al.
- **发表**: 2026-08-26  ·  **类别**: cs.MA, cs.SE
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Autonomous R\&D agents now write, run, and improve executable artifacts under automated evaluation---but largely as laboratory instruments: shown on curated benchmarks, with gains that are hard to trace to a cause and costs well above what sustained engineering practice absorbs. The limitation is structural. Most systems treat each attempt as nearly self-co…

### 6. RIPE++: Reinforced Keypoint Learning from Positive Pairs Only

- **arXiv**: [2608.19693v1](https://arxiv.org/abs/2608.19693v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.19693v1)
- **作者**: Johannes Künzel, Peter Eisert, Anna Hilsmann
- **发表**: 2026-08-20  ·  **类别**: cs.CV, cs.LG
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Sparse keypoint extraction and matching underpin core tasks in geometric computer vision, including structure-from-motion, visual SLAM, augmented reality, and medical image registration. Learning robust local feature representations, however, typically requires accurate camera poses or depth supervision, which are often unavailable in real-world settings. R…

### 7. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 8. FPicker: Topology-Guided Evolution for Filament Tracing in Low-SNR Microscopy

- **arXiv**: [2609.08305v1](https://arxiv.org/abs/2609.08305v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.08305v1)
- **作者**: Tingyin Zhao, Mingtao Huang, Yuan Shen
- **发表**: 2026-09-08  ·  **类别**: cs.CV, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Automating filament tracing in Cryo-Electron Microscopy (Cryo-EM) is essential for 3D helical reconstruction but challenged by intersecting topologies and extremely low Signal-to-Noise Ratios ($\text{SNR} = σ_s^2/σ_n^2$ < 0.1 or -10 dB). Existing paradigms fail: pixel-wise segmenters suffer from severe topological fracturing, box-based detectors face ghost…

### 9. Unblur-SLAM: Dense Neural SLAM for Blurry Inputs

- **arXiv**: [2603.26810v1](https://arxiv.org/abs/2603.26810v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.26810v1)
- **作者**: Qi Zhang, Denis Rozumny, Francesco Girlanda et al.
- **发表**: 2026-03-26  ·  **类别**: cs.CV, eess.IV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We propose Unblur-SLAM, a novel RGB SLAM pipeline for sharp 3D reconstruction from blurred image inputs. In contrast to previous work, our approach is able to handle different types of blur and demonstrates state-of-the-art performance in the presence of both motion blur and defocus blur. Moreover, we adjust the computation effort with the amount of blur in…

### 10. Query Quantized Neural SLAM

- **arXiv**: [2412.16476v1](https://arxiv.org/abs/2412.16476v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2412.16476v1)
- **作者**: Sijia Jiang, Jing Hua, Zhizhong Han
- **发表**: 2024-12-21  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural implicit representations have shown remarkable abilities in jointly modeling geometry, color, and camera poses in simultaneous localization and mapping (SLAM). Current methods use coordinates, positional encodings, or other geometry features as input to query neural implicit functions for signed distances and color which produce rendering errors to d…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (7 篇)

### 1. Solution for UCF UrbanTwin V2X-Real Track: Sim-to-Real Urban LiDAR 3D Object Detection

- **arXiv**: [2609.07608v1](https://arxiv.org/abs/2609.07608v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.07608v1)
- **作者**: Pu Luo, Cong Xu, Yumei Li et al.
- **发表**: 2026-09-07  ·  **类别**: cs.CV
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Bridging the simulation-to-reality gap in roadside LiDAR requires addressing several coupled discrepancies, including scene geometry, sampling density, return patterns, and pedestrian scale. This report presents a multi-source collaborative training and class-aware fusion framework for Sim2Real 3D detection. The method organizes digital-twin scans, diffusio…

### 2. Solution for UCF UrbanTwin LUMPI Track: Sim-to-Real Urban LiDAR 3D Object Detection

- **arXiv**: [2609.07590v1](https://arxiv.org/abs/2609.07590v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.07590v1)
- **作者**: Pu Luo, Cong Xu, Yumei Li et al.
- **发表**: 2026-09-07  ·  **类别**: cs.CV, cs.AI
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: We present our solution to the LUMPI track of the UCF UrbanTwin Sim2Real LiDAR Challenge at the 6th DriveX Workshop, ECCV 2026. The detector must be trained only on synthetic data and is evaluated on 50 held-out real LiDAR frames; a separate 50-frame synthetic submission is evaluated for point-cloud realism. Our method addresses the Sim2Real gap at three le…

### 3. BLASt3R: Bundle Adjustment of Any Image Set with Multi-View Matching and Monocular Priors

- **arXiv**: [2609.05210v1](https://arxiv.org/abs/2609.05210v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.05210v1)
- **作者**: Vincent Leroy, Philippe Weinzaepfel, Lojze Zust et al.
- **发表**: 2026-09-04  ·  **类别**: cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Recent hybrid Structure-from-Motion (SfM) systems combine the robustness of feed-forward 3D reconstruction with the accuracy of traditional bundle adjustment (BA) with pixel matching. They are usually the best performing methods however their scalability and usability remains limited since estimating dense correspondences between views is prohibitively cost…

### 4. Desc++: Efficient Descriptor Enhancement for Data Association in Existing Visual SLAM Systems

- **arXiv**: [2607.11099v1](https://arxiv.org/abs/2607.11099v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.11099v1)
- **作者**: Ting-Wei Ou, Huang-Ting Lin, Kuu-Young Young
- **发表**: 2026-07-13  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Reliable visual data association is fundamental to visual SLAM (V-SLAM), as it directly determines the quality of the camera pose estimation and map consistency. However, the handcrafted descriptors used by most mature real-time systems degrade under illumination and viewpoint changes, while learning-based front-ends that address this weakness typically req…

### 5. DROID-ANCHOR: Odometry-Anchored Recurrent Metric Depth Estimation

- **arXiv**: [2607.17058v1](https://arxiv.org/abs/2607.17058v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.17058v1)
- **作者**: Yuxuan Chen, Brook Du
- **发表**: 2026-07-19  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Precise metric depth estimation is fundamental for autonomous robot navigation, yet monocular systems inherently suffer from scale ambiguity and scale drift. While recent recurrent flow-based SLAM systems have demonstrated state-of-the-art robustness, they remain scale-ambiguous. In this paper, we propose Metric-DROID, an end-to-end recurrent architecture t…

### 6. GLidE-SLAM: GL-Accelerated Indirect-Direct Embedded SLAM

- **arXiv**: [2607.16897v1](https://arxiv.org/abs/2607.16897v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.16897v1)
- **作者**: Carlos A. Pinheiro de Sousa, Heiko Hamann, Oliver Deussen
- **发表**: 2026-07-18  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: With the growing demand for robotics, autonomous drones, and wearable extended reality systems, the deployment of Visual SLAM on embedded devices remains challenging. Tracking must sustain high frame rates while preserving compute resources for map extension and maintenance. This paper presents GLidE-SLAM, a monocular hybrid indirect-direct framework that a…

### 7. Geodesic Flow Matching for Denoising High-Dimensional Structured Representations

- **arXiv**: [2606.00248v1](https://arxiv.org/abs/2606.00248v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.00248v1)
- **作者**: Karim Habashy, Chris Eliasmith
- **发表**: 2026-05-29  ·  **类别**: cs.AI
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Vector Symbolic Algebras (VSAs) enable robust neurosymbolic reasoning by encoding symbolic information into high-dimensional distributed representations. For continuous domains, Spatial Semantic Pointers (SSPs) extend this framework by mapping variables onto continuous toroidal manifolds. However, standard approaches like Flow Matching assume a flat Euclide…

---

## 📋 本日操作建议

**建议今日深读 (Top 3):**
1. [Dex-X: Learning Visual-Tactile Dexterous Manipulation From Human Videos with Simulated Interaction](https://arxiv.org/abs/2609.07747v2) — score 23
2. [Does Imitation Learning Preserve Temporal Robustness in Dexterous Manipulation? An Expert-Learner Comparison Across Task Execution Speeds](https://arxiv.org/abs/2609.01453v1) — score 20
3. [DeCAL: Towards Physically-Grounded Dexterous Vision-Language-Action Models via Contact-Aware Latent Co-Imagination](https://arxiv.org/abs/2609.09119v1) — score 19

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
