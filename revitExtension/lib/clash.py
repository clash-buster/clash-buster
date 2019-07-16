from pyrevit import revit
from Autodesk.Revit import DB


def get_pipe_data(pipe):
    pipedict = dict()
    pipedict["Line"] = pipe.Location.Curve
    pipedict["Id"] = pipe.Id
    pipedict["dia"] = pipe.LookupParameter("Diameter").AsDouble()
    pipedict["systemTypeId"] = (pipe.LookupParameter("System Type").AsElementId())
    pipedict["pipeTypeId"] = pipe.PipeType.Id
    pipedict["levelId"] = (pipe.LookupParameter("Reference Level").AsElementId())
    pipedict["TypeofPipe"] = (pipe.LookupParameter("System Type").AsValueString())
    pipedict["Insulation Thickness"] = (pipe.LookupParameter("Insulation Thickness").AsDouble())
    return pipedict

def get_beam_data(beam):
    beamdict = dict()
    beamdict["Line"] = beam.Location.Curve
    beamdict["d"] = beam.Symbol.LookupParameter("d").AsDouble()
    beamdict["bf"] = beam.Symbol.LookupParameter("bf").AsDouble()
    return beamdict

import time


def createnewpipefrompoints(points,pipedata):
    with DB.Transaction(revit.doc) as t1:
        #print revit.doc.Title
        #print pipedata
        for i in range(len(points)-1):
            t1.Start("Create Pipe")
            #print points[i]
            #print points [i+1]
            res = DB.Plumbing.Pipe.Create(revit.doc, pipedata["systemTypeId"], pipedata["pipeTypeId"], pipedata["levelId"], points[i], points[i+1])        
            res.LookupParameter("Diameter").Set(pipedata["dia"])
            #print res
            try:
                revit.doc.Delete(pipedata["Id"])
            except:
                pass
            
            t1.Commit()
            time.sleep(0.5)
    #print res.Id
    ##for par in res.Parameters:
    #    print par.Definition.Name
    #    print par.AsValueString()


def revit_clash_plane_curve(beamline, pipeline):
  
    p0 = beamline.GetEndPoint(0)
    p1 = beamline.GetEndPoint(1)
    p2 = p1 + DB.XYZ(0,0,1)
    bmplane = DB.Plane.CreateByThreePoints(p0,p1,p2)

    #project pipe line onto plane
    pipe_projected_startpoint, dist = bmplane.Project(pipeline.GetEndPoint(0))
    
    pipe_projected_endpoint, dist = bmplane.Project(pipeline.GetEndPoint(1))  
    #print (pipe_projected_startpoint)
    #print pipe_projected_endpoint
    pipe_projected = DB.Line.CreateBound(pipe_projected_startpoint,pipe_projected_endpoint)
    intpoint = pipe_projected.Intersect(pipeline)
    #print ("pipe intersectionpoint{}".format(intpoint))