<img src="assets/logo.svg" width="96">

# ResearchOS

**让 AI 助手不再被你的项目绕晕，也让每个结果都有据可查。**

可追溯、可审计、面向 AI 的科研工作区。

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
![Works with Claude Code, Codex, and Cursor](https://img.shields.io/badge/works%20with-Claude%20Code%20%C2%B7%20Codex%20%C2%B7%20Cursor-555.svg)

[English README](README.md)

ResearchOS 是面向 AI 的科研工作区，也是一个 GitHub 项目模板。一个文件夹对应一个研究项目。它给 AI 一套固定的项目结构，并把论文主张、研究结论、实验，以及实际运行的代码、数据和配置连成一条证据链。你判断科学问题，AI 维护文件和记录。

## 你可能遇到过这些问题

- AI 写了 30 个脚本。现在到底该用哪一个？
- 你找到一张图，却不知道它来自哪份数据和哪组配置。
- AI 很肯定地引用一个结果，但后来的实验早已替代它。
- 审稿人追问某个数字的来源，你却无法说明 AI 是怎样算出它的。

## 你会得到什么

- 研究问题、假设、数据说明、代码、实验、结论、论文主张、决策和参考文献各有固定位置。
- 实验流程会在运行前写下预期，并记录准确命令、输入、配置、结果和适用范围。
- 每个实验都保存当时实际使用的代码和配置；当前可复用代码则统一放在 `src/`。
- 论文主张通过链接追溯到实验记录和输出。
- 六套现成流程分别负责初始化、帮助、实验、审计、状态查看和安全整理。

## 30 秒开始

你需要安装 [Git](https://git-scm.com/)，还需要一个能读写本地文件的 AI 编程助手：Claude Code、Codex CLI 或 Cursor。

### 把这段话发给你的 AI

> 把 `https://github.com/TravisCao/research-os` 克隆到一个以我的项目命名的文件夹。删除克隆项目中的 `.git` 文件夹，运行 `git init`，并创建第一次提交。阅读 `AGENTS.md`，然后按照 `.claude/skills/welcome/SKILL.md` 开始欢迎访谈。需要我操作时，请用通俗语言说明。

剩下的设置由 AI 完成。

## 支持的 AI 编程助手

- **Claude Code：** 在 Claude Code 中打开项目文件夹，然后说：“开始 welcome 访谈。”
- **Codex：** 把项目文件夹添加到 Codex，然后说：“开始 welcome 访谈。”

### 或使用 GitHub 模板

1. 打开 GitHub 上的 [ResearchOS](https://github.com/TravisCao/research-os)，选择 **Use this template**。
2. 在新项目文件夹中打开 AI 编程助手。
3. 对它说：“开始 welcome 访谈。”

## 前 10 分钟可以做什么

1. 完成欢迎访谈。AI 会填写项目说明、术语表和你的工作偏好。
2. 用日常语言描述你要验证的想法：“我想检验……”
3. 让 AI 把它作为一项有记录的实验来运行。AI 先写预期，再执行命令，最后保存结果和实际使用的文件。
4. 问：“关于我的假设，我们现在有哪些证据？每个结果是怎样产生的？”
5. 说：“审计这个项目。”AI 会检查缺失的证据、来源不明的图、不完整的记录和仍在引用的旧结果。

你现在就可以查看随模板提供的 [E001 示例](experiments/001-first-example/EXPERIMENT.md)。它用生成的步数数据展示一份完整实验记录。如果想先看一次完整的操作过程，请阅读[带注释的演示记录](docs/demo-transcript.md)。先做到这里。你已经可以判断 ResearchOS 是否适合你。

## 你说什么 → AI 做什么

| 你说 | AI 会做什么 |
|---|---|
| “开始 welcome 访谈。” | AI 最多问七个简短问题，然后填写项目背景。 |
| “帮我理解这个工作区。” | help 流程只解释相关部分，并给出一个下一步。 |
| “我想检验……” | AI 把测试关联到一个假设，并建立带编号的实验记录。 |
| “把这项分析作为实验运行。” | AI 在运行前记录预期和命令，然后记录并链接结果。 |
| “显示研究状态。” | AI 显示研究问题、当前假设、最近三项实验、最新结论和一个下一步。 |
| “审计这个项目。” | AI 检查论文主张、实验、图、旧结果、文件位置、链接和冻结文件。 |
| “整理这个项目。” | AI 先提出安全移动方案并请求一次确认，再移动文件和更新链接，不删除文件。 |
| “frozen code 是什么意思？” | help 流程用通俗语言解释这个概念。 |
| “这张图是从哪里来的？” | AI 检查这张图是否链接到实验输出，并报告缺失的来源。 |

## 模板里有什么

```text
research-os/
├── .claude/skills/          六套任务说明的唯一来源
├── .codex/skills/           让 Codex 使用相同任务说明的链接
├── assets/                  项目说明使用的标志文件
├── docs/                    通俗说明和演示
├── AGENTS.md                所有 AI 编程助手共用的规则
├── CLAUDE.md                引导 Claude Code 读取共用规则
├── CONTRIBUTING.md          贡献要求
├── LICENSE                  MIT 许可证条款
├── PROJECT.md               研究问题、范围、数据和方法
├── README.md                英文安装和入门说明
├── README.zh-CN.md          简体中文安装和入门说明
├── hypotheses.md            当前和已停止使用的可检验假设
├── insights.md              链接到实验的简短结论
├── data/
│   ├── DATA.md              数据来源、内容、改动和限制
│   ├── raw/                 未改动的输入数据
│   └── processed/           从原始数据得到的数据
├── experiments/
│   ├── INDEX.md             每项实验的一行索引
│   └── 001-first-example/   包含代码、配置和输出的完整示例
├── src/                     当前可复用的分析代码
├── manuscript/
│   ├── claims.md            带证据链接的待验证和已支持主张
│   └── figures/             链接到实验输出的图
├── memory/                  决策、项目术语和工作偏好
├── references/              论文和其他资料的索引
└── archive/                 为便于追溯而保留的旧材料
```

## 它怎样保持项目有序

- **先记录，再运行。** 结果出现前，实验文件先写明假设、预期、命令、输入和配置。
- **保存实际运行的文件。** 每项实验都保留执行过的代码和配置副本。
- **明确标记旧结果。** 被替代的实验标为 `superseded`，旧文件移到 `archive/`，而不是直接消失。
- **没有证据，就不写成论文主张。** 每条论文主张必须引用实验编号，每张图必须链接到来源输出。

这些是给 AI 的工作规则，不是绝对保证。研究者仍须判断方法和结论。阅读[用 10 分钟理解你的 AI](docs/concepts.zh-CN.md)，了解这套工作方式。

## 适合谁，不适合谁

ResearchOS 适合任何领域中经常使用 AI 编程助手，并希望清楚记录每个结果来源的研究者。你不需要会编程。

如果团队需要 MLflow 规模的实验追踪、共享计算资源管理或权限控制，ResearchOS 不适合你。如果你从不使用能操作本地文件的 AI 助手，它也无法发挥作用。

## 常见问题

请阅读[常见问题](docs/faq.md)。

## 开发计划

- 自动检查新文件是否归档正确的 hooks。
- 按照证据链接写作的论文写作流程。
- 面向常见研究领域的示例和说明包。
- 在 GitHub 上检查项目的持续集成审计。

以上功能仍在计划中，当前版本尚未提供。

## 许可证

ResearchOS 使用 [MIT License](LICENSE)。
