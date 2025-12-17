from pydantic import BaseModel, Field
from typing import List, Optional, Any, Dict, ClassVar

class DomainModel(BaseModel):
    # ClassVar ensures this is treated as a class attribute, not a model field
    DOMAIN: ClassVar[str]
    model_config = {"extra": "allow"}

class Profile(DomainModel):
    DOMAIN: ClassVar[str] = "PROFILE"

    firstName: Optional[str] = Field(None, alias="First Name")
    lastName: Optional[str] = Field(None, alias="Last Name")
    headline: Optional[str] = Field(None, alias="Headline")
    summary: Optional[str] = Field(None, alias="Summary")
    industry: Optional[str] = Field(None, alias="Industry")
    geoLocation: Optional[str] = Field(None, alias="Geo Location")
    zipCode: Optional[str] = Field(None, alias="Zip Code")
    address: Optional[str] = Field(None, alias="Address")
    websites: Optional[str] = Field(None, alias="Websites")
    instantMessengers: Optional[str] = Field(None, alias="Instant Messengers")
    twitterHandles: Optional[str] = Field(None, alias="Twitter Handles")
    birthDate: Optional[str] = Field(None, alias="Birth Date")
    maidenName: Optional[str] = Field(None, alias="Maiden Name")


class Position(DomainModel):
    DOMAIN: ClassVar[str] = "POSITIONS"

    companyName: Optional[str] = Field(None, alias="Company Name")
    title: Optional[str] = Field(None, alias="Title")
    description: Optional[str] = Field(None, alias="Description")
    location: Optional[str] = Field(None, alias="Location")
    startedOn: Optional[str] = Field(None, alias="Started On")
    finishedOn: Optional[str] = Field(None, alias="Finished On")


class Education(DomainModel):
    DOMAIN: ClassVar[str] = "EDUCATION"

    schoolName: Optional[str] = Field(None, alias="School Name")
    degree: Optional[str] = Field(None, alias="Degree Name")
    activities: Optional[str] = Field(None, alias="Activities")
    notes: Optional[str] = Field(None, alias="Notes")
    startDate: Optional[str] = Field(None, alias="Start Date")
    endDate: Optional[str] = Field(None, alias="End Date")

class Skill(DomainModel):
    DOMAIN: ClassVar[str] = "SKILLS"

    name: str = Field(..., alias="Name")

class Publication(DomainModel):
    DOMAIN: ClassVar[str] = "PUBLICATIONS"

    name: Optional[str] = Field(None, alias="Name")
    publisher: Optional[str] = Field(None, alias="Publisher")
    description: Optional[str] = Field(None, alias="Description")
    publishedOn: Optional[str] = Field(None, alias="Published On")
    url: Optional[str] = Field(None, alias="Url")

class Project(DomainModel):
    DOMAIN: ClassVar[str] = "PROJECTS"

class Certification(DomainModel):
    DOMAIN: ClassVar[str] = "CERTIFICATIONS"

class Language(DomainModel):
    DOMAIN: ClassVar[str] = "LANGUAGES"

class Course(DomainModel):
    DOMAIN: ClassVar[str] = "COURSES"

class Honor(DomainModel):
    DOMAIN: ClassVar[str] = "HONORS"

class VolunteeringExperience(DomainModel):
    DOMAIN: ClassVar[str] = "VOLUNTEERING_EXPERIENCES"

class Patent(DomainModel):
    DOMAIN: ClassVar[str] = "PATENTS"

class SnapshotElement(BaseModel):
    snapshotDomain: str
    snapshotData: List[Dict[str, Any]]

class PagingLink(BaseModel):
    rel: str
    href: str
    type: str

class Paging(BaseModel):
    start: int
    count: int
    total: int
    links: List[PagingLink] = []

class SnapshotResponse(BaseModel):
    paging: Optional[Paging] = None
    elements: List[SnapshotElement]