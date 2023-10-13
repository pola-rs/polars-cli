# Polars CLI

[![Crates.io](https://img.shields.io/crates/v/polars-cli)](https://crates.io/crates/polars-cli)
[![PyPI](https://img.shields.io/pypi/v/polars-cli)](https://pypi.org/project/polars-cli/)

The Polars command line interface provides a convenient way to execute SQL commands using Polars as a backend.

## Installation

The recommended way to install the Polars CLI is by using [pip](https://pip.pypa.io/):

```bash
pip install polars-cli
```

This will install a pre-compiled binary and make it available on your path under `polars`.
If you do not have Python available, you can download a suitable binary from the most recent [GitHub release](https://github.com/pola-rs/polars-cli/releases/latest/).

Alternatively, you can install the Polars CLI using [cargo](https://doc.rust-lang.org/cargo/), which will compile the code from scratch:

```bash
cargo install --locked polars-cli
```

## Usage

Running `polars` without any arguments will start an interactive shell in which you can run SQL commands.

```shell
$ polars
Polars CLI version 0.4.0
Type .help for help.

>> select * FROM read_csv('examples/datasets/foods.csv');
┌────────────┬──────────┬────────┬──────────┐
│ category   ┆ calories ┆ fats_g ┆ sugars_g │
│ ---        ┆ ---      ┆ ---    ┆ ---      │
│ str        ┆ i64      ┆ f64    ┆ i64      │
╞════════════╪══════════╪════════╪══════════╡
│ vegetables ┆ 45       ┆ 0.5    ┆ 2        │
│ seafood    ┆ 150      ┆ 5.0    ┆ 0        │
│ meat       ┆ 100      ┆ 5.0    ┆ 0        │
│ fruit      ┆ 60       ┆ 0.0    ┆ 11       │
│ …          ┆ …        ┆ …      ┆ …        │
│ seafood    ┆ 200      ┆ 10.0   ┆ 0        │
│ seafood    ┆ 200      ┆ 7.0    ┆ 2        │
│ fruit      ┆ 60       ┆ 0.0    ┆ 11       │
│ meat       ┆ 110      ┆ 7.0    ┆ 0        │
└────────────┴──────────┴────────┴──────────┘
```

Alternatively, SQL commands can be piped directly into the Polars CLI.

```bash
$ echo "SELECT category FROM read_csv('examples/datasets/foods.csv')" | polars
┌────────────┐
│ category   │
│ ---        │
│ str        │
╞════════════╡
│ vegetables │
│ seafood    │
│ meat       │
│ fruit      │
│ …          │
│ seafood    │
│ seafood    │
│ fruit      │
│ meat       │
└────────────┘
```

## Features

When compiling the Polars CLI from source, the following features can be enabled:

| Feature   | Description                                               |
| --------- | --------------------------------------------------------- |
| default   | The default feature set that includes all other features. |
| highlight | Provides syntax highlighting                              |
| parquet   | Enables reading and writing of Apache Parquet files.      |
| json      | Enables reading and writing of JSON files.                |
| ipc       | Enables reading and writing of IPC/Apache Arrow files     |
