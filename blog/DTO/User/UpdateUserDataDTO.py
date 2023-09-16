from dataclasses import dataclass
import datetime

@dataclass(frozen=True)
class UpdateUserDataDTO:
    icon: str
    username: str
    first_name: str
    last_name: str
    biography: str
    targets: str
    updated_at = str(datetime.datetime.now()).split('.')[0]
