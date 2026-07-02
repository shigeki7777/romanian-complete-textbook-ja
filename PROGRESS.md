# PROGRESS — 進捗と再開情報

> このファイルは自律構築ループの SSoT。毎ループ末尾に更新する。
> 状態: ✅ 完了 / 🔨 進行中 / 📋 未着手

最終更新: 2026-07-02(A1〜C2 全レベル本編完成時点)

## フェーズ進捗

| フェーズ | 状態 | 備考 |
|---|---|---|
| Phase 1 設計(ガバナンス文書) | ✅ | 12 文書 |
| Phase 2 基盤(骨格・index・overview) | ✅ | |
| Phase 3 A1–A2 本編 | ✅ | A1 14 章 + A2 13 章 |
| Phase 4 B1–B2 本編 | ✅ | B1 13 章 + B2 12 章 |
| Phase 5 C1–C2 本編 | ✅ | C1 12 章 + C2 11 章 |
| Phase 6 専門セクション拡張 | 🔨 | 下記「未完了」参照 — 基幹章のみ完了 |
| Phase 7 品質レビュー | 🔨 | 機械検査+抽出レビューは毎ループ実施。横断ネイティブレビューは未 |
| Phase 8 仕上げ | 📋 | |

## 完成済み(2026-07-02 時点・130 md ファイル・約 40,000 行)

- **レベル別本編 75 章すべて**(A1:14 / A2:13 / B1:13 / B2:12 / C1:12 / C2:11)— 各レベルに overview・文法・会話・読解・作文・練習・解答・チェックポイントテスト・橋渡しの完全な学習列
- ガバナンス 12 / orientation 4 / セクション index 15 / tools 2
- grammar/ 7 本(articles, present-tense, past-tenses, subjunctive, conditional, cases, pronouns)
- vocabulary/ core-500(496語)+ core-1000(491語)
- medical/ 3 本(overview, anatomy, symptoms — 出典付き)
- business/ 2 本(overview, emails)
- history/ 2 本(overview, language-history — 出典付き)+ culture/ 1 本(romania-and-moldova — 出典付き)

## 未完了・次にやるべきこと(優先順)

1. **medical/ 残り 9 章**: diagnosis, hospital-dialogues, patient-interview, medication, emergency, informed-consent, medical-interpretation, medical-documents, japanese-romanian-medical-glossary(C1/C2 の医療章が「送り先」として参照済み — 被参照の解消が急務)
2. **business/ 残り 12 章**: etiquette, meetings, presentations, negotiation, contracts, startups, sales, hr, finance, consulting, cross-cultural-communication(B2/C2 の該当章と整合させる)
3. **grammar/ 残り 21 本**: phonetics-and-orthography, nouns, gender, adjectives, numerals, verbs-overview, future-tenses, imperative, infinitive-gerund-participle, reflexive-verbs, modal-verbs, prepositions, conjunctions, word-order, negation, questions, relative-clauses, subordinate-clauses, reported-speech, discourse-markers, advanced-syntax
4. **verb-conjugation/ 全 7 本**(essential-100-verbs が最優先)
5. **vocabulary/ 残り**: core-3000, core-5000, テーマ別 13 本(daily-life〜slang-and-colloquial)
6. **reading/ listening/ speaking/ writing/ idioms/ exercises/ answer-key/ glossary/ の各章**(本編が参照する graded-readers 系から)
7. **culture/ 残り 10 章 + history/ 残り 8 章**(WebSearch 出典必須)
8. **Phase 7**: 横断品質レビュー(IPA 表記の流派統一・章間重複チェック・ネイティブレビュー募集)
9. **Phase 8**: README 更新(完成状況の反映)・全体索引・最終検査

## 品質上の懸念(オープン — ネイティブ確認推奨リスト)

各執筆エージェントの自己申告(誤り確定ではない)。Phase 7 で一括処理する。

- IPA: 二重母音の半母音表記(o̯a 等)の流派統一 / autonom の音節境界 / 各章の個別報告分
- A2: Te pup・Toate cele bune のレジスター境界 / brânzeturi・cărnuri の掲載妥当性 / チップ 10% 目安
- B1: punctele dumneavoastră forte の語順 / câte 配分用法 / 面接定型の地域差
- B2: ar urma să の報道頻度 / cafeluță の DOOM3 正形 / 俗語 a da colțul・lovele の世代差
- C1: anterior + 与格の硬さ / 縮約形の等位接続 / dânsul の地域差記述
- C2: suna a vecernie / Se au în vedere măsuri(意図的な limbaj de lemn 見本)/ halal treabă の皮肉専用度 / banc 自作 2 本の自然さ / beton・mișto 等俗語の世代注記
- 出典: Britannica/Wikipedia 依拠の通史事実を政府・学術一次出典へ順次置換(bibliography.md の注記参照)/ 話者数の確定(INS/statistica.gov.md)

## 出典確認が必要な箇所(オープン)

- 00-orientation/03 の話者数(要出典マーク済み)
- culture/ history/ の残り章はすべて執筆時に WebSearch 出典確認が必要

## 再開用プロンプト

```markdown
あなたは前回から引き続き、`/home/sasame/romanian-complete-textbook-ja`
(GitHub: shigeki7777/romanian-complete-textbook-ja) の
「日本語話者向けルーマニア語完全教科書」構築を担当する Fable 5 です。

前回までの進捗: A1〜C2 の全レベル本編 75 章が完成(検証 green・push 済み)。
参照文法 7 本・core-500/1000・medical/business/history/culture の基幹章も完成。

1. まず本ファイル(PROGRESS.md)と STYLE_GUIDE.md を読む
2. 「未完了・次にやるべきこと」の 1 番(medical/ 残り 9 章)から再開する。
   委任パターン: 高精度領域(医療・法務・文法)= Opus / フォーマット駆動
   (語彙表・練習・読解)= Sonnet / Fable は設計・抽出検査・commit のみ
3. 章ごとの「使用可能文法・既習語彙」を親が明示指定し、既存の参照章
   (medical/index.md の役割定義・被参照章)と整合させる
4. 各バッチ末尾: tools/validate-markdown.py + check-links.py → 修正 →
   該当 index リンク化 → cefr-map/CHANGELOG/PROGRESS 更新 → commit+push
5. culture/history は WebSearch で出典確認してから執筆(SOURCE_POLICY)
6. 「品質上の懸念」は消さず蓄積(Phase 7 の一括ネイティブレビュー入力)

完成条件(全セクション執筆+Phase 7-8)を満たすまで自律ループを継続する。
```
