---
permalink: /zh/
title: ""
excerpt: ""
author_profile: true
lang: zh
redirect_from: 
  - /zh/about/
  - /zh/about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

# 💡 关于我
<span class='anchor' id='about-me'></span>

我目前是**中国农业大学（CAU）**的学生。我的研究兴趣主要集中在 <span class="paper-badge-text" style="background-color: #6B7A99;">Agentic AI</span> 和 <span class="paper-badge-text" style="background-color: #4A7C8C;">多模态情感智能</span>。欢迎就相关方向合作交流。

我曾担任团队负责人并获得了 **ACM MM 2025 MER (多模态情感识别) 挑战赛 DES 赛道的第一名**。此外，我的第一作者论文已被 **ACM MM 主会 Grand Challenge 赛道**录用。

在2024年，我被选树为**广东大学生年度人物**和**人民日报国家奖学金学生代表**。

联系方式：[huangyuesheng@cau.edu.cn](mailto:huangyuesheng@cau.edu.cn) | <a href="/">English</a> / <strong>中文</strong>

# 🔥 新闻
<span class='anchor' id='-news'></span>
- *2026.01*: &nbsp;🚀 我发布 **Awesome Affective Computing**：Affective Computing & Emotion AI 精选清单，涵盖多模态情感识别、情感推理、多模态情感分析与共情式 LLM/MLLM 的论文、数据集与工具包。<a href="https://github.com/Yasen03/awesome-affective-computing" style="text-decoration: none;"> <i class="fab fa-fw fa-github" aria-hidden="true"></i> Awesome Affective Computing <img src="https://img.shields.io/github/stars/Yasen03/awesome-affective-computing?style=social" alt="Stars" style="vertical-align: middle;"></a>
- *2025.08*: &nbsp;🏆 我获得 **ACM MM 2025 MER Challenge (DES Track) 第一名**（担任团队负责人）！
- *2025.08*: &nbsp;📄 我的第一作者论文被 **ACM MM 2025 主会 Grand Challenge 赛道**录用！
- *2024.12*: &nbsp;&nbsp;🎉 我获评 2023 年度**广东大学生年度人物**（全省本硕博共评选 10 人），为同年度**最年轻的获奖者**。
- *2024.05*: &nbsp;&nbsp;🎉 我作为 100 名本科生国家奖学金获得者代表之一被**《人民日报》**报道（广东省仅 4 名）。
- *2023.12*: &nbsp;&nbsp;🎉 我获得**国家奖学金**。

# 📝 发表论文
<span class='anchor' id='-publications'></span>
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACM MM 2025</div><img src='{{ site.baseurl }}/images/affective.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
<div class="paper-title">Affective-CoT: Decomposing Multimodal Emotion Reasoning through a Hierarchical Cognitive Workflow</div>
  
**Yuesheng Huang**, Jinming Liu, Jiajia Chen, Yihang Lin, Yanmei Chen, Jianwei Dong

<div class="paper-meta">ACM MM 2025 主会 Grand Challenge 赛道</div>
<div class="paper-links">
  <a class="paper-badge" href="https://dl.acm.org/doi/10.1145/3695952.3731175"><img src="https://img.shields.io/badge/Paper-ACM%20DL-0071C5" alt="ACM DL"></a>
  <span class="paper-badge"><img src="https://img.shields.io/badge/MER2025--DES-冠军-gold" alt="Champion"></span>
  <button type="button" class="paper-badge-text citation-trigger" onclick="toggleCitation('citation-acmmm2025-zh', event)">引用</button>
</div>
<div id="citation-acmmm2025-zh" class="citation-popup">
  <div class="citation-format-container">
    <div class="citation-format-label">BibTeX</div>
    <div class="citation-format">@inproceedings{huang2025affective, <br>      title={Affective-CoT: Decomposing Multimodal Emotion Reasoning through a Hierarchical Cognitive Workflow}, <br>      author={Huang, Yuesheng and Liu, Jinming and Chen, Jiajia and Lin, Yihang and Chen, Yanmei and Dong, Jianwei}, <br>      booktitle={Proceedings of the 33rd ACM International Conference on Multimedia}, <br>      pages={13848--13855}, <br>      year={2025} <br>}</div>
  </div>
</div>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">MRAC workshop@ACM MM</div><img src='{{ site.baseurl }}/images/DARE.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
<div class="paper-title">DARE to Disagree: A Multi-Agent Adversarial Debate Framework for Open-Vocabulary Multimodal Emotion Recognition</div>
  
**Yuesheng Huang**, Meiqi Feng, Zhenming He, Yueyuan Peng, Jiawen Li

<div class="paper-meta">ACM MM 2025 MRAC Workshop</div>
<div class="paper-links">
  <a class="paper-badge" href="https://dl.acm.org/doi/10.1145/3706591.3706600"><img src="https://img.shields.io/badge/Paper-ACM%20DL-0071C5" alt="ACM DL"></a>
  <span class="paper-badge"><img src="https://img.shields.io/badge/MER_2025--FG-第7名-blue" alt="第7名"></span>
  <a class="paper-badge" href="https://github.com/GPNU-AIoT/DARE"><img src="https://img.shields.io/github/stars/GPNU-AIoT/DARE?style=social" alt="GitHub Stars"></a>
  <button type="button" class="paper-badge-text citation-trigger" onclick="toggleCitation('citation-dare2025-zh', event)">引用</button>
</div>
<div id="citation-dare2025-zh" class="citation-popup">
  <div class="citation-format-container">
    <div class="citation-format-label">BibTeX</div>
    <div class="citation-format">@inproceedings{huang2025dare, <br>      title={DARE to Disagree: A Multi-Agent Adversarial Debate Framework for Open-Vocabulary Multimodal Emotion Recognition}, <br>      author={Huang, Yuesheng and Feng, Meiqi and He, Zhenming and Peng, Yueyuan and Li, Jiawen}, <br>      booktitle={Proceedings of the 3rd International Workshop on Multimodal and Responsible Affective Computing}, <br>      pages={41--50}, <br>      year={2025} <br>}</div>
  </div>
</div>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML Workshop</div><img src='{{ site.baseurl }}/images/fig1.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
<div class="paper-title">Can Generated Images Serve as a Viable Modality for Text-Centric Multimodal Learning?</div>
  
**Yuesheng Huang**, Peng Zhang, Riliang Liu, Jiaqi Liang

<div class="paper-meta">ICML 2025 NewInML Workshop</div>
<div class="paper-links">
  <a class="paper-badge" href="https://arxiv.org/abs/2506.17623"><img src="https://img.shields.io/badge/Paper-arXiv-B31B1B" alt="arXiv"></a>
  <a class="paper-badge" href="https://icml.cc/media/PosterPDFs/ICML%202025/50506.png?t=1752508273.1077719"><img src="https://img.shields.io/badge/ICML-Poster-1aa6b7?labelColor=2f6f73" alt="ICML Poster"></a>
  <button type="button" class="paper-badge-text citation-trigger" onclick="toggleCitation('citation-arxiv2025-zh', event)">引用</button>
  <a href="https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=edyJPQQAAAAJ&citation_for_view=edyJPQQAAAAJ:W7OEmFMy1HYC"><img id="citation-badge-generated-images-zh" src="https://img.shields.io/badge/Citations-loading-6c757d" class="paper_citations" data-paper-id="edyJPQQAAAAJ:W7OEmFMy1HYC" alt="Scholar Citations"></a>
</div>
<div id="citation-arxiv2025-zh" class="citation-popup">
  <div class="citation-format-container">
    <div class="citation-format-label">BibTeX</div>
    <div class="citation-format">@misc{huang2025generatedimagesserveviable,<br>      title={Can Generated Images Serve as a Viable Modality for Text-Centric Multimodal Learning?}, <br>      author={Yuesheng Huang and Peng Zhang and Riliang Liu and Jiaqi Liang},<br>      year={2025},<br>      eprint={2506.17623},<br>      archivePrefix={arXiv},<br>      primaryClass={cs.MM},<br>      url={https://arxiv.org/abs/2506.17623}, <br>}</div>
  </div>
</div>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CMC 2024</div><img src='{{ site.baseurl }}/images/cmc.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
<div class="paper-title">Sentiment Analysis Using E-Commerce Review Keyword-Generated Image with a Hybrid Machine Learning-Based Model</div>
  
Jiawen Li, **Yuesheng Huang**, Yayi Lu, Leijun Wang*, Yongqi Ren and Rongjun Chen

<div class="paper-meta">CMC - Computers, Materials & Continua</div>
<div class="paper-links">
  <a class="paper-badge" href="https://www.techscience.com/cmc/v80n1/57421"><img src="https://img.shields.io/badge/Paper-CMC%202024-00A0E9" alt="CMC 2024"></a>
  <a class="paper-badge" href="https://github.com/Yasen03/T2I-SA"><img src="https://img.shields.io/github/stars/Yasen03/T2I-SA?style=social" alt="GitHub Stars"></a>
  <button type="button" class="paper-badge-text citation-trigger" onclick="toggleCitation('citation1-zh', event)">引用</button>
  <a href="https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=edyJPQQAAAAJ&citation_for_view=edyJPQQAAAAJ:d1gkVwhDpl0C"><img id="citation-badge-1-zh" src="https://img.shields.io/badge/Citations-2-6c757d" class="paper_citations" data-paper-id="edyJPQQAAAAJ:d1gkVwhDpl0C" alt="Scholar Citations"></a>
</div>
<div id="citation1-zh" class="citation-popup">
  <div class="citation-format-container">
    <div class="citation-format-label">GB/T</div>
    <div class="citation-format">Li J, Huang Y, Lu Y, et al. Sentiment Analysis Using E-Commerce Review Keyword-Generated Image with a Hybrid Machine Learning-Based Model[J]. Computers, Materials & Continua, 2024, 80(1).</div>
  </div>
  <div class="citation-format-container">
    <div class="citation-format-label">MLA</div>
    <div class="citation-format">Li, Jiawen, et al. "Sentiment Analysis Using E-Commerce Review Keyword-Generated Image with a Hybrid Machine Learning-Based Model." Computers, Materials & Continua 80.1 (2024).</div>
  </div>
  <div class="citation-format-container">
    <div class="citation-format-label">APA</div>
    <div class="citation-format">Li, J., Huang, Y., Lu, Y., Wang, L., Ren, Y., & Chen, R. (2024). Sentiment Analysis Using E-Commerce Review Keyword-Generated Image with a Hybrid Machine Learning-Based Model. Computers, Materials & Continua, 80(1).</div>
  </div>
</div>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Engineering Letters</div><img src='{{ site.baseurl }}/images/EL.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
<div class="paper-title">An Improved Hybrid CNN-LSTM-Attention Model with Kepler Optimization Algorithm for Wind Speed Prediction</div>
  
**Yuesheng Huang**, Jiawen Li, Yushan Li, Routing Lin, Jingru Wu, Leijun Wang, and Rongjun Chen

<div class="paper-meta">Engineering Letters</div>
<div class="paper-links">
  <a class="paper-badge" href="https://www.engineeringletters.com/issues_v32/issue_10/EL_32_10_14.pdf"><img src="https://img.shields.io/badge/Paper-Engineering%20Letters-4CAF50" alt="Engineering Letters"></a>
  <a class="paper-badge" href="https://github.com/Yasen03/KOA-CNN-LSTM-Attention"><img src="https://img.shields.io/github/stars/Yasen03/KOA-CNN-LSTM-Attention?style=social" alt="GitHub Stars"></a>
  <button type="button" class="paper-badge-text citation-trigger" onclick="toggleCitation('citation2-zh', event)">引用</button>
  <a href="https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=edyJPQQAAAAJ&citation_for_view=edyJPQQAAAAJ:2osOgNQ5qMEC"><img id="citation-badge-2-zh" src="https://img.shields.io/badge/Citations-3-6c757d" class="paper_citations" data-paper-id="edyJPQQAAAAJ:2osOgNQ5qMEC" alt="Scholar Citations"></a>
</div>
<div id="citation2-zh" class="citation-popup">
  <div class="citation-format-container">
    <div class="citation-format-label">GB/T</div>
    <div class="citation-format">Huang Y, Li J, Li Y, et al. An Improved Hybrid CNN-LSTM-Attention Model with Kepler Optimization Algorithm for Wind Speed Prediction[J]. Engineering Letters, 2024, 32(10).</div>
  </div>
  <div class="citation-format-container">
    <div class="citation-format-label">MLA</div>
    <div class="citation-format">Huang, Yuesheng, et al. "An Improved Hybrid CNN-LSTM-Attention Model with Kepler Optimization Algorithm for Wind Speed Prediction." Engineering Letters 32.10 (2024).</div>
  </div>
  <div class="citation-format-container">
    <div class="citation-format-label">APA</div>
    <div class="citation-format">Huang, Y., Li, J., Li Y., Lin, R., Wu, J., Wang, L., & Chen, R. (2024). An Improved Hybrid CNN-LSTM-Attention Model with Kepler Optimization Algorithm for Wind Speed Prediction. Engineering Letters, 32(10).</div>
  </div>
</div>
</div>
</div>

# 🏆 竞赛获奖
<span class='anchor' id='-honors-and-awards'></span>
- *2025.08* **ACM MM 2025 MER Challenge（DES Track）冠军**（团队负责人）。
- *2025.02* 中国大学生技术创新创业大赛信息技术、医疗健康、现代服务赛道三赛道**一等奖**。
- *2024.06* **广东挑战杯创业计划竞赛银奖**，广东省教育厅。
- *2024.05* **美国大学生数学建模竞赛（MCM/ICM）**E题**Finalist奖**（全球**前2%**），COMAP。
- *2023.11* 中国大学生数学建模竞赛广东赛区**一等奖**。
- *2023.08* 中国大学生计算机设计大赛广东赛区**一等奖**。
- *2023.08* 国际高校数学建模竞赛**特等奖**。
- *2023.07* 全国大学生电工数学建模竞赛**一等奖**，中国电机工程学会。
- *2021.12* Kaggle Lux AI竞赛**银牌**。

# 🎓 教育背景
<span class='anchor' id='-educations'></span>
- *2025.09 - 2026.01*, 中国农业大学, 在读
- *2021.09 - 2025.06*, 物联网工程 工学学士学位（**ESI前1%**）, 计算机科学学院, 广东技术师范大学（**优秀毕业生**）。（**GPA:91.9/100, 排名:1/112**）<button type="button" class="paper-badge-text thesis-button" onclick="toggleThesis('thesis-zh', event)">毕业设计</button>（同届全校最高分）
  <div id="thesis-zh" class="thesis-abstract">
    <div class="paper-title">基于多模态数据与大模型赋能的学生情感智能分析与监测系统设计</div>
    <div class="thesis-toolbar">
      <button type="button" class="paper-badge-text active" onclick="setThesisView('thesis-zh','abstract')">摘要</button>
      <button type="button" class="paper-badge-text" onclick="setThesisView('thesis-zh','pdf','{{ site.baseurl }}/files/pdfs/thesis.pdf')">PDF</button>
      <button type="button" class="paper-badge-text" onclick="setThesisView('thesis-zh','ppt','{{ site.baseurl }}/files/pdfs/debate.pdf')">PPT</button>
    </div>
    <div class="thesis-content">
      <strong>摘要</strong><br>
      随着人工智能与深度学习技术的深入发展，<strong>多模态情感分析</strong>在教育领域的应用潜力日益显现。传统单模态<strong>情感识别</strong>方法在捕捉学生复杂情绪状态方面存在局限，而多模态分析通过整合面部表情、语音信息与生理信号，能显著提升情感识别的准确性。当前教育信息化背景下，学生心理健康监测需求迫切，但现有方法存在时效性差、主观性强、难以规模化等问题，限制了其在校园环境的普及。<br><br>
      
      针对上述挑战，本文提出并实现了一套基于<strong>ESP32</strong>与<strong>ESP32S3</strong>硬件平台，结合轻量化多模态融合算法及<strong>大语言模型</strong>的学生情感智能分析与监测系统。该系统旨在利用低成本、高集成度的嵌入式技术，融合面部、语音、心率等多源数据，为教育工作者、家长及学生提供实时、准确、便捷的情感监测与支持工具。<br><br>
      
      在硬件层面，采用ESP32与ESP32S3双主板分布式架构。ESP32主板集成ESP32CAM、心率传感器等，实现面部表情识别、生理数据采集及基础反馈；ESP32S3主板集成数字麦克风、音频功放、显示屏等，实现基于百度<strong>文心一言API</strong>的智能对话功能。软件层面，基于Node.js构建服务端，采用SQLite进行数据存储，开发了面向教师、学生、家长的多角色Web应用界面。算法层面，设计了基于<strong>Deepface</strong>的面部情绪识别、基于文心一言API的语音情感分析，设计了动态权重决策级多模态融合算法，并引入基于数据量的多模型情绪趋势预测方法。同时，利用提示词优化了大模型在情感支持对话任务中的表现。<br><br>
      
      设计完成后，完成了系统硬件平台的搭建与调试，并对软件系统进行了全面的功能测试与验证，包括白盒测试与黑盒测试。测试结果表明，系统各模块运行稳定，功能符合设计要求，能够有效整合多模态数据进行学生情感状态分析与监测，验证了该设计的可行性与有效性。<br><br>
      
      <strong>关键词：</strong>多模态情感分析；学生情感监测；ESP32；大语言模型；数据融合
    </div>
  </div>
- *2018.09 - 2021.06*, 普通高中, 韶关市翁源中学

# 📖 研究课题
<span class='anchor' id='-research-topics'></span>
- *2023.05-2024.05*, "基于高斯树的MIMO系统检测算法研究与实现", 大学生创新创业计划项目, **主持**。(项目已结项)
- *2024.01-2026-01*, "基于深度学习的多模态数据融合细粒度情感分析研究", 广东省科技创新战略资金, 45,000元, **主持**。(项目已结项)
- *2024.05-2025.05*, "神经侦探：用于神经退行性疾病诊断的可解释多模态对比学习框架", 大学生创新创业计划项目, **主持**。(项目已结项)
- *2024.05-2025.05*, "DASAM：用于数字桑基鱼塘的通用农业视觉大模型", 国家级大学生创新创业计划项目, 参与。(项目已结项)
- *2025.05-2026.05*, "基于混合专家模型（MoE）的阿尔茨海默病早期诊断系统", 省级大学生创新创业计划项目, 第二参与人。
- *2025.05-2026.05*, "扩散模型赋能多模态决策：突破罕见病医学图像短缺的瓶颈AI辅助诊断平台", 大学生创新创业计划项目, 第二参与人。

# ©️ 专利与版权
<span class='anchor' id='-patents-and-copyrights'></span>
- *2026*, "一种基于视觉感知与特征解耦的两阶段甲骨文识别方法", 专利（已受理）
- *2025*, "基于扩散模型影像合成的多模态疾病诊断软件 V1.0", 中国软件著作权, 2025SR1592713, 第一完成人
- *2025*, "基于多模态大语言模型的学生情感智能分析系统平台 V1.0", 中国软件著作权, 2025SR1585138, 第一完成人
- *2025*, "基于深度学习的批量甲骨文在线识别平台V1.0", 中国软件著作权, 2025SR0968056
- *2024*, "基于Flask的医学图像分割平台V1.0", 中国软件著作权, 2024SR0877362
- *2023*, "医学葡聚糖信息检测系统V1.0", 中国软件著作权, 2023SR1635698
- *2023*, "基于声波感知的多臂障碍物检测与运动规划软件V1.0", 中国软件著作权, 2023SR1657692
