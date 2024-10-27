# %% Change dictionary value under list iteration
d = {1: 2, 3: 5, 4: 6, 6: None, 8: 9}
for slot, step in d.items():
    if step is None:
        d[slot] = 0

print(d)
# %%
