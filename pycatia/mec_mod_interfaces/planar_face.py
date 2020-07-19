#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.mec_mod_interfaces.face import Face


class PlanarFace(Face):
    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Reference
                |                         MecModInterfaces.Boundary
                |                             MecModInterfaces.Face
                |                                 PlanarFace
                | 
                | 2-D boundary with a planar geometry.
                | Role: This Boundary object may be, for example, the face of a
                | cube.
                | You will create a PlanarFace object using the Shapes.GetBoundary ,
                | HybridShapes.GetBoundary , Sketches.GetBoundary or Selection.SelectElement2
                | method. Then, you pass it to the operator (such as ShapeFactory.AddNewDraft
                | ).
                | The lifetime of a PlanarFace object is limited, see Boundary.
                | 
                | Example:
                |     This example asks the end user to select a face and two planar faces, and
                |     creates a draft on these faces:
                | 
                |      Dim InputObjectType(0)
                |      Set Document = CATIA.ActiveDocument
                |      Set Selection = Document.Selection
                |      'We propose to the user that he select the face to draft
                |      InputObjectType(0)="Face"
                |      Status=Selection.SelectElement2(InputObjectType,"Select the face to
                |      draft",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set FaceToDraft = Selection.Item(1).Value
                |      Selection.Clear
                |      'We propose to the user that he select the neutral face
                |      InputObjectType(0)="PlanarFace"
                |      Status=Selection.SelectElement2(InputObjectType,"Select the neutral
                |      face",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set NeutralFace = Selection.Item(1).Value
                |      Selection.Clear
                |      'We propose to the user that he select the parting
                |      element
                |      InputObjectType(0)="PlanarFace"
                |      Status=Selection.SelectElement2(InputObjectType,"Select the parting
                |      element",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set PartingElement = Selection.Item(1).Value
                |      Set Draft = ShapeFactory.AddNewDraft(
                |                      FaceToDraft,NeutralFace,0,PartingElement,0.0,0.0,1.0,0,5.0,0
                |                  )
                |      Set DraftDomains = Draft.DraftDomains
                |      Set DraftDomain = DraftDomains.Item(1)
                |      DraftDomain.SetPullingDirection 0.0, 0.0,1.0
                |      Document.Part.Update
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.planar_face = com_object

    def get_first_axis(self, o_first_axis: tuple) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetFirstAxis(CATSafeArrayVariant oFirstAxis)
                | 
                |     Returns the planar face first axis
                | 
                |     Parameters:
                | 
                |         oFirstAxis[0]
                |             The X Coordinate of the planar face first axis 
                |         oFirstAxis[1]
                |             The Y Coordinate of the planar face first axis 
                |         oFirstAxis[2]
                |             The Z Coordinate of the planar face first axis

        :param tuple o_first_axis:
        :return: None
        :rtype: None
        """
        return self.planar_face.GetFirstAxis(o_first_axis)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_first_axis'
        # # vba_code = """
        # # Public Function get_first_axis(planar_face)
        # #     Dim oFirstAxis (2)
        # #     planar_face.GetFirstAxis oFirstAxis
        # #     get_first_axis = oFirstAxis
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_origin(self, o_origin: tuple) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetOrigin(CATSafeArrayVariant oOrigin)
                | 
                |     Returns the origin of the planar face.
                | 
                |     Parameters:
                | 
                |         oOrigin[0]
                |             The X Coordinate of the planar face origin 
                |         oOrigin[1]
                |             The Y Coordinate of the planar face origin 
                |         oOrigin[2]
                |             The Z Coordinate of the planar face origin

        :param tuple o_origin:
        :return: None
        :rtype: None
        """
        return self.planar_face.GetOrigin(o_origin)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_origin'
        # # vba_code = """
        # # Public Function get_origin(planar_face)
        # #     Dim oOrigin (2)
        # #     planar_face.GetOrigin oOrigin
        # #     get_origin = oOrigin
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_second_axis(self, o_second_axis: tuple) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetSecondAxis(CATSafeArrayVariant oSecondAxis)
                | 
                |     Returns the planar face second axis.
                | 
                |     Parameters:
                | 
                |         oSecondAxis[0]
                |             The X Coordinate of the planar face second axis 
                |         oSecondAxis[1]
                |             The Y Coordinate of the planar face second axis 
                |         oSecondAxis[2]
                |             The Z Coordinate of the planar face second axis

        :param tuple o_second_axis:
        :return: None
        :rtype: None
        """
        return self.planar_face.GetSecondAxis(o_second_axis)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_second_axis'
        # # vba_code = """
        # # Public Function get_second_axis(planar_face)
        # #     Dim oSecondAxis (2)
        # #     planar_face.GetSecondAxis oSecondAxis
        # #     get_second_axis = oSecondAxis
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'PlanarFace(name="{self.name}")'
