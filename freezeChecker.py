import maya.cmds as cmds

def get_objects():
    obj = cmds.ls(type="transform")
    objlist  = []
    for ao in obj:
        shapes_name = cmds.listRelatives(ao, shapes=True)
        if(shapes_name == None):
            objlist.append(ao)
        elif cmds.nodeType(shapes_name[0]) == "camera" or cmds.nodeType(shapes_name[0]) == "light":
            continue
        else:
            objlist.append(ao)
    return objlist

def check_freeze():
    obj = get_objects()
    for ao in obj:
        move = cmds.getAttr(ao+".translate")
        scale = cmds.getAttr(ao+".scale")
        rotate = cmds.getAttr(ao+".rotate")
        if(move[0] != (0,0,0) or scale[0] != (1,1,1) or rotate[0] != (0,0,0)):
            print("Freeze Transformations not applied on: " + ao)

def main():
    check_freeze()

if __name__ == "__main__":
    main()