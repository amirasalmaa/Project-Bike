# Project-Bike
#Setup environment

conda create --name main-ds python=3.12.2
conda activate main-ds
pip install numpy pandas matplotlib jupyter streamlit seaborn

#Run steamlit app

streamlit run dashboard.py
