####################################
# In questo file inserisco tutte le funzionalità e le sezioni che mi saranno utili per
# la descrizione degli steps istanze particolari di ogni superclasse. Ad esempio qui
# definirò la sezione contenente tutti i parametri relativi a una colonna ICP utile sia
# per alcuni processi RIE e alcnui processi CVD.
####################################

from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.datamodel.data import ArchiveSection
from nomad.metainfo import MEnum, Quantity, Section, SubSection

from fabrication_facilities.schema_packages.Items import ItemPlacement
from fabrication_facilities.schema_packages.utils import (
    BeamSource,
    FabricationChemical,
    TimeRampMassflow,
    TimeRampPressure,
    TimeRampRotation,
    TimeRampTemperature,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )


class ICP_Column(ArchiveSection):
    m_def = Section(
        description="""
        Section used to describe component to obtaine inductively coupled plasma
        """
    )

    icp_power = Quantity(
        type=np.float64,
        description='Power erogated in the region of the plasma',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'watt',
        },
        unit='watt',
    )
    icp_frequency = Quantity(
        type=np.float64,
        description='Frequency of current on the gases area',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )


class Clamping_System(ArchiveSection):
    m_def = Section(
        description="""
        Class describing all parameters useful for clamping, if used during the step.
        """
    )

    clamping_type = Quantity(
        type=MEnum(
            [
                'None',
                'Mechanical',
                'Electrostatic',
            ]
        ),
        a_eln={'component': 'EnumEditQuantity'},
    )

    clamping_pressure = Quantity(
        type=np.float64,
        description='Adhesion pressure generated on the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    pressure_ramps = SubSection(
        section_def=TimeRampPressure,
        repeats=True,
    )


class Chuck(ArchiveSection):
    m_def = Section(
        description="""
        Section containing all parameters relative to the chuck.
        """
    )

    chuck_temperature = Quantity(
        type=np.float64,
        description='Temperature imposed on the chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )

    chuck_power = Quantity(
        type=np.float64,
        description='Power imposed on the chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'W'},
        unit='W',
    )

    chuck_high_frequency = Quantity(
        type=np.float64,
        description='High frequency impulse imposed on the chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'MHz'},
        unit='MHz',
    )

    chuck_low_frequency = Quantity(
        type=np.float64,
        description='Low frequency impulse imposed on the chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'MHz'},
        unit='MHz',
    )

    bias = Quantity(
        type=np.float64,
        description='Voltage imposed on the sample by electrodes',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'V'},
        unit='V',
    )

    temperature_ramps = SubSection(
        section_def=TimeRampTemperature,
        repeats=True,
    )

    clamping = SubSection(section_def=Clamping_System, repeats=False)

    item_placement = SubSection(
        section_def=ItemPlacement,
        repeats=False,
    )


class DRIE_Chuck(ArchiveSection):
    m_def = Section(
        description="""
        Section containing all parameters relative to the chuck in a DRIE process. The
        main property is the existence of an alternate powering for electrical data,
        so also the duration of each phase is reported.
        """
    )

    chuck_temperature = Quantity(
        type=np.float64,
        description='Temperature imposed on the chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )

    high_chuck_power = Quantity(
        type=np.float64,
        description='Power erogated on the chuck in the high phase',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'watt',
        },
        unit='watt',
    )

    low_chuck_power = Quantity(
        type=np.float64,
        description='Power erogated on the chuck in the low phase',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'watt',
        },
        unit='watt',
    )

    high_chuck_power_duration = Quantity(
        type=np.float64,
        description='Power erogated on the chuck in the high phase',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'sec',
        },
        unit='sec',
    )

    low_chuck_power_duration = Quantity(
        type=np.float64,
        description='Duration of the low phase',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'sec',
        },
        unit='sec',
    )

    chuck_high_frequency = Quantity(
        type=np.float64,
        description='High frequency impulse imposed on the chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'MHz'},
        unit='MHz',
    )

    chuck_low_frequency = Quantity(
        type=np.float64,
        description='Low frequency impulse imposed on the chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'MHz'},
        unit='MHz',
    )

    bias = Quantity(
        type=np.float64,
        description='Voltage imposed on the sample by electrodes',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'V'},
        unit='V',
    )

    temperature_ramps = SubSection(
        section_def=TimeRampTemperature,
        repeats=True,
    )


class Carrier(ArchiveSection):
    m_def = Section(
        description="""
        Section describing a component used to carry vertically one or more wafers
        """
    )

    slots = Quantity(
        type=int,
        description='Total number of possible positioning for wafers',
        a_eln={'component': 'NumberEditQuantity'},
    )

    position_of_item = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
        description="""
        Number of the slot where the item is located. 1 is the the first
        slot which enter in the process chamber.
        """,
    )

    position_of_dummy_wafers = Quantity(
        type=int,
        shape=['*'],
        a_eln={'component': 'NumberEditQuantity'},
        description="""
        Dummy wafers are used to reach uniformity in the chamber. If the
        step do not require dummy wafers or they are not important this field could be
        void.
        """,
    )


class Massflow_controller(FabricationChemical):
    m_def = Section(
        a_eln={'overview': True, 'hide': ['lab_id', 'datetime']},
    )
    massflow = Quantity(
        type=np.float64,
        description='Rate at which the gas flows',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'centimeter^3/minute',
        },
        unit='centimeter^3/minute',
    )

    gaseous_massflow_ramps = SubSection(
        section_def=TimeRampMassflow,
        repeats=True,
    )


class DRIE_Massflow_controller(Massflow_controller):
    m_def = Section(
        a_eln={'overview': True, 'hide': ['lab_id', 'datetime', 'massflow']},
    )

    priority = Quantity(
        type=str,
        description='Parameter describing the ordering in the chemical reactivity',
        a_eln={'component': 'StringEditQuantity'},
    )

    inactive_state_massflow = Quantity(
        type=np.float64,
        description='Rate at which the gas flows in the inactive phase of DRIE',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'centimeter^3/minute',
        },
        unit='centimeter^3/minute',
    )

    active_state_massflow = Quantity(
        type=np.float64,
        description='Rate at which the gas flows in the inactive phase of DRIE',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'centimeter^3/minute',
        },
        unit='centimeter^3/minute',
    )

    pulse_time = Quantity(
        type=np.float64,
        description='Atomistic time of activity for the gas',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )


class WetReactiveComponents(FabricationChemical):
    m_def = Section(
        definition='Chemicals for wet fabrication steps',
        a_eln={
            'properties': {
                'order': [
                    'name',
                    'chemical_formula',
                    'description',
                    'solution_concentration',
                ],
            },
        },
    )

    solution_concentration = Quantity(
        type=np.float64,
        description='Volume percentage of the reactive in the solution',
        a_eln={'component': 'NumberEditQuantity'},
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class DevelopingSolution(ArchiveSection):
    m_def = Section()

    dispensed_volume = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'milliliter'},
        unit='milliliter',
    )

    developing_solution_components = SubSection(
        section_def=WetReactiveComponents,
        repeats=True,
    )

    surfactants = SubSection(section_def=WetReactiveComponents, repeats=True)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class ResistivityControl(ArchiveSection):
    m_def = Section(
        description='Section used in case of resistivity feedbacks',
    )

    resistivity_target = Quantity(
        type=np.float64,
        description='Value used as target to stop the process',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'ohm*cm'},
        unit='ohm*cm',
    )

    increment_duration = Quantity(
        type=np.float64,
        description='Time used in the process to reach the target value',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )


class SpinningComponent(ArchiveSection):
    m_def = Section()

    spin_frequency = Quantity(
        type=np.float64,
        description='Velocity of the spinner',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'revolutions_per_minute',
        },
        unit='revolutions_per_minute',
    )
    spin_angular_acceleration = Quantity(
        type=np.float64,
        description='Acceleration of the spinner',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'revolutions_per_minute/sec',
        },
        unit='revolutions_per_minute/sec',
    )
    spin_duration = Quantity(
        type=np.float64,
        description='Acceleration of the spinner',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'sec',
        },
        unit='sec',
    )

    rotation_ramp = SubSection(
        section_def=TimeRampRotation,
        repeats=False,
    )


class Priming(ArchiveSection):
    m_def = Section()

    primer_type = Quantity(type=str, a_eln={'component': 'StringEditQuantity'})
    primer_temperature = Quantity(
        type=np.float64,
        description='Temperature of the primer',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )
    priming_duration = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )
    final_cooling_tempereature = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )
    final_cooling_duration = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )


class DeIonizedWaterRinsing(ArchiveSection):
    m_def = Section(
        description="""
        Section describing passages in a step where de ionized water is
        """
    )

    rinsing_cycles = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )

    rinsing_duration = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )


# class DeIonizedWaterDumping(ArchiveSection):
#     m_def = Section()

#     dumping_cycles = Quantity(
#         type=int,
#         a_eln={'component': 'NumberEditQuantity'},
#     )
#     dumping_drain_duration = Quantity(
#         type=np.float64,
#         a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
#         unit='minute',
#     )


# class BeamSource(ArchiveSection):
#     m_def = Section()

#     emitter_material = Quantity(type=str, a_eln={'component': 'StringEditQuantity'})

#     probe = Quantity(type=str, a_eln={'component': 'StringEditQuantity'})


class BeamColumn(ArchiveSection):
    m_def = Section()

    tension = Quantity(
        type=np.float64,
        description='Voltage accelerating the electrons',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'kV',
        },
        unit='kV',
    )

    current_target = Quantity(
        type=np.float64,
        description='Current provided',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'pampere',
        },
        unit='pampere',
    )

    beam_source = SubSection(section_def=BeamSource, repeats=False)


class Alignment(ArchiveSection):
    m_def = Section()

    alignment_mode = Quantity(
        type=MEnum(
            'No alignment',
            'Manual',
            'Auto',
        ),
        a_eln={'component': 'EnumEditQuantity'},
    )
    alignment_max_error = Quantity(
        type=np.float64,
        description='Maximum error allowed in the alignment',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'nm',
        },
        unit='nm',
    )


class WritingParameters(ArchiveSection):
    m_def = Section()

    area_dose = Quantity(
        type=np.float64,
        description='Dose per area used in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'uC/centimeter^2',
        },
        unit='uC/centimeter^2',
    )
    line_dose = Quantity(
        type=np.float64,
        description='Dose per length used in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'uC/centimeter',
        },
        unit='pC/centimeter',
    )
    dot_dose = Quantity(
        type=np.float64,
        description='Dose used in the process for single points',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'pC',
        },
        unit='pC',
    )
    writing_field_dimension = Quantity(
        type=np.float64,
        description='Area covered globally in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'um^2',
        },
        unit='um^2',
    )
    address_size = Quantity(
        type=np.float64,
        description='The minimum distance covered per step in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'nm',
        },
        unit='nm',
    )
    clock = Quantity(
        type=np.float64,
        description='Frequency used',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )
