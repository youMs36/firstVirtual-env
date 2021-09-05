from sqlalchemy import Column, Integer, String
import database

class VaccineInfo(database.Base):
    __tablename__ = 'tbvaccine_details'
    
    rowCount =  Column(Integer, primary_key=True, index=True)
    citizenId = Column(Integer, index=True)
    doseCount = Column(Integer)
    VaccineName = Column(String)
    VaccineLotNumber = Column(String)


class Citizen(database.Base):

    __tablename__ = 'tbcitizen'
    
    citizenId = Column(Integer,primary_key=True, index=True)
    firstName = Column(String)
    lastName = Column(String)
    phoneNumber = Column(String)
    emailId = Column(String)
    
    
