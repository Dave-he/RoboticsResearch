# 机器人研究每日摘要 · 2026-11-24

> 自动生成,共 116 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (6 篇)

### 1. $Z$-sight: Unifying Vision-Language-Action and Latent World Modeling

- **arXiv**: [2611.24940v1](https://arxiv.org/abs/2611.24940v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.24940v1)
- **作者**: Junjie Ye, Yiqi Zhao, Muchen Xu et al.
- **发表**: 2026-11-18  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: We introduce $Z$-sight, a unified robot foundation model that couples vision-language-action (VLA) and generative latent world modeling. Video-based world action models (WAMs) show the value of joint future-and-action generation for control, yet inherit the heavy cost of video generators. Recent latent-space policies avoid pixel generation, yet typically al…

### 2. Efficient VLA Reinforcement Learning via Subchunk Rollouts in Latent World Models

- **arXiv**: [2611.27645v1](https://arxiv.org/abs/2611.27645v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.27645v1)
- **作者**: Nan Tang, Han-Tao Zhang, Jing-Cheng Pang et al.
- **发表**: 2026-11-20  ·  **类别**: cs.LG
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Model-based reinforcement learning (MBRL) can improve pretrained vision-language-action (VLA) policies through imagined experiences. However, existing VLA-MBRL methods primarily rely on large-scale image or video generation world models, incurring large computational overhead. Latent world models offer a more efficient alternative but face two challenges: c…

### 3. Learning from Incomplete Actions: Interval Motion Supervision for Vision-Language-Action Policies

- **arXiv**: [2611.27171v1](https://arxiv.org/abs/2611.27171v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.27171v1)
- **作者**: Yunpeng Mei, Chenyu Wang, Xiaowen Zhu et al.
- **发表**: 2026-11-20  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Visual labeling of egocentric demonstrations often leaves contiguous gaps in action supervision. Reliable poses around a gap still provide its net translation and rotation. We use this information to train vision-language-action policies while preserving ordinary flow matching on reliable local actions. A composition objective constrains the aggregate motio…

### 4. Analysis of Multi-Client Inference Techniques for Vision-Language-Action Models

- **arXiv**: [2611.26944v1](https://arxiv.org/abs/2611.26944v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.26944v1)
- **作者**: Stefan de Lasa, Mohammadreza Mofayezi, Gennady Pekhimenko et al.
- **发表**: 2026-11-20  ·  **类别**: cs.DC, cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Vision-Language-Action models (VLAs) are a new class of machine learning model for generalizable robot control. While they enable robots to perform complex tasks in unseen environments, serving VLAs leaves hardware idle between inference passes and under-utilized during inference. Serving multiple clients at once can improve utilization, but fundamental mul…

### 5. RoboCoEvo: Expanding Robot Capabilities through Agent-Policy Co-Evolution

- **arXiv**: [2611.19081v1](https://arxiv.org/abs/2611.19081v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.19081v1)
- **作者**: Ran Qi, Yixin Xiao, Dawei Wang et al.
- **发表**: 2026-11-14  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Integrating MLLM-based agents with robotic foundation models has attracted increasing attention as a means of enhancing robotic capabilities. However, the improvement of such integrated systems remains largely decoupled across their agent and model components, with advances in one component not necessarily benefiting the other, substantially limiting the ca…

### 6. La-JEPA: Compact Robot Policies with Latent World Modeling

- **arXiv**: [2611.08156v2](https://arxiv.org/abs/2611.08156v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.08156v2)
- **作者**: Mateo Clémente, George Z. Xue, Amin Abyaneh et al.
- **发表**: 2026-11-05  ·  **类别**: cs.RO, cs.CV, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: World-action models adapt pretrained video generators, and vision-language-action models build on vision-language backbones, tying policy architecture and inference cost to large transformers designed for generation rather than control. While recent world-action models mostly scale the video backbone and its data, we argue that the choice of latent space is…

## 🌐 具身智能 / 机器人基础模型 (12 篇)

### 1. EmbodyAgent: Post-Training Embodied VLM Agents via Distillation, SFT, and RL

- **arXiv**: [2611.26196v1](https://arxiv.org/abs/2611.26196v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.26196v1)
- **作者**: Wei Dai, Jinkun Liu, Jiayi Chen et al.
- **发表**: 2026-11-19  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Vision-language models (VLMs) can act as closed-loop robot-use agents (RUAs) by writing and executing control code through tool interfaces. However, turning an open-weight VLM into a high-performing embodied agent requires a complete post-training stack: out-of-the-box open VLMs fail completely at interactive tool contracts, strong frontier teachers are acc…

### 2. IncR-3DSGG: Incremental Posed RGB Image Based 3D Scene Graph Generation via Privileged Depth Supervision

- **arXiv**: [2611.15429v1](https://arxiv.org/abs/2611.15429v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.15429v1)
- **作者**: Mrunmai Phatak, Daniel Kienzle, Roman Küble et al.
- **发表**: 2026-11-11  ·  **类别**: cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Scene graphs provide a compact, structured representation of environments by capturing objects and their spatial or semantic relationships in a form suitable for embodied agents. Existing 3D scene graph generation methods often rely on depth sensing at inference, either to associate object instances across views via point cloud overlap or to compute inter-o…

### 3. EvoTER: Evolving Embodied Agents via Tool-Use Experience and Reflection

- **arXiv**: [2611.27797v1](https://arxiv.org/abs/2611.27797v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.27797v1)
- **作者**: Yingting Zhou, Yuyin Zhou, Yongliang Wang et al.
- **发表**: 2026-11-20  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Long-horizon embodied tasks require agents to ground instructions in changing observations, coordinate heterogeneous tools, and recover from failures that can propagate through downstream operations. Although existing LLM-based agents retain experience and refine reusable skills, successful local repairs do not by themselves establish complete-task gains ov…

### 4. ACE-Brain-0.7: Learning Execution-Grounded Reasoning for Embodied Agents

- **arXiv**: [2611.26519v1](https://arxiv.org/abs/2611.26519v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.26519v1)
- **作者**: Yinhe Wang, Shijun Shi, Feng Pan et al.
- **发表**: 2026-11-19  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Reliable reasoning for long-horizon embodied tasks requires predictions grounded in the observed execution state. We present ACE-Brain-0.7, a 9B vision--language model that combines spatial grounding, task understanding, and progress estimation. To train the model, we curate 3.7 million question--answer pairs, drawing execution supervision from egocentric h…

### 5. Pixel2Perspective: A Benchmark for Multi-Modal and Multi-View Generalization in Vision-Language Models

- **arXiv**: [2611.24327v1](https://arxiv.org/abs/2611.24327v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.24327v1)
- **作者**: Aditya Gandhamal, Aniruddh Sikdar, Arya Kishor et al.
- **发表**: 2026-11-18  ·  **类别**: cs.CV
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Embodied AI systems, such as drones and autonomous vehicles, improve navigation by enhancing perception in environments containing unseen objects. While Visual Language Models (VLMs) offer strong image understanding, their real-world application is underexplored. For effective deployment, open-vocabulary semantic segmentation (OVSS) models, leveraging model…

### 6. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 7. Beyond Future Views: Exploring Future-State World Models for Vision-Language Navigation

- **arXiv**: [2611.27418v1](https://arxiv.org/abs/2611.27418v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.27418v1)
- **作者**: Kangyi Wu, Pengna Li, Yucheng Wang et al.
- **发表**: 2026-11-20  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-Language Navigation(VLN) requires an embodied agent to follow language instructions through unseen 3D environments, where the target spaces often lie beyond the current observation. Navigation world models address this challenge by predicting future views either as pixels or latent representations, providing valuable look-ahead information for action…

### 8. Mem-X: A Memory-Dependent Cross-Episode Benchmark for Vision-and-Language Navigation

- **arXiv**: [2611.27166v1](https://arxiv.org/abs/2611.27166v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.27166v1)
- **作者**: Zhikang Shi, Yuk Tung Samuel Fang, Hongyu Ding et al.
- **发表**: 2026-11-20  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Long-term memory enables embodied agents to reuse past observations across tasks. However, existing cross-episode vision-and-language navigation (VLN) benchmarks often leave it unclear whether successful navigation relies on historical memory or current exploration. We introduce Mem-X, a benchmark designed to evaluate memory-dependent cross-episode VLN. Mem…

### 9. Perceive Once, Escalate on Demand: Handing Off Visual KV Memory from Small to Large VLMs

- **arXiv**: [2611.26902v1](https://arxiv.org/abs/2611.26902v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.26902v1)
- **作者**: Qiang Zhou, Jianing Deng, Siyan Dong et al.
- **发表**: 2026-11-19  ·  **类别**: cs.CV, cs.AI, cs.CL
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: An embodied agent cannot afford a large vision-language model (VLM) at every step of a long video, so a cascade runs a small VLM continuously and escalates only uncertain decisions to a large one. Each escalation, however, forces the large model to re-encode a history the small model has already perceived, and this dominates its cost. We present Baton, whic…

### 10. Trajectory-Calibrated Merging of Embodied Policies

- **arXiv**: [2611.25575v1](https://arxiv.org/abs/2611.25575v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.25575v1)
- **作者**: Wenshuo Chen, Honglei Jin, Le Yang et al.
- **发表**: 2026-11-19  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Robot foundation models are increasingly adapted into task specialists to expand their embodied capabilities. Yet these capabilities remain fragmented across separate policies, and existing model-merging methods do not reliably preserve them during closed-loop execution: parameter-space alignment provides only an indirect proxy for behavior, while regressio…

## 🦵 人形 / 足式机器人 (30 篇)

### 1. LocoMuJoCo: A Comprehensive Imitation Learning Benchmark for Whole-Body Control

- **arXiv**: [2611.26293v1](https://arxiv.org/abs/2611.26293v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.26293v1)
- **作者**: Firas Al-Hafez, Davide Tateo, Oleg Kaidanov et al.
- **发表**: 2026-11-19  ·  **类别**: cs.RO
- **相关性评分**: 22  ·  **🔥 read_now**
- **摘要**: LocoMuJoCo is an open-source benchmark for imitation learning (IL) and reinforcement learning (RL) on whole-body control. The library couples MuJoCo (CPU) with MJX and the MjWarp backend (GPU) under a single API, exposes 9 humanoid, 3 (musculo-)skeletal, and 4 quadruped embodiments, and ships a curated native motion-capture dataset for every humanoid, to wh…

### 2. WEVO: World Model-Enabled VLA Optimization for Whole-Body Loco-Manipulation

- **arXiv**: [2611.25251v1](https://arxiv.org/abs/2611.25251v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.25251v1)
- **作者**: Qianzhong Chen, Muyuan Lin, Yuyin Sun et al.
- **发表**: 2026-11-18  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Reinforcement learning (RL) can improve vision-language-action (VLA) policies beyond imitation, but humanoid exploration is unsafe and simulator RL can exploit residual sim-to-real gaps. We present WEVO, a teleoperation-free framework for post-training a whole-body humanoid VLA in an action-conditioned video world model (WM). Simulated manipulation and loco…

### 3. PhyDEX: A Benchmark for Physical Reasoning in Vision-Language-Action Models via Dynamic Extrinsic Dexterity

- **arXiv**: [2611.26565v1](https://arxiv.org/abs/2611.26565v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.26565v1)
- **作者**: Hao Vo, Taisei Hanyu, Yuki Ikebe et al.
- **发表**: 2026-11-19  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models have advanced rapidly in language-conditioned robotic manipulation, yet existing benchmarks mainly evaluate gripper--object contact and largely ignore how objects interact with the environment through gravity, friction, inertia, and mass distribution. As a result, it remains unclear whether current policies truly understa…

### 4. ECHO: In-Context Behavior foundation model for Humanoid Whole-Body Control

- **arXiv**: [2611.25778v1](https://arxiv.org/abs/2611.25778v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.25778v1)
- **作者**: Xingyi Wang, Bin Li, Jiyuan Shi et al.
- **发表**: 2026-11-19  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Humanoid behavior foundation models (BFMs) acquire diverse skills through large-scale motion imitation and massively parallel reinforcement learning, yet broad behavioral capability does not ensure precise execution across physical conditions. Without distinguishing the underlying dynamics, policies may favor conservative compromises over environment-specif…

### 5. MoViC: Real-Time Humanoid Whole-Body Control from Monocular Video Streams

- **arXiv**: [2611.19998v1](https://arxiv.org/abs/2611.19998v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.19998v1)
- **作者**: Yimin Han, Jiahui Zhang, Wanyue Li et al.
- **发表**: 2026-11-15  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Real-time whole-body imitation from monocular video requires both a robust universal tracker and high-quality real-time reconstruction. We present MoViC, a framework that uses live RGB video as a control signal for humanoid robots without wearable tracking devices. The framework combines monocular human motion reconstruction, robot retargeting, and a transf…

### 6. From Tabletop to Walking Bot: Deploying a VLA Model on a Legged Manipulator Robot

- **arXiv**: [2610.32271v1](https://arxiv.org/abs/2610.32271v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.32271v1)
- **作者**: Giovanni Minelli, Antonio Langella, Giovanni B. Dessy et al.
- **发表**: 2026-10-23  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models are typically pretrained on broad, diverse datasets and subsequently fine-tuned on a comparatively small dataset tailored to a specific target robot. Such adaptation recipe is now widely established, achieving its most mature results on fixed-base arms due to their static base dynamics and consistent reference frame. Moun…

### 7. PGX: Physically Grounded Execution for Long-Horizon Humanoid Loco-Manipulation

- **arXiv**: [2611.26596v1](https://arxiv.org/abs/2611.26596v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.26596v1)
- **作者**: Kai Lu, Chenyang Ma, Ioannis Havoutis
- **发表**: 2026-11-19  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Robotic vision-language-action (VLA) models can execute diverse individual manipulation skills, yet they still struggle with long-horizon loco-manipulation tasks, where temporal structure, skills, and precision are tightly coupled within a monolithic model. We propose Physically Grounded Execution (PGX), a framework that offloads temporal and precision cont…

### 8. Driving the Style: Velocity-Conditioned Whole-Body Control from Motion Demonstrations

- **arXiv**: [2611.20888v1](https://arxiv.org/abs/2611.20888v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.20888v1)
- **作者**: Murad Dawood, Oezge Drama Berkenkamp, Antonio Gonzales Marin et al.
- **发表**: 2026-11-16  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Achieving human-like behavior on humanoid robots has advanced rapidly by leveraging motion-capture demonstrations rather than hand-crafted cost functions. Adversarial imitation supplies a style signal that lets a policy fulfill a task while adhering to a desired style, but is difficult to transfer to hardware. Whole-body tracking through reinforcement learn…

### 9. PERA: Plug-in Experts for Robotic Actions in Continual Whole-Body Control

- **arXiv**: [2611.16188v1](https://arxiv.org/abs/2611.16188v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.16188v1)
- **作者**: Shangchao Hu, Yadan Sun, Xibo Yu et al.
- **发表**: 2026-11-12  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Motion imitation enables humanoid robots to acquire whole-body skills such as walking and dancing. However, fine-tuning an entire policy for a new skill can affect existing behaviors, while training a separate policy for each skill increases training and maintenance costs. We present PERA, a method for learning new skills by reusing existing motion capabili…

### 10. OccluDex: Hierarchical 3D Visuo-Tactile Representation Learning for Egocentric Dexterous Manipulation under Self-Occlusion

- **arXiv**: [2609.39017v1](https://arxiv.org/abs/2609.39017v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39017v1)
- **作者**: Ziheng Xu, Yueyuan Chen, Xinyuan He et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Reliable dexterous manipulation requires continuous estimation of object geometry and hand-object contact throughout interaction. With egocentric sensing, however, the manipulating hand frequently occludes task-relevant object surfaces and contact regions, reducing the visual evidence available for state estimation and thereby making robust closed-loop cont…

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

### 3. TactileLab: Sim-to-Real Dexterous Robot Manipulation with Efficient Shear-Sensitive Tactile Simulation

- **arXiv**: [2611.07881v1](https://arxiv.org/abs/2611.07881v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.07881v1)
- **作者**: Yijiong Lin, Wenhao He, Toby Jack et al.
- **发表**: 2026-11-05  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Robotic simulators that represent shear within tactile sensing are becoming increasingly important for contact-rich manipulation. However, simulating contact shear with high-fidelity deformable or soft-body simulation is computationally demanding, limiting scalability to large-scale reinforcement learning. Here we introduce \textit{TactileLab}, a scalable m…

### 4. FoRe: A Force-Guided Framework for Autonomous Grasp Recovery in Vision-Language-Action Models

- **arXiv**: [2611.27011v1](https://arxiv.org/abs/2611.27011v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.27011v1)
- **作者**: Shuai Peng, Yongkai Liao, Yuxin Cheng et al.
- **发表**: 2026-11-20  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models have demonstrated strong performance in grasp-based manipulation, yet reliable recovery from local grasping failures remains challenging. Specifically, in pick-and-place tasks, policies may continue transport after a failed grasp instead of retrying, potentially reflecting overreliance on proprioceptive cues for stage pro…

### 5. SoTa: Soft Tactile Skins for Dexterous Manipulation

- **arXiv**: [2610.02338v1](https://arxiv.org/abs/2610.02338v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.02338v1)
- **作者**: Jingyun Yang, Baiyu Shi, Timothy Yu et al.
- **发表**: 2026-10-01  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: A growing body of work suggests that tactile sensing gives robot policies contact information that complements vision in dexterous manipulation. However, visuo-tactile robot data remains scarce: dexterous demonstrations require teleoperating robots, which limits dataset scale. Human demonstrations are far cheaper to collect and offer a path to scale this da…

### 6. SHAPE: Discrete Supervision and Parallel Continuous Streams for Learning Dexterous Manipulation from Egocentric Human Data

- **arXiv**: [2611.24585v1](https://arxiv.org/abs/2611.24585v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.24585v1)
- **作者**: Yaping Li, Zhihong Liu, Jiacheng Li et al.
- **发表**: 2026-11-18  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Egocentric human recordings are far cheaper than dexterous robot demonstrations, promising stronger pretraining and direct skill learning without task-specific robot data. Yet humans and robots differ in morphology and kinematics, so human recordings lack the joint positions and actuator commands that supervise robot policies, providing only retargeted end-…

### 7. RoboDyna: A Benchmark for Evaluating Robotic Manipulation under Physically Grounded Dynamics

- **arXiv**: [2611.26969v1](https://arxiv.org/abs/2611.26969v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.26969v1)
- **作者**: Zhiyuan Li, Rui Heng Yang, Xuan Zhao et al.
- **发表**: 2026-11-20  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Object manipulation in the dynamic real world requires understanding how the environment functions and evolves, and acting accordingly. Existing benchmarks, however, do not adequately address these needs. Physics-oriented benchmarks evaluate predictive fidelity but not closed-loop action. Dynamic robotic manipulation benchmarks often use simplified, physica…

### 8. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

### 9. TipDex-VTLA: Learning When to Refine Actions with Touch for Dexterous Manipulation

- **arXiv**: [2611.25683v1](https://arxiv.org/abs/2611.25683v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.25683v1)
- **作者**: Xudi Ge, Yepeng Liu, Haifeng Liu et al.
- **发表**: 2026-11-19  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Changes in illumination can induce action drift in dexterous manipulation even when the physical state remains unchanged. Although existing vision--tactile--language--action (VTLA) policies incorporate tactile feedback, when and how touch refines actions under changing visual conditions remains challenging. We introduce \textbf{TipDex-VTLA}, a VTLA policy t…

### 10. A$^2$-VLA: Adapting Vision-Language-Action Policies to New Tools through Agentic Affordance Discovery

- **arXiv**: [2611.25656v1](https://arxiv.org/abs/2611.25656v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.25656v1)
- **作者**: Chenyuan Zhou, Chaoyi Huang, Zibo Wang et al.
- **发表**: 2026-11-19  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Tools with different shapes can have similar functions, but transferring manipulation skills across tools requires understanding how tool geometry relates to the specific task and adjusting the manipulation strategy accordingly. The key challenge is to discover the common affordances that contribute to task completion across different tools and verify wheth…

## 🎓 模仿学习 / 强化学习 (14 篇)

### 1. EyeDiT: Anatomy-Grounded Multi-Modal Eye Generation and Simulation

- **arXiv**: [2611.23670v1](https://arxiv.org/abs/2611.23670v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.23670v1)
- **作者**: Yonghan Lee, Zachary Willms, Kun Liu et al.
- **发表**: 2026-11-18  ·  **类别**: cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Synthetic eye data are critical for rapid development of eye tracking (ET) in AR/VR applications. However, existing synthetic eye generators are largely image-centric and lack a high-quality underlying 3D anatomy of the eye, which limits their control mainly to the gaze and provides no anatomical labels. To address this problem, we propose EyeDiT, an anatom…

### 2. Bracketing Shows the Way: Adaptive Multi-Exposure Policy as Input for Robust Visual SLAM

- **arXiv**: [2610.33174v1](https://arxiv.org/abs/2610.33174v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.33174v1)
- **作者**: Olivier Gamache, Anthony Lavertu, David-Alexandre Duclos et al.
- **发表**: 2026-10-23  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Rapid illumination transitions can disturb Visual SLAM (VSLAM) by saturating images before the Automatic Exposure (AE) policy adapts, removing the visual correspondences needed to maintain tracking. Our proposed methods mitigate this disturbance at two levels: B-Adapt acquires adaptive exposure brackets to cover the scene dynamic range while promoting photo…

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

### 2. Fixing the Twin, Not the Detector: Sim-to-Real Roadside LiDAR Detection from Digital-Twin Data

- **arXiv**: [2611.26035v1](https://arxiv.org/abs/2611.26035v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.26035v1)
- **作者**: KuanLin Chen, Feng-jui Kuo
- **发表**: 2026-11-19  ·  **类别**: cs.CV, cs.LG
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Roadside LiDAR detectors are expensive to train on real labels, and digital twins promise to replace these labels, but a detector trained on a twin meets a different sensor, different objects and different annotation conventions on the real site. We describe the pipeline that placed first in the LUMPI track of the UrbanTwin Sim2Real LiDAR Challenge (IEEE Bi…

### 3. Spade-SLAM: Sparse Correspondence Anchors for Dense Self-Supervised Visual SLAM

- **arXiv**: [2611.01937v1](https://arxiv.org/abs/2611.01937v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.01937v1)
- **作者**: Julian Philipp Schmitt, Weirong Chen, Ganlin Zhang et al.
- **发表**: 2026-11-01  ·  **类别**: cs.CV
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: We introduce Spade-SLAM, a self-supervised dense visual SLAM framework that substantially narrows the long-standing performance gap to supervised methods in a zero-shot setting. By demonstrating that high-fidelity tracking can be achieved without explicit ground-truth pose and depth labels, our approach offers a highly effective and label-efficient alternat…

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
- **相关性评分**: 7  ·  **👀 watch**
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

## 🧭 导航 / 路径规划 (1 篇)

### 1. Accuracy potential of visual localization exploiting high-end street-level imagery

- **arXiv**: [2607.24409v2](https://arxiv.org/abs/2607.24409v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.24409v2)
- **作者**: Jonas Meyer, Stephan Nebiker, Pascal Theiler et al.
- **发表**: 2026-07-27  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Many applications, such as surveying, autonomous navigation, robotics and augmented reality, require accurate pose information with respect to a reference frame. Visual localization can complement GNSS positioning, whose availability and accuracy are often limited. However, the accuracy potential of visual localization has not yet been systematically invest…

## 🧪 仿真 / Sim2Real (1 篇)

### 1. Domain-Aware Conformal Prediction for Trustworthy Spacecraft Pose Estimation under Sim-to-Real Shift

- **arXiv**: [2611.26065v1](https://arxiv.org/abs/2611.26065v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.26065v1)
- **作者**: Nidhal Eddine Chenni, Arunkumar Rathinam, Djamila Aouada
- **发表**: 2026-11-19  ·  **类别**: cs.CV
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Autonomous rendezvous and proximity operations require not only an accurate estimate of the pose of the target spacecraft, but also a reliable indication of when this estimate can be trusted. Conformal prediction provides such an indication with a formal guarantee, by producing pose uncertainty sets that contain the true pose with a specified probability. S…

## 🤏 软体机器人 / 柔性控制 (6 篇)

### 1. Ferrofluid Shape Control with Deep Reinforcement Learning

- **arXiv**: [2611.25232v1](https://arxiv.org/abs/2611.25232v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.25232v1)
- **作者**: Anthony Czubarow, Antonio Terpin, Raffaello D'Andrea
- **发表**: 2026-11-18  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Ferrofluids are liquids containing magnetic nanoparticles, enabling shape control through external magnetic fields. This deformability supports their use as soft robotic bodies that can navigate confined spaces and manipulate objects. Their nonlinear continuum dynamics, however, make reliable control challenging. Existing work shows how spatial magnetic fie…

### 2. PneuGen: Task-Driven Agentic Co-Design of Soft Pneumatic Robots

- **arXiv**: [2611.13344v1](https://arxiv.org/abs/2611.13344v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.13344v1)
- **作者**: Shaohong Zhong, Marco Pontin, Perla Maiolino
- **发表**: 2026-11-09  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Task-driven design of soft robots requires the consideration of factors such as geometry, morphology, material properties, and actuation, resulting in a large and complex design space that is challenging to explore. Computational optimisation methods leverage signals from simulation to iteratively improve designs to achieve task objectives. However, these m…

### 3. Accelerated Reinforcement Learning for Soft Robotics: Hours Instead of Years

- **arXiv**: [2611.11718v1](https://arxiv.org/abs/2611.11718v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.11718v1)
- **作者**: Roshan S. Kaundinya, Hehui Zheng, Robert K. Katzschmann et al.
- **发表**: 2026-11-09  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Reinforcement learning (RL) requires large amounts of interaction data or a reliable simulator, both hard to obtain for nonlinear soft robotic hardware. Recent work shows that a time-scale separation inherent to soft robot dynamics justifies their reduction to low-dimensional invariant manifolds, known as adiabatic spectral submanifolds (aSSMs). We demonstr…

### 4. Actuation and Control of Passive Tendon-Driven Soft Extensions Through Rigid Manipulator Motion

- **arXiv**: [2611.15386v1](https://arxiv.org/abs/2611.15386v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.15386v1)
- **作者**: Ignacio Cuiral-Zueco, Gonzalo López-Nicolás, Youcef Mezouar
- **发表**: 2026-11-11  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Industrial manipulators offer reach and precision but can damage nearby structures in confined spaces. Soft robots provide compliant contact but typically have limited reach. Rigid-soft systems combine their advantages, although they often require dedicated actuation and control hardware. We propose actuating a passive tendon-driven soft extension through m…

### 5. SunLightBots: Turning sunlight into self-sustained, high-power motion in soft robots

- **arXiv**: [2611.14729v1](https://arxiv.org/abs/2611.14729v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2611.14729v1)
- **作者**: Yoo Jin Lee, Melanie Torres Crespo, Zhongxiao Deng et al.
- **发表**: 2026-11-10  ·  **类别**: cs.RO, cond-mat.soft, physics.app-ph
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Soft robots built from active materials can directly convert environmental stimuli into motion, offering a route to energy autonomy and embodied control. However, environmental energy is generally harvested at low power, whereas rapid, mechanically demanding actions require high mechanical output power. Reconciling this mismatch while sustaining self-regula…

### 6. DeepSoMo: Deformable Object Motion Estimation under Proprioceptive Partial Observability via Predictive Latent Dynamics

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
3. [LocoMuJoCo: A Comprehensive Imitation Learning Benchmark for Whole-Body Control](https://arxiv.org/abs/2611.26293v1) — score 22

> 筛选说明:本次 Top 3 已排除(已研读跳过 1 篇、综述跳过 1 篇)。

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
