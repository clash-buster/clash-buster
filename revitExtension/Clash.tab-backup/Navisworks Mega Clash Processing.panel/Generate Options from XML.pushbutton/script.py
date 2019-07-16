import clr
import sys
from Autodesk.Revit import DB, Creation, UI
from pyrevit import revit
import clash 
import rhino_decider


doc = revit.doc
uidoc = revit.uidoc
uiapp = __revit__.Application

revitversion = int(uiapp.VersionNumber )

__title__ = "Generate\nOptions"


""" Read XML File and Collect Required Elements"""
def readxml():
    outdata = dict()
    outdata["clashid"] = ""
    outdata["elementAId"] = 653435 #beam
    outdata["elementBId"] = 676828 #pipe
    outdata["imagefilename"] = ""
    return outdata
    
class clashdata(object):
    def __init__(self):
        self.xmldata = readxml()
        self.beam = revit.doc.GetElement(DB.ElementId(self.xmldata["elementAId"]))
        self.beamdata = clash.get_beam_data(self.beam)
        self.pipe = revit.doc.GetElement(DB.ElementId(self.xmldata["elementBId"]))
        self.pipedata = clash.get_pipe_data(self.pipe)


def structuralframingopening():
    for ref in beam.GetReferences(DB.FamilyInstanceReferenceType.CenterFrontBack):
        print ref
        radius = 10
        startAngle = 0
        endAngle = 2 * Math.PI     
        curve = Arc.Create(plane, radius, startAngle, endAngle)
        Creation.Document.NewOpening(beam, CurveArray, ref) 

cd = clashdata()

#import clash
#pipel = cd.pipedata["Line"]
#beaml = cd.beamdata["Line"]
#p_int = clash.revit_clash_plane_curve(beaml,pipel)
##p_middle = p_int - DB.XYZ(0,0,2)
#p0 = pipel.GetEndPoint(0)
#p1 = pipel.GetEndPoint(1)
#clash.createnewpipefrompoints([p0,p_middle,p1], cd.pipedata)
#clash.createnewpipefrompoints([DB.XYZ(0,0,0),DB.XYZ(500,0,0)], cd.pipedata)

pointsdict = rhino_decider.get_intersection_data(cd.beamdata, cd.pipedata)

v = pointsdict["option_crawl90"]
clash.createnewpipefrompoints(rhino_decider.convert_rhinopoint_to_xyz(v), cd.pipedata)
"""
with TransactionGroup(doc) as trg:
    trg.Start("Copy view(s) from link")
    t1 = Transaction(doc) #copy view
    t2 = Transaction(doc) #open view
    
    
        t1.Start("Import Views from Arch")
        
        
        t1.Commit()
    trg.Assimilate()





#log usage
try:
    from definitions1 import silmanlogger
    silmanlogger(__file__, "???")
except:
    print "the script ran to the end, but there was an error logging usage, (how can we justify more tools if we don't know they are being used?), contact hazell@silman.com"
    a=1
"""

