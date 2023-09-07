#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.manufacturing_interfaces.manufacturing_output_generator import ManufacturingOutputGenerator


class ManufacturingAptGenerator(ManufacturingOutputGenerator):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                    ManufacturingInterfaces.ManufacturingOutputGenerator
                |                         ManufacturingAPTGenerator
                | 
                | Generator of APT output machining code.
                | 
                | See also:
                |     ManufacturingOutputGenerator 

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_apt_generator = com_object

    def __repr__(self):
        return f'ManufacturingAptGenerator(name="{self.name}")'
