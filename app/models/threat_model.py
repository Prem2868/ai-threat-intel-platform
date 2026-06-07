# Threat Model Definition\n\nfrom pydantic import BaseModel\n\nclass Threat(BaseModel):\n    id: str\n    severity: int\n    description: str\n    source: str
