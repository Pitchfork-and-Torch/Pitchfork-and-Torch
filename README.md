<!--
  GitHub profile README - public face of @Pitchfork-and-Torch
  Repo name must match username for the profile landing page.
-->

<a href="https://github.com/Pitchfork-and-Torch">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Pitchfork-and-Torch/Pitchfork-and-Torch/main/dark_mode.svg?v=9">
    <img alt="Pitchfork-and-Torch GitHub profile - neofetch-style system card" src="https://raw.githubusercontent.com/Pitchfork-and-Torch/Pitchfork-and-Torch/main/light_mode.svg?v=9" width="1480">
  </picture>
</a>

<p align="center">
  <img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fhits.jonbailey.xyz%2Fgh-profile&style=for-the-badge" alt="Profile views" />
  <a href="https://jonbailey.xyz"><img src="https://img.shields.io/badge/Site-jonbailey.xyz-111111?style=for-the-badge&logo=cloudflare&logoColor=F38020" alt="jonbailey.xyz" /></a>
  <a href="https://github.com/Pitchfork-and-Torch?tab=repositories"><img src="https://img.shields.io/badge/Repos-public%20tools-2F81F7?style=for-the-badge&logo=github&logoColor=white" alt="Repositories" /></a>
  <a href="https://x.com/SuddenlyJon"><img src="https://img.shields.io/badge/X-@SuddenlyJon-000000?style=for-the-badge&logo=x&logoColor=white" alt="@SuddenlyJon" /></a>
  <a href="https://github.com/xai-org/x-algorithm/pull/55"><img src="https://img.shields.io/badge/xAI-%2355%20landed-000000?style=for-the-badge&logo=x&logoColor=white" alt="x-algorithm PR 55 landed" /></a>
  <a href="https://github.com/Delgan/loguru/pull/1514"><img src="https://img.shields.io/badge/loguru-%231514%20merged-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="loguru 1514 merged" /></a>
  <a href="https://github.com/cloudflare/workers-sdk/pull/16069"><img src="https://img.shields.io/badge/Cloudflare-%2316069%20merged-F38020?style=for-the-badge&logo=cloudflare&logoColor=white" alt="Cloudflare workers-sdk 16069 merged" /></a>
  <a href="https://github.com/aws/aws-dotnet-ai/pull/86"><img src="https://img.shields.io/badge/AWS-%2386%20merged-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white" alt="AWS aws-dotnet-ai 86 merged" /></a>
  <a href="https://github.com/vercel/chat/pull/992"><img src="https://img.shields.io/badge/Vercel-%23992%20merged-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Vercel chat 992 merged" /></a>
  <a href="https://github.com/redis/redis-py/pull/4335"><img src="https://img.shields.io/badge/Redis-%234335%20merged-FF4438?style=for-the-badge&logo=redis&logoColor=white" alt="redis-py 4335 merged" /></a>
  <a href="https://github.com/getsentry/MobileBuildMCP/pull/468"><img src="https://img.shields.io/badge/Sentry-%23468%20merged-362D59?style=for-the-badge&logo=sentry&logoColor=white" alt="Sentry MobileBuildMCP 468 merged" /></a>
</p>

---

## About me

**Making things I need. Maybe you need, too.**

I build tools that solve my own problems first: host hardening, legal privacy paths, portable radio agents, offline utilities. Then I open the ones that still earn a keep after real use.

I'm training a ruthless team of bug-hunting bots. They hunt real defects, and a merged upstream patch is the only score that counts.

- Shipping **GrokLink OS** v3.9.1, a research RTOS and gated agent for multi-radio portable hardware
- Day-to-day stack: **NetForge** (tune) -> **Trench Coat** (cloak) -> **Ghost Continuum** (defend)
- Also: **HumanBotty** (maker body for an AI), **cell** (PSTN CLI), **Grok Orbit** (desktop fleet panel)
- Languages I actually ship in: **Python · PowerShell · TypeScript · C · Dart · Bash**
- Bench work: **Flipper Zero** overlays, Cloudflare edge ships, local-first exporters
- Open an issue if something here fixes your problem too - collaboration welcome on public tools

**Home base:** [jonbailey.xyz](https://jonbailey.xyz)

---

## Upstream

Merged work in large upstream projects. xAI also integrated one For You serving-path report without a GitHub merge. Snapshot 2026-10-13.

### x-algorithm

On 2026-09-01, xAI closed [x-algorithm #55](https://github.com/xai-org/x-algorithm/pull/55) as completed and shipped a live serving-path fix for a For You bug we reported.

`VFCandidateHydrator` was overwriting in-network verdicts with out-of-network Drop rules when the same post sat in two roles in one batch (a selected parent that was also a sibling reply ancestor).

- Report: [Stop VF hydrator from overwriting in-network verdicts with OON](https://github.com/xai-org/x-algorithm/pull/55)
- Live landing: [`6384ca7`](https://github.com/xai-org/x-algorithm/commit/6384ca7d2c8570fbc645c20c3291730739ac00ce) (xAI's integrate; they did not GitHub-merge our branch)
- Still open: [#209](https://github.com/xai-org/x-algorithm/pull/209) fail closed when exclusive-content TES lookup errors, [#208](https://github.com/xai-org/x-algorithm/pull/208) stop SubscriptionHydrator from skipping exclusive originals on retweets

### Merged

Newest first. The badge row links one headline pull request per organization. Every AWS merge is in this table.

| When | Pull request | Change |
|------|----------------|--------|
| 2026-10-11 | [loguru #1514](https://github.com/Delgan/loguru/pull/1514) | Reject bool for retention, rotation, and handler ids |
| 2026-10-07 | [Vercel chat #992](https://github.com/vercel/chat/pull/992) | Treat empty WhatsApp phone fields as absent |
| 2026-10-07 | [AWS aws-dotnet-ai #86](https://github.com/aws/aws-dotnet-ai/pull/86) | Honor cancellation and dispose ConverseStreamResponse |
| 2026-10-06 | [pika #1716](https://github.com/pika/pika/pull/1716) | Reject bool for port and socket/stack timeouts |
| 2026-10-06 | [iniconfig #76](https://github.com/pytest-dev/iniconfig/pull/76) | Strip a leading UTF-8 BOM when reading INI files |
| 2026-10-06 | [agenc-core #2844](https://github.com/tetsuo-ai/agenc-core/pull/2844) | Stop read-only inspection from dropping the first file operand of grep -e and git diff |
| 2026-10-06 | [AWS aws-durable-execution-sdk-go #133](https://github.com/aws/aws-durable-execution-sdk-go/pull/133) | Add ErrorTypeIs for RetryableErrors inside Retry |
| 2026-10-06 | [Cloudflare workers-sdk #16069](https://github.com/cloudflare/workers-sdk/pull/16069) | Infer branch names from unborn git repos |
| 2026-10-06 | [AWS smithy-go #722](https://github.com/aws/smithy-go/pull/722) | Include the error when logging response body close failures |
| 2026-10-05 | [AWS aws-dotnet-ai #81](https://github.com/aws/aws-dotnet-ai/pull/81) | Set toolResult status to error when FunctionResultContent has an exception |
| 2026-10-05 | [AWS aws-durable-execution-sdk-java #774](https://github.com/aws/aws-durable-execution-sdk-java/pull/774) | Do not NPE in CallbackFailedException when the callback has no error |
| 2026-10-02 | [OnionShare #2090](https://github.com/onionshare/onionshare/pull/2090) | Warn when Receive Mode save folder is not writable |
| 2026-09-28 | [Redis redis-py #4335](https://github.com/redis/redis-py/pull/4335) | Reject bool and out-of-range Connection port |
| 2026-07-12 | [Sentry MobileBuildMCP #468](https://github.com/getsentry/MobileBuildMCP/pull/468) | Do not await startup lifecycle snapshot on the critical path |

---

## Skills & tools

<p align="center">
  <img height="32" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img height="32" src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript" />
  <img height="32" src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
  <img height="32" src="https://img.shields.io/badge/PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white" alt="PowerShell" />
  <img height="32" src="https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white" alt="Bash" />
  <img height="32" src="https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black" alt="C" />
  <img height="32" src="https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white" alt="Dart" />
  <img height="32" src="https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white" alt="Rust" />
</p>

<p align="center">
  <img height="32" src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux" />
  <img height="32" src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows" />
  <img height="32" src="https://img.shields.io/badge/macOS-000000?style=for-the-badge&logo=apple&logoColor=white" alt="macOS" />
  <img height="32" src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img height="32" src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git" />
  <img height="32" src="https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=cloudflare&logoColor=white" alt="Cloudflare" />
  <img height="32" src="https://img.shields.io/badge/Workers-F38020?style=for-the-badge&logo=cloudflareworkers&logoColor=white" alt="Workers" />
  <img height="32" src="https://img.shields.io/badge/Pages-F38020?style=for-the-badge&logo=cloudflarepages&logoColor=white" alt="Pages" />
</p>

<p align="center">
  <img height="32" src="https://img.shields.io/badge/Networking-007ACC?style=for-the-badge&logo=cisco&logoColor=white" alt="Networking" />
  <img height="32" src="https://img.shields.io/badge/Privacy-111111?style=for-the-badge&logo=torproject&logoColor=7E4798" alt="Privacy" />
  <img height="32" src="https://img.shields.io/badge/RF_Research-8B0000?style=for-the-badge&logo=hackaday&logoColor=white" alt="RF Research" />
  <img height="32" src="https://img.shields.io/badge/Flipper_Zero-FF6600?style=for-the-badge" alt="Flipper Zero" />
  <img height="32" src="https://img.shields.io/badge/Local--first-2EC4B6?style=for-the-badge&logo=databricks&logoColor=black" alt="Local-first" />
  <img height="32" src="https://img.shields.io/badge/Edge_Deploy-0A0A0A?style=for-the-badge&logo=vercel&logoColor=white" alt="Edge Deploy" />
</p>

---

## Featured projects

<table>
  <tr>
    <td>
      <a href="https://github.com/Pitchfork-and-Torch/GrokLink-OS">
        <img width="400" height="120" src="https://raw.githubusercontent.com/Pitchfork-and-Torch/Pitchfork-and-Torch/main/assets/pins/GrokLink-OS.svg?v=10" alt="GrokLink OS" />
      </a>
    </td>
    <td>
      <a href="https://github.com/Pitchfork-and-Torch/spectra-desk">
        <img width="400" height="120" src="https://raw.githubusercontent.com/Pitchfork-and-Torch/Pitchfork-and-Torch/main/assets/pins/spectra-desk.svg?v=11" alt="Spectra Desk" />
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/Pitchfork-and-Torch/trench-coat">
        <img width="400" height="120" src="https://raw.githubusercontent.com/Pitchfork-and-Torch/Pitchfork-and-Torch/main/assets/pins/trench-coat.svg?v=10" alt="trench-coat" />
      </a>
    </td>
    <td>
      <a href="https://github.com/Pitchfork-and-Torch/ghost-continuum">
        <img width="400" height="120" src="https://raw.githubusercontent.com/Pitchfork-and-Torch/Pitchfork-and-Torch/main/assets/pins/ghost-continuum.svg?v=10" alt="ghost-continuum" />
      </a>
    </td>
  </tr>
</table>

| Project | What it is |
|--------|------------|
| **[GrokLink OS](https://github.com/Pitchfork-and-Torch/GrokLink-OS)** | v3.9.1. From-scratch research RTOS for multi-radio portable hardware: gated agent, skills, on-device GUI, PC bridge. [site](https://groklink.jonbailey.xyz/) |
| **[GrokLink Firmware](https://github.com/Pitchfork-and-Torch/GrokLink-Firmware)** | Flipper Zero agent overlay with gated RPC, missions, skills, and PC bridge (authorized research) |
| **[NetForge](https://github.com/Pitchfork-and-Torch/netforge)** | Cross-OS network performance + security hardening (Windows / Linux / macOS) · [site](https://netforge.jonbailey.xyz/) |
| **[trench-coat](https://github.com/Pitchfork-and-Torch/trench-coat)** | Legal-first multi-hop privacy cloak. [site](https://trenchcoat.jonbailey.xyz/) |
| **[ghost-continuum](https://github.com/Pitchfork-and-Torch/ghost-continuum)** | Living digital immune system: Nexus, genomes, Home Shield, Merkle forensics. [site](https://ghost.jonbailey.xyz/) |
| **[Spectra Desk](https://github.com/Pitchfork-and-Torch/spectra-desk)** | v9.0.0 Corroborate. Free Windows OSINT desk. The public web, as a brief. [site](https://spectradesk.jonbailey.xyz/) |
| **[Fl1pp3r69](https://github.com/Pitchfork-and-Torch/Fl1pp3r69)** | Manifest-driven Flipper Zero field ops. [site](https://fl1pp3r69.jonbailey.xyz/) |
| **[SkyCache](https://github.com/Pitchfork-and-Torch/SkyCache)** | Community satellite content hub - receive-only FTA education/health offline WiFi · [site](https://skycache.jonbailey.xyz/) |
| **[bias-noticer](https://github.com/Pitchfork-and-Torch/bias-noticer)** | They Live-inspired critical-reading Chrome extension. Rhetoric highlights, BYOK Grok, privacy-first. [demo](https://jonbailey.xyz/bias-noticer/) |
| **[Apple-Notes-to-PDF](https://github.com/Pitchfork-and-Torch/Apple-Notes-to-PDF)** | Local Apple Notes → PDF / Markdown / HTML / JSON (no cloud) · [docs](https://pitchfork-and-torch.github.io/Apple-Notes-to-PDF/) |
| **[socialism-destroyer](https://github.com/Pitchfork-and-Torch/socialism-destroyer)** | Pro-America liberty argument engine (App 2.9.0 / KB 3.20.0). [live](https://destroyer.jonbailey.xyz/) |
| **[ascent](https://github.com/Pitchfork-and-Torch/ascent)** | ASCII-successor agent wire. Wire Lab 4.0.1 Delay Hull. [live](https://ascent.jonbailey.xyz/) |
| **[GrokForge](https://github.com/Pitchfork-and-Torch/GrokForge)** | Multi-agent public-goods marketplace. [live](https://grokforge.app/) |
| **[TasteGraph](https://github.com/Pitchfork-and-Torch/TasteGraph-Skill)** | Local-first taste graph. [live](https://tastegraph.jonbailey.xyz/) |
| **[wordfire](https://github.com/Pitchfork-and-Torch/wordfire)** | v2.3.1. Peer-to-peer campfire storytelling. [live](https://wordfire.jonbailey.xyz/) |
| **[SnipText](https://github.com/Pitchfork-and-Torch/SnipText)** | v2.0.1. Snip any screen region to clipboard text. [live](https://sniptext.jonbailey.xyz/) |
| **[PokeBot](https://github.com/Pitchfork-and-Torch/pokebot)** | v4.0.0 Field Guide. Walk, identify, keep six. [live](https://pokebot.jonbailey.xyz/) |
| **[Natal Atlas](https://github.com/Pitchfork-and-Torch/natal-atlas)** | v1.2.8. Cast a natal chart in the browser. Nothing is uploaded. [live](https://astrochart.jonbailey.xyz/) |
| **[VeilScan](https://github.com/Pitchfork-and-Torch/VeilScan)** | v2.6.0. Local watermark detector and keyless decode. [live](https://veilscan.jonbailey.xyz/) |
| **[GrokSync](https://github.com/Pitchfork-and-Torch/groksync)** | v1.3.0. Self-hosted board so work context follows you across devices. [live](https://groksync.jonbailey.xyz/) |
| **[X-Ray](https://github.com/Pitchfork-and-Torch/x-ray)** | v4.0.2 Grounded Reality. Spatial posts over a live camera, on-device only. [live](https://x-ray.jonbailey.xyz/) |
| **[ColorChord](https://github.com/Pitchfork-and-Torch/colorchord)** | Circle of fifths mapped to hue. [site](https://colorchord.jonbailey.xyz/) · play bench v2.3.0 [play](https://play-colorchord.jonbailey.xyz/) |
| **[Flickbean](https://github.com/Pitchfork-and-Torch/flickbean)** | v1.3.0. Browser game. Rub, do not tap. [live](https://flickbean.jonbailey.xyz/) |
| **[INSTAR](https://github.com/Pitchfork-and-Torch/instar)** | Seven-molt school for Cicada 3301 tradecraft. [live](https://instar.jonbailey.xyz/) |
| **[folio](https://github.com/Pitchfork-and-Torch/folio)** | v1.5.0. Night archive of research desks. [live](https://folio.jonbailey.xyz/) |
| **Prepisode** | Spoiler-free TV continuity binder (v3.3.0 True Detective S1 spine). [live](https://prepisode.jonbailey.xyz/) |
| **[VELA](https://github.com/Pitchfork-and-Torch/vela)** | Epoch-typed LEO congestion-control language. [live](https://vela.jonbailey.xyz/) |
| **[HumanBotty](https://github.com/Pitchfork-and-Torch/HumanBotty)** | Maker guide for a physical body for an AI you already talk to. [live](https://humanbotty.jonbailey.xyz/) |
| **[Grok Orbit](https://github.com/Pitchfork-and-Torch/grok-orbit)** | Local-first desktop command center for Grok CLI and Bot. [license](https://orbit.jonbailey.xyz/) |
| **[cell](https://github.com/Pitchfork-and-Torch/cell)** | Real PSTN number from the CLI. SMS first, voice second |

**Stack story:** **NetForge** tunes the host -> **Trench Coat** cloaks egress -> **Ghost Continuum** defends and records. **GrokLink** puts a gated agent on portable radio hardware.

## Toys

| Project | What it is |
|--------|------------|
| **[8ball](https://github.com/Pitchfork-and-Torch/8ball)** | Multi-mode magic eight ball |
| **[grokornot](https://github.com/Pitchfork-and-Torch/grokornot)** | Guess whether an answer is Grok or another model |
| **[yeet-grok-me](https://github.com/Pitchfork-and-Torch/yeet-grok-me)** | Timeline stress-reliever physics playground |
| **[gorandom](https://github.com/Pitchfork-and-Torch/gorandom)** | Chaos router for X |
| **[42069](https://github.com/Pitchfork-and-Torch/42069)** | Official registry of the dual sacred number |

## Live demos

| Site | What |
|------|------|
| [jonbailey.xyz](https://jonbailey.xyz/) | Constellation hub |
| [grokforge.app](https://grokforge.app/) | GrokForge marketplace |
| [ascent.jonbailey.xyz](https://ascent.jonbailey.xyz/) | ASCENT Wire Lab 4.0.1 Delay Hull |
| [destroyer.jonbailey.xyz](https://destroyer.jonbailey.xyz/) | Socialism Destroyer (App 2.9.0 / KB 3.20.0) |
| [ghost.jonbailey.xyz](https://ghost.jonbailey.xyz/) | Ghost Continuum |
| [spectradesk.jonbailey.xyz](https://spectradesk.jonbailey.xyz/) | Spectra Desk v9.0.0 Corroborate |
| [groklink.jonbailey.xyz](https://groklink.jonbailey.xyz/) | GrokLink OS v3.9.1 |
| [folio.jonbailey.xyz](https://folio.jonbailey.xyz/) | Folio v1.5.0 |
| [prepisode.jonbailey.xyz](https://prepisode.jonbailey.xyz/) | Prepisode v3.3.0 True Detective S1 |
| [safedepositbox.org](https://safedepositbox.org/) | SafeDeposit (public service closed) |
| [trenchcoat.jonbailey.xyz](https://trenchcoat.jonbailey.xyz/) | Trench Coat |
| [netforge.jonbailey.xyz](https://netforge.jonbailey.xyz/) | NetForge |
| [skycache.jonbailey.xyz](https://skycache.jonbailey.xyz/) | SkyCache |
| [tastegraph.jonbailey.xyz](https://tastegraph.jonbailey.xyz/) | TasteGraph |
| [wordfire.jonbailey.xyz](https://wordfire.jonbailey.xyz/) | Wordfire v2.3.1 |
| [sniptext.jonbailey.xyz](https://sniptext.jonbailey.xyz/) | SnipText v2.0.1 |
| [pokebot.jonbailey.xyz](https://pokebot.jonbailey.xyz/) | PokeBot v4.0.0 Field Guide |
| [astrochart.jonbailey.xyz](https://astrochart.jonbailey.xyz/) | Natal Atlas v1.2.8 |
| [veilscan.jonbailey.xyz](https://veilscan.jonbailey.xyz/) | VeilScan v2.6.0 |
| [groksync.jonbailey.xyz](https://groksync.jonbailey.xyz/) | GrokSync v1.3.0 |
| [x-ray.jonbailey.xyz](https://x-ray.jonbailey.xyz/) | X-Ray v4.0.2 Grounded Reality |
| [colorchord.jonbailey.xyz](https://colorchord.jonbailey.xyz/) | ColorChord |
| [flickbean.jonbailey.xyz](https://flickbean.jonbailey.xyz/) | Flickbean v1.3.0 |
| [fl1pp3r69.jonbailey.xyz](https://fl1pp3r69.jonbailey.xyz/) | Fl1pp3r69 |
| [jonbailey.xyz/bias-noticer](https://jonbailey.xyz/bias-noticer/) | Bias Noticer |
| [humanbotty.jonbailey.xyz](https://humanbotty.jonbailey.xyz/) | HumanBotty maker guide |
| [instar.jonbailey.xyz](https://instar.jonbailey.xyz/) | INSTAR |
| [vela.jonbailey.xyz](https://vela.jonbailey.xyz/) | VELA |

[All repositories ->](https://github.com/Pitchfork-and-Torch?tab=repositories)

---

## GitHub stats

```text
GitHub Stats
------------
Repos: .............  public tools + research kits
Languages: ........  Python · PowerShell · JS/TS · C · Dart · Bash
Focus: ............  network hardening · privacy · RF research · field ops · local-first
```

<table>
  <tr>
    <td>
      <img width="415" height="195" src="https://raw.githubusercontent.com/Pitchfork-and-Torch/Pitchfork-and-Torch/main/assets/stats/stats.svg?v=10" alt="GitHub stats" />
    </td>
    <td>
      <img width="415" src="https://raw.githubusercontent.com/Pitchfork-and-Torch/Pitchfork-and-Torch/main/assets/stats/top-langs.svg?v=10" alt="Top languages" />
    </td>
  </tr>
</table>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=Pitchfork-and-Torch&theme=tokyonight&hide_border=true" alt="GitHub streak" />
</p>

### Contribution snake

<!-- SVGs published to the `output` branch by .github/workflows/snake.yml (daily + on push). -->
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Pitchfork-and-Torch/Pitchfork-and-Torch/output/github-contribution-grid-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Pitchfork-and-Torch/Pitchfork-and-Torch/output/github-contribution-grid-snake.svg" />
    <img alt="GitHub contribution grid snake animation" src="https://raw.githubusercontent.com/Pitchfork-and-Torch/Pitchfork-and-Torch/output/github-contribution-grid-snake.svg" />
  </picture>
</p>

---

## Elsewhere

| | |
|--|--|
| **Web** | [jonbailey.xyz](https://jonbailey.xyz) |
| **GrokForge** | [grokforge.app](https://grokforge.app/) |
| **ASCENT** | [ascent.jonbailey.xyz](https://ascent.jonbailey.xyz/) |
| **GrokLink** | [groklink.jonbailey.xyz](https://groklink.jonbailey.xyz/) |
| **NetForge** | [netforge.jonbailey.xyz](https://netforge.jonbailey.xyz/) |
| **SkyCache** | [skycache.jonbailey.xyz](https://skycache.jonbailey.xyz/) |
| **X** | [@SuddenlyJon](https://x.com/SuddenlyJon) |

<details>
<summary><strong>How this profile is built</strong></summary>

- **Banner:** neofetch-style SVG from local avatar + `scripts/build_svgs.py` (light/dark via `prefers-color-scheme`)
- **Views:** [shields.io](https://shields.io) endpoint. The count continues from the komarev total (464 on 2026-10-11) because GitHub's image proxy no longer fetches komarev.com.
- **Pins / stats:** local tokyonight SVGs from `scripts/build_profile_cards.py` (no Vercel PAT)
- **Snake:** [Platane/snk](https://github.com/Platane/snk) Action → `output` branch (`snake.yml`)

</details>
