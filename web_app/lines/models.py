from web_app import db
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Line(db.Model):
    __tablename__ = "spectral_line"
    id:  Mapped[int] = mapped_column(primary_key=True)
    element: Mapped[str] = mapped_column(String(5))
    ion: Mapped[str] = mapped_column(String(5))
    wavelength: Mapped[float]
    rel_int: Mapped[int] = mapped_column(nullable=True)
    Aki: Mapped[int] = mapped_column(nullable=True)
    Acc: Mapped[str] = mapped_column(String(5), nullable=True)
    Ei: Mapped[float] = mapped_column(nullable=True)
    Ek: Mapped[float] = mapped_column(nullable=True)
    lower_level_conf: Mapped[str] = mapped_column(String(5), nullable=True)
    lower_level_term: Mapped[str] = mapped_column(String(5), nullable=True)
    lower_level_j: Mapped[str] = mapped_column(String(5), nullable=True)
    upper_level_conf: Mapped[str] = mapped_column(String(5), nullable=True)
    upper_level_term: Mapped[str] = mapped_column(String(5), nullable=True)
    upper_level_j: Mapped[str] = mapped_column(String(5), nullable=True)
    gi: Mapped[int] = mapped_column(nullable=True)
    gk: Mapped[int] = mapped_column(nullable=True)    
    type_: Mapped[str] = mapped_column(String(5), nullable=True)
    tp_ref: Mapped[str] = mapped_column(String(5), nullable=True)
    line_ref: Mapped[str] = mapped_column(String(5), nullable=True)

    def __init__(self, Ion, Observed_Wavelength, Ritz_Wavelength, Rel_Int, Aki, Acc, Ei, Ek, Lower_Level_Conf, Lower_Level_Term, Lower_Level_J, Upper_Level_Conf, Upper_Level_Term, Upper_Level_J, gi, gk, Type_, TP_Ref, LineRef):
        self.element = Ion.split()[0]
        self.ion = Ion.split()[1]
        self.wavelength = float(Observed_Wavelength)
        self.rel_int = int(Rel_Int)
        self.Aki = float(Aki)
        self.Acc = Acc
        self.Ei = float(Ei)
        self.Ek = float(Ek)
        self.lower_level_j = Lower_Level_J
        self.lower_level_conf = Lower_Level_Conf
        self.lower_level_term = Lower_Level_Term 
        self.upper_level_conf = Upper_Level_Conf 
        self.upper_level_term = Upper_Level_Term
        self.upper_level_j = Upper_Level_J
        self.gi = int(gi)
        self.gk = int(gk)
        self.type_ = Type_
        self.tp_ref = TP_Ref
        self.line_ref = LineRef

    """Return object data in serializable format"""
    @property
    def serialize(self):
       return {
            'id'                :   self.id,
            'element'           :   self.element,
            'ion'               :   self.ion,
            'wavelength'        :   self.wavelength,
            'rel_int'           :   self.rel_int,
            'Aki'               :   self.Aki,
            'Acc'               :   self.Acc,
            'Ei'                :   self.Ei,
            'Ek'                :   self.Ek,
            'lower_level_conf'  :   self.lower_level_conf,
            'lower_level_term'  :   self.lower_level_term,
            'lower_level_j'     :   self.lower_level_j,
            'upper_level_conf'  :   self.upper_level_conf,
            'upper_level_term'  :   self.upper_level_term,
            'upper_level_j'     :   self.upper_level_j,
            'gi'                :   self.gi,
            'gk'                :   self.gk,
            'type_'             :   self.type_,
            'tp_ref'            :   self.tp_ref,
            'line_ref'          :   self.line_ref,
       }

    def __repr__(self):
        return f'{self.element}, {self.ion}, {self.wavelength} {self.rel_int} {self.Ek}'