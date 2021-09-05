from fastapi import FastAPI, Depends, status, Response
import schemas
import models
import database 
from sqlalchemy.orm import Session

applicationInstance = FastAPI()

models.database.Base.metadata.create_all(database.engine)


# Requirement 1. get the details of citizen given the CitizenId  -- done
# Requirement 2. enter the details like CitizenId, FirstName, LastName, Vaccine Info ( like DoseCount, VaccineName, VaccineLotNumber, NextAppointmentStartDate, NextAppointmentEndDate)  -- 
# session - handling
# user not found handling

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@applicationInstance.get('/citizenVaccinationDetails/{id}', status_code= status.HTTP_200_OK)
def getCitizenVaccinationDetailsByCitezenId(id, response : Response, db : Session = Depends(get_db)):  
    resultSet = db.query(models.Citizen).filter(models.Citizen.citizenId == id).first()
    if not resultSet:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'details ' : f"Citizen with ID = {id} is not available" }
    return resultSet

 

@applicationInstance.post('/insertDetails', status_code= status.HTTP_201_CREATED)
def insertDoseInfo(citizenInfoRequest : schemas.CitizenVaccineDetails, db : Session = Depends(get_db)):
    
    # vInfo = citizenInfoRequest.vaccineInfo
    # vaccineInfoObject :models.VaccineInfo
    new_record = models.Citizen(citizenId=citizenInfoRequest.citizenId,
                                firstName = citizenInfoRequest.firstName,
                                lastName = citizenInfoRequest.lastName,
                                phoneNumber = citizenInfoRequest.phoneNumber,
                                emailId = citizenInfoRequest.emailId,
                                )
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

