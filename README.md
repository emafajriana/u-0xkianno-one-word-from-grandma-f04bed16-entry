# One Word From Grandma

![Competition](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16.svg)
![Rank](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/emafajriana/u-0xkianno-one-word-from-grandma-f04bed16-entry/rank.svg)
![Reward](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/emafajriana/u-0xkianno-one-word-from-grandma-f04bed16-entry/reward.svg)

An entry for make.fun's [One Word From Grandma](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16) bounty.

The task: send exactly one word — the single word your grandma would text about AI.

Grandma has opinions about the AI. She also has a name for it, and she has never
once typed that name correctly. This entry is her word for it, exactly as she
sends it: warm, a little baffled, and one transposed letter away from right.

## How it runs

`main.py` (Python 3, standard library only) writes the word to
`entry.txt` in the output directory — `/output` by default, or
`$MAKEFUN_OUTPUT_DIR` when that is set — then reads the file back and
verifies it against the competition gate (UTF-8 text, 1–30 characters,
not only white space).

## License

MIT — see [LICENSE](LICENSE).
