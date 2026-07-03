# フルコンジュゲーション表 — 読み方と自作の仕方【対象 CEFR: A1〜C1】

## この参照ページの使い方

このページは活用表そのものの巨大な一覧ではない。**「辞書で2つの形を引けば、残りの全形が自分で導ける」**という手順を身につけるための、いわば活用の「操作マニュアル」である。ルーマニア語の動詞は形が多い(直説法5時制・接続法・条件法・命令法・分詞・動名詞…)が、そのすべてを丸暗記する必要はない。**現在形1人称単数(eu 形)と過去分詞(participiu)の2つ**を押さえれば、規則動詞は全時制が機械的に導ける。このページはその導出のフローと、日本語話者が特につまずく「語幹の交替(語幹母音・子音が活用中に姿を変える現象)」の6パターンを、代表動詞の表で示す。

個々の完全活用表は次の姉妹ページが担当する。ここは重複を避け、それらへの**ハブ(道しるべ)**として機能する。

- 規則動詞の4活用群の語尾表 → [`regular-verbs.md`](./regular-verbs.md)
- 不規則動詞(a fi, a avea, a putea…)の語幹交替 → [`irregular-verbs.md`](./irregular-verbs.md)
- 頻出100動詞の全時制一覧 → [`essential-100-verbs.md`](./essential-100-verbs.md)
- 再帰動詞の再帰代名詞込み活用 → [`reflexive-verb-tables.md`](./reflexive-verb-tables.md)

運用面(「どの時制をいつ使うか」)は [grammar/](../grammar/index.md) が正である。ここは形態面(「その形をどう作るか」)に徹する。

---

## 1. 導出の全体像 — 2つの主要形からすべてが出る

ルーマニア語の規則動詞は、次の**2つの主要形(基本形)**が分かれば、他の全形が規則で導ける。

1. **直説法現在1人称単数(eu 形)** — これが「どの活用型か」を決める鍵。とくに第 I 群(-a)と第 IV 群(-i)は、eu 形を見れば「素の活用」か「拡張活用(-ez / -esc)」かが一目で分かる。
2. **過去分詞(participiu)** — 複合過去・大過去・受動態・完了不定詞がすべてこれを土台にする。

辞書はこの2つを必ず載せている。だから新出動詞に出会ったら、**不定詞・eu 形・過去分詞の3点セット**でメモする習慣をつける。これが本ページ最大の実務助言である。

### 1.1 導出フローチャート

```
辞書で引く: [不定詞] a lucra
   │
   ├─▶ eu 形は?  → lucrez   （-ez で終わる → 第 I 群 -ez 拡張型）
   │       │
   │       ├─ 現在形    : lucrez / lucrezi / lucrează / lucrăm / lucrați / lucrează
   │       ├─ 接続法3人称 : să lucreze （現在3人称 -ă → -e に交替）
   │       ├─ 半過去     : lucram / lucrai / lucra / lucram / lucrați / lucrau
   │       ├─ 命令法2単   : lucrează! （肯定）／ nu lucra!（否定＝不定詞形）
   │       └─ 動名詞     : lucrând
   │
   └─▶ 過去分詞は? → lucrat  （-a 群 → -at）
           │
           ├─ 複合過去   : am / ai / a / am / ați / au + lucrat
           ├─ 大過去     : lucrasem / lucraseși / lucrase …
           ├─ 未来       : voi / vei / va + lucra（不定詞）／ o să lucrez（接続法）
           └─ 条件法     : aș / ai / ar + lucra（不定詞）
```

このフローを一度たどれば、「未来と条件法は不定詞から」「複合過去と大過去は分詞から」「接続法と命令法は現在形から」という**役割分担**が見えてくる。時制ごとに「どの主要形を土台にするか」を下表にまとめる。

| 時制・法 | 土台にする主要形 | 作り方の核 |
|---|---|---|
| 直説法現在 | 語幹(不定詞から -a/-ea/-e/-i を除く) | 人称語尾を付ける(§2) |
| 接続法現在 | 直説法現在 | 3人称のみ -ă↔-e 交替([subjunctive](../grammar/subjunctive.md)) |
| 命令法 | 現在形・不定詞 | 肯定2単は活用形、否定2単は「nu + 不定詞」(§4) |
| 半過去 | 語幹 | -am/-ai/-a/-am/-ați/-au(第 II〜IV は -eam…) |
| 複合過去 | **過去分詞** | a avea 短縮形(am/ai/a/am/ați/au)+ 分詞 |
| 大過去 | **過去分詞の語幹** | -sem/-seși/-se/-serăm/-serăți/-seră |
| 未来(標準) | **不定詞** | voi/vei/va/vom/veți/vor + 不定詞 |
| 条件法 | **不定詞** | aș/ai/ar/am/ați/ar + 不定詞 |
| 動名詞(gerunziu) | 語幹 | -ând(I・語幹末が硬)/ -ind(II〜IV) |

---

## 2. 現在形の語尾 — 型の見分けが9割

現在形は活用群と型(素の活用か拡張活用か)で語尾が決まる。詳細な語尾表は [`regular-verbs.md`](./regular-verbs.md) にあるので、ここでは**型を eu 形で見分ける**要点だけ再掲する(正の解説は [grammar/present-tense.md](../grammar/present-tense.md))。

| 型 | eu 形の目印 | 代表動詞 | eu / tu / el / noi / voi / ei |
|---|---|---|---|
| 第 I 群 素 | 語幹 + `-u` | a intra | intru / intri / intră / intrăm / intrați / intră |
| 第 I 群 -ez | eu 形が `-ez` | a lucra | lucrez / lucrezi / lucrează / lucrăm / lucrați / lucrează |
| 第 IV 群 素 | 語幹のみ(語尾なし) | a dormi | dorm / dormi / doarme / dormim / dormiți / dorm |
| 第 IV 群 -esc | eu 形が `-esc` | a vorbi | vorbesc / vorbești / vorbește / vorbim / vorbiți / vorbesc |

**最重要の注意**: -ez / -esc の拡張は **eu / tu / 3単 / 3複の4か所だけ**に現れ、noi と voi には現れない(lucr**ăm**, vorb**im**)。ここを取り違えて *lucrezăm* などとしないこと。どちらの型かは規則で完全予測できないため、**eu 形をセットで覚える**のが唯一の確実な方法である。

なお外来語・新語由来の第 I 群動詞(-a)は圧倒的に **-ez 型**に入る(a forma→formez, a nota→notez, a fuma→fumez)。専門編の医療・ビジネス動詞([medical-verbs.md](./medical-verbs.md) / [business-verbs.md](./business-verbs.md))はこの傾向が特に強く、a consulta→consult のような素の型は少数派である。

---

## 3. 語幹交替の6パターン — 動詞が「化ける」規則

日本語話者にとって最大の難所は、活用の途中で**語幹そのものの母音や子音が変わる**現象である。日本語の「食べる」はどう活用しても語幹「食べ」が動かないが、ルーマニア語では a dormi(眠る)が d**o**rm と d**oa**rme のように語幹母音を変える。これは不規則ではなく**規則的な交替(alternanță)**であり、6つのパターンに整理できる。「強勢が当たる母音は開く/子音は前舌母音の前で軟らかくなる」という2つの力が働いていると理解すると、丸暗記から解放される。

### 3.1 母音交替(強勢がかかると開く)

強勢(アクセント)が語幹母音に落ちる人称(典型は3人称単数)で、母音が「割れて」開く。

#### パターン① o → oa

| 動詞 | 意味 | eu(弱勢) | el, ea(強勢) | 交替 |
|---|---|---|---|---|
| a dormi | 眠る | dorm | d**oa**rme | o→oa |
| a putea | できる | pot | p**oa**te | o→oa |
| a purta | 身につける | port | p**oa**rtă | o→oa |
| a coborî | 降りる | cobor | cob**oa**ră | o→oa |

強勢が o に落ちると **oa** /o̯a/ に開く。coboară /koˈbo̯a.rə/ のように、強勢のない他の o はそのまま。

#### パターン② e → ea

| 動詞 | 意味 | eu(弱勢) | el, ea(強勢) | 交替 |
|---|---|---|---|---|
| a ședea | 座る | șed | ș**ea**de | e→ea |
| a spăla | 洗う | spăl | sp**a**lă（注) | — |
| a pleca | 発つ | plec | pl**ea**că | e→ea |
| a aștepta | 待つ | aștept | așt**ea**ptă | e→ea |

強勢が e に落ちると **ea** /e̯a/ に開く(pleacă /ˈple̯a.kə/)。接続法・命令ではこの ea がまた e に戻る(să plece)ため、「開いた ea は接続法で閉じる」という往復も一緒に覚える。

### 3.2 母音交替(語末・語尾の影響で閉じる/暗くなる)

#### パターン③ a → ă

語幹末の a が、後ろの語尾によって曖昧母音 ă /ə/ に弱まる。第 I 群でよく起きる。

| 動詞 | 意味 | 不定詞語幹 | 3単現(-ă) | 例 |
|---|---|---|---|---|
| a mânca | 食べる | mânc-/mănânc- | mănân**c**ă | eu mănânc /məˈnɨnk/, noi mâncăm /mɨnˈkəm/ |
| a spăla | 洗う | spăl- | sp**a**lă | a→ă は語幹内の交替(spăl↔spal) |
| a lucra | 働く | lucr- | lucre**a**ză | 3単で -ează |

a mânca は綴りが最難関。eu m**ă**nânc は先頭が ă、noi m**â**ncăm は â。同じ動詞内で ă↔â が入れ替わる(強勢の有無で /ə/ か /ɨ/ か)。

#### パターン④ ă → e

語幹の ă が、前舌母音の語尾(-i, -e)の前で e に上がる。

| 動詞 | 意味 | 交替の起きる形 | 例 |
|---|---|---|---|
| a cădea | 落ちる | cad → cazi（e系語尾で語幹が変わる） | eu cad, tu cazi |
| a apărea | 現れる | apar → apari | ă↔a の揺れも伴う |
| a vedea | 見る | văd → vezi | v**ă**d(1単)→ v**e**zi(2単) |

a vedea の v**ă**d(eu, ei) と ve**zi**(tu)・ve**de**(el) は、ă↔e の交替の代表例である([grammar/present-tense.md](../grammar/present-tense.md) §3.1)。

### 3.3 子音交替(前舌母音 i / e の前で軟音化)

語幹末の子音は、後ろに来る母音が i / e のとき音が軟らかくなる。**綴りは変わらず音だけ変わる**ものと、綴りごと変わるものがある。

#### パターン⑤ t → ț

語幹末の t は、複数語尾 -i や2人称の前で ț /t͡s/ に変わる。**綴りも変わる**。

| 動詞 | 意味 | t のまま | ț に交替 | 例 |
|---|---|---|---|---|
| a simți | 感じる | simt(eu, ei) | sim**ț**i(tu) | eu simt /simt/, tu simți /simt͡sʲ/ |
| a înghiți | 飲み込む | înghit | înghi**ț**i | tu înghiți |
| a se răsti | 食ってかかる | răst | răs**t**ești | -esc 型では別途 |

これは名詞・形容詞の複数形(student→studen**ț**i)と同じ交替で、ルーマニア語全体を貫く規則である。

#### パターン⑥ s → ș

語幹末の s は、同じく前舌母音の前で ș /ʃ/ に変わる。**綴りも変わる**。

| 動詞 | 意味 | s のまま | ș に交替 | 例 |
|---|---|---|---|---|
| a coase | 縫う | cos | co**ș**i | tu coși /koʃʲ/ |
| a scoate | 取り出す | scot | — | (t→ではなく別扱い) |

s→ș は動詞では出現が限られるが、名詞複数(pas→pa**ș**i「歩」)で頻出するため、同じ交替として一括で覚えると効率がよい。

### 3.4 加えて:c/g の軟音化(綴り不変・音のみ)

パターン⑤⑥と並ぶ最頻出の子音交替が、語幹末の **c / g** の軟音化である。これは**綴りが変わらず音だけ変わる**ため、日本語話者が見落としやすい。

| 動詞 | 意味 | 硬音(c/g) | 軟音(前舌母音の前) | 音の変化 |
|---|---|---|---|---|
| a merge | 行く | merg /merɡ/ | mergi /merd͡ʒʲ/ | g → /d͡ʒ/ |
| a face | する | fac /fak/ | faci /fat͡ʃʲ/ | c → /t͡ʃ/ |
| a zice | 言う | zic /zik/ | zici /zit͡ʃʲ/ | c → /t͡ʃ/ |

「c の後ろに e / i が来ると /t͡ʃ/、g の後ろに e / i が来ると /d͡ʒ/」という発音規則([grammar/present-tense.md](../grammar/present-tense.md) §6)がそのまま動詞活用に現れている。綴りが同じでも音が動くことを、音読で体に入れる。

---

## 4. 命令法(imperativ)の作り方 — 肯定と否定は別ルート

命令法は日本語話者がしばしば混乱する。ルーマニア語の**2人称単数命令は、肯定と否定でまったく作り方が違う**からである。

| | 2人称単数(tu) | 2人称複数(voi) |
|---|---|---|
| **肯定** | 動詞により現在3単形 or 2単形（下記) | 現在形2複と同形(-ați / -eți / -iți) |
| **否定** | **nu + 不定詞**(a を除く) | nu + 現在形2複(肯定と同形) |

### 4.1 肯定命令2人称単数の目安

- **自動詞・第 IV 群など**は現在形の3人称単数と同形になりやすい: a merge → **Mergi!**（行け）※実際は2単形、a veni → **Vino!**（来い、不規則）。
- **他動詞・第 I 群**は現在3単と同形が多い: a lucra → **Lucrează!**、a cânta → **Cântă!**、a aștepta → **Așteaptă!**
- 高頻度の不規則命令は丸暗記: a fi → **Fii!**、a avea → **Ai!**、a da → **Dă!**、a lua → **Ia!**、a face → **Fă!**、a zice → **Zi!**、a duce → **Du!**

### 4.2 否定命令2人称単数は必ず「nu + 不定詞」

肯定命令がどんな形でも、**否定命令の2人称単数は「nu + 不定詞(a なし)」で一律**に作れる。ここは例外なく規則的なので、日本語話者はまずこれを覚えると楽になる。

| 動詞 | 肯定2単 | 否定2単(nu + 不定詞) |
|---|---|---|
| a lucra | Lucrează! | **Nu lucra!** |
| a merge | Mergi! | **Nu merge!** |
| a vorbi | Vorbește! | **Nu vorbi!** |
| a face | Fă! | **Nu face!** |
| a fi | Fii! | **Nu fi!** |

2人称複数は肯定・否定とも同形(現在2複)なので単純: Lucrați! / Nu lucrați!、Mergeți! / Nu mergeți!。

### 4.3 弱形代名詞の位置(命令法)

再帰動詞・目的語代名詞を伴うと、位置が肯定/否定で入れ替わる(詳細は [reflexive-verb-tables.md](./reflexive-verb-tables.md)・[grammar/pronouns.md](../grammar/pronouns.md))。

- 肯定命令: 動詞の**後ろ**にハイフンで付ける — Ajut**ă-mă**!(私を助けて)、Spal**ă-te**!(体を洗いなさい)
- 否定命令: 動詞の**前**に戻る — Nu **mă** ajuta!、Nu **te** spăla!

---

## 5. 過去分詞から作る時制 — 分詞の語尾5系統

複合過去・大過去・受動態・完了不定詞は、すべて過去分詞を土台にする。分詞の語尾は活用群におおむね対応するが不規則も多い(正の解説と20語一覧は [grammar/past-tenses.md](../grammar/past-tenses.md) §1.2〜1.3)。

| 分詞語尾 | 主な由来 | 例(不定詞 → 分詞) |
|---|---|---|
| **-at** | 第 I 群(-a) | a lucra → lucrat、a mânca → mâncat |
| **-ut** | 第 II 群 + 多くの不規則 | a vedea → văzut、a face → făcut |
| **-s** | 第 III 群の一部 | a merge → mers、a scrie → scris |
| **-t** | 第 III 群の一部 | a rupe → rupt、a coace → copt |
| **-it** | 第 IV 群(-i) | a dormi → dormit、a vorbi → vorbit |
| **-ât** | 第 IV 群(-î) | a coborî → coborât、a hotărî → hotărât |

分詞さえ手元にあれば、複合過去は「a avea 短縮形(am/ai/a/am/ați/au)+ 分詞」で機械的に組める。**分詞は性・数で変化しない**(ea a plecat、not *plecată*)ので、この点はロマンス諸語より易しい。

---

## 6. 全時制の縦断表 — a lucra(規則)を1枚で

導出の成果を確認するため、規則第 I 群 -ez 型の a lucra(働く)を全時制で並べる。**この1枚がすべて §1〜§5 の規則から導けている**ことを味わってほしい。他の型の完全表は姉妹ページに譲る。

| 時制・法 | eu | tu | el, ea | noi | voi | ei, ele |
|---|---|---|---|---|---|---|
| 現在 | lucrez | lucrezi | lucrează | lucrăm | lucrați | lucrează |
| 半過去 | lucram | lucrai | lucra | lucram | lucrați | lucrau |
| 複合過去 | am lucrat | ai lucrat | a lucrat | am lucrat | ați lucrat | au lucrat |
| 大過去 | lucrasem | lucraseși | lucrase | lucraserăm | lucraserăți | lucraseră |
| 未来(標準) | voi lucra | vei lucra | va lucra | vom lucra | veți lucra | vor lucra |
| 未来(口語 o să) | o să lucrez | o să lucrezi | o să lucreze | o să lucrăm | o să lucrați | o să lucreze |
| 接続法現在 | să lucrez | să lucrezi | să lucreze | să lucrăm | să lucrați | să lucreze |
| 条件法現在 | aș lucra | ai lucra | ar lucra | am lucra | ați lucra | ar lucra |
| 命令法 | — | Lucrează! / Nu lucra! | — | — | Lucrați! / Nu lucrați! | — |
| 分詞 | lucrat（不変) | | | | | |
| 動名詞 | lucrând | | | | | |

条件法の助動詞 aș/ai/ar/am/ați/ar と未来標準の voi/vei/va/vom/veți/vor は動詞によらず一定なので、これも「助動詞1セット + 不定詞」で覚える([grammar/conditional.md](../grammar/conditional.md))。

---

## 7. よくある誤用(❌→✅)

| ❌ 誤り | ✅ 正しく | 説明 |
|---|---|---|
| noi lucr**ez**ăm | noi lucr**ăm** | -ez/-esc は noi/voi に付かない |
| 否定命令に活用形:Nu lucr**ează**! | Nu **lucra**!（不定詞) | 否定2単は「nu + 不定詞」 |
| 分詞を性で変化:ea a plecat**ă** | ea a **plecat** | ルーマニア語分詞は複合過去で不変 |
| 強勢母音を開かない:el *dorme* | el d**oa**rme | o→oa 交替を綴りに反映 |
| c/g の軟音化を無視して発音 | mergi=/merd͡ʒʲ/, faci=/fat͡ʃʲ/ | 綴り不変でも音は軟音化 |
| t→ț を綴らない:tu *simti* | tu sim**ț**i | t→ț は綴りも変わる |
| 未来を分詞で:*voi lucrat* | voi **lucra**（不定詞) | 標準未来は不定詞から |

---

## 8. 学習の指針 — このページを使い倒す

1. **新出動詞は「不定詞・eu 形・過去分詞」の3点でメモ**する。これだけで規則動詞は全形が導ける。
2. eu 形の語尾(-ez / -esc / それ以外)で**現在形の型を確定**し、[`regular-verbs.md`](./regular-verbs.md) の語尾表に当てはめる。
3. 3人称で語幹が「化けた」ら、§3 の6パターンのどれかを疑う。原理(強勢で開く/前舌母音で軟音化)で説明できれば暗記量が激減する。
4. 不規則動詞(a fi, a avea, a vrea, a putea, a lua, a da, a sta, a bea, a mânca…)だけは主要形が予測不能なので [`irregular-verbs.md`](./irregular-verbs.md) で個別に確認する。
5. 専門動詞の活用と用例は [medical-verbs.md](./medical-verbs.md)・[business-verbs.md](./business-verbs.md) を参照する。

---

ナビゲーション: [活用索引](./index.md) | [README](../README.md)
