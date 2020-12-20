# Github Manage Access as Code

## How to Use

1. Make organization name's directory

```bash
mkdir <organization name>
```

2. Make repository name's Yaml

```bash
touch <organization name>/<repository name>.yml
```

3. Write manage access

You can only use team names.

```yaml
pull:
  - team1
push:
  - team2
admin:
  - team3
maintain:
  - team4
triage:
  - team5
```

4. Execute

```bash
pip3 install pygithub
python3 main.py
```

### tree

```bash
├── organization-name
│   ├── repo1.yml # repository_name.yml
│   ├── repo2.yml
│   └── repo3.yml
└── main.py
```