from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.datamodel.data import (
    ArchiveSection,
    EntryData,
)
from nomad.datamodel.metainfo.basesections import ElementalComposition
from nomad.datamodel.metainfo.eln import Chemical
from nomad.metainfo import (
    Datetime,
    MEnum,
    Package,
    Quantity,
    Section,
    SubSection,
)

from fabrication_facilities.schema_packages.steps.utils import (
    Carrier,
    Chuck,
)
from fabrication_facilities.schema_packages.utils import (
    FabricationChemical,
    TimeRampPressure,
    TimeRampTemperature,
    generate_elementality,
    parse_chemical_formula,
)
from fabrication_facilities.schema_packages.fabrication_utilities import (
    EquipmentReference,
    Equipment,
    EquipmentTechnique,
    TechniqueCategories,
    TechniqueGeneralCategory,
    TechniqueMainCategory,
    TechniqueSubCategory,
)
from fabrication_facilities.schema_packages.materials import (
    CharacterizationOutput,
    CharacterizationMaterial,
)
if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='Characterization steps schema')

#CHARACTERIZATION PROCESS, STEP, STEPBASE

class CharacterizationProcessStepBase(ArchiveSection):
    m_def = Section(
        definition="""
        Atomistic component of a generic non-NeXuS characterization step, it should be inherited
        """,
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
                    'notes',
                ],
            },
        },
    )

    job_number = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    operator = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    starting_date = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity'},
    )
    ending_date = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity'},
    )
    duration = Quantity(
        type=np.float64,
        description='Time used in this single atomic step',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )
    id_item_processed = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    tag = Quantity(
        type=str,
        description='Role of the step in fabrication (effective, conditioning, etc.)',
        a_eln={'component': 'StringEditQuantity'},
    )
    notes = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )

class CharacterizationProcessStep(CharacterizationProcessStepBase, EntryData):
    m_def = Section(
        a_eln={
            'hide': [
                'tag',
                'duaration',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'affiliation',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'notes',
                ],
            },
        },
    )

    description = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )
    affiliation = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    location = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    room = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    step_type = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    definition_of_process_step = Quantity(
        type=EquipmentTechnique,
        a_eln={'component': 'ReferenceEditQuantity'},
    )
    keywords = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    recipe_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    recipe_file = Quantity(
        type=str,
        a_eln={'component': 'FileEditQuantity'},
    )
    recipe_preview = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )

    instruments = SubSection(
        section_def=EquipmentReference,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        if self.instruments.section is not None:
            super().normalize(archive, logger)


class CharacterizationProcess(EntryData, ArchiveSection):
    m_def = Section(
        a_eln={
            'properties': {
                'order': [
                    'name',
                    'project',
                    'affiliation',
                    'id_proposal',
                    'id_item_processed',
                    'locations',
                    'cost_model',
                    'description',
                    'author',
                    'starting_date',
                    'ending_date',
                    'notes',
                ]
            },
            'hide': [
                'end_time',
                'datetime',
                'lab_id',
                'method',
                'location',
            ],
        },
    )
    id_proposal = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    project = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    id_item_processed = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    affiliation = Quantity(
        type=MEnum(
            [
                'NFFA-DI',
                'iENTRANCE@ENL',
            ],
        ),
        a_eln={'component': 'EnumEditQuantity'},
    )
    locations = Quantity(
        type=str,
        shape=['*'],
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'institutions',
        },
    )
    name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    description = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )
    author = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    cost_model = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    starting_date = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity'},
    )
    ending_date = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity'},
    )
    notes = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )

    steps = Quantity(
        type=CharacterizationProcessStep,
        shape=['*'],
        a_eln={'component': 'ReferenceEditQuantity'},
    )
    instruments = SubSection(
        section_def=EquipmentReference,
        repeats=True,
    )
    output = SubSection(section_def=CharacterizationOutput, repeat=False)

class AFMbase(CharacterizationProcessStepBase):
    m_def = Section (
        a_eln={'properties': {
                'order': [
                    'job_number',
                    'name',
                    'tag',
                    'id_item_processed',
                    'operator',
                    'starting_date',
                    'ending_date',
                    'duration',
                    'afm_tip_model',
                    'afm_mode',
                    'afm_resonance',
                    'afm_phase',
                    'notes',
                    'rawdatafile',
                ]
            },
        },
    )

    afm_tip_model = Quantity(
        type=str,
        description='tip brand and model',
        a_eln={'label':'tip','component': 'StringEditQuantity',},

    )

    afm_mode = Quantity(
        type=str,
        description='analysis mode',
        a_eln={'label':'mode','component': 'StringEditQuantity',},

    )

    afm_resonance = Quantity(
        type=np.float64,
        description='tip calibration parameter',
        a_eln={'label':'afm_resonance','component': 'StringEditQuantity',},

    )
    afm_phase = Quantity(
        type=np.float64,
        description='tip calibration parameter',
        a_eln={'label':'afm_phasede','component': 'StringEditQuantity',},

    )
    rawdatafile = Quantity(
        type=str,
        description='raw datafile address',
        a_eln={'label':'rawdatafile','component': 'StringEditQuantity',},

    )
    material_caracterized = SubSection(section_def=FabricationChemical, repeats=True)

    chuck = SubSection(section_def=Chuck, repeats=False)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
