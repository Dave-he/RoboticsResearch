# 机器人研究每日摘要 · 2026-11-20

> 自动生成,共 112 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (8 篇)

### 1. $Z$-sight: Unifying Vision-Language-Action and Latent World Modeling

- **arXiv**: [2611.24940v1](https://arxiv.org/abs/2611.24940v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.24940v1)
- **作者**: Junjie Ye, Yiqi Zhao, Muchen Xu et al.
- **发表**: 2026-11-18  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: We introduce $Z$-sight, a unified robot foundation model that couples vision-language-action (VLA) and generative latent world modeling. Video-based world action models (WAMs) show the value of joint future-and-action generation for control, yet inherit the heavy cost of video generators. Recent latent-space policies avoid pixel generation, yet typically al…

### 2. Allocentric Memory, Egocentric Acting: A Dual-Frame VLA for Urban Aerial Navigation

- **arXiv**: [2611.24247v1](https://arxiv.org/abs/2611.24247v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.24247v1)
- **作者**: Haotian Xu, Yue Hu, Zhengqiu Zhu et al.
- **发表**: 2026-11-18  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Language-goal aerial navigation requires a UAV to reach a destination specified in natural language using observations collected during flight. A key challenge is linking changing egocentric perception with spatial evidence anchored to stable locations for long-range navigation. We propose CityNav-VLA, a dual-frame vision-language-action model for urban nav…

### 3. RoboCoEvo: Expanding Robot Capabilities through Agent-Policy Co-Evolution

- **arXiv**: [2611.19081v1](https://arxiv.org/abs/2611.19081v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.19081v1)
- **作者**: Ran Qi, Yixin Xiao, Dawei Wang et al.
- **发表**: 2026-11-14  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Integrating MLLM-based agents with robotic foundation models has attracted increasing attention as a means of enhancing robotic capabilities. However, the improvement of such integrated systems remains largely decoupled across their agent and model components, with advances in one component not necessarily benefiting the other, substantially limiting the ca…

### 4. When Delay Meets Drift: Physical Safety of Robot Foundation Models Is a Cross-Layer Problem

- **arXiv**: [2611.02101v1](https://arxiv.org/abs/2611.02101v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.02101v1)
- **作者**: Liangkai Liu, Bimal Thapa Magar
- **发表**: 2026-11-01  ·  **类别**: cs.RO, cs.CV, cs.ET
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Robot foundation models now act in a closed loop, yet their safety is evaluated one variation at a time: robustness benchmarks perturb the scene while assuming instantaneous inference, and real-time execution methods study inference delay in nominal scenes. We argue that physical safety is not a property of the model alone, but emerges from how variations i…

### 5. Homeward: No Place Like the Training View

- **arXiv**: [2611.24455v1](https://arxiv.org/abs/2611.24455v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.24455v1)
- **作者**: Mingyang Lyu, Yinqian Sun, Gongce Cao et al.
- **发表**: 2026-11-18  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Vision-language-action (VLA) policies implicitly assume that third-person cameras remain fixed at their data-collection poses; once a camera is bumped, remounted, or swapped at deployment, task success degrades precipitously even though the underlying task and robot remain unchanged. We present Homeward, a training-free, plug-and-play observation adapter th…

### 6. ESI: An Embodied Self-Improvement Flywheel for LLM-VLA Agents

- **arXiv**: [2611.18176v2](https://arxiv.org/abs/2611.18176v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.18176v2)
- **作者**: Yundi Cai, Zihan Wang, Chenxi Han et al.
- **发表**: 2026-11-13  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Independently pretrained language models and vision-language-action (VLA) policies provide complementary building blocks for embodied agents, but connecting them does not automatically produce coordinated behavior. The VLA may generate actions that diverge from the LLM's intended subtask and, upon regaining control after a correction, undo the promising sta…

### 7. NereidVLA: Learning to Understand and Navigate the Underwater World

- **arXiv**: [2611.24864v1](https://arxiv.org/abs/2611.24864v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.24864v1)
- **作者**: Chenjie Zhao, Zhiliang Zhu, Quan Chen et al.
- **发表**: 2026-11-18  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Underwater navigation requires translating visual spatial cues into motion, yet marine vision-language datasets rarely include paired robot trajectories. We present NereidVLA, a vision-language-action model that transfers marine spatial knowledge to language-conditioned 3D navigation. We first train Sea2Know on approximately two million marine examples to l…

### 8. La-JEPA: Compact Robot Policies with Latent World Modeling

- **arXiv**: [2611.08156v1](https://arxiv.org/abs/2611.08156v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.08156v1)
- **作者**: Mateo Clémente, George Z. Xue, Amin Abyaneh et al.
- **发表**: 2026-11-05  ·  **类别**: cs.RO, cs.CV, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: World-action models adapt pretrained video generators, and vision-language-action models build on pretrained vision-language backbones; both tie policy architecture and inference cost to large transformers designed for generation rather than control. It remains unclear how much these generation-oriented choices affect control. In this work, we introduce Lat…

## 🌐 具身智能 / 机器人基础模型 (10 篇)

### 1. HospitalBench: Diagnosing Where and Why Embodied Agents Fail on Long Hospital Task Chains

- **arXiv**: [2611.19274v1](https://arxiv.org/abs/2611.19274v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.19274v1)
- **作者**: Gaytri Jena, Kapil Wanaskar, Aman Chadha et al.
- **发表**: 2026-11-14  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Long-horizon embodied tasks fail in ways that end-task success cannot see. HospitalBench is a diagnostic benchmark of ten hospital chores in NVIDIA Isaac Sim, each two unscored warm-up steps followed by a causal chain of five scored sub-tasks in one continuous simulation: the state one step leaves (an object pose, a choice, a fact seen once) determines what…

### 2. Lost in the Hallway: Benchmarking Persistent Spatial Memory Across Revisits

- **arXiv**: [2611.21485v1](https://arxiv.org/abs/2611.21485v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.21485v1)
- **作者**: Henry Zheng, Weibo Gong, Yang Yue et al.
- **发表**: 2026-11-16  ·  **类别**: cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Persistent spatial understanding is essential for embodied agents to operate reliably in environments they repeatedly encounter. It requires recognizing revisited places despite viewpoint changes, distinguishing them from similar-looking rooms, and updating memories as environments change. Yet existing evaluations often leave physical place identity across…

### 3. IncR-3DSGG: Incremental Posed RGB Image Based 3D Scene Graph Generation via Privileged Depth Supervision

- **arXiv**: [2611.15429v1](https://arxiv.org/abs/2611.15429v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.15429v1)
- **作者**: Mrunmai Phatak, Daniel Kienzle, Roman Küble et al.
- **发表**: 2026-11-11  ·  **类别**: cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Scene graphs provide a compact, structured representation of environments by capturing objects and their spatial or semantic relationships in a form suitable for embodied agents. Existing 3D scene graph generation methods often rely on depth sensing at inference, either to associate object instances across views via point cloud overlap or to compute inter-o…

### 4. Pixel2Perspective: A Benchmark for Multi-Modal and Multi-View Generalization in Vision-Language Models

- **arXiv**: [2611.24327v1](https://arxiv.org/abs/2611.24327v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.24327v1)
- **作者**: Aditya Gandhamal, Aniruddh Sikdar, Arya Kishor et al.
- **发表**: 2026-11-18  ·  **类别**: cs.CV
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Embodied AI systems, such as drones and autonomous vehicles, improve navigation by enhancing perception in environments containing unseen objects. While Visual Language Models (VLMs) offer strong image understanding, their real-world application is underexplored. For effective deployment, open-vocabulary semantic segmentation (OVSS) models, leveraging model…

### 5. Every Camera Grows Up: Camera-Height Regression in Interactive Video World Models

- **arXiv**: [2611.21782v1](https://arxiv.org/abs/2611.21782v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.21782v1)
- **作者**: Sheng Lu, Guangpin Tao, Tong Lu et al.
- **发表**: 2026-11-16  ·  **类别**: cs.CV
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Interactive video world models serve as simulators for embodied agents: from a starting image and an action trajectory, they generate the views the agent would see. The starting image fixes how high the camera is, for example 0.15 m for a floor robot or 2.2 m for an overhead camera, and a faithful simulator must keep this height as the camera moves. We show…

### 6. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 7. Vanguard: Knowing When to Trust the Draft in Speculative Vision-Language Agents

- **arXiv**: [2611.23917v1](https://arxiv.org/abs/2611.23917v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.23917v1)
- **作者**: Hanqi Mao, Jiajun Fan, Ruihan Guo et al.
- **发表**: 2026-11-18  ·  **类别**: cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-language agents that browse websites, operate phones and act in homes reason before every action, so every step waits for a large model, a latency and cost that stand in the way of deployment. Step-level speculation lets a small model draft each step and calls the large model only on rejected drafts, but its outcome rests on the judge, and a judge th…

### 8. Manufacturing Differential Sparsity: Planner-Hardware Co-Design for Efficient World Model Planning

- **arXiv**: [2611.22483v1](https://arxiv.org/abs/2611.22483v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.22483v1)
- **作者**: Wenbo Zhu, Paul Yi-Chia Chen, Yuanhan Li et al.
- **发表**: 2026-11-17  ·  **类别**: cs.AR, cs.AI, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: JEPA-style latent world models let embodied agents plan toward new goals with model predictive control, but they are still too slow for real-life embodied control: sampling-based MPC repeats predictor inference tens of thousands of times per plan, and even on high-end GPUs one planning step can take tens of seconds. We observe substantial latent locality in…

### 9. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

### 10. Reinforcement Learning Enables Scaling Generalist Robot Policy Improvement

- **arXiv**: [2611.06905v1](https://arxiv.org/abs/2611.06905v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.06905v1)
- **作者**: Michal Korniak, Marco Bagatella, Ralf Römer et al.
- **发表**: 2026-11-04  ·  **类别**: cs.LG, cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: The introduction of generalist robot policies has enabled a single, large model to learn to perform a variety of tasks from a vast pre-training corpus. While these models often exhibit powerful zero-shot generalization capabilities, they typically require an adaptation phase to achieve sufficient performance in deployment. Iterated self-improvement via rein…

## 🦵 人形 / 足式机器人 (25 篇)

### 1. PolyMorphWBC: Whole-Body Control from End-Effector Trajectories for Quadrupedal Mobile Manipulation across Arm Morphologies with Extended Reach

- **arXiv**: [2611.15117v1](https://arxiv.org/abs/2611.15117v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.15117v1)
- **作者**: Heng Li, Yang Li, Yifan Duan et al.
- **发表**: 2026-11-11  ·  **类别**: cs.RO
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: Quadrupedal mobile manipulators can extend their manipulation workspace by coordinating the mounted arm with the mobile base. At the task level, short-horizon end-effector (EE) trajectories provide an interface for specifying the desired manipulation motion without prescribing how it should be realized by the arm and base. However, executing such trajectori…

### 2. MoViC: Real-Time Humanoid Whole-Body Control from Monocular Video Streams

- **arXiv**: [2611.19998v1](https://arxiv.org/abs/2611.19998v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.19998v1)
- **作者**: Yimin Han, Jiahui Zhang, Wanyue Li et al.
- **发表**: 2026-11-15  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Real-time whole-body imitation from monocular video requires both a robust universal tracker and high-quality real-time reconstruction. We present MoViC, a framework that uses live RGB video as a control signal for humanoid robots without wearable tracking devices. The framework combines monocular human motion reconstruction, robot retargeting, and a transf…

### 3. Driving the Style: Velocity-Conditioned Whole-Body Control from Motion Demonstrations

- **arXiv**: [2611.20888v1](https://arxiv.org/abs/2611.20888v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.20888v1)
- **作者**: Murad Dawood, Oezge Drama Berkenkamp, Antonio Gonzales Marin et al.
- **发表**: 2026-11-16  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Achieving human-like behavior on humanoid robots has advanced rapidly by leveraging motion-capture demonstrations rather than hand-crafted cost functions. Adversarial imitation supplies a style signal that lets a policy fulfill a task while adhering to a desired style, but is difficult to transfer to hardware. Whole-body tracking through reinforcement learn…

### 4. From Tabletop to Walking Bot: Deploying a VLA Model on a Legged Manipulator Robot

- **arXiv**: [2610.32271v1](https://arxiv.org/abs/2610.32271v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.32271v1)
- **作者**: Giovanni Minelli, Antonio Langella, Giovanni B. Dessy et al.
- **发表**: 2026-10-23  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models are typically pretrained on broad, diverse datasets and subsequently fine-tuned on a comparatively small dataset tailored to a specific target robot. Such adaptation recipe is now widely established, achieving its most mature results on fixed-base arms due to their static base dynamics and consistent reference frame. Moun…

### 5. ROSE: A Shared Cross-Embodiment Facial-Motion Latent Space for Humanoid Robot Expression

- **arXiv**: [2611.20950v1](https://arxiv.org/abs/2611.20950v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.20950v1)
- **作者**: Yongji Fu, Man Cao, Yi Zhou et al.
- **发表**: 2026-11-16  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Natural, coherent full-face dynamic expressions are central to making humanoid robots socially approachable, yet existing systems commonly realize only limited lip motion or scripted expressions. The limitation is both physical and algorithmic. A compact head leaves little room for densely packed, independently controllable actuation; meanwhile, learned sys…

### 6. SG-ODOM: Event-Driven Proprioceptive State Estimation with Stability-Gated Contact Updates for Legged Robots

- **arXiv**: [2611.20710v1](https://arxiv.org/abs/2611.20710v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.20710v1)
- **作者**: Francesco Iotti, Chiyun Noh, Franco Angelini et al.
- **发表**: 2026-11-16  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Reliable proprioceptive state estimation for legged robots fuses inertial sensing with kinematic sensing from leg encoders. The latter assumes a foot is stationary during the stance phase; however, physical foot touchdown does not necessarily provide a stationary reference for odometry, particularly during impact and load transfer. Repeatedly applying kinem…

### 7. PERA: Plug-in Experts for Robotic Actions in Continual Whole-Body Control

- **arXiv**: [2611.16188v1](https://arxiv.org/abs/2611.16188v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.16188v1)
- **作者**: Shangchao Hu, Yadan Sun, Xibo Yu et al.
- **发表**: 2026-11-12  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Motion imitation enables humanoid robots to acquire whole-body skills such as walking and dancing. However, fine-tuning an entire policy for a new skill can affect existing behaviors, while training a separate policy for each skill increases training and maintenance costs. We present PERA, a method for learning new skills by reusing existing motion capabili…

### 8. OccluDex: Hierarchical 3D Visuo-Tactile Representation Learning for Egocentric Dexterous Manipulation under Self-Occlusion

- **arXiv**: [2609.39017v1](https://arxiv.org/abs/2609.39017v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39017v1)
- **作者**: Ziheng Xu, Yueyuan Chen, Xinyuan He et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Reliable dexterous manipulation requires continuous estimation of object geometry and hand-object contact throughout interaction. With egocentric sensing, however, the manipulating hand frequently occludes task-relevant object surfaces and contact regions, reducing the visual evidence available for state estimation and thereby making robust closed-loop cont…

### 9. From Temperature-Limited to Battery-Limited Legged Locomotion

- **arXiv**: [2611.22231v1](https://arxiv.org/abs/2611.22231v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.22231v1)
- **作者**: Raphaël Ségas, Balázs Opra, Léo Ghafari et al.
- **发表**: 2026-11-17  ·  **类别**: cs.RO, cs.LG, eess.SY
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: On legged robots, sustained locomotion often ends in thermal shutdown rather than battery depletion: the heat of walking concentrates in a few joint motors, which overheat long before the battery is empty. We train thermally aware locomotion policies by reinforcement learning without ever observing temperature, and demonstrate this on a Unitree Go2 quadrupe…

### 10. Towards Probabilistically Safe Reinforcement Learning: Theory and Deployment on Humanoid and Aerial Robots

- **arXiv**: [2611.19616v1](https://arxiv.org/abs/2611.19616v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.19616v1)
- **作者**: Pol Mestres, Varun Gabbita, Jason H. K. Siu et al.
- **发表**: 2026-11-14  ·  **类别**: cs.RO, eess.SY
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Reinforcement learning (RL) enables robots to acquire complex skills, but standard RL formulations do not guarantee that learned policies satisfy safety constraints, which limits their use in safety-critical settings. Existing safe RL methods with provable guarantees typically support only restricted classes of constraints and require unbiased estimators of…

## 🦾 操控 / 灵巧手 / 抓取 (35 篇)

### 1. Finetuning VLAs for Dexterous Manipulation: The Right Checkpoint Is All You Need

- **arXiv**: [2611.23676v1](https://arxiv.org/abs/2611.23676v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.23676v1)
- **作者**: Artur Kuramshin, Charlotte Cloutier, Michael Przystupa et al.
- **发表**: 2026-11-18  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 24  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action models have demonstrated strong manipulation capabilities. A limitation of VLA models is that most manipulation datasets focus on parallel-jaw gripper systems, making transfer to multi-finger hands challenging, particularly as teleoperation datasets are harder to collect with multi-fingered robots. In this work, we study how to best a…

### 2. 3DTouch: A Tactile-aware VLA Model with 3D Geometric Relations for Dexterous Manipulation

- **arXiv**: [2611.23961v1](https://arxiv.org/abs/2611.23961v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.23961v1)
- **作者**: Xin Zhang, Shiqi Zhang, Siyuan Cao et al.
- **发表**: 2026-11-18  ·  **类别**: cs.RO
- **相关性评分**: 23  ·  **🔥 read_now**
- **摘要**: In contact-rich dexterous manipulation, occlusion by the fingers and interacting objects obscures local geometry, preventing visual observations from fully capturing contact locations. Visually similar scenes may also differ subtly in the relative positions of interacting objects, leading to different contact states. We propose 3DTouch, a tactile-geometric…

### 3. DAPPT: Domain-Aware Policies from Procedural Trajectories for Sim-to-Real Dexterous Tool Use

- **arXiv**: [2611.20202v1](https://arxiv.org/abs/2611.20202v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.20202v1)
- **作者**: Beining Han, Jia Deng
- **发表**: 2026-11-15  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Sim-to-real RL has achieved impressive results in dexterous manipulation but remains limited to tasks with accurate rigid-body simulation. However, these methods cannot be applied to skills that involve deformable and particles, with which the simulation speed will become too slow for large-scale RL learning. We present DAPPT, a sim-to-real framework for en…

### 4. TactileLab: Sim-to-Real Dexterous Robot Manipulation with Efficient Shear-Sensitive Tactile Simulation

- **arXiv**: [2611.07881v1](https://arxiv.org/abs/2611.07881v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.07881v1)
- **作者**: Yijiong Lin, Wenhao He, Toby Jack et al.
- **发表**: 2026-11-05  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Robotic simulators that represent shear within tactile sensing are becoming increasingly important for contact-rich manipulation. However, simulating contact shear with high-fidelity deformable or soft-body simulation is computationally demanding, limiting scalability to large-scale reinforcement learning. Here we introduce \textit{TactileLab}, a scalable m…

### 5. SHAPE: Discrete Supervision and Parallel Continuous Streams for Learning Dexterous Manipulation from Egocentric Human Data

- **arXiv**: [2611.24585v1](https://arxiv.org/abs/2611.24585v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.24585v1)
- **作者**: Yaping Li, Zhihong Liu, Jiacheng Li et al.
- **发表**: 2026-11-18  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Egocentric human recordings are far cheaper than dexterous robot demonstrations, promising stronger pretraining and direct skill learning without task-specific robot data. Yet humans and robots differ in morphology and kinematics, so human recordings lack the joint positions and actuator commands that supervise robot policies, providing only retargeted end-…

### 6. SoTa: Soft Tactile Skins for Dexterous Manipulation

- **arXiv**: [2610.02338v1](https://arxiv.org/abs/2610.02338v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.02338v1)
- **作者**: Jingyun Yang, Baiyu Shi, Timothy Yu et al.
- **发表**: 2026-10-01  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: A growing body of work suggests that tactile sensing gives robot policies contact information that complements vision in dexterous manipulation. However, visuo-tactile robot data remains scarce: dexterous demonstrations require teleoperating robots, which limits dataset scale. Human demonstrations are far cheaper to collect and offer a path to scale this da…

### 7. RECLAIM: Robot-Vision-Informed Adversarial Patch Defense via Embodied Attention Feedback

- **arXiv**: [2611.24494v1](https://arxiv.org/abs/2611.24494v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.24494v1)
- **作者**: Jiayou Zhu, Peng Guo, Litian Zhang et al.
- **发表**: 2026-11-18  ·  **类别**: cs.RO, cs.CR, cs.CV
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Vision-language-action policies control embodied agents through a perception-action loop grounded in physical interaction, where adversarial patches can corrupt action predictions and thereby alter subsequent observations. To mitigate these threats, many existing defenses rely on policy adaptation or auxiliary models, but require additional training or infe…

### 8. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

### 9. From Human Videos to Bimanual Dexterous Manipulation Data: Confidence-Guided RL Refinement of Video Priors

- **arXiv**: [2611.21908v1](https://arxiv.org/abs/2611.21908v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.21908v1)
- **作者**: Yanghong Liu, Yang Chen, Kailang Xu et al.
- **发表**: 2026-11-16  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Collecting demonstrations for bimanual dexterous manipulation is costly, motivating the use of human videos as a source of robot training data. However, uncertainty in video-derived motion estimates and differences between human and robot embodiments make direct motion transfer challenging. In this work, we introduce PriDex, a framework that transforms huma…

### 10. Towards Pose-Robust Few-Shot Vision-Language-Action Models

- **arXiv**: [2611.24360v1](https://arxiv.org/abs/2611.24360v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.24360v1)
- **作者**: Wenhao Li, Zhongyi Han, Yuhao Wei et al.
- **发表**: 2026-11-18  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Fine-tuning a vision-language-action (VLA) model on a few dozen demonstrations is the standard way to put a manipulation policy on a robot, yet the resulting policy silently assumes that the camera and the robot base stay exactly where they were during data collection: a bumped tripod or a base re-docked a few centimetres away makes it reach for the wrong p…

## 🎓 模仿学习 / 强化学习 (14 篇)

### 1. Bracketing Shows the Way: Adaptive Multi-Exposure Policy as Input for Robust Visual SLAM

- **arXiv**: [2610.33174v1](https://arxiv.org/abs/2610.33174v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.33174v1)
- **作者**: Olivier Gamache, Anthony Lavertu, David-Alexandre Duclos et al.
- **发表**: 2026-10-23  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Rapid illumination transitions can disturb Visual SLAM (VSLAM) by saturating images before the Automatic Exposure (AE) policy adapts, removing the visual correspondences needed to maintain tracking. Our proposed methods mitigate this disturbance at two levels: B-Adapt acquires adaptive exposure brackets to cover the scene dynamic range while promoting photo…

### 2. EyeDiT: Anatomy-Grounded Multi-Modal Eye Generation and Simulation

- **arXiv**: [2611.23670v1](https://arxiv.org/abs/2611.23670v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.23670v1)
- **作者**: Yonghan Lee, Zachary Willms, Kun Liu et al.
- **发表**: 2026-11-18  ·  **类别**: cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Synthetic eye data are critical for rapid development of eye tracking (ET) in AR/VR applications. However, existing synthetic eye generators are largely image-centric and lack a high-quality underlying 3D anatomy of the eye, which limits their control mainly to the gaze and provides no anatomical labels. To address this problem, we propose EyeDiT, an anatom…

### 3. Degeneracy-Orthogonal Geometric Constraints for LiDAR SLAM

- **arXiv**: [2609.36753v1](https://arxiv.org/abs/2609.36753v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.36753v1)
- **作者**: Minseo Kim, Yina Kim, Jinhwa Hwang et al.
- **发表**: 2026-09-29  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Autonomous robot navigation relies on simultaneous localization and mapping (SLAM) to estimate motion and maintain an accurate pose within an environment. However, in axially uniform corridors such as long tunnels and pipelines, LiDAR odometry is fundamentally limited by unconstrained drift along the feature-weak travel direction. This structural degeneracy…

### 4. Chain-SLAM: Globally Consistent Backend for Multi-Session LiDAR SLAM via Chained Loop Closure

- **arXiv**: [2609.12221v1](https://arxiv.org/abs/2609.12221v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.12221v1)
- **作者**: Zhiheng Li, Xinhao Liu, Juexiao Zhang et al.
- **发表**: 2026-09-10  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Maintaining consistency over long spatial and temporal horizons remains a fundamental challenge in large-scale LiDAR SLAM, particularly when integrating maps collected across multiple sessions. We present Chain-SLAM, a LiDAR SLAM backend enabling online multi-session map alignment and reuse with global consistency at large scale. We implement a chained loop…

### 5. Generative adversarial imitation learning for robot swarms: Learning from human demonstrations and trained policies

- **arXiv**: [2603.02783v1](https://arxiv.org/abs/2603.02783v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.02783v1)
- **作者**: Mattes Kraus, Jonas Kuckling
- **发表**: 2026-03-03  ·  **类别**: cs.RO, cs.LG, cs.MA
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, robots are supposed to learn from demonstrations of the desired behavior. Most of the work in imitation learning for swarm robotics provides the demonstrations as rollouts of an existing policy. In this work, we provide a framework based on generative adversarial imitation learning that aims to learn collective behaviors from human de…

### 6. End-to-End Deep Imitation Learning: Robot Soccer Case Study

- **arXiv**: [1807.09205v1](https://arxiv.org/abs/1807.09205v1)  ·  **PDF**: [link](https://arxiv.org/pdf/1807.09205v1)
- **作者**: Okan Aşık, Binnur Görer, H. Levent Akın
- **发表**: 2018-06-28  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, behavior learning is generally done using the features extracted from the demonstration data. Recent deep learning algorithms enable the development of machine learning methods that can get high dimensional data as an input. In this work, we use imitation learning to teach the robot to dribble the ball to the goal. We use B-Human robo…

### 7. RingNav: Task-Shaped Circular Memory for Visual Heading

- **arXiv**: [2610.19044v1](https://arxiv.org/abs/2610.19044v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.19044v1)
- **作者**: Naitri Rajyaguru, Aryan Tajne, Stephen Jardim et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Tiny robots have limited computation and memory, yet visual navigation systems often maintain more state than a task requires. We ask whether persistent memory can instead be shaped by the task. We present \textbf{RingNav}, a \(10.6\)k--parameter visual heading estimator that constrains its memory to the circular manifold \(S^1\). RingNav learns only the tu…

### 8. DPGS-SLAM: Diffusion-Prior and Provenance-Aware Monocular Gaussian Splatting SLAM for Dynamic Visual Sensing

- **arXiv**: [2611.12038v2](https://arxiv.org/abs/2611.12038v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.12038v2)
- **作者**: Yifan Luo, Takafumi Matsumaru, Vibekananda Dutta et al.
- **发表**: 2026-11-09  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: This paper presents DPGS-SLAM (Diffusion-Prior and Provenance-Aware Monocular Gaussian Splatting SLAM) for dense mapping in environments containing dynamic objects. Objects in dynamic motion remain a significant challenge for dense visual SLAM since dynamic observations can contaminate camera tracking and scene reconstruction. Although 3DGS (3D Gaussian spl…

### 9. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 10. Unblur-SLAM: Dense Neural SLAM for Blurry Inputs

- **arXiv**: [2603.26810v1](https://arxiv.org/abs/2603.26810v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.26810v1)
- **作者**: Qi Zhang, Denis Rozumny, Francesco Girlanda et al.
- **发表**: 2026-03-26  ·  **类别**: cs.CV, eess.IV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We propose Unblur-SLAM, a novel RGB SLAM pipeline for sharp 3D reconstruction from blurred image inputs. In contrast to previous work, our approach is able to handle different types of blur and demonstrates state-of-the-art performance in the presence of both motion blur and defocus blur. Moreover, we adjust the computation effort with the amount of blur in…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (10 篇)

### 1. SKiD-SLAM: Resource-Aware Distributed Multi-Robot LiDAR SLAM for Planetary Missions with Field Deployments at Analog Sites

- **arXiv**: [2610.38141v1](https://arxiv.org/abs/2610.38141v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.38141v1)
- **作者**: Hogyun Kim, Juwon Kim, Dongjin Cho et al.
- **发表**: 2026-10-28  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **📚 综述(归档备查,按协议 §4 不深读)**
- **摘要**: Future planetary exploration missions require teams of robots to collaboratively map unknown environments under severe communication limits, constrained onboard computation, and no central infrastructure. In this field report, we present SKiD-SLAM, a distributed multi-robot LiDAR simultaneous localization and mapping (SLAM) system for such environments, and…

### 2. Spade-SLAM: Sparse Correspondence Anchors for Dense Self-Supervised Visual SLAM

- **arXiv**: [2611.01937v1](https://arxiv.org/abs/2611.01937v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.01937v1)
- **作者**: Julian Philipp Schmitt, Weirong Chen, Ganlin Zhang et al.
- **发表**: 2026-11-01  ·  **类别**: cs.CV
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: We introduce Spade-SLAM, a self-supervised dense visual SLAM framework that substantially narrows the long-standing performance gap to supervised methods in a zero-shot setting. By demonstrating that high-fidelity tracking can be achieved without explicit ground-truth pose and depth labels, our approach offers a highly effective and label-efficient alternat…

### 3. ASTRA: ASV Simulator for Transferable Realistic Autonomy

- **arXiv**: [2611.21789v1](https://arxiv.org/abs/2611.21789v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.21789v1)
- **作者**: Tsimafei Lazouski, Cody Sheltraw, Alan Papalia et al.
- **发表**: 2026-11-16  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Autonomy development for marine autonomous surface vehicles (ASVs) remains challenging because field testing is costly and difficult to reproduce. Existing marine simulation tools provide mature capabilities in vessel dynamics, robotics integration, and visual rendering, but these strengths are emphasized differently across platforms. This paper presents AS…

### 4. LIN-SLAM: Lightweight LiDAR--Inertial Neural SLAM for Real-Time Onboard Navigation

- **arXiv**: [2610.21199v1](https://arxiv.org/abs/2610.21199v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.21199v1)
- **作者**: Shiqi Che, Yijie Liu, Shuo Wang et al.
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **✅ 已研读**
- **摘要**: Geometric light detection and ranging (LiDAR)--inertial simultaneous localization and mapping (SLAM) provides efficient state estimation but lacks the continuous map representation and global refinement capabilities of neural implicit SLAM, while neural implicit methods remain computationally expensive. We propose Lightweight LiDAR--Inertial Neural SLAM (LI…

### 5. Evaluation of Front-End Feature Matching for Lunar Visual SLAM

- **arXiv**: [2610.30774v1](https://arxiv.org/abs/2610.30774v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.30774v1)
- **作者**: Guillem Casadesus Vila, Grace Gao
- **发表**: 2026-10-22  ·  **类别**: cs.CV
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Lunar rovers will primarily rely on cameras for localization until navigation satellite services are deployed, and will continue to need them afterwards for relative navigation, hazard detection, and surface operations. Visual odometry (VO) and Simultaneous Localization and Mapping (SLAM) mostly estimate motion by matching features between frames. However,…

### 6. Smartphone Indoor Localization Enhanced by Hierarchical Multi-Sensor Context Recognition

- **arXiv**: [2610.39691v1](https://arxiv.org/abs/2610.39691v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.39691v1)
- **作者**: Wenhui Feng, Muhan Weng, Jianyu Liu et al.
- **发表**: 2026-10-29  ·  **类别**: cs.LG, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Smartphone indoor localization requires low-cost, robust positioning across scene transitions and phone-use variations. Pedestrian dead reckoning (PDR) enables infrastructure-free deployment but accumulates errors from heading drift, structural transitions, and carrying-mode changes. Existing methods often treat contextual cues as a single event stream or l…

### 7. Line-Augmented cuVSLAM: Robust Visual Odometry in Low-Texture Environments

- **arXiv**: [2610.20958v1](https://arxiv.org/abs/2610.20958v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.20958v1)
- **作者**: Dara Molloy, Terry Wu, Wonju Lee et al.
- **发表**: 2026-10-14  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Autonomous mobile robots in warehouses and production facilities operate in precisely the environments that defeat point-feature visual odometry: featureless aisles, uniform walls, repetitive racking and specular floors. Such environments are, however, rich in straight-edge structure: rack uprights, door frames, wall junctions and cabinet outlines present h…

### 8. RTISSLAM-3D: Full 6-DoF SLAM With an In-Air 3D Imaging Sonar

- **arXiv**: [2610.22552v1](https://arxiv.org/abs/2610.22552v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.22552v1)
- **作者**: Jan Steckel, Vincent Katter, Wouter Jansen
- **发表**: 2026-10-15  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Echolocating bats navigate dense forests using sonar alone, and in-air 3D imaging sonars now capture the entire frontal hemisphere with every pulse. Sonar SLAM, however, has so far been planar: current systems estimate a 2D trajectory and discard the elevation information in the sonar images, an assumption that does not hold on rough and sloped terrain such…

### 9. Parameter Sensitivity Analysis for Aerial LiDAR-Inertial Odometries in low-altitude flights

- **arXiv**: [2609.12837v1](https://arxiv.org/abs/2609.12837v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.12837v1)
- **作者**: Robert Milijas, Jose Ramiro Martinez-de Dios, Stjepan Bogdan
- **发表**: 2026-09-11  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: LiDAR-based SLAM (Simultaneous Localization and Mapping) and LIO (LiDAR-inertial odometry) algorithms are often used for precise navigation of unmanned aerial vehicles, especially during interactions with the aerial robot's environment. However, the performance of these algorithms is greatly dependent on the scenario, LiDAR, and robot motion characteristics…

### 10. Geodesic Flow Matching for Denoising High-Dimensional Structured Representations

- **arXiv**: [2606.00248v1](https://arxiv.org/abs/2606.00248v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.00248v1)
- **作者**: Karim Habashy, Chris Eliasmith
- **发表**: 2026-05-29  ·  **类别**: cs.AI
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Vector Symbolic Algebras (VSAs) enable robust neurosymbolic reasoning by encoding symbolic information into high-dimensional distributed representations. For continuous domains, Spatial Semantic Pointers (SSPs) extend this framework by mapping variables onto continuous toroidal manifolds. However, standard approaches like Flow Matching assume a flat Euclide…

## 🧭 导航 / 路径规划 (2 篇)

### 1. Unreasonable Confidence from Simulator Misspecification: Directional Robustness on the SPEED+ Sim-to-Real Benchmark

- **arXiv**: [2611.20321v1](https://arxiv.org/abs/2611.20321v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.20321v1)
- **作者**: Nikolay Dolgov
- **发表**: 2026-11-15  ·  **类别**: cs.CV, cs.AI, cs.LG
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Vision-based navigation systems for orbit must be trained almost entirely on synthetic imagery, because real labelled images of a given spacecraft in flight rarely exist. Benchmarks like SPEED+ are built for that situation: the training set comes from a simulator, and the test sets are real images of a satellite mockup under two kinds of lighting. That simu…

### 2. Accuracy potential of visual localization exploiting high-end street-level imagery

- **arXiv**: [2607.24409v2](https://arxiv.org/abs/2607.24409v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.24409v2)
- **作者**: Jonas Meyer, Stephan Nebiker, Pascal Theiler et al.
- **发表**: 2026-07-27  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Many applications, such as surveying, autonomous navigation, robotics and augmented reality, require accurate pose information with respect to a reference frame. Visual localization can complement GNSS positioning, whose availability and accuracy are often limited. However, the accuracy potential of visual localization has not yet been systematically invest…

## 🧪 仿真 / Sim2Real (2 篇)

### 1. Exploring the link between predictive uncertainty and the sim-to-real gap in deep learning models utilizing synthetic data

- **arXiv**: [2611.21365v2](https://arxiv.org/abs/2611.21365v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.21365v2)
- **作者**: Alexander Moriz, Lukas Krebs, Amon Göppert et al.
- **发表**: 2026-11-16  ·  **类别**: cs.CV
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Today, state-of-the-art methods for quality control (QC) are based on Machine Vision, combining deep learning (DL) models with camera-based inspection. Yet, the integration of such solutions in industrial applications is often impeded by data sparsity and trust in model reliability. While synthetic data offers a promising approach to generate the necessary…

### 2. Practice in Text, Act in Pixels: Correcting Where Perception Fails

- **arXiv**: [2611.22722v1](https://arxiv.org/abs/2611.22722v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.22722v1)
- **作者**: Zhongling Xu, Hairong Wang
- **发表**: 2026-11-17  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: GUI agents can learn cheaply from a text view of an interface and act on screenshots through a vision-language screen reader. Yet on a simulated mobile platform with a low-cost reader, policies that complete most tasks in text fail on many of the same tasks on screenshots. We ask where a small budget of real screenshots is best spent to close this gap. We f…

## 🤏 软体机器人 / 柔性控制 (5 篇)

### 1. PneuGen: Task-Driven Agentic Co-Design of Soft Pneumatic Robots

- **arXiv**: [2611.13344v1](https://arxiv.org/abs/2611.13344v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.13344v1)
- **作者**: Shaohong Zhong, Marco Pontin, Perla Maiolino
- **发表**: 2026-11-09  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Task-driven design of soft robots requires the consideration of factors such as geometry, morphology, material properties, and actuation, resulting in a large and complex design space that is challenging to explore. Computational optimisation methods leverage signals from simulation to iteratively improve designs to achieve task objectives. However, these m…

### 2. Accelerated Reinforcement Learning for Soft Robotics: Hours Instead of Years

- **arXiv**: [2611.11718v1](https://arxiv.org/abs/2611.11718v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.11718v1)
- **作者**: Roshan S. Kaundinya, Hehui Zheng, Robert K. Katzschmann et al.
- **发表**: 2026-11-09  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Reinforcement learning (RL) requires large amounts of interaction data or a reliable simulator, both hard to obtain for nonlinear soft robotic hardware. Recent work shows that a time-scale separation inherent to soft robot dynamics justifies their reduction to low-dimensional invariant manifolds, known as adiabatic spectral submanifolds (aSSMs). We demonstr…

### 3. Actuation and Control of Passive Tendon-Driven Soft Extensions Through Rigid Manipulator Motion

- **arXiv**: [2611.15386v1](https://arxiv.org/abs/2611.15386v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.15386v1)
- **作者**: Ignacio Cuiral-Zueco, Gonzalo López-Nicolás, Youcef Mezouar
- **发表**: 2026-11-11  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Industrial manipulators offer reach and precision but can damage nearby structures in confined spaces. Soft robots provide compliant contact but typically have limited reach. Rigid-soft systems combine their advantages, although they often require dedicated actuation and control hardware. We propose actuating a passive tendon-driven soft extension through m…

### 4. SunLightBots: Turning sunlight into self-sustained, high-power motion in soft robots

- **arXiv**: [2611.14729v1](https://arxiv.org/abs/2611.14729v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.14729v1)
- **作者**: Yoo Jin Lee, Melanie Torres Crespo, Zhongxiao Deng et al.
- **发表**: 2026-11-10  ·  **类别**: cs.RO, cond-mat.soft, physics.app-ph
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Soft robots built from active materials can directly convert environmental stimuli into motion, offering a route to energy autonomy and embodied control. However, environmental energy is generally harvested at low power, whereas rapid, mechanically demanding actions require high mechanical output power. Reconciling this mismatch while sustaining self-regula…

### 5. DeepSoMo: Deformable Object Motion Estimation under Proprioceptive Partial Observability via Predictive Latent Dynamics

- **arXiv**: [2611.11242v1](https://arxiv.org/abs/2611.11242v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.11242v1)
- **作者**: Hanwen Zhao, Weicheng Dai, Luoyao Chen et al.
- **发表**: 2026-11-08  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Estimating the motion of deformable bodies in soft robotics from proprioceptive sensing is challenging due to partial observability, as internal observations provide only indirect access to global motion, contact, and shape evolution. In such settings, instantaneous observations are insufficient, and accurate estimation requires temporally consistent latent…

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
1. [Finetuning VLAs for Dexterous Manipulation: The Right Checkpoint Is All You Need](https://arxiv.org/abs/2611.23676v1) — score 24
2. [3DTouch: A Tactile-aware VLA Model with 3D Geometric Relations for Dexterous Manipulation](https://arxiv.org/abs/2611.23961v1) — score 23
3. [PolyMorphWBC: Whole-Body Control from End-Effector Trajectories for Quadrupedal Mobile Manipulation across Arm Morphologies with Extended Reach](https://arxiv.org/abs/2611.15117v1) — score 18

> 筛选说明:本次 Top 3 已排除(已研读跳过 1 篇、综述跳过 1 篇)。

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
