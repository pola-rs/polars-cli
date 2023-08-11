# Polars CLI

## CLI

**Build from source**

```bash
cargo install --locked --path .
```

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
