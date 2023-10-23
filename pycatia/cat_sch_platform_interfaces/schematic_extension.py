#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_list_of_objects import SchListOfObjects
from pycatia.system_interfaces.any_object import AnyObject


class SchematicExtension(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchematicExtension
                | 
                | Manage schematic extensions.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.schematic_extension = com_object

    def add_extension(
            self,
            i_app_obj_to_be_extended: AnyObject,
            i_extension_type: int,
            i_lgrr: SchListOfObjects
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddExtension(AnyObject iAppObjToBeExtended,
                | CatSchIDLExtensionType iExtensionType,
                | SchListOfObjects iLGRR)
                | 
                |     Adds a Schematic extension to an application object.
                | 
                |     Parameters:
                | 
                |         iAppObjToBeExtended
                |             The application object to be extended. 
                |         iExtensionType
                |             The extension type. 
                |         iLGRR
                |             If iLGRR is not NULL, then its members will be linked to the
                |             extension as graphics 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchematicExtension
                |          Dim objArg1 As AnyObject
                | 
                |          Dim objArg3 As SchListOfObjects
                |           ...
                |          objThisIntf.AddExtensionobjArg1,CatSchIDLExtensionType_Enum,objArg3

        :param AnyObject i_app_obj_to_be_extended:
        :param int i_extension_type:
        :param SchListOfObjects i_lgrr:
        :rtype: None
        """
        return self.schematic_extension.AddExtension(
            i_app_obj_to_be_extended.com_object,
            i_extension_type,
            i_lgrr.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_extension'
        # # vba_code = """
        # # Public Function add_extension(schematic_extension)
        # #     Dim iAppObjToBeExtended (2)
        # #     schematic_extension.AddExtension iAppObjToBeExtended
        # #     add_extension = iAppObjToBeExtended
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_extension(self, i_app_extended_obj: AnyObject, i_extension_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveExtension(AnyObject iAppExtendedObj,
                | CatSchIDLExtensionType iExtensionType)
                | 
                |     Removes a Schematic extension to an application object.
                | 
                |     Parameters:
                | 
                |         iAppExtendedObj
                |             The application object to be have its extension removed.
                |             
                |         iExtensionType
                |             The extension type. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchematicExtension
                |          Dim objArg1 As AnyObject
                |           ...
                |          objThisIntf.RemoveExtensionobjArg1,CatSchIDLExtensionType_Enum

        :param AnyObject i_app_extended_obj:
        :param int i_extension_type:
        :rtype: None
        """
        return self.schematic_extension.RemoveExtension(i_app_extended_obj.com_object, i_extension_type)

    def __repr__(self):
        return f'SchematicExtension(name="{self.name}")'
