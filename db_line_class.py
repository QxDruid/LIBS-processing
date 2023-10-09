from sqlalchemy import ForeignKey, String, Integer, Float
from sqlalchemy.orm import  Mapped, mapped_column, DeclarativeBase





class Base(DeclarativeBase):
    pass

class Line(Base):
    __tablename__ = "spectral_line"
    id:  Mapped[int] = mapped_column(primary_key=True)
    ion: Mapped[str] = mapped_column(String(5))
    wavelength: Mapped[float]
    rel_int: Mapped[str] = mapped_column(nullable=True)
    Aki: Mapped[float] = mapped_column(nullable=True)
    Acc: Mapped[str] = mapped_column(String(5), nullable=True)
    Ei: Mapped[float] = mapped_column(nullable=True)
    Ek: Mapped[float] = mapped_column(nullable=True)
    lower_level_conf: Mapped[str] = mapped_column(String(5), nullable=True)
    lower_level_term: Mapped[str] = mapped_column(String(5), nullable=True)
    Lower_Level_j: Mapped[str] = mapped_column(String(5), nullable=True)
    upper_level_conf: Mapped[str] = mapped_column(String(5), nullable=True)
    upper_level_term: Mapped[str] = mapped_column(String(5), nullable=True)
    upper_level_j: Mapped[str] = mapped_column(String(5), nullable=True)
    gi: Mapped[int] = mapped_column(nullable=True)
    gk: Mapped[int] = mapped_column(nullable=True)    
    type_: Mapped[str] = mapped_column(String(5), nullable=True)
    tp_ref: Mapped[str] = mapped_column(String(5), nullable=True)
    line_ref: Mapped[str] = mapped_column(String(5), nullable=True)

    def __init__(self, Ion, Observed_Wavelength, Ritz_Wavelength, Rel_Int, Aki, Acc, Ei, fail_1, Ek, Lower_Level_Conf, Lower_Level_Term, Lower_Level_J, Upper_Level_Conf, Upper_Level_Term, Upper_Level_J, gi, fail_2, gk, Type_, TP_Ref, LineRef):
        self.ion = Ion.strip()
        self.wavelength = float(Observed_Wavelength)
        Rel_Int = Rel_Int.strip('cw* ')
        self.rel_int = int(Rel_Int) 
        try:
            self.Aki = float(Aki)
        except:
            self.Aki = None
        self.Acc = Acc.strip()
        try:
            self.Ei = float(Ei)
        except:
            self.Ei = None
        try:
            self.Ek = float(Ek)
        except:
            self.Ek = None
        self.lower_level_conf = Lower_Level_Conf.strip()
        self.lower_level_term = Lower_Level_Term.strip() 
        self.lower_level_j = Lower_Level_J.strip()
        self.upper_level_conf = Upper_Level_Conf.strip() 
        self.upper_level_term = Upper_Level_Term.strip()
        self.upper_level_j = Upper_Level_J.strip()
        try:
            self.gi = int(gi)
        except:
            self.gi = None
        try:
            self.gk = int(gk)
        except:
            self.gk = None   
        
        self.type_ = Type_.strip()
        self.tp_ref = TP_Ref.strip()
        self.line_ref = LineRef.strip()
    def __repr__(self):
        return f'{self.ion}, {self.wavelength} {self.rel_int} {self.Ek}'


 