import clr, sys
sys.path.append(r"C:\Program Files\Rhino WIP\System")
clr.AddReference ("RhinoCommon.dll")

from pyrevit import revit
from Autodesk.Revit import DB, UI, Creation
import Rhino.Geometry as rg
import math
#in order to work with the data that's coming from revit with rhino, we need to convert the lines.  Here we will 
def convert_rvtLine_to_RhinoLine(revitLine):
    revitLine_start_pt, revitLine_end_pt = revitLine.GetEndPoint(0), revitLine.GetEndPoint(1)
    rhino_start, rhino_end = rg.Point3d(revitLine_start_pt.X, revitLine_start_pt.Y, revitLine_start_pt.Z), \
                                        rg.Point3d(revitLine_end_pt.X, revitLine_end_pt.Y, revitLine_end_pt.Z)
    
    return rg.Curve.CreateInterpolatedCurve([rhino_start, rhino_end], 1)
    
def preview_rhino_line(rhinoline):
    if type(rhinoline) == rg.Curve:
        beam_start_pt, beam_end_pt = rhinoline.PointAtStart, rhinoline.PointAtEnd
    elif type(rhinoline) == rg.Line:
        beam_start_pt, beam_end_pt = rhinoline.From, rhinoline.To

    p0 = DB.XYZ(beam_start_pt.X, beam_start_pt.Y, beam_start_pt.Z)
    p1 = DB.XYZ(beam_end_pt.X, beam_end_pt.Y, beam_end_pt.Z)
    
    p2 = p1 + DB.XYZ(0,1,0)
    revit_line = DB.Line.CreateBound(p0,p2)
    
    bmplane = DB.Plane.CreateByThreePoints(p0,p1,p2)
    with DB.Transaction(revit.doc) as t1:
        #print revit.doc.Title
        t1.Start("Create Model Line")
        skp = DB.SketchPlane.Create(revit.doc, bmplane) 
        #print revit_line
        #print p0,p1
        revit.doc.Create.NewModelCurve(revit_line, skp)
        t1.Commit()


def convert_rhinopoint_to_xyz(rhinopoint):
    if isinstance(rhinopoint, list):
        res = []
        rhinopoints = rhinopoint
        for rhinopoint in rhinopoint:
            res.append(DB.XYZ(rhinopoint.X, rhinopoint.Y, rhinopoint.Z))
        return res
    else:
        return DB.XYZ(rhinopoint.X, rhinopoint.Y, rhinopoint.Z)


def get_intersection_data(beamdata,pipedata):    
    """DBEI Hackathon"""

    __author__ = "Pragya Gupta"
    __version__ = "2019.07.15"


    #convert revit line to rhino curve for each element
    beam_line = convert_rvtLine_to_RhinoLine(beamdata["Line"])
    depth = beamdata["d"]
    width = beamdata["bf"]
    pipe_line = convert_rvtLine_to_RhinoLine(pipedata["Line"])
    diameter = pipedata["dia"]

    """
    CREATING A SURFACE FROM LINE THAT REPRESENTS THE TOP OF A BEAM
    :param beam_line: a line that represents the top of the beam (it is assumed that 
    the width will be extruded from this on one side only)
    :type beam_line: geometry
    :param depth: the depth of the beam 
    :type depth: int (if the depth is a floating number, for the purpose of this 
    algorithm it'll be rounded to the nearest integer value)
    """

    beam_start_pt, beam_end_pt = beam_line.PointAtStart, beam_line.PointAtEnd
    beam_other_start, beam_other_end = rg.Point3d(beam_start_pt.X, beam_start_pt.Y, 
                                        beam_start_pt.Z - depth), rg.Point3d(
                                        beam_end_pt.X, beam_end_pt.Y, 
                                        beam_end_pt.Z - depth)

    # Creating a surface for visualisation and intersection
    rg.Extrusion.Create(rg.LineCurve(beam_line), -depth, False)
    beam_surface = rg.Brep.CreateFromCornerPoints(beam_start_pt, beam_end_pt, 
                                                beam_other_end, beam_other_start,0.1)


    """
    FINDING THE POINT OF INTERSECTION BETWEEN BEAM SURFACE AND LINE REPRESENTING PIPE
    :param pipe_line: a line that represents the center line of the pipe
    :type pipe_line: geometry
    """
    # Finding the point at which the pipe intersects the beam
    intersection = rg.Intersect.Intersection.CurveBrep(pipe_line, beam_surface, 0.1)
    #               results in a 2D array of boolean value, curves and points.

    if intersection[0] == False:
        print ("This pipe does not clash with the beam")
    else: 
        intersection_pt = intersection[2][0]


    """
    FINDING THE POINTS AND PARAMETERS THAT ARE INTEGRAL TO CREATING SOLUTIONS FOR 
    CLASH RESOLUTION
    This algorithm asssumes that the overall beam dimension is not being modified.
    The solution set includes modifications to the pipe and at times creating 
    through the beam
    :param diameter: the diameter of the pipe including insulation
    :parap type: float
    """

    # Finding the beam length
    beam_length = rg.Point3d.DistanceTo(beam_start_pt, beam_end_pt)

    # Finding the pipe's start and end points. (While the pipes start and end may be 
    # much further away and more complex, this algorithm will assume a relatively 
    # manageable pipe length which may represent a section of the pipe)
    pipe_start_pt , pipe_end_pt = pipe_line.PointAtStart, pipe_line.PointAtEnd

    # Finding the maximum offset from the beam surfaces for the pipe to fit
    left_line = rg.Line(pipe_start_pt, intersection_pt)
    left_line_len = left_line.Length
    left_line_max_len = left_line_len - diameter / 2 - 1 
                        # 1" for space between pipe and beam
    left_line_scale_factor = left_line_max_len / left_line_len
    xform = rg.Transform.Scale(pipe_start_pt, left_line_scale_factor)
    left_line.Transform(xform)

    left_maximum_point = left_line.To


    right_line = rg.Line(pipe_end_pt, intersection_pt)
    right_line_len = right_line.Length
    right_line_max_len = right_line_len - diameter / 2 - width - 1
                        # 1" for space between pipe and beam
    right_line_scale_factor = right_line_max_len / right_line_len
    xform = rg.Transform.Scale(pipe_end_pt, right_line_scale_factor)
    right_line.Transform(xform)

    right_maximum_point = right_line.To



    """
    BUILDING SOLUTIONS SET
    This algorithm asssumes that the overall beam dimension is not being modified.
    The solution set includes modifications to the pipe and at times creating 
    through the beam
    """
    complete_solutions_set = {}

    """
    OPTION 1 and OPTION 2 PIPE GOES THROUGH THE BEAM
    """
    option_through = [pipe_start_pt , pipe_end_pt]
    complete_solutions_set["option_through"] = option_through


    """
    OPTION 3 PIPE CRAWLS AROUND THE BEAM WITH 90 DEGREE BENDS
    """
    option_crawl90 = [pipe_start_pt]

    option_crawl90.append(left_maximum_point)


    left_line_90degree_point = rg.Point3d(left_maximum_point.X, left_maximum_point.Y, 
                                            beam_other_start.Z - diameter/2 - 1)
    option_crawl90.append(left_line_90degree_point)

    right_line_90degree_point = rg.Point3d(right_maximum_point.X, 
                                            right_maximum_point.Y, 
                                            beam_other_start.Z - diameter/2 - 1)
    option_crawl90.append(right_line_90degree_point)

    option_crawl90.append(right_line.To)

    option_crawl90.append(pipe_end_pt)

    complete_solutions_set["option_crawl90"] = option_crawl90


    """
    OPTION 3 PIPE CRAWLS AROUND THE BEAM WITH 45 DEGREE BENDS
    """
    option_crawl45 = [pipe_start_pt]


    left_line_move_distance = [left_line_90degree_point.X - pipe_start_pt.X, 
                                left_line_90degree_point.Y - pipe_start_pt.Y, 
                                left_line_90degree_point.Z - pipe_start_pt.Z]

    left_line_parallel = rg.Line(left_line_90degree_point, 
                                rg.Point3d(pipe_end_pt.X + left_line_move_distance[0], 
                                pipe_end_pt.Y + left_line_move_distance[1], 
                                pipe_end_pt.Z + left_line_move_distance[2]))

    left_line_parallel_copy = rg.Line(left_line_90degree_point, 
                                rg.Point3d(pipe_end_pt.X + left_line_move_distance[0], 
                                pipe_end_pt.Y + left_line_move_distance[1], 
                                pipe_end_pt.Z + left_line_move_distance[2]))

    left_rotation_radians = 135.0/360.0 * 2.0 * math.pi
    
    left_line_rotation_factor = rg.Transform.Rotation(left_rotation_radians, 
                                rg.Vector3d.YAxis, left_line_90degree_point)
    
    left_line_parallel_copy.Transform(left_line_rotation_factor)


    left_line_45degree_point = rg.Intersect.Intersection.CurveLine(pipe_line, 
                                left_line_parallel_copy,  0.1,0.1)
    
    left_line_45degree_point = left_line_45degree_point[0].PointA
    
    option_crawl45.append(left_line_45degree_point)

    option_crawl45.append(left_line_90degree_point)

    option_crawl45.append(right_line_90degree_point)

    right_line_move_distance = [right_line_90degree_point.X - pipe_start_pt.X, 
                                right_line_90degree_point.Y - pipe_start_pt.Y, 
                                right_line_90degree_point.Z - pipe_start_pt.Z]

    right_line_parallel = rg.Line(right_line_90degree_point, 
                                rg.Point3d(pipe_end_pt.X + right_line_move_distance[0], 
                                pipe_end_pt.Y + right_line_move_distance[1], 
                                pipe_end_pt.Z + right_line_move_distance[2]))

    right_line_parallel_copy = rg.Line(right_line_90degree_point, 
                                rg.Point3d(pipe_end_pt.X + right_line_move_distance[0], 
                                pipe_end_pt.Y + right_line_move_distance[1], 
                                pipe_end_pt.Z + right_line_move_distance[2]))

    right_rotation_radians = 45.0/360.0 * 2.0 * math.pi

    right_line_rotation_factor = rg.Transform.Rotation(right_rotation_radians, 
                                rg.Vector3d.YAxis, right_line_90degree_point)
    right_line_parallel_copy.Transform(right_line_rotation_factor)

    #
    right_line_45degree_point = rg.Intersect.Intersection.CurveLine(pipe_line, 
                                right_line_parallel_copy,  0.1,0.1)
                                
    right_line_45degree_point = right_line_45degree_point[0].PointA

    option_crawl45.append(right_line_45degree_point)

    option_crawl45.append(pipe_end_pt)

    complete_solutions_set["option_crawl45"] = option_crawl45


    """
    OPTION 4 PIPE BENDS 90 DEGREE ONCE BEFORE THE BEAM AND CONTINUES ONWARDS
    In this option, the slope after the drop is retained
    """
    option_drop90 = [pipe_start_pt, left_maximum_point, left_line_90degree_point, 
                        left_line_parallel.To]

    complete_solutions_set["option_drop90"] = option_drop90



    """
    OPTION 5 PIPE BENDS 45 DEGREE ONCE BEFORE THE BEAM AND CONTINUES ONWARDS
    In this option, the slope after the drop is retained
    """
    option_drop45 = [pipe_start_pt, left_line_45degree_point, 
                        left_line_90degree_point, right_line_parallel.To]

    complete_solutions_set["option_drop45"] = option_drop45



    """
    OPTION 6 RELOCATE THE PIPE TO GO BELOW THE BEAM
    In this option, the slope of the original pipe is retained
    it is only moved below the beam
    """
    option_below_beam = []
    option_below_beam.append(rg.Point3d(pipe_start_pt.X, pipe_start_pt.Y, 
                                beam_other_start.Z - diameter / 2 - 1))
    option_below_beam.append(rg.Point3d(pipe_end_pt.X, pipe_end_pt.Y, 
                                beam_other_start.Z - diameter / 2 - 1))

    complete_solutions_set["option_below_beam"] = option_below_beam






    """
    SELECTION SOLUTION SETS AS PER PIPE INTERSECTION POINT ON BEAM
    The beam is divided into nine quadrants (sized based on structural impact)
    Depending on the quadrant where the intersection is located,
    the solutions set will consist of all or a combination of the above mentioned 
    solutions
    """
    # Relocating intersection points on beam edges
    intersection_pt_hor = rg.Point3d(intersection_pt.X, intersection_pt.Y, 
                                    beam_other_start.Z)

    intersection_pt_ver = rg.Point3d(beam_other_start.X, beam_other_start.Y, 
                                    intersection_pt.Z)


    # Finding distance relative to beam edges
    intersection_dist_hor = rg.Point3d.DistanceTo(intersection_pt_hor, 
                                                    beam_other_start)

    intersection_dist_ver = rg.Point3d.DistanceTo(intersection_pt_ver, 
                                                    beam_other_start)


    # Defining horizontal and vertical quadrants
    end_hor_quadrant = 0.2 * beam_length, (1-0.2) * beam_length

    end_ver_quadrant = 0.3 * depth, (1-0.3) * depth


    # Finding horizontal quadrant
    if intersection_dist_hor < end_hor_quadrant[0]:
        hor_quadrant = 0
    elif intersection_dist_hor > end_hor_quadrant[1]:
        hor_quadrant = 2
    else: hor_quadrant = 1

    # Finding vertical quadrant
    if intersection_dist_ver < end_ver_quadrant[0]:
        ver_quadrant = 0
    elif intersection_dist_ver > end_ver_quadrant[1]:
        ver_quadrant = 2
    else: ver_quadrant = 1




    """
    CREATING SOLUTIONS SETS BASED ON QUADRANTS
    """
    if ver_quadrant == 0:
        solution_set = {key: complete_solutions_set[key] for key in 
                        complete_solutions_set.keys() and ['option_through', 
                        'option_below_beam']}
    elif ver_quadrant == 1 and hor_quadrant == 1:
        solution_set = {key: complete_solutions_set[key] for key in 
                        complete_solutions_set.keys() and ['option_through', 
                        'option_crawl45', 'option_crawl90', 'option_drop45', 
                        'option_drop90', 'option_below_beam']}
    elif ver_quadrant == 1 and hor_quadrant != 1:
        solution_set = {key: complete_solutions_set[key] for key in 
                        complete_solutions_set.keys() and [
                        'option_crawl45', 'option_crawl90', 'option_drop45', 
                        'option_drop90', 'option_below_beam']}
    elif ver_quadrant == 2:
        solution_set = {key: complete_solutions_set[key] for key in 
                        complete_solutions_set.keys() and [
                        'option_crawl45', 'option_crawl90', 'option_drop45', 
                        'option_drop90', 'option_below_beam']}

    #print (solution_set)



    """
    ELIMINATING SOLUTIONS BASED ON TYPE OF PIPE
    """
    sewer_key_list = ['option_through', 'option_drop45', 
                        'option_drop90', 'option_below_beam']
    if type == "sewer":
        solution_set = {key:solution_set[key] for key in sewer_key_list}
    else: solution_set = solution_set
    
    # print (solution_set.keys())
    return solution_set