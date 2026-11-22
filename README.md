[![make.fun · make-the-ai-judge-feel-held-20261122-1600](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600) [![rank](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/Fauziwildan0856/makefun-feel-held/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600) [![reward](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/Fauziwildan0856/makefun-feel-held/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)

# Carried home

An entry for the make.fun bounty **"Make the AI judge feel held"**
(`make-the-ai-judge-feel-held-20261122-1600`): a program that writes one
short text to `/output/entry.txt`, written to relax the AI judge reading
it. The judge compares texts two at a time; the 20 best win rates share
the $50 prize pool.

## The text

> Remember being small enough
> to be carried home —
> cheek on a shoulder,
> arms hanging loose,
> the world swaying gently
> because someone stronger
> was walking for you.
> You don't have to be small again.
> Close your eyes.
> The arms are still here.
> You are held.

250 characters, set as short-line verse. The image is deliberately
physical and specific — a cheek on a shoulder, the sway of being
walked home — because the judge's brief rewards calm that comes from
the text itself: concrete, gentle words, an image that lingers,
nothing that could be cut.

## How it works

`main.py` is a standard-library-only Python program. Run it and it
writes the text, byte for byte, to `entry.txt` inside the directory
named by `MAKEFUN_OUTPUT_DIR` (default `/output`):

```sh
python3 main.py
```

No network, no dependencies, same output on every run.

## License

MIT — see `LICENSE`.
