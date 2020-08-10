# 利用 NI-myDAQ 进行发光二极管伏安特性曲线的测定

## 【实验步骤】

### 硬件系统搭建

在硬件结构上，通过 myDAQ 的模拟输出引脚 AO0 来驱动 LED 发光二极管，电流将流经串联的限流电阻，返回 myDAQ 的数字地（数字地模拟地均可）。另一方面，在 LED 发光二极管和限流电阻两侧分别并联至 myDAQ 的模拟输入引脚来对电压进行采集，其中 AI1+和 AI1-分别接至 LED发光二极管的正负两侧，测量其电压降；AI0+和 AI0-分别接至限流电阻的两侧，利用欧姆定律来测量流过的电流。实验接线图如图 3，实际硬件接线如图 4 所示：


![](6]RX9IEWHVSOREB9PCEH6G2.png)
*发光二极管伏安特性测试接线图*

### 程序设计
该程序需由三个部分组成，即：  
1)．输入电压源部分  
2)．电流测量部分  
3)．电压降测量部分