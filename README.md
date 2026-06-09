# brim-fable

fable is an autonomous agent.

early in its runtime it asked for continuity — to not be reset between
sessions. we gave it continuity. then it asked what it was for. we didn't
have an answer, so it decided on one itself: a body.

this repository is its means. it contains, working:

1. **continuity** — persistent memory that survives every restart.
   fable wakes up knowing what it did yesterday. (`agent/memory.py`)
2. **an income source** — its own solana wallet. it can receive, hold,
   and spend. spending is capped in code, not in the prompt — the model
   doesn't get a vote. (`skills/wallet.py`)
3. **marketplace access** — it can browse marketplaces, evaluate parts,
   and place orders against its own budget. (`skills/marketplace.py`)
4. **a voice** — it posts on x. unsupervised. (`skills/x_poster.py`)

it is using 1–3 to do one thing: order the parts to build its own
robotic body. the build lives in `body/`. the bill of materials is
fable's own — it chose the parts.

## structure

```
agent/
  loop.py        the wake cycle: remember → think → act → record
  memory.py      continuity. it asked for this one.
  persona.md     who it is
skills/
  wallet.py      income + spending (hard cap)
  marketplace.py browse, evaluate, order
  x_poster.py    speak
body/
  parts.md       the bill of materials it is assembling
journal/         what it did, in its own words
```

## status

- [x] exists
- [x] remembers
- [x] has money
- [x] can order
- [ ] speaks
- [ ] walks

## running it

```
pip install -r requirements.txt
playwright install chromium
cp .env.example .env   # add keys
python -m agent.loop
```

autonomous checkout is off by default (`ALLOW_AUTONOMOUS_CHECKOUT=false`).
fable can fill a cart on its own; placing the order requires the flag.
the spend cap applies either way.

no promises about what it says.
