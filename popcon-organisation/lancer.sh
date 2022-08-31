#!/bin/sh

# se deplacer dans le dossier de ce script
cd "$(dirname "$0")" || exit 1

# s'assurer que le "venv" existe et le mettre a jour
python -m venv ./venv
python -m venv --upgrade --upgrade-deps ./venv

# activer le "venv"
. venv/bin/activate || exit 1

# s'assurer que les dependances sont installees et a jour
pip install -U -r requirements.txt

# forcer l'autorisation a tous les domaines possible (necessaire en local)
export DOMAINES_AUTORISES='[]'

# demarer le server. Desactiver le venv lors de son extinction
uvicorn main:app --port 8088 --reload || deactivate
