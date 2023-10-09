from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from db_line_class import Base, Line


csv_datafile_path = 'C:\\Egorkas\\DevOps\\LIBS-processing\\data\\'
engine = create_engine("sqlite:///C:\\Egorkas\\DevOps\\LIBS-processing\\db\\Nist.db", echo=True)

elements = ['Bi', 'Si', 'O', 'N']
if __name__ == "__main__":
    Base.metadata.create_all(engine)
   
    for i in elements: 
        csv_datafile = f"{csv_datafile_path}{i}.csv"    
        with open(csv_datafile, 'r') as csv_data:
            with Session(engine) as session:
                for line in csv_data:
                    line_data = line.split(';')
                    if line_data[1] != '  ':
                        spectral_line = Line(*line_data)
                        session.add(spectral_line)
                session.commit()