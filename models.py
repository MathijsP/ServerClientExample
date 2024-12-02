from pydantic import BaseModel


class User(BaseModel):
    user_name: str
    token: str


class Material(BaseModel):
    name: str
    youngs_modulus_MPa: float
    poisson_coeff: float


class Inputs(BaseModel):
    user: User
    materials: list[Material]
