from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models.user import *


engine = create_engine("sqlite:///Data.db")
Base.metadata.create_all(engine)

with Session(engine) as session:
    users = []
    demands = []
    for i in range(5):
        user = User(telegram_id=f'@id{i + 1}')
        users.append(user)
    for i in users:
        for j in range(2):
            demand = Demand(message=f'@msg{j + 1}',
                            owner=i.telegrm_id)
            demands.append(demand)
    session.add_all(users)
    session.add_all(demands)
    session.commit()