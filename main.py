from sqlalchemy import create_engine
import pandas as pd


engine = create_engine(
    "mysql+pymysql://root:Velvetthunder91!@127.0.0.1:3306/theme_park"
)

