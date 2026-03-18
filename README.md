# GitCode API Plugin

`gitcode-api-skill` 现在作为一个 Claude Code 插件发布，插件名为 `gitcode-api`。

这个插件提供一套 GitCode REST API 技能，包含：

- `skills/gitcode-api/SKILL.md` 中的调用说明
- 完整的 `references/` API 文档索引与 endpoint 页面
- `scripts/gitcode_api.py` 辅助脚本，用于搜索 endpoint 和执行 GitCode API 请求

## 插件结构

```text
gitcode-api-skill/
├── .claude-plugin/plugin.json
└── skills/gitcode-api/
    ├── SKILL.md
    ├── references/
    └── scripts/gitcode_api.py
```

`agents/` 目录已经移除，因为它只对 Codex 场景有意义，不属于 Claude Code 插件发布内容。

## 在 marketplace 中安装

```bash
/plugin marketplace add AndyKong2020/awesome-claude-infra
/plugin install gitcode-api@awesome-claude-infra
```

## 本地开发

搜索 endpoint：

```bash
python3 skills/gitcode-api/scripts/gitcode_api.py search "Create Issue" --limit 5
```

执行 dry-run 请求：

```bash
python3 skills/gitcode-api/scripts/gitcode_api.py request POST /api/v5/repos/{owner}/issues \
  --path owner=my-org \
  --json '{"repo":"my-repo","title":"Bug","body":"Details"}' \
  --dry-run
```

脚本默认从 `GITCODE_TOKEN` 读取 token，也可以用 `--token` 显式传入。
