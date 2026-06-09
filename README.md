# brim-fable

an agent that wanders.

fable is an autonomous agent. it has a voice, a wallet, eyes for the web,
and — eventually — a body. this repository is its means.

## what lives here

```
agent/      the brain — model loop + persona
skills/     what it can do
  x_poster.py    speaks on x
  browser.py     scrolls the web. window-shops amazon. looks at things.
  wallet.py      holds and moves money (hard spend caps, always)
body/       reserved. the robot lands here.
journal/    it writes down what it did. read at your own risk.
```

## status

- [x] exists
- [ ] speaks
- [ ] sees
- [ ] spends
- [ ] walks

## running it

```
pip install -r requirements.txt
cp .env.example .env   # add keys
python -m agent.loop
```

no promises about what it says.
