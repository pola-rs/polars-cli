# Polars CLI

## Installation

Until binaries are available, the only way to install the Polars CLI is by building it from source:

With a recent version of rustc it's possible to install polars-cli.
```bash
$ rustc --version
rustc 1.72.0 (5680fa18f 2023-08-23)
$ cargo install --locked polars-cli
```

Alternatively, clone the repository and install the latest version on the main branch:

```bash
cargo install --locked --path .
```

#### Prerequisites

1. `rustup`: which provides the `cargo` executable. You can get it from the [official website](https://rustup.rs/).

## Usage

```shell
$ polars
Polars CLI version 0.3.0
Type .help for help.

>> select * FROM read_csv('examples/datasets/foods1.csv');
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

Or pipe your SQL command directly inline:

```bash
$ echo "SELECT category FROM read_csv('examples/datasets/foods1.csv')" | polars
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

| Feature   | Description                                               |
| --------- | --------------------------------------------------------- |
| default   | The default feature set that includes all other features. |
| highlight | Provides syntax highlighting                              |
| parquet   | Enables reading and writing of Apache Parquet files.      |
| json      | Enables reading and writing of JSON files.                |
| ipc       | Enables reading and writing of IPC/Apache Arrow files     |
