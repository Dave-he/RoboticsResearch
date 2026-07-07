# 机器人研究每日摘要 · 2026-06-11

> 自动生成,共 89 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (6 篇)

### 1. A Practical Recipe Towards Improving Sim-and-Real Correlation for VLA Evaluation

- **arXiv**: [2606.10366v1](https://arxiv.org/abs/2606.10366v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.10366v1)
- **作者**: Shuo Wang, Hanyuan Xu, Yingdong Hu et al.
- **发表**: 2026-06-09  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Simulation has become an essential tool for evaluating and improving vision-language-action (VLA) policies, offering scalable, reproducible, and controllable alternatives to costly real-world robot evaluation. Recent simulation benchmarks have made substantial progress on realism and diversity, yet these platforms have not been widely adopted as reliable pr…

### 2. Robots Need More than VLA and World Models

- **arXiv**: [2606.06556v1](https://arxiv.org/abs/2606.06556v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.06556v1)
- **作者**: Elis Karcini, Faisal Mehrban, Quang Nguyen et al.
- **发表**: 2026-06-04  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Generalist robot intelligence is often framed as a policy-scaling problem: collect more robot demonstrations, train larger Vision-Language-Action (VLA) models, and expect broader generalisation. In this position paper, we argue that this framing is incomplete. The central bottleneck is not only policy learning, but the absence of mechanisms that convert the…

### 3. VLGA: Vision-Language-Geometry-Action Models for Autonomous Driving

- **arXiv**: [2606.12396v1](https://arxiv.org/abs/2606.12396v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.12396v1)
- **作者**: Jin Yao, Dhruva Dixith Kurra, Tom Lampo et al.
- **发表**: 2026-06-10  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-language-action (VLA) models can describe scenes and reason about them in language, yet still struggle to ground their actions in the dense 3D world around them. Existing approaches either inject features from a frozen 3D foundation model without an objective that ensures the policy uses them, or constrain geometry with sparse box and map losses that…

### 4. CHORUS: Decentralized Multi-Embodiment Collaboration with One VLA Policy

- **arXiv**: [2606.12352v1](https://arxiv.org/abs/2606.12352v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.12352v1)
- **作者**: Ria Doshi, Tian Gao, Annie Chen et al.
- **发表**: 2026-06-10  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Multi-robot collaboration allows robots to efficiently take on a wide range of tasks, from moving a couch through a doorway to assembling structures on a construction site. However, achieving such coordination in mobile multi-robot settings remains challenging: centralized methods conditioned on the combined observations of a team scale poorly with team siz…

### 5. Learning What to Say to Your VLA: Mostly Harmless Vision Language Action Model Steering

- **arXiv**: [2606.12299v1](https://arxiv.org/abs/2606.12299v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.12299v1)
- **作者**: Hyun Joe Jeong, Gokul Swamy, Andrea Bajcsy
- **发表**: 2026-06-10  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-Language-Action (VLA) models provide a natural language interface to robot control, but the mapping from language to behavior is often brittle and unintuitive: semantically similar instructions can induce drastically different behaviors, while some capabilities may not be elicitable through prompting alone. As a result, both human instructions and ze…

### 6. Silent Failures in Physical AI: A Literature Review of Runtime Action Authorization for Autonomous Systems

- **arXiv**: [2606.00090v1](https://arxiv.org/abs/2606.00090v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.00090v1)
- **作者**: Barak Or
- **发表**: 2026-05-23  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Physical AI systems increasingly map multimodal observations, language instructions, and learned world representations into physically consequential actions. Robotics foundation models, vision-language-action models, and world-model-based autonomous systems can condition decisions that move vehicles, robots, drones, and industrial machines. This transition…

## 🌐 具身智能 / 机器人基础模型 (6 篇)

### 1. ABot-Earth 0.5: Generative 3D Earth Model

- **arXiv**: [2606.09967v1](https://arxiv.org/abs/2606.09967v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.09967v1)
- **作者**: Ming Qian, Tianjian Ouyang, Mingchao Sun et al.
- **发表**: 2026-06-08  ·  **类别**: cs.CV
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: We present ABot-Earth 0.5, a generative 3D framework designed to synthesize vast, seamless 3D environments from ubiquitous, geospatially referenced satellite imagery. To achieve this, we propose a novel generative model formulated directly with the 3D Gaussian Splatting (3DGS) representation. The model is trained on a diverse corpus of existing real-world u…

### 2. ScaRF-SLAM: Scale-Consistent Reconstruction with Feed-Forward Models and Classical Visual SLAM

- **arXiv**: [2606.00307v1](https://arxiv.org/abs/2606.00307v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.00307v1)
- **作者**: Yuhao Zhang, Yifu Tao, Frank Dellaert et al.
- **发表**: 2026-05-29  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Recent works have explored unifying SLAM with geometric foundation models (GFMs). However, directly using GFM predictions for tracking is highly sensitive to model capability and uncertainty, as geometric inaccuracies in the predictions can adversely affect pose estimation. To address this limitation, we present a decoupled framework that integrates classic…

### 3. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 4. Efficient Skill Grounding via Code Refactoring with Small Language Models

- **arXiv**: [2606.07999v1](https://arxiv.org/abs/2606.07999v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.07999v1)
- **作者**: Sera Choi, Wonje Choi, Saehun Chun et al.
- **发表**: 2026-06-06  ·  **类别**: cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Effective skill grounding is essential for deploying reusable skills in embodied agents, as even minor embodiment or environmental differences can render an entire skill incompatible. This challenge is particularly pronounced in embodied settings, where agents must operate in dynamic, partially observable environments without access to large language models…

### 5. A 3D Isovist World Model -- Revealing a City's Unseen Geometry and Its Emergent Cross-City Signature

- **arXiv**: [2606.03609v2](https://arxiv.org/abs/2606.03609v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.03609v2)
- **作者**: Xuhui Lin, Stephen Law, Nanjiang Chen et al.
- **发表**: 2026-06-02  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Embodied agents that navigate cities rely on world models that predict how their surroundings will change as they move. But for navigation, what matters is not what the buildings look like; it is where the agent can go. Most world models nonetheless predict appearance, learning how a scene looks rather than the space an agent can move through. Those that do…

### 6. VASO: Formally Verifiable Self-Evolving Skills for Physical AI Agents

- **arXiv**: [2606.05395v1](https://arxiv.org/abs/2606.05395v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.05395v1)
- **作者**: Yunhao Yang, Neel P. Bhatt, Kevin Wang et al.
- **发表**: 2026-06-03  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Reusable robot skills are becoming the basic units through which embodied agents turn open-ended instructions into long-horizon physical behavior. We argue that, while foundation models have collapsed the cost of creating these skills, the cost of trusting them has not. Existing skill-evolution loops refine skills through execution feedback, unit tests, env…

## 🦵 人形 / 足式机器人 (25 篇)

### 1. X2-N: A Transformable Wheel-legged Humanoid Robot with Dual-mode Locomotion and Manipulation

- **arXiv**: [2604.21541v1](https://arxiv.org/abs/2604.21541v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2604.21541v1)
- **作者**: Yan Ning, Xingzhou Chen, Delong Li et al.
- **发表**: 2026-04-23  ·  **类别**: cs.RO
- **相关性评分**: 20  ·  **🔥 read_now**
- **摘要**: Wheel-legged robots combine the efficiency of wheeled locomotion with the versatility of legged systems, enabling rapid traversal over both continuous and discrete terrains. However, conventional designs typically employ fixed wheels as feet and limited degrees of freedom (DoFs) at the hips, resulting in reduced stability and mobility during legged locomoti…

### 2. PRIME: Physically-consistent Robotic Inertial and Motion Estimation for Legged and Humanoid Robots

- **arXiv**: [2605.17681v1](https://arxiv.org/abs/2605.17681v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2605.17681v1)
- **作者**: Jiarong Kang, Kunzhao Ren, Tao Pang et al.
- **发表**: 2026-05-17  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Humanoid and legged robots interact with the environment through intermittent contacts, making accurate motion estimation fundamentally dependent on reasoning about contact dynamics. However, standard sensing pipelines-whether based on onboard proprioception with Extended Kalman Filters (EKFs) or external motion capture systems-recover only kinematics, whil…

### 3. Critic Architecture Matters: Dual vs. Unified Critics for Humanoid Loco-Manipulation

- **arXiv**: [2606.11891v1](https://arxiv.org/abs/2606.11891v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.11891v1)
- **作者**: Mehmet Turan Yardımcı
- **发表**: 2026-06-10  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Multi-objective reinforcement learning for humanoid robots must coordinate locomotion and manipulation within a single policy. A natural design choice is whether to use a single (unified) critic that estimates the combined value of all objectives, or separate (dual) critics with disjoint reward signals. We present a controlled comparison on the Unitree G1 h…

### 4. Learning Object Manipulation from Scratch via Contrastive Interaction

- **arXiv**: [2606.11525v1](https://arxiv.org/abs/2606.11525v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.11525v1)
- **作者**: Tongle Shen, Caleb Chuck, Fan Feng et al.
- **发表**: 2026-06-10  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Contrastive Reinforcement Learning (CRL) has seen recent success in a wide variety of goal-conditioned robotics tasks by learning structured representations of the dynamics. However, despite its success in locomotion and simpler control domains, CRL often struggles in interaction-rich manipulation. We argue that a key source of this difficulty is object-cen…

### 5. EM-Fall: Embodied mmWave Sensing for Day-and-Night Fall Detection on Humanoid Robots

- **arXiv**: [2606.11109v1](https://arxiv.org/abs/2606.11109v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.11109v1)
- **作者**: Yanshuo Lu, Yuxuan Hu, Shenghai Yuan et al.
- **发表**: 2026-06-09  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Falls are one of the leading causes of injury and hospitalization among elderly individuals, making reliable fall awareness an essential capability for safety monitoring in residential environments. However, existing fall detection systems often rely on wearable devices or fixed sensing installations, which may suffer from low user compliance, limited spati…

### 6. OMG: Omni-Modal Motion Generation for Generalist Humanoid Control

- **arXiv**: [2606.10340v1](https://arxiv.org/abs/2606.10340v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.10340v1)
- **作者**: Siqiao Huang, Kun-Ying Lee, Dongming Qiao et al.
- **发表**: 2026-06-09  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Humanoid whole-body control has made significant progress in recent years, yet existing approaches remain limited to few-skill policies with heavy reward engineering, or motion trackers that are difficult to extend to new input modalities. We argue that the key to general-purpose humanoid control is to build a scalable brain, a module capable of reasoning w…

### 7. HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers

- **arXiv**: [2606.06493v3](https://arxiv.org/abs/2606.06493v3)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.06493v3)
- **作者**: Lizhi Yang, Junheng Li, Nehar Poddar et al.
- **发表**: 2026-06-04  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: For a humanoid robot to be deployed in the real world, the choice of command space (i.e., the interface between task planning and whole-body control) is crucial. Existing whole-body controllers typically demand dense kinematic or spatial references that planners struggle to synthesize from task semantics. We instead propose a compact, explicit interface tha…

### 8. M3imic: Learning a Versatile Whole-Body Controller for Multimodal Motion Mimicking

- **arXiv**: [2606.04829v1](https://arxiv.org/abs/2606.04829v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.04829v1)
- **作者**: Zuxing Lu, Ziang Zheng, Yao Lyu et al.
- **发表**: 2026-06-03  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Building a general-purpose whole-body controller is essential for enabling diverse motion capabilities in humanoid robots across a wide range of downstream tasks, including locomotion and loco-manipulation. Different tasks rely on distinct motion reference modalities: locomotion primarily depends on coordinated robot joint trajectories, whereas manipulation…

### 9. X-OP: Cross-Morphology Whole-Body Teleoperation via MPC Retargeting

- **arXiv**: [2606.07934v1](https://arxiv.org/abs/2606.07934v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.07934v1)
- **作者**: Jen-Wei Wang, Sarthak Kaingade, Andrea Tagliabue et al.
- **发表**: 2026-06-06  ·  **类别**: cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Whole-body teleoperation is essential for scalable robot data collection in loco-manipulation tasks, yet existing approaches relying on exoskeleton suits or multi-camera setups impose prohibitive cost, complexity, and environmental constraints. Recent methods using a single extended reality (XR) device with end-to-end reinforcement learning policies partial…

### 10. Bionic Human-Motion Style Transfer for Physically Executable Whole-Body Control of Humanoid Robots

- **arXiv**: [2606.03536v1](https://arxiv.org/abs/2606.03536v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.03536v1)
- **作者**: Tianchen Huang, Mingkuan Zhao, Yang Gao et al.
- **发表**: 2026-06-02  ·  **类别**: cs.RO
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Expressive whole-body motion is important for humanoid robots operating in human environments, where robots are expected to move stably while presenting readable and adjustable body behaviors. However, most expressive motions are still obtained from fixed demonstrations or manually designed scripts, making it difficult to reuse a demonstrated style across d…

## 🦾 操控 / 灵巧手 / 抓取 (32 篇)

### 1. Blind Dexterous Grasping via Real2Sim2Real Tactile Policy Learning

- **arXiv**: [2606.11767v1](https://arxiv.org/abs/2606.11767v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.11767v1)
- **作者**: Shengcheng Luo, Xiyan Huang, Zhe Xu et al.
- **发表**: 2026-06-10  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 26  ·  **🔥 read_now**
- **摘要**: Blind grasping with a dexterous hand is a crucial manipulation capability. Nevertheless, learning such tactile-only policies for real robots remains challenging due to the tactile sim-to-real gap and the limited expressiveness of sparse tactile signals. To bridge this gap, we propose a framework for tactile-only blind grasping that is deployable on a physic…

### 2. Bridging the Morphology Gap: Adapting VLA Models to Dexterous Manipulation via Intent-Conditioned Fine-Tuning

- **arXiv**: [2606.12109v1](https://arxiv.org/abs/2606.12109v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.12109v1)
- **作者**: Chuanke Pang, Junyi Huang, Zhijun Zhao et al.
- **发表**: 2026-06-10  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 24  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models have demonstrated remarkable zero-shot generalization in robotic manipulation, yet the vast majority of pre-trained pipelines remain strictly confined to low-DoF parallel grippers. Adapting these rich semantic priors to high-DoF dexterous hands introduces a severe morphology gap, direct end-to-end joint fine-tuning inhere…

### 3. RGB-S: Image-Aligned Tactile Saliency for Robust Dexterous Manipulation

- **arXiv**: [2606.08765v1](https://arxiv.org/abs/2606.08765v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.08765v1)
- **作者**: Shengcheng Luo, Kefei Wu, Xiaoying Zhou et al.
- **发表**: 2026-06-07  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Effective visuo-tactile integration is critical for robotic dexterous manipulation, especially when visual observations are unreliable or occluded. However, robustly aligning sparse, heterogeneous tactile measurements with dense visual representations remains a fundamental challenge. Most existing approaches require policies to learn cross-modal corresponde…

### 4. MoDex: A Diffusion Policy for Sequential Multi-Object Dexterous Grasping

- **arXiv**: [2606.05407v1](https://arxiv.org/abs/2606.05407v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.05407v1)
- **作者**: Haofei Lu, Hongjia Liu, Yifei Dong et al.
- **发表**: 2026-06-03  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: This work addresses sequentially grasping multiple objects with a single dexterous hand without releasing those already held. Most dexterous grasping methods commit all of the hand's degrees of freedom to a single object, underutilizing its dexterity and leaving no redundancy for subsequent grasps. The proposed solution, MoDex, is a diffusion policy that pr…

### 5. APT: Action Expert Pretraining Improves Instruction Generalization of Vision-Language-Action Policies

- **arXiv**: [2606.12366v1](https://arxiv.org/abs/2606.12366v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.12366v1)
- **作者**: Kechun Xu, Zhenjie Zhu, Anzhe Chen et al.
- **发表**: 2026-06-10  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models that couple pretrained Vision-Language Models (VLMs) with continuous action experts have achieved strong manipulation performance, yet generalization to out-of-distribution (OOD) language instructions remains poor. A known challenge is the structural imbalance in VLA data, where language is far less diverse than visual an…

### 6. DuoBench: A Reproducible Benchmark for Bimanual Manipulation in Simulation and the Real World

- **arXiv**: [2606.11901v1](https://arxiv.org/abs/2606.11901v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.11901v1)
- **作者**: Tobias Jülg, Seongjin Bien, Simon Hilber et al.
- **发表**: 2026-06-10  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Bimanual robot systems substantially expand manipulation capabilities, but coordinating two arms introduces additional control complexity and failure modes that are not well captured by existing benchmarks. We introduce DuoBench, an extensible benchmarking framework for bimanual manipulation policies on the FR3 Duo platform. DuoBench comprises eleven tasks…

### 7. Dexterous Point Policy: Learning Point-based Dexterous Hand Policies from Human Demonstrations

- **arXiv**: [2606.10614v1](https://arxiv.org/abs/2606.10614v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.10614v1)
- **作者**: Beomjun Kim, Seong Hyeon Park, Seunghoon Sim et al.
- **发表**: 2026-06-09  ·  **类别**: cs.RO, cs.CV, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Robotic foundation models pre-trained on human demonstration videos have shown promise, but a significant embodiment gap remains when the resulting policies are deployed on real robots. A common remedy is to fine-tune these models on robot-specific demonstrations. However, robot data collection can be prohibitively expensive and time-consuming, which is par…

### 8. YUBI: Yielding Universal Bidigital Interface for Bimanual Dexterous Manipulation at Scale

- **arXiv**: [2606.10244v1](https://arxiv.org/abs/2606.10244v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.10244v1)
- **作者**: Takehiko Ohkawa, Jumpei Arima, Yuki Noguchi et al.
- **发表**: 2026-06-08  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce Yielding Universal Bidigital Interface (YUBI), a finger-aligned gripper designed to enable intuitive, ergonomic, and scalable data collection for bimanual dexterous manipulation. While handheld data collection systems such as Universal Manipulation Interface (UMI) enable affordable data collection, their bulky pistol-grip designs can pose ergon…

### 9. DexPIE: Stable Dexterous Policy Improvement from Real-World Experience

- **arXiv**: [2606.09615v1](https://arxiv.org/abs/2606.09615v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.09615v1)
- **作者**: Ruizhe Liao, Wenrui Chen, Liangji Zeng et al.
- **发表**: 2026-06-08  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation presents substantial challenges for imitation learning due to its high-dimensional action space and complex contact-rich dynamics. Policies trained purely from demonstrations often suffer from compounding errors during deployment and require large amounts of expert data to achieve reliable performance. To move beyond the limitations o…

### 10. RealDexUMI: A Wearable Universal Manipulation Interface for Dexterous Robot Learning

- **arXiv**: [2606.06033v2](https://arxiv.org/abs/2606.06033v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.06033v2)
- **作者**: Chaoyi Xu, Yixuan Jiang, Jiahui Huan et al.
- **发表**: 2026-06-04  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Learning dexterous manipulation requires demonstrations that preserve fine hand-object interactions while remaining executable at deployment. Existing pipelines either lose deployable dexterity through retargeting or embodiment conversion, or rely on robot-specific teleoperation that is costly to scale and often lacks intuitive, contact-aware control for de…

## 🎓 模仿学习 / 强化学习 (13 篇)

### 1. Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics

- **arXiv**: [2606.12365v1](https://arxiv.org/abs/2606.12365v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.12365v1)
- **作者**: Adam Wei, Nicholas Pfaff, Thomas Cohn et al.
- **发表**: 2026-06-10  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We propose Ambient Diffusion Policy, a simple and principled method for imitation learning from suboptimal data in robotics. High-quality, task-specific robot data is expensive and time-consuming to collect, while suboptimal datasets with lower-quality or out-of-distribution demonstrations are abundant. Existing methods that co-train on both data sources in…

### 2. Bridging the sim2real gap in the table tennis robot with a transformer-based ball states predictor

- **arXiv**: [2606.11464v1](https://arxiv.org/abs/2606.11464v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.11464v1)
- **作者**: Yin Bi, Christian Conti, Bilan Yang et al.
- **发表**: 2026-06-09  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Robotic table tennis is a representative benchmark for high-speed, closed-loop robotic control in dynamic environments, where accurate and fast prediction of ball states is critical for reliable planning and control. Physics-based approaches rely heavily on accurate parameter identification and precise initial state, while learning-based methods often strug…

### 3. KinematicRL: A Sim-to-Real Reinforcement Learning Framework For Social Navigation With Kinodynamic Feasibility

- **arXiv**: [2606.12042v1](https://arxiv.org/abs/2606.12042v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.12042v1)
- **作者**: Zhiming Xu, Haodong Yang, Chengju Liu et al.
- **发表**: 2026-06-10  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Deep Reinforcement Learning (DRL) has shown promise for social navigation, yet its real-world deployment remains hindered by a persistent sim-to-real gap arising from simplified first-order dynamics and context-specific human state estimation pipelines. This work presents a unified framework that addresses these limitations to produce dynamically feasible n…

### 4. From Simulation to Real-World: An In-Field 6D Pose Dataset and Baseline for Robotic Strawberry Harvesting

- **arXiv**: [2606.11381v1](https://arxiv.org/abs/2606.11381v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.11381v1)
- **作者**: Woojung Son, Won Suk Lee, Zijing Huang et al.
- **发表**: 2026-06-09  ·  **类别**: cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Robotic strawberry harvesting requires precise 6D pose estimation; however, collecting 6D pose ground truth in real agricultural fields is inherently challenging. Existing 6D pose estimation methods have therefore relied solely on synthetic data that lacks scene-level realism, leaving their performance under real agricultural field conditions unquantified.…

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

### 7. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

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

### 10. Dual Pose-Graph Semantic Localization for Vision-Based Autonomous Drone Racing

- **arXiv**: [2604.15168v1](https://arxiv.org/abs/2604.15168v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2604.15168v1)
- **作者**: David Perez-Saura, Miguel Fernandez-Cortizas, Alvaro J. Gaona et al.
- **发表**: 2026-04-16  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Autonomous drone racing demands robust real-time localization under extreme conditions: high-speed flight, aggressive maneuvers, and payload-constrained platforms that often rely on a single camera for perception. Existing visual SLAM systems, while effective in general scenarios, struggle with motion blur and feature instability inherent to racing dynamics…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (7 篇)

### 1. Robust Visual SLAM for UAV Navigation in GPS-Denied and Degraded Environments: A Multi-Paradigm Evaluation and Deployment Study

- **arXiv**: [2605.03678v1](https://arxiv.org/abs/2605.03678v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2605.03678v1)
- **作者**: Prasoon Kumar, Akshay Deepak, Sandeep Kumar
- **发表**: 2026-05-05  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Reliable localization in GPS-denied, visually degraded environments is critical for autonomous UAV opera- tions. This paper presents a systematic comparative evaluation of five V-SLAM systems ORB-SLAM3, DPVO, DROID-SLAM, DUSt3R, and MASt3R spanning classical, deep learning, recurrent, and Vision Transformer (ViT) paradigms. Experiments are conducted on cura…

### 2. FusionCore: A 23-State Unscented Kalman Filter for IMU, Wheel Encoder, GPS, and Visual SLAM Fusion in ROS 2

- **arXiv**: [2605.25239v1](https://arxiv.org/abs/2605.25239v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2605.25239v1)
- **作者**: Manan Kharwar
- **发表**: 2026-05-24  ·  **类别**: cs.RO, eess.SP
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: We present FusionCore, an open-source ROS 2 sensor fusion package that fuses IMU, wheel encoder odometry, GPS, and Visual SLAM pose into a single 100 Hz odometry stream using a 23-state Unscented Kalman Filter (UKF). The 23rd state is an online estimate of the wheel encoder's systematic yaw rate bias, identified through GPS heading cross-covariance and subt…

### 3. Passage-Aware Structural Mapping for RGB-D Visual SLAM

- **arXiv**: [2604.24707v1](https://arxiv.org/abs/2604.24707v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2604.24707v1)
- **作者**: Ali Tourani, Miguel Fernandez-Cortizas, Saad Ejaz et al.
- **发表**: 2026-04-27  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Doorways and passages are critical structural elements for indoor robot navigation, yet they remain underexplored in modern Visual SLAM (VSLAM) frameworks. This paper presents a passage-aware structural mapping approach for RGB-D VSLAM that detects doors and traversable openings by jointly fusing geometric, semantic, and topological cues. Doors are modeled…

### 4. Geodesic Flow Matching for Denoising High-Dimensional Structured Representations

- **arXiv**: [2606.00248v1](https://arxiv.org/abs/2606.00248v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.00248v1)
- **作者**: Karim Habashy, Chris Eliasmith
- **发表**: 2026-05-29  ·  **类别**: cs.AI
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Vector Symbolic Algebras (VSAs) enable robust neurosymbolic reasoning by encoding symbolic information into high-dimensional distributed representations. For continuous domains, Spatial Semantic Pointers (SSPs) extend this framework by mapping variables onto continuous toroidal manifolds. However, standard approaches like Flow Matching assume a flat Euclide…

### 5. WildPose: A Unified Framework for Robust Pose Estimation in the Wild

- **arXiv**: [2605.12774v1](https://arxiv.org/abs/2605.12774v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2605.12774v1)
- **作者**: Jianhao Zheng, Liyuan Zhu, Zihan Zhu et al.
- **发表**: 2026-05-12  ·  **类别**: cs.CV
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Estimating camera pose in dynamic environments is a critical challenge, as most visual SLAM and SfM methods assume static scenes. While recent dynamic-aware methods exist, they are often not unified: semantic-based approaches are brittle, per-sequence optimization methods fail on short sequences, and other learned models may degrade on static-only scenes. W…

### 6. Hardware-Aware Neural Feature Extraction for Resource-Constrained Devices

- **arXiv**: [2605.04282v2](https://arxiv.org/abs/2605.04282v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2605.04282v2)
- **作者**: Francesco Tosini, Simone Pedroni, Christian Veronesi et al.
- **发表**: 2026-05-05  ·  **类别**: cs.LG
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Visual SLAM is a core component of spatial computing systems, yet deploying learned local feature extractors on microcontroller-class hardware remains challenging due to memory, bandwidth, and quantization constraints. While modern neural descriptors provide strong robustness, their practical adoption is often hindered by system-level bottlenecks that are n…

### 7. HI-SLAM2: Geometry-Aware Gaussian SLAM for Fast Monocular Scene Reconstruction

- **arXiv**: [2411.17982v3](https://arxiv.org/abs/2411.17982v3)  ·  **PDF**: [link](https://arxiv.org/pdf/2411.17982v3)
- **作者**: Wei Zhang, Qing Cheng, David Skuddis et al.
- **发表**: 2024-11-27  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: We present HI-SLAM2, a geometry-aware Gaussian SLAM system that achieves fast and accurate monocular scene reconstruction using only RGB input. Existing Neural SLAM or 3DGS-based SLAM methods often trade off between rendering quality and geometry accuracy, our research demonstrates that both can be achieved simultaneously with RGB input alone. The key idea…

---

## 📋 本日操作建议

**建议今日深读 (Top 3):**
1. [Blind Dexterous Grasping via Real2Sim2Real Tactile Policy Learning](https://arxiv.org/abs/2606.11767v1) — score 26
2. [Bridging the Morphology Gap: Adapting VLA Models to Dexterous Manipulation via Intent-Conditioned Fine-Tuning](https://arxiv.org/abs/2606.12109v1) — score 24
3. [X2-N: A Transformable Wheel-legged Humanoid Robot with Dual-mode Locomotion and Manipulation](https://arxiv.org/abs/2604.21541v1) — score 20

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
