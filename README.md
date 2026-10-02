# prime-spiral

Render an Ulam spiral as a compact terminal pattern: `#` marks prime numbers and `.` marks composite numbers or 1.

## Use

Requires Python 3.10+; no packages to install.

```sh
python prime_spiral.py
python prime_spiral.py --size 11
```

The grid is square and must have an odd width from 3 through 101. The center starts at 1 and values spiral outward. Primality is determined with a sieve; no randomness or network access is used.

## License

MIT
