import enum


class AttackBallType(str, enum.Enum):
    high = 'high'
    medium = 'medium'
    quick = 'quick'
    other = 'other'


class AttackSkill(str, enum.Enum):
    headSpike = 'headSpike'
    softSpike = 'softSpike'
    dink = 'dink'


class AttackEvaluationType(str, enum.Enum):
    kill = 'kill'
    overPass = 'overPass'
    possibleCover = 'possibleCover'
    blocked = 'blocked'
    inPlay = 'inPlay'
    error = 'error'
