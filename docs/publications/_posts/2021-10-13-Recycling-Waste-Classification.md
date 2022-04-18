---
title:  便携式设备上基于Vision Transformer的废物分类回收
tags:
  - SCI
thumbnail_type: png
---
由于废物种类繁多，依靠人工分类废物和回收可回收资源将成本高昂且效率低下。近年基于卷积神经网络（CNN）的可回收垃圾自动分类已成为垃圾回收的主流方法。然而，由于CNN感受野的限制，分类的准确性已达到了瓶颈，这限制了相关方法和系统的实施。为了解决上述挑战，提出了一种基于自注意机制的深度神经网络结构，即Vision Transformer，以提高自动分类的准确性。在垃圾网数据集上的实验结果表明，该方法的准确率最高可达96.98%。通过部署到便携式设备，可方便地实现垃圾自动分类，这拓宽了垃圾自动分类的应用范围，对资源节约和回收具有重要意义。


## 算法总体方案
{: .text-center}

{: .text-center}
![Overall scheme of the proposed method]({{ site.baseurl }}/assets/images{{ page.url }}/1.png){: .w-75}


## VIT算法架构
{: .text-center}

{: .text-center}
![Structure of vision transformer]({{ site.baseurl }}/assets/images{{ page.url }}/2.png){: .w-75}


## 自注意机制的可视化展示
{: .text-center}

{: .text-center}
![Visualization of self-attention mechanisms]({{ site.baseurl }}/assets/images{{ page.url }}/3.png){: .w-75}

{: .text-center}
![Visualization of self-attention mechanisms]({{ site.baseurl }}/assets/images{{ page.url }}/4.png){: .w-75}
