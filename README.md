conda create -n popo python=3.12 -y
conda activate popo

pip freeze > requirements.txt
pip install -r requirements.txt


cp .env.example .env