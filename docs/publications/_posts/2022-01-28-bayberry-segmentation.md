---
title: 基于多模块卷积神经网络的复杂环境下杨梅分割
tags:
  - SCI
thumbnail_type: png
---
目前果园自动采摘系统主要依靠机器视觉从背景中分割果实，但大多数现有的方法仅局限于光照强度固定且果实无遮挡的环境，对于光照变化大、重叠遮挡严重的杨梅生长环境仍难以推广应用。为此，提出了基于多模块卷积神经网络的复杂环境杨梅分割方法。通过构建基于图像校正的卷积神经网络和基于puzzle算法的形状补全模块，提高了模型对自然环境光照的鲁棒性并克服了果实重叠遮挡问题。通过实际环境数据验证，杨梅果实的语义分割和实例分割的平均精度分别达到0.913和0.755，对果园自动采摘具有重要意义。


## 数据增强示例
{: .text-center}

{: .text-center}
![Examples of the data augmentation]({{ site.baseurl }}/assets/images{{ page.url }}/1.png){: .w-75}


## 算法总体方案
{: .text-center}

{: .text-center}
![Overall scheme of the proposed method]({{ site.baseurl }}/assets/images{{ page.url }}/2.png){: .w-75}


## Puzzle算法流程
{: .text-center}

{: .text-center}
![The flow of the puzzle algorithm]({{ site.baseurl }}/assets/images{{ page.url }}/3.png){: .w-75}


## 不同语义分割方法的效果展示
{: .text-center}

{: .text-center}
![Visual results of different semantic segmentation methods]({{ site.baseurl }}/assets/images{{ page.url }}/4.png){: .w-75}


## 不同实例分割方法的效果展示
{: .text-center}

{: .text-center}
![Visual results of different instance segmentation methods]({{ site.baseurl }}/assets/images{{ page.url }}/5.png){: .w-75}


## 不同现实复杂环境下的结果展示
{: .text-center}

{: .text-center}
![Segmentation results in different real-life environments]({{ site.baseurl }}/assets/images{{ page.url }}/6.png){: .w-75}
