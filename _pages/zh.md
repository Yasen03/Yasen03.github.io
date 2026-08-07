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

我目前在清华大学深圳国际研究生院（SIGS）攻读硕士学位。我的研究兴趣主要集中在 <span class="paper-badge-text" style="background-color: #6B7A99;">AI生成音视频检测（内容安全）</span> 和 <span class="paper-badge-text" style="background-color: #4A7C8C;">世界模型</span>。欢迎就相关方向合作交流。

联系方式：[yueshenghuang@stu.gpnu.edu.cn](mailto:yueshenghuang@stu.gpnu.edu.cn) | <a href="/">English</a> / <strong>中文</strong>

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
<div class="paper-title">Affective-CoT: Decomposing Multimodal Emotion Reasoning through a Hierarchical Cognitive Workflow（🏆 MER2025-DES Champion）</div>
  
**Yuesheng Huang**, Jinming Liu, Jiajia Chen, Yihang Lin, Yanmei Chen<sup>*</sup>, Jianwei Dong

<div class="paper-meta">ACM MM 2025 Main Conference Grand Challenge Track（Oral）</div>
<div class="paper-links">
  <a class="paper-badge" href="https://dl.acm.org/doi/10.1145/3695952.3731175"><img src="https://img.shields.io/badge/Paper-ACM%20DL-0071C5" alt="ACM DL"></a>
  <button type="button" class="paper-badge-text citation-trigger" onclick="toggleCitation('citation-acmmm2025-zh', event)">引用</button>
  <a class="paper-badge" href="https://scholar.google.com/citations?user=edyJPQQAAAAJ"><img id="citation-badge-affective-cot-zh" src="https://img.shields.io/badge/Citations-1-blue?style=social&logo=google-scholar" class="paper_citations" data-paper-id="manual:affective-cot-2025" alt="Scholar Citations"></a>
</div>
<div id="citation-acmmm2025-zh" class="citation-popup">
  <div class="citation-format-container">
    <div class="citation-format-label">BibTeX</div>
    <div class="citation-format">@inproceedings{huang2025affective, <br>      title={Affective-CoT: Decomposing Multimodal Emotion Reasoning through a Hierarchical Cognitive Workflow}, <br>      author={Huang, Yuesheng and Liu, Jinming and Chen, Jiajia and Lin, Yihang and Chen, Yanmei and Dong, Jianwei}, <br>      booktitle={Proceedings of the 33rd ACM International Conference on Multimedia}, <br>      pages={13848--13855}, <br>      year={2025} <br>}</div>
  </div>
</div>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">MRAC@ACM MM</div><img src='{{ site.baseurl }}/images/DARE.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
<div class="paper-title">DARE to Disagree: A Multi-Agent Adversarial Debate Framework for Open-Vocabulary Multimodal Emotion Recognition</div>
  
**Yuesheng Huang**, Meiqi Feng, Zhenming He, Yueyuan Peng, Jiawen Li<sup>*</sup>

<div class="paper-meta">ACM MM 2025 MRAC Workshop（Oral）</div>
<div class="paper-links">
  <a class="paper-badge" href="https://dl.acm.org/doi/10.1145/3706591.3706600"><img src="https://img.shields.io/badge/Paper-ACM%20DL-0071C5" alt="ACM DL"></a>
  <a class="paper-badge" href="https://github.com/GPNU-AIoT/DARE"><img src="https://img.shields.io/github/stars/GPNU-AIoT/DARE?style=social" alt="GitHub Stars"></a>
  <button type="button" class="paper-badge-text citation-trigger" onclick="toggleCitation('citation-dare2025-zh', event)">引用</button>
  <a class="paper-badge" href="https://scholar.google.com/citations?user=edyJPQQAAAAJ"><img id="citation-badge-dare-zh" src="https://img.shields.io/badge/Citations-1-blue?style=social&logo=google-scholar" class="paper_citations" data-paper-id="manual:dare-2025" alt="Scholar Citations"></a>
</div>
<div id="citation-dare2025-zh" class="citation-popup">
  <div class="citation-format-container">
    <div class="citation-format-label">BibTeX</div>
    <div class="citation-format">@inproceedings{huang2025dare, <br>      title={DARE to Disagree: A Multi-Agent Adversarial Debate Framework for Open-Vocabulary Multimodal Emotion Recognition}, <br>      author={Huang, Yuesheng and Feng, Meiqi and He, Zhenming and Peng, Yueyuan and Li, Jiawen}, <br>      booktitle={Proceedings of the 3rd International Workshop on Multimodal and Responsible Affective Computing}, <br>      pages={41--50}, <br>      year={2025} <br>}</div>
  </div>
</div>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML NewInML</div><img src='{{ site.baseurl }}/images/fig1.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
<div class="paper-title">Synthetic Perception: Can Generated Images Unlock Latent Visual Prior for Text-Centric Reasoning?</div>
  
**Yuesheng Huang**<sup>*</sup>, Peng Zhang, Xiaoxin Wu, Riliang Liu, Jiaqi Liang

<div class="paper-meta">ICML 2025 NewInML Workshop（Poster）</div>
<div class="paper-links">
  <a class="paper-badge" href="https://arxiv.org/abs/2506.17623"><img src="https://img.shields.io/badge/Paper-arXiv-B31B1B" alt="arXiv"></a>
  <button type="button" class="paper-badge-text citation-trigger" onclick="toggleCitation('citation-arxiv2025-zh', event)">引用</button>
  <a href="https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=edyJPQQAAAAJ&citation_for_view=edyJPQQAAAAJ:W7OEmFMy1HYC"><img id="citation-badge-generated-images-zh" src="https://img.shields.io/badge/Citations-loading-6c757d" class="paper_citations" data-paper-id="edyJPQQAAAAJ:W7OEmFMy1HYC" alt="Scholar Citations"></a>
</div>
<div id="citation-arxiv2025-zh" class="citation-popup">
  <div class="citation-format-container">
    <div class="citation-format-label">BibTeX</div>
    <div class="citation-format">@misc{huang2025syntheticperception,<br>      title={Synthetic Perception: Can Generated Images Unlock Latent Visual Prior for Text-Centric Reasoning?}, <br>      author={Yuesheng Huang and Peng Zhang and Xiaoxin Wu and Riliang Liu and Jiaqi Liang},<br>      year={2025},<br>      eprint={2506.17623},<br>      archivePrefix={arXiv},<br>      primaryClass={cs.MM},<br>      url={https://arxiv.org/abs/2506.17623}, <br>}</div>
  </div>
</div>
</div>
</div>

- **Sentiment Analysis Using E-Commerce Review Keyword-Generated Image with a Hybrid Machine Learning-Based Model.** Jiawen Li, **Yuesheng Huang**, Yayi Lu, Leijun Wang\*, Yongqi Ren, Rongjun Chen. *Computers, Materials & Continua*, 2024. [[论文](https://www.techscience.com/cmc/v80n1/57421)] <a href="https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=edyJPQQAAAAJ&citation_for_view=edyJPQQAAAAJ:d1gkVwhDpl0C"><img class="paper_citations" data-paper-id="edyJPQQAAAAJ:d1gkVwhDpl0C" src="https://img.shields.io/badge/Citations-25-blue?style=social&logo=google-scholar" alt="Scholar Citations"></a>
- **An Improved Hybrid CNN-LSTM-Attention Model with Kepler Optimization Algorithm for Wind Speed Prediction.** **Yuesheng Huang**, Jiawen Li\*, Yushan Li, Routing Lin, Jingru Wu, Leijun Wang, Rongjun Chen. *Engineering Letters*, 2024. [[论文](https://www.engineeringletters.com/issues_v32/issue_10/EL_32_10_14.pdf)] [[代码](https://github.com/Yasen03/KOA-CNN-LSTM-Attention)] <a href="https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=edyJPQQAAAAJ&citation_for_view=edyJPQQAAAAJ:2osOgNQ5qMEC"><img class="paper_citations" data-paper-id="edyJPQQAAAAJ:2osOgNQ5qMEC" src="https://img.shields.io/badge/Citations-12-blue?style=social&logo=google-scholar" alt="Scholar Citations"></a>

# 🏆 竞赛获奖
<span class='anchor' id='-honors-and-awards'></span>
- *2025.08* **ACM MM 2025 MER Challenge（DES Track）冠军**（团队负责人）。
- *2024.05* **美国大学生数学建模竞赛（MCM/ICM）**E题**Finalist奖**（全球**前2%**），COMAP。
- *2023.11* 中国大学生数学建模竞赛广东赛区**一等奖**。
- *2023.08* 中国大学生计算机设计大赛广东赛区**一等奖**。
- *2021.12* Kaggle Lux AI竞赛**银牌**。

# 🎓 教育背景
<span class='anchor' id='-educations'></span>
- *2026 - 2028*, 硕士研究生，清华大学深圳国际研究生院（SIGS）。
- *2021.09 - 2025.06*, 物联网工程 工学学士学位（**ESI前1%**）, 计算机科学学院, 广东技术师范大学（**优秀毕业生**）。（**GPA:92.1/100, 排名:1/111**）
- *2018.09 - 2021.06*, 普通高中, 韶关市翁源中学

# 📖 研究课题
<span class='anchor' id='-research-topics'></span>
- *2023.05-2024.05*, "基于高斯树的MIMO系统检测算法研究与实现", 大学生创新创业计划项目, **主持**。(项目已结项)
- *2024.01-2026-01*, "基于深度学习的多模态数据融合细粒度情感分析研究", 广东省科技创新战略资金, 45,000元, **主持**。(项目已结项)
- *2024.05-2025.05*, "神经侦探：用于神经退行性疾病诊断的可解释多模态对比学习框架", 大学生创新创业计划项目, **主持**。(项目已结项)
- *2024.05-2025.05*, "DASAM：用于数字桑基鱼塘的通用农业视觉大模型", 国家级大学生创新创业计划项目, 参与。(项目已结项)
