# 机器人研究每日摘要 · 2026-10-15

> 自动生成,共 92 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (9 篇)

### 1. LIBERO-RIG: A Hardware-Setup Robustness Benchmark for Vision-Language-Action Models

- **arXiv**: [2610.18843v1](https://arxiv.org/abs/2610.18843v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.18843v1)
- **作者**: Andrea Yaoyun Cui, Hanyu Wang, Xinyi Wang et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Robot policies are expected to generalize across deployment environments, including variations in the robot itself: cameras are bumped and remounted, calibrations drift, controllers run at different rates, and end-effector pads wear down. We present LIBERO-RIG, a benchmark that perturbs only the robot's hardware and setup while holding every LIBERO task fix…

### 2. ACCRUE: Continual Off-Policy Reinforcement Learning for Robot Foundation Models

- **arXiv**: [2610.18596v1](https://arxiv.org/abs/2610.18596v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.18596v1)
- **作者**: Changyeon Kim, Kimin Lee, Yashraj Narang et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Reinforcement learning (RL) post-training improves robot foundation models (RFMs) beyond their demonstrations, but real-world deployment demands more: learning new tasks efficiently while retaining previously acquired behaviors. Existing continual RL methods on top of VLAs mitigate forgetting but rely on on-policy updates with limited forward transfer, wher…

### 3. EnactOpt: Diagnosis-Guided Harness Evolution for Embodied Agents

- **arXiv**: [2610.14977v1](https://arxiv.org/abs/2610.14977v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.14977v1)
- **作者**: ZhiYuan Feng, Zhuoshi Pan, Zhaolu Kang et al.
- **发表**: 2026-10-10  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Embodied agents built on foundation models rely on an execution harness to organize observations, guide actions, and incorporate execution feedback into subsequent decisions. Failures can arise not only from limited model capabilities, but also from how the harness presents evidence and guides its use. These model-external mechanisms provide an adaptation t…

### 4. $Δ$ Flow Matching for Robot Foundation Models

- **arXiv**: [2610.15794v1](https://arxiv.org/abs/2610.15794v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.15794v1)
- **作者**: Kuangji Zuo, Tuo An, Xinying Guo et al.
- **发表**: 2026-10-11  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Flow matching is a common generative recipe for robot foundation models. Vision-language-action models (VLAs) generate action chunks, while world-action models (WAMs) additionally generate future visual states. Both start generation from a fixed Gaussian prior, despite temporal continuity between past and future states and actions. This requires costly trai…

### 5. ChunkAct: Action Chunking for Agentic Robotics

- **arXiv**: [2610.18874v1](https://arxiv.org/abs/2610.18874v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.18874v1)
- **作者**: Bingxin Xu, Wenrui Bao, Xinxin Liu et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO, cs.AI, cs.CL
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Agentic robotics places a large language model (LLM) agent in the robot control loop, where it composes perception, motion, and vision-language-action (VLA) tools under the guidance of a memory and thereby generalizes to new tasks without retraining. This generality comes at a steep price in efficiency. Every primitive requires a round of LLM reasoning over…

### 6. ARC: A Reasoning Recipe for Robot Foundation Models

- **arXiv**: [2610.12386v1](https://arxiv.org/abs/2610.12386v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12386v1)
- **作者**: Gokul Puthumanaillam, Tao Sun, Elie Aljalbout et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: The prevailing approach to improving robot foundation models (RFMs) relies on larger models, more robot demonstrations, and costly training at scale. We show that there exists an effective and efficient complementary approach: the right reasoning recipe can substantially improve the zero-shot task performance of existing state-of-the-art RFMs. We refer to t…

### 7. What Matters in Quality-Aware VLA Pretraining: A Benchmark and Empirical Study

- **arXiv**: [2610.18869v1](https://arxiv.org/abs/2610.18869v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.18869v1)
- **作者**: Mingxuan Yan, Litian Gong, Dihong Huang et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: How should demonstration quality be used during vision-language-action (VLA) pretraining to improve performance after target-task fine-tuning? We compare weighting, filtering, and conditioning across reward definitions and label granularities using 5,000 naturally suboptimal human demonstrations and 24 target tasks. Within each VLA, we match demonstrations…

### 8. EmbodiedEvo: Self-improving Coding Agents for Physical Intelligence

- **arXiv**: [2610.18867v1](https://arxiv.org/abs/2610.18867v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.18867v1)
- **作者**: Wenyi Li, Yizhe Chi, Youjie Zheng et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Bringing general-purpose agents into the physical world calls for an executable representation of physical intelligence. Compared with vision-language-action (VLA) models, which map observations and language instructions directly to actions, code makes control logic explicit and reusable. Code can serve not only as a policy representation but also as the wo…

### 9. SEAR: Self-Evolving Agentic Robotics

- **arXiv**: [2610.18792v1](https://arxiv.org/abs/2610.18792v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.18792v1)
- **作者**: Xinyi Wang, Bangzheng Li, Hanyu Wang et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO, cs.AI, cs.CL
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Frontier language-model agents can now improve robots on their own: they write control code, test it, and keep what works as skills and memories for the next task. We introduce SEAR (Self-Evolving Agentic Robotics), a framework and benchmark built around two questions. Is the agent really learning, or just trying more often? And does what it learns still he…

## 🌐 具身智能 / 机器人基础模型 (10 篇)

### 1. StateSkill-Agent: An Effective and Efficient Embodied Agent via State-conditioned Skill

- **arXiv**: [2610.14601v1](https://arxiv.org/abs/2610.14601v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.14601v1)
- **作者**: Changxu Wei, Jingyi Zhang, Zhiyu Zheng et al.
- **发表**: 2026-10-10  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: In this work, we aim to develop an embodied MLLM agent that understands and solves embodied tasks by learning, abstracting, and reusing transferrable and generalizable behavioral patterns. To this end, we propose StateSkill, a new skill representation for embodied agents, which introduces the concept of "finite-state machines" into skill modeling for effect…

### 2. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 3. Two Routes to Interoceptive Prioritisation: Dissociating Likelihood Precision and Preference Reweighting in Active Inference

- **arXiv**: [2610.18617v1](https://arxiv.org/abs/2610.18617v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.18617v1)
- **作者**: St John Grimbly, Nicolas Kuske, Evert A. Boonstra et al.
- **发表**: 2026-10-13  ·  **类别**: cs.AI, q-bio.NC
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: An embodied agent must prioritise among competing bodily needs. In active inference, it can respond to an urgent need by increasing the precision of information about that need or by increasing its preference for outcomes that relieve it. We compare these two interventions, separately and together, in a foraging gridworld with three lethal needs, and ask ho…

### 4. MemAct: Streaming Spatial Understanding with Memory and Active Exploration

- **arXiv**: [2610.17640v1](https://arxiv.org/abs/2610.17640v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.17640v1)
- **作者**: Yuxi Wei, Wei Huang, Qirui Chen et al.
- **发表**: 2026-10-13  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Spatial understanding is essential for embodied agents navigating and interacting with the physical world. As observations arrive incrementally, agents must reason in a streaming manner. Yet streaming understanding must also be closed-loop: task-relevant evidence may require both recalling past observations and actively acquiring new views. Existing streami…

### 5. Observe, Share, or Predict? Disentangling Partner Information in Embodied Multi-Agent Collaboration

- **arXiv**: [2610.16895v1](https://arxiv.org/abs/2610.16895v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.16895v1)
- **作者**: Adrián Szlatincsán, Filippo Ziliotto, Bruno Lepri et al.
- **发表**: 2026-10-12  ·  **类别**: cs.AI, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: LLMs are used as high-level controllers for embodied agents, but it remains unclear whether they support collaborative reasoning, such as anticipating a collaborator's actions in real-time teamwork without dialogue. We ask if observing the partner's state, exchanging object knowledge, and predicting the partner's next action, shape task outcomes and coordin…

### 6. FoundationVIO: Enforcing Metric Scale in Feed-forward Visual-Inertial Odometry

- **arXiv**: [2610.14951v1](https://arxiv.org/abs/2610.14951v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.14951v1)
- **作者**: Jin Rhee, Yuhao Zhang, Frank Dellaert et al.
- **发表**: 2026-10-10  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Feed-forward geometric foundation models (GFMs) directly predict dense geometry and camera poses from batches of images. Emerging visual SLAM methods chain together consecutive GFM batches to form dense point cloud maps. A core challenge is how to address the ambiguous geometric scale of GFM predictions: independent predictions are locally consistent up-to-…

### 7. PVFH-Bench: Benchmarking Premise-Induced Visual Fixation Hallucinations in Vision-Language Models

- **arXiv**: [2610.14635v1](https://arxiv.org/abs/2610.14635v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.14635v1)
- **作者**: Xinhao Wang, Junbo Cui, Zhenghao Liu et al.
- **发表**: 2026-10-10  ·  **类别**: cs.CL, cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Large Vision-Language Models (LVLMs) have achieved remarkable progress across a wide range of multimodal tasks. However, object hallucination remains a persistent challenge, undermining model reliability in applications such as visual question answering, embodied agents, and human-AI decision support systems. In this paper, inspired by cognitive science stu…

### 8. Kinematic MeanFlow: One-Step Action Generation Policy for Robotic Foundation Models

- **arXiv**: [2610.00864v1](https://arxiv.org/abs/2610.00864v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.00864v1)
- **作者**: Jiawei Fan, Sifeng Wang, Yuqing Hou et al.
- **发表**: 2026-10-01  ·  **类别**: cs.RO, cs.AI, cs.CL
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: In this paper, we study how to achieve one-step action generation in Robotic Foundation Models (RFMs), aiming to overcome the high inference latency of multi-step flow matching. MeanFlow provides a promising framework for this goal, yet its direct application leads to performance collapse. We discover that this stems from two distinctive dynamics exhibited…

### 9. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

### 10. EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution

- **arXiv**: [2610.10498v1](https://arxiv.org/abs/2610.10498v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10498v1)
- **作者**: Python Song, Zhixuan Liang, Kelsey Fu et al.
- **发表**: 2026-10-07  ·  **类别**: cs.AI
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Robot foundation models provide strong visuomotor control, yet their performance can degrade when object positions or task instructions change. Further improvements often require post-training on substantial robot data, which can be costly to collect through methods such as teleoperation. Agentic harnesses can adapt around the model, but current self-evolvi…

## 🦵 人形 / 足式机器人 (27 篇)

### 1. SHOES: Sim-to-real Hardware-adaptation via On-policy Expansion of Skills for Legged Robots

- **arXiv**: [2610.16457v1](https://arxiv.org/abs/2610.16457v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.16457v1)
- **作者**: Kota Tsuruhara, Tsung-Yuan Chen, Kento Kawaharazuka
- **发表**: 2026-10-12  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Humans expand their locomotion capability by wearing appropriate footwear, such as hiking boots for mountains or skates for ice. Footwear changes the ground-contact interface and enables traversal of otherwise difficult terrain. In contrast, locomotion controllers are typically trained for a fixed morphology, and their performance can degrade when shoes alt…

### 2. Adaptive Whole-Body MPC with Optimal Posture Planning for Humanoid Robots under Unknown Payloads

- **arXiv**: [2610.12972v1](https://arxiv.org/abs/2610.12972v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12972v1)
- **作者**: Manh Cuong Nguyen, Duc Cuong Vu, Viet Anh Vu et al.
- **发表**: 2026-10-09  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Humanoid robots performing lifting and material-handling tasks must maintain balance despite unknown and varying payloads. However, payload uncertainty significantly affects whole-body dynamics and may destabilize conventional controllers. We propose an adaptive whole-body control architecture that integrates three components: (i) a centroidal model predict…

### 3. PanTact: Teaching Whole-Body Dexterity with a Wearable Contact Interface

- **arXiv**: [2610.12558v1](https://arxiv.org/abs/2610.12558v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12558v1)
- **作者**: Xiaomeng Xu, Han Zhang, Zhian Ruan et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Humanoid robots have many degrees of freedom and contact surfaces, yet most loco-manipulation research restricts manipulation to the hands and avoids other body contacts with the environment. To extend manipulation beyond the hands, we present PanTact, a system that learns humanoid whole-body dexterity, the capability to manipulate with any suitable body su…

### 4. OccluDex: Hierarchical 3D Visuo-Tactile Representation Learning for Egocentric Dexterous Manipulation under Self-Occlusion

- **arXiv**: [2609.39017v1](https://arxiv.org/abs/2609.39017v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39017v1)
- **作者**: Ziheng Xu, Yueyuan Chen, Xinyuan He et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Reliable dexterous manipulation requires continuous estimation of object geometry and hand-object contact throughout interaction. With egocentric sensing, however, the manipulating hand frequently occludes task-relevant object surfaces and contact regions, reducing the visual evidence available for state estimation and thereby making robust closed-loop cont…

### 5. Modeling and Control of a Rigid-soft Hybrid-link Humanoid Robot

- **arXiv**: [2610.15073v1](https://arxiv.org/abs/2610.15073v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.15073v1)
- **作者**: Zewen He, Taiki Ishigaki, Ko Yamamoto
- **发表**: 2026-10-10  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Physical flexibility plays a significant role not only in human motions but also in robot motions. For example, a humanoid robot with passive and flexible elements, which can be regarded as a rigid--soft hybrid-link system, has the advantages of storing energy and mitigating impact in a dynamic motion. However, the motion design and control of a hybrid-link…

### 6. HWAM: Humanoid World Action Model With Joint State--Action Generation

- **arXiv**: [2610.12026v2](https://arxiv.org/abs/2610.12026v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.12026v2)
- **作者**: Yan Yang, Jikun Rong, Minzhao Zhu et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Humanoid robots are a promising platform for general-purpose manipulation. Recent Vision-Language-Action (VLA) policies learn actions directly from multimodal observations, while World Action Models (WAMs) further incorporate future visual prediction to improve action generation. However, in hierarchical humanoid systems, VLA and WAM policies output referen…

### 7. EgoExplorer: A Vision-Motion-Touch Observatory for Human Loco-Manipulation In Situ

- **arXiv**: [2610.18872v1](https://arxiv.org/abs/2610.18872v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.18872v1)
- **作者**: Yunsong Zhou, Xuekun Jiang, Haiqi Shen et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Learning humanoid loco-manipulation from human demonstrations rests on observing how locomotion, posture, and object interaction evolve together as tasks unfold. Scaling collection across diverse environments, in turn, favors lightweight, portable capture systems. Yet, existing datasets provide only partial views of this coordination. Thus, we introduce Ego…

### 8. TRACE: Efficient Transfer Learning for Neural Whole-Body Control Across Humanoid Embodiments

- **arXiv**: [2610.17999v1](https://arxiv.org/abs/2610.17999v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.17999v1)
- **作者**: Qingyu Lan, Zhihao Tian, Zifan Wang et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Humanoid behavior foundation models (BFMs) enable diverse whole-body control, but adapting a pretrained controller to a new embodiment remains challenging because of kinematic and dynamic mismatch. We present TRACE, a framework for efficient cross-embodiment adaptation that preserves pretrained motion representations while specializing feedback control to t…

### 9. Belief-Overlap Partial Inversion: Object-Centric Flow Replanning for Humanoid Loco-Manipulation

- **arXiv**: [2610.13087v1](https://arxiv.org/abs/2610.13087v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.13087v1)
- **作者**: Chen Yu, Sudarshan S Harithas, Juan Borbon et al.
- **发表**: 2026-10-09  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: People often learn how an unfamiliar object moves through a small exploratory push, using its response to guide their next motion. Inspired by this behavior, we study humanoids pushing carts whose mass and caster stiffness are initially unknown. Our object-centric framework closes online estimation, flow-based planning, and whole-body control into a loop, c…

### 10. SABER: Learning Attention-based Semantic Affordance for Legged Locomotion

- **arXiv**: [2609.21572v2](https://arxiv.org/abs/2609.21572v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.21572v2)
- **作者**: Hari Prasanth Palanivelu, Samuel Sze, Kennard Garrison Johannes et al.
- **发表**: 2026-09-18  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Perceptive legged locomotion has advanced rapidly by integrating terrain geometry into learned policies, yet the integration of terrain meaning remains sparse: a pipe, a patch of grass, or a fragile box may be geometrically traversable while being inappropriate for contact. In industrial environments, where legged robots increasingly operate, a single mispl…

## 🦾 操控 / 灵巧手 / 抓取 (26 篇)

### 1. OmniDex: Scaling Dexterous Hand Grasping to Diverse Cluttered Scenes

- **arXiv**: [2610.11194v1](https://arxiv.org/abs/2610.11194v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.11194v1)
- **作者**: Naiyu Fang, Zhongjin Luo, Yuxin Mo et al.
- **发表**: 2026-10-08  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Dexterous grasping is the foundational primitive in embodied AI, demanding massive data to train robust models. As real-world data collection is expensive, simulation has become the mainstream paradigm. Yet, while cluttered scenes best reflect real-world applications, learning to grasp within them is bottlenecked by a critical scarcity of large-scale data.…

### 2. EigenDEXplore: Structured Exploration for Dexterous Manipulation with Human Priors

- **arXiv**: [2610.07681v1](https://arxiv.org/abs/2610.07681v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.07681v1)
- **作者**: Harsh Gupta, Tyler Ga Wei Lum, Changhao Wang et al.
- **发表**: 2026-10-06  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation poses a challenging high-dimensional optimization problem, as useful behaviors require coordinated motion across many hand joints. In reinforcement learning (RL) and sampling-based trajectory optimization, exploration commonly relies on independent robot joint perturbations, making coordinated behaviors difficult to discover. Prior wo…

### 3. EgoCPT: Learning Dexterous Manipulation from a Single Ego-Centric Video with Contact-Aware Optimization

- **arXiv**: [2610.17572v1](https://arxiv.org/abs/2610.17572v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.17572v1)
- **作者**: Zhixin Sun, Kairui Shi, Tianao Ren et al.
- **发表**: 2026-10-13  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: While expert demonstrations on real robots are difficult to collect, human ego-centric videos are easy to collect and abundant on the internet. However, learning dexterous manipulation policies from human videos remains challenging---one of the most important challenges being the difficulty of reconstructing physically grounded robot trajectories due to the…

### 4. DexNinja: Learning Robust Dexterous Cutting Policy with a Real-to-Sim-to-Real Data Engine

- **arXiv**: [2610.17208v1](https://arxiv.org/abs/2610.17208v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.17208v1)
- **作者**: Haozhe Lou, Runyi Yang, Wanqi Zhong et al.
- **发表**: 2026-10-12  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Cutting a piece of food looks effortless in human hands. For a robot, however, every cut is a high-contact interaction with a deformable, elasto-plastic object whose behavior changes with pose, contact mode, and cutting stage. Collecting real-world data is expensive and wasteful: each trial typically contaminates or damages the food, so obtaining scalable r…

### 5. AutoBio+: Benchmarking Dexterous Manipulation with Dynamic Experimental Phenomena in Realistic Laboratories

- **arXiv**: [2610.13643v2](https://arxiv.org/abs/2610.13643v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.13643v2)
- **作者**: Xuanye Wu, Yue Shi, Yongcan Yang et al.
- **发表**: 2026-10-09  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Automating biological laboratories requires robots to perform dexterous tool interactions under realistic visual conditions while handling dynamic experimental phenomena, presenting significant challenges for robotic manipulation. To enable systematic evaluation under these conditions, we introduce AutoBio+, a simulation benchmark and framework for dexterou…

### 6. Force-Modulated Dexterity: Unified Compliance for Contact-Rich Manipulation

- **arXiv**: [2610.17161v1](https://arxiv.org/abs/2610.17161v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.17161v1)
- **作者**: Ying Yuan, David Held, Jitendra Malik et al.
- **发表**: 2026-10-12  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Teleoperation is widely used to collect high-quality demonstrations for robot learning. Dexterous manipulation, however, requires coordinated control of motion and contact forces. Operators can specify motion, but struggle to reproduce the subtle force adjustments of human manipulation without feeling the robot's contacts. We introduce Force-Modulated Dexte…

### 7. NarrativeFlow: Flow-Based Vision-Language-Action Model Using Robot Velocity Fields

- **arXiv**: [2610.00981v1](https://arxiv.org/abs/2610.00981v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.00981v1)
- **作者**: Shota Kobayashi, Koki Seno, Daichi Yashima et al.
- **发表**: 2026-10-01  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We focus on language-conditioned flow-based manipulation, where robot flows (robot velocity fields) serve as embodiment-agnostic, motion-centric representations for leveraging data collected from multiple robot platforms. This task is crucial because language-conditioned manipulation is essential for practical robotic systems, yet scaling robot foundation m…

### 8. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

### 9. DexCast: Learning Real-World Dexterous Control from Human Videos

- **arXiv**: [2610.14691v1](https://arxiv.org/abs/2610.14691v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.14691v1)
- **作者**: Zihan Gao, Yuhong Zhang, Mengzhe Wang et al.
- **发表**: 2026-10-10  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Recent advances in 3D hand-object interaction (HOI) perception have opened new opportunities for learning dexterous robotic skills from human videos. However, existing dexterous imitation learning methods often rely on costly and manually teleoperated robot demonstrations, requiring substantial human effort. Therefore, we build DEXCAST, a framework that lea…

### 10. Beyond Actions: Learning Future Operation Targets for Vision-Language-Action Models

- **arXiv**: [2610.13212v2](https://arxiv.org/abs/2610.13212v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.13212v2)
- **作者**: Min Lin, Bokai Zhou, Jianqi Lin et al.
- **发表**: 2026-10-09  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Actions specify what a robot should execute, but do not describe what those commands will achieve. Vision-language-action (VLA) policies nevertheless learn primarily by predicting action chunks from images, language, and state. We introduce Action--Future Coupled Effect Learning (AFCE), which makes a future-grounded physical Effect the policy's primary pred…

## 🎓 模仿学习 / 强化学习 (13 篇)

### 1. XAI-Guided Fourier Domain Generalisation for Pure-Simulation Sim-to-Real Deep Reinforcement Learning

- **arXiv**: [2610.16478v1](https://arxiv.org/abs/2610.16478v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.16478v1)
- **作者**: Wei Yao, Chuyao Wang, Ziwei Wang et al.
- **发表**: 2026-10-12  ·  **类别**: cs.AI, cs.CV
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Deep reinforcement learning has shown strong potential for vision-based autonomous driving, but policies trained in simulation often suffer severe performance degradation when deployed in the real world. Existing sim-to-real methods commonly address this gap through image-transfer-based domain adaptation or policy-agnostic domain randomisation. However, the…

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

### 7. WorldRecon: Generative Multi-View Mesh Reconstruction for Large-Scale 3D World

- **arXiv**: [2610.18846v1](https://arxiv.org/abs/2610.18846v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.18846v1)
- **作者**: Mengchen Zhang, Yang Li, Chunshi Wang et al.
- **发表**: 2026-10-13  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Reconstructing complete, high-quality meshes of large-scale scenes from unposed multi-view images requires faithful geometric grounding while plausibly completing surfaces that are unobserved or only sparsely captured. We present WorldRecon, a generative multi-view reconstruction framework for recovering complete, large-scale 3D scene meshes from unposed RG…

### 8. D-World: An Explicit World-Language-Action Model with Recursive Self-Improvement under Dual Control

- **arXiv**: [2610.17114v1](https://arxiv.org/abs/2610.17114v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.17114v1)
- **作者**: Xuan Wen, Baichao Wang
- **发表**: 2026-10-12  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Frontier large language models (LLMs) now reason about space well enough to program robots, yet the world models behind robot policies are implicit, held in network weights or predicted video, and cannot be inspected or corrected directly. We present D-World, an explicit world-language-action model built on the Sense, Plan and Act decomposition. A perceptio…

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

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (6 篇)

### 1. Human-in-the-Loop Neuro-Symbolic Drift Anticipation for Reliable Visual SLAM

- **arXiv**: [2610.05757v1](https://arxiv.org/abs/2610.05757v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.05757v1)
- **作者**: Junhyun Nam, Wonse Jo
- **发表**: 2026-10-05  ·  **类别**: cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: This paper introduces Hybrid DeepSEE (HDS), a Human-in-the-Loop (HITL) neuro-symbolic framework for proactive drift anticipation in Visual SLAM (V-SLAM). While data-driven models offer predictive power, their "black-box" nature often yields physically inconsistent outputs in out-of-distribution (OOD) environments. To address this, HDS integrates neural drif…

### 2. Know-Your-Scene (KYS)-SLAM: Hierarchical Semantic-Motion Priors for Feature Matching in Stereo Visual SLAM

- **arXiv**: [2609.27509v1](https://arxiv.org/abs/2609.27509v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.27509v1)
- **作者**: Preeti Chatterjee, Jin Lu, Jin Sun et al.
- **发表**: 2026-09-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Stereo visual SLAM systems built on local descriptors suffer from semantic ambiguity, instance-level confusion, and independently moving objects, each corrupting data association and accumulating as trajectory drift. Prevailing semantic and dynamic SLAM methods address this through binary feature rejection, sacrificing correspondence density for outlier sup…

### 3. Does Dynamic-Point Filtering Help When Texture Is Scarce? A Controlled Study of ORB-SLAM2 Front-Ends in Synthetic Indoor Scenes

- **arXiv**: [2610.10564v1](https://arxiv.org/abs/2610.10564v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2610.10564v1)
- **作者**: Zekui Xue
- **发表**: 2026-10-02  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Dynamic-point filters are routinely added to feature-based visual SLAM, and several recent systems argue that removing dynamic features can leave too few static features in low-texture regions. So far, these systems have been evaluated only on texture-rich benchmark sequences. We present a controlled study that isolates this interaction. We render synthetic…

### 4. MVP-SLAM: Multi-Camera Visual-Inertial Floorplan-Prior SLAM

- **arXiv**: [2609.39596v1](https://arxiv.org/abs/2609.39596v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.39596v1)
- **作者**: Asier Bikandi-Noya, Miguel Fernandez-Cortizas, Muhammad Shaheer et al.
- **发表**: 2026-09-30  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Indoor building construction sites are demanding environments for visual SLAM, where variable lighting and repetitive, low-textured structures make the system drift over long trajectories, though structural elements such as walls remain distinguishable despite these conditions. These buildings are constructed according to their as-planned floor plans, avail…

### 5. Cube-Splat: High-Fidelity 360° Gaussian Splatting SLAM via Cubemap Factorization and Adjoint-Consistent Optimization

- **arXiv**: [2609.21347v1](https://arxiv.org/abs/2609.21347v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.21347v1)
- **作者**: Xiangfei Guo, Hao Shi, Yufan Zhang et al.
- **发表**: 2026-09-18  ·  **类别**: cs.CV
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Recent progress in 3D Gaussian Splatting (3DGS) has enabled dense visual SLAM with pinhole cameras, yet most pipelines are not designed for panoramic imagery. We present Cube-Splat, the first panoramic GS-SLAM framework that factorizes each 360° frame into a cubemap of four fixed-orientation virtual pinhole views sharing a single optical center. By designat…

### 6. Geodesic Flow Matching for Denoising High-Dimensional Structured Representations

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
1. [OmniDex: Scaling Dexterous Hand Grasping to Diverse Cluttered Scenes](https://arxiv.org/abs/2610.11194v1) — score 19
2. [SHOES: Sim-to-real Hardware-adaptation via On-policy Expansion of Skills for Legged Robots](https://arxiv.org/abs/2610.16457v1) — score 17
3. [Adaptive Whole-Body MPC with Optimal Posture Planning for Humanoid Robots under Unknown Payloads](https://arxiv.org/abs/2610.12972v1) — score 17

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
