import arcpy
from arcpy import env
from arcpy.sa import *

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the .pyt file)."""
        self.label = "Create 3D Printable STL"
        self.alias = ""
        self.tools = [CreateSTL]

class CreateSTL(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Create STL from DEM"
        self.description = "Creates a 3D printable STL file from a DEM"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []

        # Input DEM
        param0 = arcpy.Parameter(
            displayName="Input DEM",
            name="input_dem",
            datatype="DEMRasterLayer",
            parameterType="Required",
            direction="Input")
        params.append(param0)

        # Output STL file
        param1 = arcpy.Parameter(
            displayName="Output STL File",
            name="output_stl",
            datatype="DEFile",
            parameterType="Required",
            direction="Output")
        params.append(param1)

        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify parameters before internal validation is performed."""
        return

    def updateMessages(self, parameters):
        """Modify messages created by internal validation for each parameter."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        input_dem = parameters[0].valueAsText
        output_stl = parameters[1].valueAsText

        # Set environment settings
        env.workspace = arcpy.env.scratchGDB
        env.overwriteOutput = True

        # Process: Create TIN from DEM
        tin = arcpy.CreateTin_3d("temp_tin", "", input_dem, "DELAUNAY")

        # Process: Export TIN to STL
        arcpy.ddd.TinDomain_3d(tin, output_stl, "STL")

        return
