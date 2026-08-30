from dataclasses import dataclass, field
from datetime import datetime, timezone
@dataclass
class TraceEvent:
    name:str
    detail:str
    timestamp:str=field(default_factory=lambda:datetime.now(timezone.utc).isoformat())
class Trace:
    def __init__(self): self.events=[]
    def add(self,name,detail): self.events.append(TraceEvent(name,detail))
    def as_dict(self): return [e.__dict__ for e in self.events]
