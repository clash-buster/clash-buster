
__title__ = "In Session Clash"

__title__ = "Chec Conflicts\nin Revit"


from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.DB import *
from Autodesk.Revit.ApplicationServices import ControlledApplication
from pyrevit import revit
from pyrevit.forms import SelectFromList
from pyrevit import output
output = output.get_output()
 
import clr
import sys

from System.Collections.Generic import List

doc = revit.doc
uidoc = revit.uidoc
uiapp = __revit__.Application

revitversion = int(uiapp.VersionNumber )

#Get Links
links = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_RvtLinks).WhereElementIsNotElementType().ToElements()

def check_element_interferances(element, _doc):
    # Setup the filtered element collector for all document elements.
    interferingCollector = DB.FilteredElementCollector(_doc)

    # Only accept element instances
    interferingCollector.WhereElementIsNotElementType()

    # Exclude intersections with the door itself or the host wall for the door.
    excludedElements = List[ElementId]()
    excludedElements.Add(element.Id)
    exclusionFilter = ExclusionFilter(excludedElements)
    interferingCollector.WherePasses(exclusionFilter)

    # Set up a filter which matches elements whose solid geometry intersects 
    # with the accessibility region
    intersectionFilter = DB.ElementIntersectsSolidFilter(doorAccessibilityRegion)
    interferingCollector.WherePasses(intersectionFilter)

    # Return all elements passing the collector
    interferingCollector.ToElementIds()


with TransactionGroup(doc) as trg:
    trg.Start("Copy view(s) from link")
    t1 = Transaction(doc) #copy view
    
    
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