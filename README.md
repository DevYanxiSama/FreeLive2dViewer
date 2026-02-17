# FreeLive2dViewer 🎭

<img src="https://img.shields.io/badge/license-自定义非商用-blue" alt="License">
<img src="https://img.shields.io/badge/python-3.8+-green" alt="Python">
<img src="https://img.shields.io/badge/live2d-v3-orange" alt="Live2D">
<img src="https://img.shields.io/badge/PyQt5-5.15+-yellow" alt="PyQt5">

**一个开源且免费的 Live2D 模型查看器**，支持拖拽加载、参数实时调节，让你轻松预览和调试 Live2D 模型！

## ✨ 特性

- 📂 **拖拽加载** - 直接将 `.model3.json` 文件拖入即可加载
- 🎮 **参数调节** - 实时调节模型的所有参数（如眨眼、手势等）
- 🖼️ **多模型支持** - 快速切换不同的 Live2D 模型
- 🎯 **简洁界面** - 左侧参数列表，右侧实时预览
- 🪟 **窗口自适应** - 调整窗口大小时模型自动适配

## ⚠️ 重要声明

### 使用限制
- ✅ 允许个人学习、研究、非商业使用
- ✅ 允许基于本项目二次开发
- ❌ **严禁商业使用** - 不得将本项目用于任何商业目的

### 模型版权
本项目不附带任何 Live2D 模型文件。演示图中的模型来自以下 B 站 UP 主：
- **断夏Official** - [B站空间](https://space.bilibili.com/36979456)
- **万童Official** - [B站空间](https://space.bilibili.com/1932040601)

如需使用这些模型，请联系原作者获取授权。

## 🚀 快速开始

### 环境要求
- Python 3.8 或更高版本
- 支持 OpenGL 的显卡

### 安装步骤

1. **克隆或下载本项目**
```bash
git clone https://github.com/DevYanxiSama/FreeLive2dViewer.git
cd FreeLive2dViewer
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **运行程序**
```bash
python Live2dViewer.py
```

## 🎮 使用指南

### 基本操作
1. **启动程序**后，左侧为参数调节区，右侧为模型预览区
2. **加载模型**：将你的 Live2D 模型文件夹中的 `.model3.json` 文件直接拖拽到左侧区域
3. **调节参数**：加载成功后，左侧会列出所有可调节的参数，通过滑块实时调整
4. **预览效果**：右侧会实时显示参数调整后的模型效果

### 支持的模型格式
- Live2D Cubism 3 及以上版本的模型
- 需要完整的模型文件（`.moc3`、纹理图片、`.model3.json`）

## 🖼️ 演示效果

### 竖着大拇指的雪莉
<img width="924" alt="雪莉点赞" src="https://github.com/user-attachments/assets/d397f797-1ac1-4179-bce8-a0a2da923f2e" />

### 挠着头的雪莉
<img width="842" alt="雪莉思考" src="https://github.com/user-attachments/assets/7e4c0255-1bbe-4801-b448-4a8b81888aec" />

> 以上 Live2D 模型来自 **断夏Official** 和 **万童Official**，仅作演示使用。

## 🏗️ 项目结构

```
FreeLive2dViewer/
├── Live2dViewer.py      # 主程序
├── requirements.txt     # 依赖列表
└── README.md           # 说明文档
```

## 🔧 技术实现

本项目基于以下核心技术：
- **[live2d-py](https://github.com/EasyLive2D/live2d-py)** - Python 版的 Live2D 库（MIT 许可证）
- **PyQt5** - 强大的 GUI 框架
- **OpenGL** - 图形渲染

## 🤝 参与贡献

欢迎提交 Issue 和 Pull Request！

### 已知问题
- 目前参数列表会重复添加（正在修复中）
- 某些模型可能不兼容

### 待办功能
- [ ] 参数分组显示
- [ ] 保存/加载参数预设
- [ ] 多语言支持
- [ ] 模型信息显示

## 📄 许可证

本项目采用 **自定义非商业许可证**：

- ✅ 允许自由使用、修改、分发（非商业用途）
- ✅ 允许个人学习和研究
- ✅ 允许基于本项目二次开发
- ❌ **严禁任何形式的商业使用**

### 使用的开源项目
- [live2d-py](https://github.com/EasyLive2D/live2d-py) - MIT 许可证
- PyQt5 - GPL 许可证

## 🙏 致谢

### 开源项目
感谢 [live2d-py](https://github.com/EasyLive2D/live2d-py) 项目，为本工具提供了 Live2D 核心支持。

### 模型创作者
- **断夏Official** - [B站空间](https://space.bilibili.com/36979456)
- **万童Official** - [B站空间](https://space.bilibili.com/1932040601)

感谢两位的优秀创作！

## 📮 联系方式

- 项目主页：[GitHub](https://github.com/DevYanxiSama/FreeLive2dViewer)
- 问题反馈：[提交 Issue](https://github.com/DevYanxiSama/FreeLive2dViewer/issues)

---
**FreeLive2dViewer** - 让 Live2D 模型预览更简单！✨
