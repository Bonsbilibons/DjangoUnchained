from dataclasses import dataclass
import datetime

@dataclass(frozen=True)
class CreatePostDTO:
    title: str
    description: str
    images: str
    user: str
    updated_at = str(datetime.datetime.now()).split('.')[0]
    created_at = str(datetime.datetime.now()).split('.')[0]
