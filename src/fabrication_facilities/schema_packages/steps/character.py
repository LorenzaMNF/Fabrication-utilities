from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.datamodel.data import (
    ArchiveSection,
)
from nomad.datamodel.metainfo.basesections import ElementalComposition
from nomad.datamodel.metainfo.eln import Chemical
from nomad.metainfo import (
    MEnum,
    Package,
    Quantity,
    Section,
    SubSection,
)

from fabrication_facilities.schema_packages.fabrication_utilities import (
    FabricationProcessStep,
    FabricationProcessStepBase,
)
from fabrication_facilities.schema_packages.steps.utils import (
    BeamColumn,
)
from fabrication_facilities.schema_packages.utils import (
    parse_chemical_formula,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='Characterization processes schema')


class AFMbase(FabricationProcessStepBase):
    m_def = Section(
        a_eln={
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'tag',
                    'id_item_processed',
                    'operator',
                    'starting_date',
                    'ending_date',
                    'duration',
                    'baking_temperature',
                    'baking_pressure',
                    'notes',
                ]
            },
        },
    )

    afm_tip = Quantity(
        type=str,
        description='the model of the probing tip',
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    
    afm_mode = Quantity(
        type=str,
        description='if proxy or in contact, if linear or scanning',
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    
    afm_setpoint = Quantity(
        type=np.float64,
        description='ask to Erica Iacob',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        unit='nm',
    )
    afm_fb_gain = Quantity(
        type=np.float64,
        description='ask to Erica Iacob',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        unit='nm',
    )
    afm_tip_resonance = Quantity(
        type=np.float64,
        description='ask to Erica Iacob',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        unit='MHz',
    )
    afm_tip_phase = Quantity(
        type=np.float64,
        description='ask to Erica Iacob',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        unit='nm',
    )
    afm_laser_intensity = Quantity(
        type=np.float64,
        description='ask to Erica Iacob',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        unit='mA',
    )
    afm_fb_gain_o = Quantity(
        type=np.float64,
        description='ask to Erica Iacob',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        unit='nm',
    )
