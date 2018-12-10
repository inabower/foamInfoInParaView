# state file generated using paraview version 5.5.2

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.5.2

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

viewSize = [960,720]

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = viewSize
renderView1.AnnotationColor = [0.0, 1.0, 0.0]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.OrientationAxesLabelColor = [0.0, 1.0, 0.0]
renderView1.CenterOfRotation = [0.10468097019940614, -0.005672699883580212, 0.004999999776482582]
renderView1.StereoType = 0
renderView1.CameraPosition = [0.11843224802794783, -0.002301340623646028, 0.6347494503554006]
renderView1.CameraFocalPoint = [0.11843224802794783, -0.002301340623646028, 0.004999999776482578]
renderView1.CameraViewUp = [1.0, -6.661338147750939e-16, 0.0]
renderView1.CameraParallelScale = 0.25227776252140266
renderView1.Background = [1.0, 1.0, 1.0]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.XTitleColor = [0.0, 1.0, 0.0]
renderView1.AxesGrid.XTitleFontFile = ''
renderView1.AxesGrid.YTitleColor = [0.0, 1.0, 0.0]
renderView1.AxesGrid.YTitleFontFile = ''
renderView1.AxesGrid.ZTitleColor = [0.0, 1.0, 0.0]
renderView1.AxesGrid.ZTitleFontFile = ''
renderView1.AxesGrid.XLabelColor = [0.0, 1.0, 0.0]
renderView1.AxesGrid.XLabelFontFile = ''
renderView1.AxesGrid.YLabelColor = [0.0, 1.0, 0.0]
renderView1.AxesGrid.YLabelFontFile = ''
renderView1.AxesGrid.ZLabelColor = [0.0, 1.0, 0.0]
renderView1.AxesGrid.ZLabelFontFile = ''

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'PVFoamReader'
pVFoamReader2 = PVFoamReader(FileName='.')
pVFoamReader2.MeshParts = []
pVFoamReader2.VolumeFields = ['p']

# create a new '3D Text'
a3DText2 = a3DText()
a3DText2.Text = 'outlet1'

# create a new '3D Text'
a3DText3 = a3DText()
a3DText3.Text = 'inlet'

# create a new '3D Text'
a3DText1 = a3DText()
a3DText1.Text = 'outlet2'

# create a new 'Text'
text1 = Text()
text1.Text = 'inlet\noutlet1\noutlet2'

# create a new 'PVFoamReader'
pVFoamReader1 = PVFoamReader(FileName='.')
pVFoamReader1.MeshParts = ['internalMesh']
pVFoamReader1.VolumeFields = ['p', 'U']

# create a new 'Slice'
slice1 = Slice(Input=pVFoamReader1)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.10999999940395355, 0.0, 0.009999999776482582]
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# create a new 'Glyph'
glyph1 = Glyph(Input=slice1,
    GlyphType='2D Glyph')
glyph1.Scalars = ['POINTS', 'None']
glyph1.Vectors = ['POINTS', 'U']
glyph1.ScaleMode = 'vector'
glyph1.ScaleFactor = 0.0005
glyph1.GlyphMode = 'All Points'
glyph1.MaximumNumberOfSamplePoints = 50000
glyph1.GlyphTransform = 'Transform2'

# init the '2D Glyph' selected for 'GlyphType'
glyph1.GlyphType.GlyphType = 'ThickArrow'
glyph1.GlyphType.Filled = 1

# create a new 'Text'
text2 = Text()
text2.Text = 'text2\n'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from pVFoamReader1
pVFoamReader1Display = Show(pVFoamReader1, renderView1)

# trace defaults for the display properties.
pVFoamReader1Display.Representation = 'Wireframe'
pVFoamReader1Display.AmbientColor = [0.0, 0.0, 0.0]
pVFoamReader1Display.ColorArrayName = ['POINTS', '']
pVFoamReader1Display.Opacity = 0.4
pVFoamReader1Display.SpecularColor = [0.0, 1.0, 0.0]
pVFoamReader1Display.EdgeColor = [0.0, 1.0, 0.0]
pVFoamReader1Display.OSPRayScaleArray = 'U'
pVFoamReader1Display.OSPRayScaleFunction = 'PiecewiseFunction'
pVFoamReader1Display.SelectOrientationVectors = 'None'
pVFoamReader1Display.ScaleFactor = 0.04199999868869782
pVFoamReader1Display.SelectScaleArray = 'None'
pVFoamReader1Display.GlyphType = 'Arrow'
pVFoamReader1Display.GlyphTableIndexArray = 'None'
pVFoamReader1Display.GaussianRadius = 0.002099999934434891
pVFoamReader1Display.SetScaleArray = ['POINTS', 'U']
pVFoamReader1Display.ScaleTransferFunction = 'PiecewiseFunction'
pVFoamReader1Display.OpacityArray = ['POINTS', 'U']
pVFoamReader1Display.OpacityTransferFunction = 'PiecewiseFunction'
pVFoamReader1Display.DataAxesGrid = 'GridAxesRepresentation'
pVFoamReader1Display.SelectionCellLabelFontFile = ''
pVFoamReader1Display.SelectionPointLabelFontFile = ''
pVFoamReader1Display.PolarAxes = 'PolarAxesRepresentation'
pVFoamReader1Display.ScalarOpacityUnitDistance = 0.030212983464441696

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pVFoamReader1Display.ScaleTransferFunction.Points = [-0.526659369468689, 0.0, 0.5, 0.0, 8.081972122192383, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pVFoamReader1Display.OpacityTransferFunction.Points = [-0.526659369468689, 0.0, 0.5, 0.0, 8.081972122192383, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pVFoamReader1Display.DataAxesGrid.XTitleColor = [0.0, 1.0, 0.0]
pVFoamReader1Display.DataAxesGrid.XTitleFontFile = ''
pVFoamReader1Display.DataAxesGrid.YTitleColor = [0.0, 1.0, 0.0]
pVFoamReader1Display.DataAxesGrid.YTitleFontFile = ''
pVFoamReader1Display.DataAxesGrid.ZTitleColor = [0.0, 1.0, 0.0]
pVFoamReader1Display.DataAxesGrid.ZTitleFontFile = ''
pVFoamReader1Display.DataAxesGrid.XLabelColor = [0.0, 1.0, 0.0]
pVFoamReader1Display.DataAxesGrid.XLabelFontFile = ''
pVFoamReader1Display.DataAxesGrid.YLabelColor = [0.0, 1.0, 0.0]
pVFoamReader1Display.DataAxesGrid.YLabelFontFile = ''
pVFoamReader1Display.DataAxesGrid.ZLabelColor = [0.0, 1.0, 0.0]
pVFoamReader1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
pVFoamReader1Display.PolarAxes.PolarAxisTitleColor = [0.0, 1.0, 0.0]
pVFoamReader1Display.PolarAxes.PolarAxisTitleFontFile = ''
pVFoamReader1Display.PolarAxes.PolarAxisLabelColor = [0.0, 1.0, 0.0]
pVFoamReader1Display.PolarAxes.PolarAxisLabelFontFile = ''
pVFoamReader1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 1.0, 0.0]
pVFoamReader1Display.PolarAxes.LastRadialAxisTextFontFile = ''
pVFoamReader1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 1.0, 0.0]
pVFoamReader1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from slice1
slice1Display = Show(slice1, renderView1)

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')
pLUT.AutomaticRescaleRangeMode = 'Never'
pLUT.RGBPoints = [-20.0, 0.0, 0.0, 1.0, 33.02677536010742, 1.0, 0.0, 0.0]
pLUT.ColorSpace = 'HSV'
pLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
pLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['POINTS', 'p']
slice1Display.LookupTable = pLUT
slice1Display.EdgeColor = [0.0, 1.0, 0.0]
slice1Display.OSPRayScaleArray = 'U'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.ScaleFactor = 0.04199999868869782
slice1Display.SelectScaleArray = 'None'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'None'
slice1Display.GaussianRadius = 0.002099999934434891
slice1Display.SetScaleArray = ['POINTS', 'U']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'U']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.SelectionCellLabelFontFile = ''
slice1Display.SelectionPointLabelFontFile = ''
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [-0.29971450567245483, 0.0, 0.5, 0.0, 8.081894874572754, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [-0.29971450567245483, 0.0, 0.5, 0.0, 8.081894874572754, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
slice1Display.DataAxesGrid.XTitleColor = [0.0, 1.0, 0.0]
slice1Display.DataAxesGrid.XTitleFontFile = ''
slice1Display.DataAxesGrid.YTitleColor = [0.0, 1.0, 0.0]
slice1Display.DataAxesGrid.YTitleFontFile = ''
slice1Display.DataAxesGrid.ZTitleColor = [0.0, 1.0, 0.0]
slice1Display.DataAxesGrid.ZTitleFontFile = ''
slice1Display.DataAxesGrid.XLabelColor = [0.0, 1.0, 0.0]
slice1Display.DataAxesGrid.XLabelFontFile = ''
slice1Display.DataAxesGrid.YLabelColor = [0.0, 1.0, 0.0]
slice1Display.DataAxesGrid.YLabelFontFile = ''
slice1Display.DataAxesGrid.ZLabelColor = [0.0, 1.0, 0.0]
slice1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
slice1Display.PolarAxes.PolarAxisTitleColor = [0.0, 1.0, 0.0]
slice1Display.PolarAxes.PolarAxisTitleFontFile = ''
slice1Display.PolarAxes.PolarAxisLabelColor = [0.0, 1.0, 0.0]
slice1Display.PolarAxes.PolarAxisLabelFontFile = ''
slice1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 1.0, 0.0]
slice1Display.PolarAxes.LastRadialAxisTextFontFile = ''
slice1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 1.0, 0.0]
slice1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from glyph1
glyph1Display = Show(glyph1, renderView1)

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = ['POINTS', '']
glyph1Display.LookupTable = pLUT
glyph1Display.EdgeColor = [0.0, 1.0, 0.0]
glyph1Display.Position = [0.0, 0.0, 0.0001]
glyph1Display.OSPRayScaleArray = 'GlyphVector'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'GlyphVector'
glyph1Display.ScaleFactor = 0.042205482721328735
glyph1Display.SelectScaleArray = 'GlyphVector'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'GlyphVector'
glyph1Display.GaussianRadius = 0.002110274136066437
glyph1Display.SetScaleArray = ['POINTS', 'GlyphVector']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'GlyphVector']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.SelectionCellLabelFontFile = ''
glyph1Display.SelectionPointLabelFontFile = ''
glyph1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [-0.29971450567245483, 0.0, 0.5, 0.0, 8.081894874572754, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [-0.29971450567245483, 0.0, 0.5, 0.0, 8.081894874572754, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
glyph1Display.DataAxesGrid.XTitleColor = [0.0, 1.0, 0.0]
glyph1Display.DataAxesGrid.XTitleFontFile = ''
glyph1Display.DataAxesGrid.YTitleColor = [0.0, 1.0, 0.0]
glyph1Display.DataAxesGrid.YTitleFontFile = ''
glyph1Display.DataAxesGrid.ZTitleColor = [0.0, 1.0, 0.0]
glyph1Display.DataAxesGrid.ZTitleFontFile = ''
glyph1Display.DataAxesGrid.XLabelColor = [0.0, 1.0, 0.0]
glyph1Display.DataAxesGrid.XLabelFontFile = ''
glyph1Display.DataAxesGrid.YLabelColor = [0.0, 1.0, 0.0]
glyph1Display.DataAxesGrid.YLabelFontFile = ''
glyph1Display.DataAxesGrid.ZLabelColor = [0.0, 1.0, 0.0]
glyph1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
glyph1Display.PolarAxes.Translation = [0.0, 0.0, 0.0001]
glyph1Display.PolarAxes.PolarAxisTitleColor = [0.0, 1.0, 0.0]
glyph1Display.PolarAxes.PolarAxisTitleFontFile = ''
glyph1Display.PolarAxes.PolarAxisLabelColor = [0.0, 1.0, 0.0]
glyph1Display.PolarAxes.PolarAxisLabelFontFile = ''
glyph1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 1.0, 0.0]
glyph1Display.PolarAxes.LastRadialAxisTextFontFile = ''
glyph1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 1.0, 0.0]
glyph1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
glyph1Display.DiffuseColor = [0.0, 0.0, 0.0]

# show data from text1
text1Display = Show(text1, renderView1)

# trace defaults for the display properties.
text1Display.Color = [0.0, 0.0, 0.0]
text1Display.FontFamily = 'Courier'
text1Display.FontFile = ''
text1Display.FontSize = 9
text1Display.WindowLocation = 'LowerLeftCorner'

# show data from a3DText3
a3DText3Display = Show(a3DText3, renderView1)

# trace defaults for the display properties.
a3DText3Display.Representation = 'Surface'
a3DText3Display.ColorArrayName = ['POINTS', '']
a3DText3Display.DiffuseColor = [0.0, 0.0, 0.0]
a3DText3Display.EdgeColor = [0.0, 0.0, 0.0]
a3DText3Display.Position = [-0.01, 0.01, -0.01]
a3DText3Display.Scale = [0.01, 0.01, 0.01]
a3DText3Display.Orientation = [0.0, 0.0, 270.0]
a3DText3Display.OSPRayScaleFunction = 'PiecewiseFunction'
a3DText3Display.SelectOrientationVectors = 'None'
a3DText3Display.ScaleFactor = 0.2873561888933182
a3DText3Display.SelectScaleArray = 'None'
a3DText3Display.GlyphType = 'Arrow'
a3DText3Display.GlyphTableIndexArray = 'None'
a3DText3Display.GaussianRadius = 0.014367809444665909
a3DText3Display.SetScaleArray = ['POINTS', '']
a3DText3Display.ScaleTransferFunction = 'PiecewiseFunction'
a3DText3Display.OpacityArray = ['POINTS', '']
a3DText3Display.OpacityTransferFunction = 'PiecewiseFunction'
a3DText3Display.DataAxesGrid = 'GridAxesRepresentation'
a3DText3Display.SelectionCellLabelFontFile = ''
a3DText3Display.SelectionPointLabelFontFile = ''
a3DText3Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
a3DText3Display.DataAxesGrid.XTitleColor = [0.0, 1.0, 0.0]
a3DText3Display.DataAxesGrid.XTitleFontFile = ''
a3DText3Display.DataAxesGrid.YTitleColor = [0.0, 1.0, 0.0]
a3DText3Display.DataAxesGrid.YTitleFontFile = ''
a3DText3Display.DataAxesGrid.ZTitleColor = [0.0, 1.0, 0.0]
a3DText3Display.DataAxesGrid.ZTitleFontFile = ''
a3DText3Display.DataAxesGrid.XLabelColor = [0.0, 1.0, 0.0]
a3DText3Display.DataAxesGrid.XLabelFontFile = ''
a3DText3Display.DataAxesGrid.YLabelColor = [0.0, 1.0, 0.0]
a3DText3Display.DataAxesGrid.YLabelFontFile = ''
a3DText3Display.DataAxesGrid.ZLabelColor = [0.0, 1.0, 0.0]
a3DText3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
a3DText3Display.PolarAxes.Translation = [-0.01, 0.01, -0.01]
a3DText3Display.PolarAxes.Scale = [0.01, 0.01, 0.01]
a3DText3Display.PolarAxes.Orientation = [0.0, 0.0, 270.0]
a3DText3Display.PolarAxes.PolarAxisTitleColor = [0.0, 1.0, 0.0]
a3DText3Display.PolarAxes.PolarAxisTitleFontFile = ''
a3DText3Display.PolarAxes.PolarAxisLabelColor = [0.0, 1.0, 0.0]
a3DText3Display.PolarAxes.PolarAxisLabelFontFile = ''
a3DText3Display.PolarAxes.LastRadialAxisTextColor = [0.0, 1.0, 0.0]
a3DText3Display.PolarAxes.LastRadialAxisTextFontFile = ''
a3DText3Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 1.0, 0.0]
a3DText3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from a3DText2
a3DText2Display = Show(a3DText2, renderView1)

# trace defaults for the display properties.
a3DText2Display.Representation = 'Surface'
a3DText2Display.ColorArrayName = ['POINTS', '']
a3DText2Display.DiffuseColor = [0.0, 0.0, 0.0]
a3DText2Display.EdgeColor = [0.0, 1.0, 0.0]
a3DText2Display.Position = [0.19, -0.18, -0.01]
a3DText2Display.Scale = [0.01, 0.01, 0.01]
a3DText2Display.Orientation = [0.0, 0.0, 270.0]
a3DText2Display.OSPRayScaleFunction = 'PiecewiseFunction'
a3DText2Display.SelectOrientationVectors = 'None'
a3DText2Display.ScaleFactor = 0.287356188893318
a3DText2Display.SelectScaleArray = 'None'
a3DText2Display.GlyphType = 'Arrow'
a3DText2Display.GlyphTableIndexArray = 'None'
a3DText2Display.GaussianRadius = 0.0143678094446659
a3DText2Display.SetScaleArray = ['POINTS', '']
a3DText2Display.ScaleTransferFunction = 'PiecewiseFunction'
a3DText2Display.OpacityArray = ['POINTS', '']
a3DText2Display.OpacityTransferFunction = 'PiecewiseFunction'
a3DText2Display.DataAxesGrid = 'GridAxesRepresentation'
a3DText2Display.SelectionCellLabelFontFile = ''
a3DText2Display.SelectionPointLabelFontFile = ''
a3DText2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
a3DText2Display.DataAxesGrid.XTitleColor = [0.0, 1.0, 0.0]
a3DText2Display.DataAxesGrid.XTitleFontFile = ''
a3DText2Display.DataAxesGrid.YTitleColor = [0.0, 1.0, 0.0]
a3DText2Display.DataAxesGrid.YTitleFontFile = ''
a3DText2Display.DataAxesGrid.ZTitleColor = [0.0, 1.0, 0.0]
a3DText2Display.DataAxesGrid.ZTitleFontFile = ''
a3DText2Display.DataAxesGrid.XLabelColor = [0.0, 1.0, 0.0]
a3DText2Display.DataAxesGrid.XLabelFontFile = ''
a3DText2Display.DataAxesGrid.YLabelColor = [0.0, 1.0, 0.0]
a3DText2Display.DataAxesGrid.YLabelFontFile = ''
a3DText2Display.DataAxesGrid.ZLabelColor = [0.0, 1.0, 0.0]
a3DText2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
a3DText2Display.PolarAxes.Translation = [0.19, -0.18, -0.01]
a3DText2Display.PolarAxes.Scale = [0.01, 0.01, 0.01]
a3DText2Display.PolarAxes.Orientation = [0.0, 0.0, 270.0]
a3DText2Display.PolarAxes.PolarAxisTitleColor = [0.0, 1.0, 0.0]
a3DText2Display.PolarAxes.PolarAxisTitleFontFile = ''
a3DText2Display.PolarAxes.PolarAxisLabelColor = [0.0, 1.0, 0.0]
a3DText2Display.PolarAxes.PolarAxisLabelFontFile = ''
a3DText2Display.PolarAxes.LastRadialAxisTextColor = [0.0, 1.0, 0.0]
a3DText2Display.PolarAxes.LastRadialAxisTextFontFile = ''
a3DText2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 1.0, 0.0]
a3DText2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from a3DText1
a3DText1Display = Show(a3DText1, renderView1)

# trace defaults for the display properties.
a3DText1Display.Representation = 'Surface'
a3DText1Display.ColorArrayName = ['POINTS', '']
a3DText1Display.DiffuseColor = [0.0, 0.0, 0.0]
a3DText1Display.EdgeColor = [0.0, 1.0, 0.0]
a3DText1Display.Position = [0.19, 0.22, -0.01]
a3DText1Display.Scale = [0.01, 0.01, 0.01]
a3DText1Display.Orientation = [0.0, 0.0, 270.0]
a3DText1Display.OSPRayScaleFunction = 'PiecewiseFunction'
a3DText1Display.SelectOrientationVectors = 'None'
a3DText1Display.ScaleFactor = 0.287356188893318
a3DText1Display.SelectScaleArray = 'None'
a3DText1Display.GlyphType = 'Arrow'
a3DText1Display.GlyphTableIndexArray = 'None'
a3DText1Display.GaussianRadius = 0.0143678094446659
a3DText1Display.SetScaleArray = ['POINTS', '']
a3DText1Display.ScaleTransferFunction = 'PiecewiseFunction'
a3DText1Display.OpacityArray = ['POINTS', '']
a3DText1Display.OpacityTransferFunction = 'PiecewiseFunction'
a3DText1Display.DataAxesGrid = 'GridAxesRepresentation'
a3DText1Display.SelectionCellLabelFontFile = ''
a3DText1Display.SelectionPointLabelFontFile = ''
a3DText1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
a3DText1Display.DataAxesGrid.XTitleColor = [0.0, 1.0, 0.0]
a3DText1Display.DataAxesGrid.XTitleFontFile = ''
a3DText1Display.DataAxesGrid.YTitleColor = [0.0, 1.0, 0.0]
a3DText1Display.DataAxesGrid.YTitleFontFile = ''
a3DText1Display.DataAxesGrid.ZTitleColor = [0.0, 1.0, 0.0]
a3DText1Display.DataAxesGrid.ZTitleFontFile = ''
a3DText1Display.DataAxesGrid.XLabelColor = [0.0, 1.0, 0.0]
a3DText1Display.DataAxesGrid.XLabelFontFile = ''
a3DText1Display.DataAxesGrid.YLabelColor = [0.0, 1.0, 0.0]
a3DText1Display.DataAxesGrid.YLabelFontFile = ''
a3DText1Display.DataAxesGrid.ZLabelColor = [0.0, 1.0, 0.0]
a3DText1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
a3DText1Display.PolarAxes.Translation = [0.19, 0.22, -0.01]
a3DText1Display.PolarAxes.Scale = [0.01, 0.01, 0.01]
a3DText1Display.PolarAxes.Orientation = [0.0, 0.0, 270.0]
a3DText1Display.PolarAxes.PolarAxisTitleColor = [0.0, 1.0, 0.0]
a3DText1Display.PolarAxes.PolarAxisTitleFontFile = ''
a3DText1Display.PolarAxes.PolarAxisLabelColor = [0.0, 1.0, 0.0]
a3DText1Display.PolarAxes.PolarAxisLabelFontFile = ''
a3DText1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 1.0, 0.0]
a3DText1Display.PolarAxes.LastRadialAxisTextFontFile = ''
a3DText1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 1.0, 0.0]
a3DText1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from text2
text2Display = Show(text2, renderView1)

# trace defaults for the display properties.
text2Display.Color = [0.0, 0.0, 0.0]
text2Display.FontFamily = 'Courier'
text2Display.FontFile = ''
text2Display.FontSize = 7
text2Display.WindowLocation = 'LowerRightCorner'

# setup the color legend parameters for each legend in this view

# get color legend/bar for pLUT in view renderView1
pLUTColorBar = GetScalarBar(pLUT, renderView1)
pLUTColorBar.AutoOrient = 0
pLUTColorBar.Orientation = 'Horizontal'
pLUTColorBar.WindowLocation = 'AnyLocation'
pLUTColorBar.Position = [0.3750905141202028, 0.8826347305389222]
pLUTColorBar.Title = 'pressure [Pa]'
pLUTColorBar.ComponentTitle = ''
pLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
pLUTColorBar.TitleFontFamily = 'Courier'
pLUTColorBar.TitleFontFile = ''
pLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
pLUTColorBar.LabelFontFamily = 'Courier'
pLUTColorBar.LabelFontFile = ''
pLUTColorBar.AutomaticLabelFormat = 0
pLUTColorBar.LabelFormat = '%.f'
pLUTColorBar.RangeLabelFormat = '%.f'
pLUTColorBar.ScalarBarLength = 0.20834902244750153

# set color bar visibility
pLUTColorBar.Visibility = 1

# show color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# show color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')
pPWF.Points = [-20.0, 0.0, 0.5, 0.0, 33.02677536010742, 1.0, 0.5, 0.0]
pPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(text2)
# ----------------------------------------------------------------

import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import subprocess

picDir = 'pic'
figName = 'test1'
pngDir = picDir + '/' + figName
if not os.path.isdir(pngDir):
	os.makedirs(pngDir)

#Read boundaryFieldNames
boundaries = ['inlet', 'outlet1', 'outlet2']

# Time List
times = pVFoamReader2.TimestepValues

files = {'inlet':'postProcessing/inletAverage/0/surfaceFieldValue.dat',
          'outlet1':'postProcessing/outlet1Average/0/surfaceFieldValue.dat',
          'outlet2':'postProcessing/outlet2Average/0/surfaceFieldValue.dat'}

p = pd.DataFrame()
magU = pd.DataFrame()
for b in boundaries:
    file = files[b]
    dat = pd.read_csv(file,sep='\t',header=4,index_col=0)
    tmpP = dat['areaAverage(p)']
    tmpU = []
    for t in dat.index:
        uvec = dat['areaAverage(U)'].loc[t]
        uxyz = np.array(list(map(float, uvec[1:-1].split(' '))))
        tmpU.append(np.linalg.norm(uxyz))
    p[b] = tmpP
    magU[b] = pd.Series(tmpU,index=dat.index)

from PyFoam.RunDictionary.ParsedParameterFile import ParsedParameterFile
controlDict = ParsedParameterFile('system/controlDict').content

checkMeshLines = subprocess.check_output('checkMesh').split('\n')
checkMesh = {}
tmpDict = {}
title = ''
nowLoading = False
for l in checkMeshLines:
    if nowLoading:
        if l == '':
            checkMesh[title] = tmpDict
            tmpDict = {}
            nowLoading = False
        elif title == 'Geometry':
            if l.find('Overall domain bounding box') > -1:
                tmpDict['boundaryBox'] = l.replace('Overall domain bounding box','').strip()
            elif l.find('Boundary openness') > -1:
                tmpDict['boundaryOpenness'] = l.replace('Boundary openness','').replace('OK.','').strip()
            elif l.find('Max cell openness =') > -1:
                tmpDict['maxCellOpenness'] = l.replace('Max cell openness =','').replace('OK.','').strip()
            elif l.find('Max aspect ratio = ') > -1:
                tmpDict['maxAspectRatio'] = l.replace('Max aspect ratio = ','').replace('OK.','').strip()
            elif l.find('Minimum face area') > -1:
                s = l.replace('    Minimum face area = ','').replace('. Maximum face area ','').replace('.  Face area magnitudes OK.','').split('=')
                tmpDict['minFaceArea'] = float(s[0].strip())
                tmpDict['maxFaceArea'] = float(s[1].strip())
            elif l.find('Min volume =') > -1:
                s = l.replace('Min volume =','').replace('. Max volume','').replace('.  Total volume','').replace('.  Cell volumes OK.','').split('=')
                tmpDict['minVolume'] = float(s[0].strip())
                tmpDict['maxVolume'] = float(s[1].strip())
                tmpDict['totalVolume'] = float(s[2].strip())
            elif l.find('Mesh non-orthogonality') > -1:
                s = l.replace('Mesh non-orthogonality Max:','').split('average:')
                tmpDict['maxNonOrthogonality'] = float(s[0].strip())
                tmpDict['meanNonOrthogonality'] = float(s[1].strip())
            elif l.find('Max skewness =') > -1:
                tmpDict['maxSkewness'] =float(l.replace('Max skewness =','').replace('OK.','').strip())
        elif title == 'Mesh stats':
            s = l.split(':')
            tmpDict[s[0].strip()] = int(s[1].strip())
    if l == 'Mesh stats':
        title = 'Mesh stats'
        tmpDict = {}
        nowLoading = True
    elif  l == 'Checking geometry...':
        title = 'Geometry'
        tmpDict = {}
        nowLoading = True

foamProperties = 'Solver : ' + controlDict['application'] + '\n'
if controlDict['writeControl'] == 'adjustableRunTime':
    foamProperties += 'adjustableRunTime\nmaxCourantNo : ' + '{0:.1f}'.format(controlDict['maxCo']) + '\n'
else:
    foamProperties += 'deltaT : ' + '{0:.2e}'.format(controlDict['deltaT']) + '\n\n'
    
foamProperties += 'Mesh Properties\n'
for key in ['cells','faces','boundary patches']:
    foamProperties += '  ' + key + ' : ' + str(checkMesh['Mesh stats'][key]) + '\n'
for key in ['totalVolume','minVolume','maxSkewness','maxAspectRatio','maxNonOrthogonality']:
    foamProperties += '  ' + key + ' : ' + str(checkMesh['Geometry'][key]) + '\n'

text2.Text = foamProperties

n = 0
for time in times:
	renderView1.ViewTime = time
		
	tmpTxt = 'Time : {0:1.1f}'.format(time) + ' / {0:1.1f}\n\n'.format(controlDict['endTime'])
	for b in boundaries:
		tmpTxt += b + '\n  p[Pa]  : {0:3.2f}'.format(p[b][time]) + '\n  U[m/s] : {0:3.2f}'.format(magU[b][time]) + '\n'
	text1.Text = tmpTxt
	SaveScreenshot(pngDir+'/'+ figName + '_{0:04d}.png'.format(n), renderView1, ImageResolution=viewSize)
	n += 1

cmd = 'convert -loop 0 -delay 20 {}/{}*.png {}/{}.gif'.format(pngDir,figName,picDir,figName)
subprocess.call(cmd.split(' '))
