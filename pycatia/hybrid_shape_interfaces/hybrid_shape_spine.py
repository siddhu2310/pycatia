#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeSpine(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeSpine
                | 
                | Represents the hybrid spine curve feature object.
                | Role:Use the CATIAHybridShapeFactory to create a HybridShapeSpine
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_spine = com_object

    @property
    def orientation(self) -> int:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Orientation() As long
                | 
                |     Gets or Sets the orientation. Orientation by reference with the normal to
                |     the first section/plane

        :return: int
        :rtype: int
        """

        return self.hybrid_shape_spine.Orientation

    @orientation.setter
    def orientation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_spine.Orientation = value

    @property
    def start_point(self) -> Reference:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property StartPoint() As Reference
                | 
                |     Returns or sets the start point of the spine.

        :return: Reference
        :rtype: Reference
        """

        return Reference(self.hybrid_shape_spine.StartPoint)

    @start_point.setter
    def start_point(self, reference_point: Reference):
        """
        :param Reference reference_point:
        """

        self.hybrid_shape_spine.StartPoint = reference_point.com_object

    def add_guide(self, i_guide: Reference) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddGuide(Reference iGuide)
                | 
                |     Adds a guide to the spine curve.
                | 
                |     Parameters:
                | 
                |         iGuide
                |             The guide curve to be added

        :param Reference i_guide:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_spine.AddGuide(i_guide.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_guide'
        # # vba_code = """
        # # Public Function add_guide(hybrid_shape_spine)
        # #     Dim iGuide (2)
        # #     hybrid_shape_spine.AddGuide iGuide
        # #     add_guide = iGuide
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_section(self, i_section: Reference) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddSection(Reference iSection)
                | 
                |     Adds a section or a plane to the spine curve.
                | 
                |     Parameters:
                | 
                |         iSection
                |             The section curve or plane to be added
                | 
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): PlanarFace.

        :param Reference i_section:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_spine.AddSection(i_section.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_section'
        # # vba_code = """
        # # Public Function add_section(hybrid_shape_spine)
        # #     Dim iSection (2)
        # #     hybrid_shape_spine.AddSection iSection
        # #     add_section = iSection
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_guide(self, i_idx: int, op_ia_guide: Reference) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetGuide(long iIdx,
                | Reference opIAGuide)
                | 
                |     Retrieves a guide .
                | 
                |     Parameters:
                | 
                |         iIdx
                |             The index of the guide 
                |         opIAGuide
                |             The guide retrieved

        :param int i_idx:
        :param Reference op_ia_guide:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_spine.GetGuide(i_idx, op_ia_guide.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_guide'
        # # vba_code = """
        # # Public Function get_guide(hybrid_shape_spine)
        # #     Dim iIdx (2)
        # #     hybrid_shape_spine.GetGuide iIdx
        # #     get_guide = iIdx
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_number_of_guides(self) -> int:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetNumberOfGuides() As long
                | 
                |     Retrieves number of guides in a spine curve.
                | 
                |     Parameters:
                | 
                |         oNbGuides
                |             Number of guides in a spine curve

        :return: int
        :rtype: int
        """
        return self.hybrid_shape_spine.GetNumberOfGuides()

    def get_number_of_sections(self) -> int:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetNumberOfSections() As long
                | 
                |     Retrieves number of sections in a spine curve.
                | 
                |     Parameters:
                | 
                |         oNbSections
                |             Number of sections in a spine curve

        :return: int
        :rtype: int
        """
        return self.hybrid_shape_spine.GetNumberOfSections()

    def get_section(self, i_idx: int, o_section: Reference) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetSection(long iIdx,
                | Reference oSection)
                | 
                |     Retrieves a section or a plane.
                | 
                |     Parameters:
                | 
                |         iIdx
                |             The index of the section 
                |         oSection
                |             The section retrieved

        :param int i_idx:
        :param Reference o_section:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_spine.GetSection(i_idx, o_section.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_section'
        # # vba_code = """
        # # Public Function get_section(hybrid_shape_spine)
        # #     Dim iIdx (2)
        # #     hybrid_shape_spine.GetSection iIdx
        # #     get_section = iIdx
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def modify_guide_curve(self, ip_ia_guide: Reference, ip_ia_new_guide: Reference) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub ModifyGuideCurve(Reference ipIAGuide,
                | Reference ipIANewGuide)
                | 
                |     Modifies a guide from the spine curve.
                | 
                |     Parameters:
                | 
                |         ipIAGuide
                |             The guide curve to be replaced. 
                |         ipIANewGuide
                |             The new guide curve or plane which replaces the old
                |             one.

        :param Reference ip_ia_guide:
        :param Reference ip_ia_new_guide:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_spine.ModifyGuideCurve(ip_ia_guide.com_object, ip_ia_new_guide.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'modify_guide_curve'
        # # vba_code = """
        # # Public Function modify_guide_curve(hybrid_shape_spine)
        # #     Dim ipIAGuide (2)
        # #     hybrid_shape_spine.ModifyGuideCurve ipIAGuide
        # #     modify_guide_curve = ipIAGuide
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def modify_section_curve(self, ip_ia_section: Reference, ip_ia_new_section: Reference) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub ModifySectionCurve(Reference ipIASection,
                | Reference ipIANewSection)
                | 
                |     Modifies a section or a plane from the spine curve.
                | 
                |     Parameters:
                | 
                |         ipIASection
                |             The section curve or plane to be replaced. 
                |         ipIANewSection
                |             The new section curve or plane which replaces the old
                |             one.

        :param Reference ip_ia_section:
        :param Reference ip_ia_new_section:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_spine.ModifySectionCurve(ip_ia_section.com_object, ip_ia_new_section.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'modify_section_curve'
        # # vba_code = """
        # # Public Function modify_section_curve(hybrid_shape_spine)
        # #     Dim ipIASection (2)
        # #     hybrid_shape_spine.ModifySectionCurve ipIASection
        # #     modify_section_curve = ipIASection
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_guide(self, i_guide: Reference) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveGuide(Reference iGuide)
                | 
                |     Removes a guide from the spine curve.
                | 
                |     Parameters:
                | 
                |         iGuide
                |             The guide curve to be removed.

        :param Reference i_guide:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_spine.RemoveGuide(i_guide.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_guide'
        # # vba_code = """
        # # Public Function remove_guide(hybrid_shape_spine)
        # #     Dim iGuide (2)
        # #     hybrid_shape_spine.RemoveGuide iGuide
        # #     remove_guide = iGuide
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_section(self, i_section: Reference) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveSection(Reference iSection)
                | 
                |     Removes a section or a plane from the spine curve.
                | 
                |     Parameters:
                | 
                |         iSection
                |             The section curve or plane to be removed.
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): PlanarFace.

        :param Reference i_section:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_spine.RemoveSection(i_section.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_section'
        # # vba_code = """
        # # Public Function remove_section(hybrid_shape_spine)
        # #     Dim iSection (2)
        # #     hybrid_shape_spine.RemoveSection iSection
        # #     remove_section = iSection
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_start_point(self, i_point: Reference) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetStartPoint(Reference iPoint)
                | 
                |     Sets the start point of the spine curve.
                | 
                |     Parameters:
                | 
                |         iPoint
                |             The point to be set as the spine curve start
                |             point.
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): Vertex.

        :param Reference i_point:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_spine.SetStartPoint(i_point.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_start_point'
        # # vba_code = """
        # # Public Function set_start_point(hybrid_shape_spine)
        # #     Dim iPoint (2)
        # #     hybrid_shape_spine.SetStartPoint iPoint
        # #     set_start_point = iPoint
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'HybridShapeSpine(name="{self.name}")'
