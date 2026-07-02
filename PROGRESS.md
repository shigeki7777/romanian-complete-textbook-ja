# PROGRESS — 進捗と再開情報

> このファイルは自律構築ループの SSoT。毎ループ末尾に更新する。
> 状態: ✅ 完了 / 🔨 進行中 / 📋 未着手

最終更新: 2026-07-02(Loop 1)

## フェーズ進捗

| フェーズ | 状態 | 備考 |
|---|---|---|
| Phase 1 設計(ガバナンス文書) | ✅ | 11 文書 |
| Phase 2 基盤(骨格・index・overview) | 🔨 | Loop 1 で完了予定 |
| Phase 3 A1–A2 本編 | 🔨 | A1 14 章 → Loop 2 |
| Phase 4 B1–B2 本編 | 📋 | |
| Phase 5 C1–C2 本編 | 📋 | |
| Phase 6 専門セクション拡張 | 📋 | |
| Phase 7 品質レビュー | 📋 | 毎ループの部分レビューは実施 |
| Phase 8 仕上げ | 📋 | |

## 作成済みファイル

- ガバナンス: README / LICENSE / CONTRIBUTING / CHANGELOG / ROADMAP / STYLE_GUIDE / SOURCE_POLICY / QUALITY_CHECKLIST / cefr-map / study-plan / bibliography / PROGRESS
- (以後、各ループで追記)

## 未完了・次にやるべきこと(優先順)

1. 全セクション index.md(15 本)+ 00-orientation(4 本)+ レベル overview(6 本)
2. tools/check-links.py + tools/validate-markdown.py
3. A1 本編 14 章(01〜13)
4. A2 本編 13 章
5. grammar/ コア章(articles, nouns, gender, present-tense, verbs-overview)
6. medical/business/culture/history の overview 章(出典調査込み)
7. vocabulary/core-500
8. B1 以降

## 品質上の懸念(オープン)

- (なし — 発生時にここへ記録)

## 出典確認が必要な箇所(オープン)

- (なし — 「要出典」を付けた箇所をここへ登録)

## 再開用プロンプト

```markdown
あなたは前回から引き続き、`/home/sasame/romanian-complete-textbook-ja`
(GitHub: shigeki7777/romanian-complete-textbook-ja) の
「日本語話者向けルーマニア語完全教科書」構築を担当する Fable 5 です。

1. まず本ファイル(PROGRESS.md)と STYLE_GUIDE.md / QUALITY_CHECKLIST.md を読む
2. 「未完了・次にやるべきこと」の先頭タスクから自律実行ループを再開する
3. 執筆は STYLE_GUIDE の章テンプレート厳守。委任時は STYLE_GUIDE §4-5 を
   プロンプトに添付し、成果物を必ず検査してから親が一括 commit + push する
4. 各ループ末尾: 品質レビュー → 修正 → cefr-map/CHANGELOG/PROGRESS 更新 →
   commit + push → 継続判定
5. 歴史・制度・統計は SOURCE_POLICY に従い出典を確認してから書く
```
