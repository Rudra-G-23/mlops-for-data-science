
**Install the DVC**
```cmd
uv add dvc
```
Few Data Work
- Add dummy data
- prepare
- Train
- model save
- Now open Bash terminal and put this command

**Explanation**

| flag | meaning    |
| ---- | ---------- |
| -n   | stage name |
| -d   | dependency |
| -o   | output     |


**Prepare State**
```bash
dvc stage add -n prepare \
-d dvc/src/prepare.py \
-d dvc/data/raw/data.csv \
-o dvc/data/processed/clean_data.csv \
python dvc/src/prepare.py
```

**Training Stage**
```bash
dvc stage add -n train \
-d dvc/src/train.py \
-d dvc/data/processed/clean_data.csv \
-o dvc/model/model.pkl \
python dvc/src/train.py
```

**Now run `dvc repro`**
You will see this output in terminal
```bash
Running stage 'prepare':
> python dvc/src/prepare.py
Data Preprocessing done!
Generating lock file 'dvc.lock'
Updating lock file 'dvc.lock'

Running stage 'train':
> python dvc/src/train.py
Model training completed!
Updating lock file 'dvc.lock'
```