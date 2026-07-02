# PROGRESS — 進捗と再開情報

> このファイルは自律構築ループの SSoT。毎ループ末尾に更新する。
> 状態: ✅ 完了 / 🔨 進行中 / 📋 未着手

最終更新: 2026-07-02(Loop 4 完了時点)

## フェーズ進捗

| フェーズ | 状態 | 備考 |
|---|---|---|
| Phase 1 設計(ガバナンス文書) | ✅ | 12 文書 |
| Phase 2 基盤(骨格・index・overview) | ✅ | 69 md ファイル体制 |
| Phase 3 A1–A2 本編 | ✅ | A1 14 章 + A2 13 章(全章に練習・解答・テスト) |
| Phase 4 B1–B2 本編 | 📋 | 次ループの最優先 |
| Phase 5 C1–C2 本編 | 📋 | |
| Phase 6 専門セクション拡張 | 🔨 | grammar 3 本・core-500 のみ完了。medical/business/culture/history の各章は未執筆 |
| Phase 7 品質レビュー | 🔨 | 毎ループの機械検査+抽出レビューは実施済み。ネイティブレビューは未 |
| Phase 8 仕上げ | 📋 | |

## 作成済みファイル(2026-07-02 時点・69 ファイル)

- ガバナンス 12: README / LICENSE / CONTRIBUTING / CHANGELOG / ROADMAP / STYLE_GUIDE / SOURCE_POLICY / QUALITY_CHECKLIST / cefr-map / study-plan / bibliography / PROGRESS
- 00-orientation 4 / レベル overview 6 / セクション index 15 / tools 2
- **01-a1: 全 14 章 ✅** / **02-a2: 全 13 章 ✅**
- grammar: articles / present-tense / past-tenses
- vocabulary: core-500 ハブ + 4 分冊(496 語)

## 未完了・次にやるべきこと(優先順)

1. **B1 本編 13 章**(03-b1/01〜12)— 接続法・条件法・半過去の導入章は grammar/subjunctive.md, conditional.md を先に書いてアンカーにすると品質が安定する(A2 で past-tenses.md を先行させた方式の踏襲)
2. grammar/ 続き: subjunctive / conditional / nouns / gender / cases / pronouns(B1 で必要になる順)
3. medical/ の基幹 3 章: overview(制度は出典必須)/ anatomy / symptoms — A2 第7章から `medical/*.md` への参照をリンク化する
4. business/ overview + emails(B1 の business-email-b1 のアンカー)
5. vocabulary/core-1000(A2→B1 の語彙目標)
6. B2 → C1 → C2 本編(各レベル、章執筆 → 総復習 → 解答 → テスト → 橋渡しの順)
7. culture/ history/ 全章(**WebSearch で出典確認してから執筆** — SOURCE_POLICY 厳守)
8. reading/ listening/ speaking/ writing/ idioms/ verb-conjugation/ exercises/ answer-key/ glossary/ の各章
9. 全体そろい後: Phase 7 横断品質レビュー(ネイティブチェック依頼を CONTRIBUTING 経由で募る)

## 品質上の懸念(オープン — ネイティブ確認推奨リスト)

執筆エージェントが自己申告した「確信度がやや低い」箇所。誤りと確認されたものではない。

- 02-a2/07: Mă doare în gât(în あり形)の頻度感 / De azi-dimineață のハイフン / 112 通報の実務慣習
- 02-a2/08: Te pup・Toate cele bune のレジスター境界(親密度ライン)
- 02-a2/01: 再帰動詞 a se îmbrăca の活用(mă îmbrac — 標準形で記載済み、念のため)
- 02-a2/02: チップ 10% 目安・ciorbă/supă の区別などの文化記述(「目安」表現で緩衝済み)
- 01-a1/07: brânzeturi / cărnuri(種類複数)の語彙表掲載の妥当性、口語数詞縮約 -șpe の地域差
- 04 章の o să 3 人称形(meargă/vină/plece/facă/aibă/fie)— 標準形として正しいはずだが最終校閲対象
- IPA 全般: 二重母音の半母音表記(o̯a/wa 等)の流派統一は Phase 7 で一括点検

## 出典確認が必要な箇所(オープン)

- 00-orientation/03: ルーマニア語話者数(要出典マーク付きで保守的表現にしてある — INS/EU 統計で確定する)
- culture/ history/ の執筆時: 全事実に SOURCE_POLICY 準拠の出典が必要(未執筆)
- medical/overview 執筆時: ルーマニア医療制度(CNAS)・EHIC は公式サイトで確認

## 再開用プロンプト

```markdown
あなたは前回から引き続き、`/home/sasame/romanian-complete-textbook-ja`
(GitHub: shigeki7777/romanian-complete-textbook-ja) の
「日本語話者向けルーマニア語完全教科書」構築を担当する Fable 5 です。

前回までの進捗: A1 全14章・A2 全13章・参照文法3本(articles/present-tense/
past-tenses)・語彙 core-500(496語)・全ガバナンス文書が完成済み(69ファイル、
検証スクリプト green、全て GitHub に push 済み)。

1. まず本ファイル(PROGRESS.md)と STYLE_GUIDE.md / QUALITY_CHECKLIST.md を読む
2. 「未完了・次にやるべきこと」の 1 番(B1 本編)から自律実行ループを再開する。
   手順: grammar/subjunctive.md と conditional.md を先に執筆(Opus 委任+検査)
   → B1 章 01〜08 を 2〜3 エージェントに並列委任(章ごとの使用可能文法リストを
   プロンプトに明示)→ 09〜12(総復習/解答/テスト/橋渡し)は全章完成後に
   1 エージェントで整合執筆 → cefr-map リンク化
3. 執筆規約: STYLE_GUIDE 章テンプレート厳守 / コンマ付き ș・ț / IPA 強勢必須 /
   委任成果は必ず抽出検査(特に IPA の強勢位置・語末 -i の口蓋化・活用形)
   / サブエージェントに commit させず親が一括 commit+push(頻繁に)
4. 各ループ末尾: python3 tools/validate-markdown.py と tools/check-links.py を
   実行 → 修正 → cefr-map/CHANGELOG/PROGRESS 更新 → commit+push → 継続判定
5. 歴史・制度・統計は SOURCE_POLICY に従い WebSearch で出典確認してから書く
6. 「品質上の懸念」リストは消し込まず蓄積する(Phase 7 の一括ネイティブ
   レビューの入力になる)

完成条件を満たすまで自律実行ループを継続してください。
```
