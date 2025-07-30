#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.datamodel.data import ArchiveSection, EntryData
from nomad.datamodel.metainfo.eln import Instrument
from nomad.metainfo import (
    Package,
    Quantity,
    Section,
    SubSection,
)

from fabrication_facilities.schema_packages.equipments.utils import (
    BeamColumnCapabilites,
    CarrierDescription,
    ChuckCapabilities,
    ICP_ColumnCapabilities,
    Massflow_parameter,
    SpinnerSpinParameters,
    WritingCapabilities,
)
from fabrication_facilities.schema_packages.fabrication_utilities import Equipment
from fabrication_facilities.schema_packages.utils import (
    ReactiveComponents,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='Equipments specific definitions ')


class BakingFurnace(Equipment):
    m_def = Section(
        a_eln={
            'hide': [
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'lab_id',
                    'description',
                    'affiliation',
                    'institution',
                    'product_model',
                    'manufacturer_name',
                    'inventary_code',
                    'is_bookable',
                    'automatic_loading',
                    'contamination_class',
                    'min_baking_temperature',
                    'max_baking_temperature',
                    'min_baking_pressure',
                    'max_baking_pressure',
                    'notes',
                ],
            },
        }
    )

    min_baking_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature available in the chamber',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_baking_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature available in the chamber',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    min_baking_pressure = Quantity(
        type=np.float64,
        description='Minimal pressure available in the chamber',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    max_baking_pressure = Quantity(
        type=np.float64,
        description='Maximal pressure available in the chamber',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )


class RIE_Etcher(Equipment):
    m_def = Section(
        a_eln={
            'hide': [
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'lab_id',
                    'description',
                    'affiliation',
                    'institution',
                    'product_model',
                    'manufacturer_name',
                    'inventary_code',
                    'is_bookable',
                    'automatic_loading',
                    'contamination_class',
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'vacuum_system_name',
                    'min_chamber_temperature',
                    'max_chamber_temperature',
                    'notes',
                ],
            },
        },
        description='Base classes for etching instruments',
    )

    vacuum_system_name = Quantity(
        type=str,
        description='Type of vacuum pump adopted',
        a_eln={
            'component': 'StringEditQuantity',
        },
    )

    min_chamber_pressure = Quantity(
        type=np.float64,
        description='Minimal pressure available',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    max_chamber_pressure = Quantity(
        type=np.float64,
        description='Maximal pressure available',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    min_chamber_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature at disposal for the wall',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_chamber_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the wall',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    gases = SubSection(
        section_def=Massflow_parameter,
        repeats=True,
    )

    chuck = SubSection(
        section_def=ChuckCapabilities,
        repeats=False,
    )


class ICP_RIE_Etcher(RIE_Etcher):
    m_def = Section(
        description='Dry etching class for instruments where a plasma is involved',
        a_eln={
            'hide': [
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'lab_id',
                    'description',
                    'affiliation',
                    'institution',
                    'product_model',
                    'manufacturer_name',
                    'inventary_code',
                    'is_bookable',
                    'automatic_loading',
                    'contamination_class',
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'vacuum_system_name',
                    'min_chamber_temperature',
                    'max_chamber_temperature',
                    'notes',
                ],
            },
        },
    )

    icp_parameters = SubSection(
        section_def=ICP_ColumnCapabilities,
        repeats=False,
    )


class DRIE_BOSCH_Etcher(ICP_RIE_Etcher):
    m_def = Section(
        description='Dry etching instrument for deep geometries',
        a_eln={
            'hide': [
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'lab_id',
                    'description',
                    'affiliation',
                    'institution',
                    'product_model',
                    'manufacturer_name',
                    'inventary_code',
                    'is_bookable',
                    'automatic_loading',
                    'contamination_class',
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'vacuum_system_name',
                    'min_chamber_temperature',
                    'max_chamber_temperature',
                    'notes',
                ],
            },
        },
    )


class Wet_Bench_Unit(Equipment):
    m_def = Section(
        description="""
        Bath containing a chemical solution or pure substance to perform wet processes,
        """,
        a_eln={
            'hide': [
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'lab_id',
                    'description',
                    'affiliation',
                    'institution',
                    'product_model',
                    'manufacturer_name',
                    'inventary_code',
                    'is_bookable',
                    'automatic_loading',
                    'contamination_class',
                    'volume_of_solution',
                    'min_bath_temperature',
                    'max_bath_temperature',
                    'max_overflow_time',
                    'pumping_mechanism',
                    'solution_renewal',
                    'max_number_of_repetitions',
                ]
            },
        },
    )

    hood_system = Quantity(
        type=str,
        description="""
        Name of the hood system used for safety. It could be used also to identify the
        location of each tank in the labs.
        """,
        a_eln={'component': 'StringEditQuantity'},
    )

    volume_of_solution = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'liter'},
        unit='liter',
    )

    min_bath_temperature = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )

    max_bath_temperature = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )

    # max_overflow_time = Quantity(
    #     type=np.float64,
    #     description='Maximum amount of flow at disposal',
    #     a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
    #     unit='sec',
    # )

    pumping_mechanism = Quantity(
        type=bool,
        description='There is a filtering system for the bath?',
        a_eln={'component': 'BoolEditQuantity'},
    )

    # recycle_mechanism = Quantity(
    #     type=bool,
    #     description='There is a filtering system for the bath?',
    #     a_eln={'component': 'BoolEditQuantity'},
    # )

    solution_renewal = Quantity(
        type=str,
        description='Frequency of the renewal of the solution in the bath',
        a_eln={'component': 'StringEditQuantity'},
    )

    max_number_of_repetitions = Quantity(
        type=int,
        description='Maximum number of successive steps allowed for that well',
        a_eln={'component': 'NumberEditQuantity'},
    )

    max_time_of_usage = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )

    ultrasounds_required = Quantity(
        type=bool,
        a_eln={
            'component': 'BoolEditQuantity',
        },
    )

    reactives = SubSection(section_def=ReactiveComponents, repeats=True)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        if self.volume_of_solution is not None:
            super().normalize(archive, logger)
            for token in self.reactives:
                token.final_solution_concentration = (
                    token.initial_concentration
                    * token.dispensed_volume
                    / (100 * self.volume_of_solution)
                )


class Dump_Rinser(Equipment):
    m_def = Section(
        a_eln={
            'hide': [
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'lab_id',
                    'description',
                    'affiliation',
                    'institution',
                    'product_model',
                    'manufacturer_name',
                    'inventary_code',
                    'is_bookable',
                    'automatic_loading',
                    'contamination_class',
                    'max_overflow_time',
                    'pumping_mechanism',
                    'cycles_drain_time',
                    'final_drain_time',
                    'resistivity_cut_off',
                    'notes',
                ]
            },
        }
    )

    resistivity_cut_off = Quantity(
        type=np.float64,
        description='Value used as target to stop the process',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'ohm*cm'},
        unit='ohm*cm',
    )

    max_overflow_time = Quantity(
        type=np.float64,
        description='Maximum amount of flow at disposal',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )


class Wet_Bench(Instrument, EntryData, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'lab_id',
                    'description',
                    'institution',
                    'product_model',
                    'manufacturer_name',
                    'inventary_code',
                    'notes',
                ]
            },
        }
    )

    lab_id = Quantity(
        type=str,
        description='ID assigned by lab for findability',
        a_eln={'component': 'StringEditQuantity', 'label': 'id'},
    )
    inventary_code = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    institution = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    manufacturer_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    product_model = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )

    notes = Quantity(
        type=str,
        a_eln={
            'component': 'RichTextEditQuantity',
        },
    )

    tanks = SubSection(section_def=Wet_Bench_Unit, repeats=True)
    dumping_rinser = SubSection(section_def=Dump_Rinser, repeats=True)


class LPCVD_System(Equipment):
    m_def = Section(
        a_eln={
            'hide': [
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'lab_id',
                    'description',
                    'affiliation',
                    'institution',
                    'product_model',
                    'manufacturer_name',
                    'inventary_code',
                    'is_bookable',
                    'automatic_loading',
                    'contamination_class',
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'vacuum_system_name',
                    'min_chamber_temperature',
                    'max_chamber_temperature',
                    'notes',
                ],
            },
        },
        description='Instrument used to perform LPCVD steps',
    )

    vacuum_system_name = Quantity(
        type=str,
        description='Type of vacuum pump adopted',
        a_eln={
            'component': 'StringEditQuantity',
        },
    )

    min_chamber_pressure = Quantity(
        type=np.float64,
        description='Minimal pressure available',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    max_chamber_pressure = Quantity(
        type=np.float64,
        description='Maximal pressure available',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    min_chamber_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature at disposal for the wall',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_chamber_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the wall',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    gases = SubSection(
        section_def=Massflow_parameter,
        repeats=True,
    )

    allowed_carriers = SubSection(
        section_def=CarrierDescription,
        repeats=True,
    )


class PECVD_System(Equipment):
    m_def = Section(
        description='Class instrument for PECVD procedures',
        a_eln={
            'hide': [
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'lab_id',
                    'description',
                    'affiliation',
                    'institution',
                    'product_model',
                    'manufacturer_name',
                    'inventary_code',
                    'is_bookable',
                    'automatic_loading',
                    'contamination_class',
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'vacuum_system_name',
                    'min_chamebr_temperature',
                    'max_chamber_temperature',
                    'notes',
                ],
            },
        },
    )

    vacuum_system_name = Quantity(
        type=str,
        description='Type of vacuum pump adopted',
        a_eln={
            'component': 'StringEditQuantity',
        },
    )

    min_chamber_pressure = Quantity(
        type=np.float64,
        description='Minimal pressure available',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    max_chamber_pressure = Quantity(
        type=np.float64,
        description='Maximal pressure available',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    min_chamber_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature at disposal for the wall',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_chamber_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the wall',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    gases = SubSection(
        section_def=Massflow_parameter,
        repeats=True,
    )

    chuck = SubSection(
        section_def=ChuckCapabilities,
        repeats=False,
    )


class ICP_CVD_System(PECVD_System):
    m_def = Section(
        description='Class for instruments devoted to ICP_CVD procedures',
        a_eln={
            'hide': [
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'lab_id',
                    'description',
                    'affiliation',
                    'institution',
                    'product_model',
                    'manufacturer_name',
                    'inventary_code',
                    'is_bookable',
                    'automatic_loading',
                    'contamination_class',
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'vacuum_system_name',
                    'min_chamber_temperature',
                    'max_chamber_temperature',
                    'notes',
                ],
            },
        },
    )

    icp_parameters = SubSection(section_def=ICP_ColumnCapabilities, repeats=False)


class Spinner(Equipment):
    m_def = Section(
        description="""
        Class for instruments devoted to spinning procedures like resist depositions.
        """,
        a_eln={
            'hide': [
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'lab_id',
                    'description',
                    'affiliation',
                    'institution',
                    'product_model',
                    'manufacturer_name',
                    'inventary_code',
                    'is_bookable',
                    'automatic_loading',
                    'contamination_class',
                    # 'min_spin_frequency',
                    # 'max_spin_frequency',
                    # 'max_spin_angular_acceleration',
                    'item_contact_type',
                    'notes',
                ]
            },
        },
    )

    item_contact_type = Quantity(type=str, a_eln={'component': 'StringEditQuantity'})

    spin_capabilities = SubSection(
        section_def=SpinnerSpinParameters,
        repeats=False,
    )

    # min_spin_frequency = Quantity(
    #     type=np.float64,
    #     description='Mnimum velocity of the spinner',
    #     a_eln={
    #         'component': 'NumberEditQuantity',
    #         'defaultDisplayUnit': 'revolutions_per_minute',
    #     },
    #     unit='revolutions_per_minute',
    # )

    # max_spin_frequency = Quantity(
    #     type=np.float64,
    #     description='Maximal velocity of the spinner',
    #     a_eln={
    #         'component': 'NumberEditQuantity',
    #         'defaultDisplayUnit': 'revolutions_per_minute',
    #     },
    #     unit='revolutions_per_minute',
    # )

    # max_spin_angular_acceleration = Quantity(
    #     type=np.float64,
    #     description='Maximal acceleration of the spinner',
    #     a_eln={
    #         'component': 'NumberEditQuantity',
    #         'defaultDisplayUnit': 'revolutions_per_minute/sec',
    #     },
    #     unit='revolutions_per_minute/sec',
    # )


class ElectronBeamLithographer(Equipment):
    m_def = Section(
        a_eln={
            'hide': [
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'lab_id',
                    'description',
                    'affiliation',
                    'institution',
                    'product_model',
                    'manufacturer_name',
                    'inventary_code',
                    'is_bookable',
                    'automatic_loading',
                    'contamination_class',
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                ],
            },
        }
    )

    min_chamber_pressure = Quantity(
        type=np.float64,
        description='Minimal pressure available',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    max_chamber_pressure = Quantity(
        type=np.float64,
        description='Maximal pressure available',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    # beam_source_available = SubSection(section_def=BeamSource, repeats=False)
    beam_column_capabilities = SubSection(
        section_def=BeamColumnCapabilites, repeats=False
    )

    writing_capabilities = SubSection(section_def=WritingCapabilities, repeats=False)


class FocusedIonBeamLithographer(ElectronBeamLithographer):
    m_def = Section(
        a_eln={
            'hide': [
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'lab_id',
                    'description',
                    'affiliation',
                    'institution',
                    'product_model',
                    'manufacturer_name',
                    'inventary_code',
                    'is_bookable',
                    'automatic_loading',
                    'contamination_class',
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'notes',
                ],
            },
        }
    )


class ResistDeveloper(Equipment, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'inventary_code',
                    'affiliation',
                    'product_model',
                    'institution',
                    'manufacturer_name',
                    'is_bookable',
                    'automatic_loading',
                    'description',
                    'min_chuck_temperature',
                    'max_chuck_temperature',
                ],
            },
        }
    )

    min_chuck_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_chuck_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )


class Rinser(Equipment, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'inventary_code',
                    'affiliation',
                    'product_model',
                    'institution',
                    'manufacturer_name',
                    'is_bookable',
                    'automatic_loading',
                    'description',
                    'min_chuck_temperature',
                    'max_chuck_temperature',
                ],
            },
        }
    )

    min_chuck_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_chuck_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )
    
#preliminary test about inserting a new equipment, July 30 2025 - recipe parameters taken from FabLIMS
class AFM(Equipment, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'inventary_code',
                    'affiliation',
                    'product_model',
                    'institution',
                    'manufacturer_name',
                    'is_bookable',
                    'automatic_loading',
                    'description',
                ],
            },
        }
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
    )
    afm_fb_gain = Quantity(
        type=np.float64,
        description='ask to Erica Iacob',
        a_eln={
            'component': 'NumberEditQuantity',
        },
    )
    afm_tip_resonance = Quantity(
        type=np.float64,
        description='ask to Erica Iacob',
        a_eln={
            'component': 'NumberEditQuantity',
        },
    )
    afm_tip_phase = Quantity(
        type=np.float64,
        description='ask to Erica Iacob',
        a_eln={
            'component': 'NumberEditQuantity',
        },
    )
    afm_laser_intensity = Quantity(
        type=np.float64,
        description='ask to Erica Iacob',
        a_eln={
            'component': 'NumberEditQuantity',
        },
    )
    afm_fb_gain_o = Quantity(
        type=np.float64,
        description='ask to Erica Iacob',
        a_eln={
            'component': 'NumberEditQuantity',
        },
    )
