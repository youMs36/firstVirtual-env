from pydantic import BaseModel

class VaccineInfo(BaseModel):

    doseCount : int
    vaccineSupplier : str
    vaccineLotNumber : str
    # nextAppointmentStartDate : datetime.date
    citizenId : str

class CitizenVaccineDetails(BaseModel):

    citizenId :str
    firstName : str
    lastName : str
    # vaccineInfo : VaccineInfo
    phoneNumber : str
    emailId : str


