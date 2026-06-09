# security & operating boundaries

brim-fable acts in the real world — it can hold money, spend it, and place
orders. that is the point of the project, and it is also why the boundaries
below are enforced in code rather than left to the model or to trust.

## the boundaries

- **it only ever touches accounts the operator owns and funds.** the wallet,
  the marketplace login, and the x account all belong to the human running
  it. nothing here accesses anyone else's account, and nothing is designed
  to.
- **spending is capped in code.** the cap is lifetime-cumulative and checked
  against a ledger on disk (`journal/spends.jsonl`) before any transfer. the
  model cannot raise it, and cannot talk past it. raising it is a human edit
  to a config value.
- **autonomous checkout ships off** (`ALLOW_AUTONOMOUS_CHECKOUT=false`). the
  agent can research and fill a cart on its own; placing an order is a
  deliberate opt-in by the operator.
- **no credentials live in this repo.** keys load from `.env` (gitignored).
  the marketplace login lives in `.browser/` (gitignored). nothing secret is
  committed, and the history has been kept clean of it.

## secrets

never commit `.env`, `.browser/`, or `journal/spends.jsonl`. the `.gitignore`
covers all three. if you fork this, regenerate your own keys — do not reuse
any value you find in an example file.

## reporting

found a way for this to spend, order, or post outside the boundaries above?
that's a real bug. open an issue describing it, without including any secret
material.
