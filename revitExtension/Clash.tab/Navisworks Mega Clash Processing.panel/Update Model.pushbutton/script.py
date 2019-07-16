
from Autodesk.Revit import DB, Creation, UI
from pyrevit import revit
import clash
import rhino_decider
import clr
import sys

doc = revit.doc
uidoc = revit.uidoc
uiapp = __revit__.Application

revitversion = int(uiapp.VersionNumber )

""" Read Decision Maker Results File"""
def readxml(elid1, elid2):
    outdata = dict()
    outdata["clashid"] = ""
    outdata["elementAId"] = elid1 #beam
    outdata["elementBId"] = elid2 #pipe
    outdata["imagefilename"] = ""
    return outdata
    
class clashdata(object):
    def __init__(self, el1, el2, chosenoption):

        

        self.xmldata = readxml(el1, el2)
        self.beam = revit.doc.GetElement(DB.ElementId(self.xmldata["elementAId"]))
        self.beamdata = clash.get_beam_data(self.beam)
        self.pipe = revit.doc.GetElement(DB.ElementId(self.xmldata["elementBId"]))
        self.pipedata = clash.get_pipe_data(self.pipe)


def structuralframingopening():
    for ref in beam.GetReferences(DB.FamilyInstanceReferenceType.CenterFrontBack):
        #print ref
        radius = 10
        startAngle = 0
        endAngle = 2 * Math.PI     
        curve = Arc.Create(plane, radius, startAngle, endAngle)
        Creation.Document.NewOpening(beam, CurveArray, ref) 

solutions = ['option_below_beam', "option_crawl90", "option_drop45", "option_drop90"]
beamids = [999333,999333,999333,999333]
pipeids = [989548, 955727, 955633, 989553]

for s,b, p in zip(solutions, beamids, pipeids):
        cd = clashdata(b, p, s)
        pointsdict = rhino_decider.get_intersection_data(cd.beamdata, cd.pipedata)

        v = pointsdict[s]
        clash.createnewpipefrompoints(rhino_decider.convert_rhinopoint_to_xyz(v), cd.pipedata)
        